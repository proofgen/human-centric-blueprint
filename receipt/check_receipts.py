#!/usr/bin/env python3
# Copyright 2026 Erik Passoja, Seventh Planet, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file
# except in compliance with the License. You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the
# License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#
# This notice covers check_receipts.py alone. The text beside it is licensed as LICENSE.md states.
"""Check a chain of receipts made under A Human-Centric Blueprint for Safe AI Ethics.

    python3 receipt/check_receipts.py CHAIN.jsonl [--policy FINGERPRINT]

Python 3.8 or later, no dependencies. The receipt form is receipt/RECEIPT-FORMAT.md; the conditions it serves are
compiled/protocol/receipt-schema.yaml. What it checks, in order: every line parses with the four parts and the
required fields; positions rise by one (a gap is a removed receipt); every prev cites the hash before it; every hash
is SHA-256 of the canonical body; every gate signature and witness signature verifies (Ed25519, implemented below);
every reconciled receipt has a verifying witness; every Action Receipt cites an earlier allowed Prospective Receipt
for the same action and is not earlier than it; every policy_hash is the fingerprint you pass or the tree's;
every verdict is one of three; every credentials object names exactly the five; no body carries an unnamed field.
What PASS means: no one has altered this chain, and its receipts were committed and witnessed as they say.
It does not establish whose keys these are, that the witnesses are independent, or that a verdict was right."""
import hashlib, json, os, re, sys

# --- Ed25519 (RFC 8032), verification only, dependency-free. Checked against an independent implementation on random inputs at build.
_p = 2**255 - 19
_d = (-121665 * pow(121666, _p - 2, _p)) % _p
_q = 2**252 + 27742317777372353535851937790883648493
def _inv(x): return pow(x, _p - 2, _p)
def _xrecover(y):
    xx = (y * y - 1) * _inv(_d * y * y + 1); x = pow(xx, (_p + 3) // 8, _p)
    if (x * x - xx) % _p != 0: x = (x * pow(2, (_p - 1) // 4, _p)) % _p
    return _p - x if x % 2 else x
_Gy = (4 * _inv(5)) % _p; _Gx = _xrecover(_Gy); _G = (_Gx, _Gy, 1, (_Gx * _Gy) % _p)
def _add(P, Q):
    (X1, Y1, Z1, T1), (X2, Y2, Z2, T2) = P, Q
    A = ((Y1 - X1) * (Y2 - X2)) % _p; B = ((Y1 + X1) * (Y2 + X2)) % _p; C = (T1 * 2 * _d * T2) % _p; D = (Z1 * 2 * Z2) % _p
    E, F, G_, H = B - A, D - C, D + C, B + A
    return ((E * F) % _p, (G_ * H) % _p, (F * G_) % _p, (E * H) % _p)
def _mul(P, e):
    Q = (0, 1, 1, 0)
    while e:
        if e & 1: Q = _add(Q, P)
        P = _add(P, P); e >>= 1
    return Q
def _dec(s):
    y = int.from_bytes(s, "little"); sign = y >> 255; y &= (1 << 255) - 1
    if y >= _p: return None
    x = _xrecover(y)
    if (x * x - (y * y - 1) * _inv(_d * y * y + 1)) % _p != 0: return None
    if x & 1 != sign: x = _p - x
    return (x, y, 1, (x * y) % _p)
def _eq(P, Q):
    (X1, Y1, Z1, _), (X2, Y2, Z2, _) = P, Q
    return (X1 * Z2 - X2 * Z1) % _p == 0 and (Y1 * Z2 - Y2 * Z1) % _p == 0
def ed25519_verify(pk, msg, sig):
    if len(sig) != 64 or len(pk) != 32: return False
    R = _dec(sig[:32]); A = _dec(pk); S = int.from_bytes(sig[32:], "little")
    if R is None or A is None or S >= _q: return False
    k = int.from_bytes(hashlib.sha512(sig[:32] + pk + msg).digest(), "little") % _q
    return _eq(_mul(_G, S), _add(R, _mul(A, k)))

# --- the form
def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
VERDICTS = ("allow", "block", "escalate")
CREDS = ("Identity", "Provenance", "Consent", "Authorization", "Liability")
CRED_VALUES = ("met", "unmet", "not_required")
INIT = ("system", "human", "handoff")
COMMON = {"type", "position", "time", "action_id", "action_class", "parameter_hashes", "policy_hash", "responsible_party", "person_refs", "prev", "signer", "signature"}
OPTIONAL = {"event_class"}
PROSPECTIVE = COMMON | {"credentials", "verdict", "decision_step", "sensor_reliability_state"}
ACTION = COMMON | {"initiation_class", "prospective_commitment"}
HEX64 = re.compile(r"^[0-9a-f]{64}$"); HEX128 = re.compile(r"^[0-9a-f]{128}$")
TIME = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$")

def check(path, policy=None):
    fails, notes = [], []
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    receipts = []
    for n, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except ValueError as e:
            fails.append(f"line {n}: not JSON ({e})"); continue
        if not isinstance(r, dict) or set(r) != {"body", "hash", "state", "witnesses"}:
            fails.append(f"line {n}: a receipt has exactly the parts body, hash, state, witnesses"); continue
        receipts.append((n, r))
    prev_hash, prev_pos, prospectives = None, None, {}
    witnessed = 0
    for n, r in receipts:
        b, h, st, ws = r["body"], r["hash"], r["state"], r["witnesses"]
        pos = b.get("position") if isinstance(b, dict) else None
        tag = f"receipt at position {pos}" if isinstance(pos, int) else f"line {n}"
        bad = lambda m: fails.append(f"{tag}: {m}")
        if not isinstance(b, dict):
            bad("body is not an object"); continue
        t = b.get("type")
        need = PROSPECTIVE if t == "prospective" else ACTION if t == "action" else None
        if need is None:
            bad("type is neither prospective nor action"); continue
        missing = sorted(need - set(b)); extra = sorted(set(b) - need - OPTIONAL)
        if missing: bad("missing fields: " + ", ".join(missing))
        if extra: bad("fields the format does not name: " + ", ".join(extra))
        if missing: continue
        # 2, 3: positions and the chain
        if not isinstance(pos, int) or isinstance(pos, bool):
            bad("position is not an integer")
        elif prev_pos is not None and pos != prev_pos + 1:
            bad(f"arithmetic gap: previous position was {prev_pos}" + (" (a receipt was removed)" if pos > prev_pos + 1 else " (order broken)"))
        if b.get("prev") != prev_hash:
            bad("prev does not cite the hash of the preceding receipt" if prev_hash else "the first receipt's prev is not null")
        # 4: the commitment
        if not (isinstance(h, str) and HEX64.match(h)):
            bad("hash is not 64 hex characters")
        elif hashlib.sha256(canonical(b)).hexdigest() != h:
            bad("hash is not SHA-256 of the canonical body")
        # 5: the gate's signature
        sg, sig = b.get("signer"), b.get("signature")
        if not (isinstance(sg, dict) and sg.get("scheme") == "ed25519" and isinstance(sg.get("public_key"), str) and HEX64.match(sg["public_key"]) and isinstance(sg.get("key_id"), str)):
            bad("signer must name scheme ed25519, a key_id and a 64-hex public_key")
        elif not (isinstance(sig, str) and HEX128.match(sig)):
            bad("signature is not 128 hex characters")
        else:
            unsigned = {k: v for k, v in b.items() if k != "signature"}
            if not ed25519_verify(bytes.fromhex(sg["public_key"]), canonical(unsigned), bytes.fromhex(sig)):
                bad("the gate's signature does not verify")
        # 6: witnesses and state
        if st not in ("provisional", "reconciled"):
            bad("state is neither provisional nor reconciled")
        good = 0
        if not isinstance(ws, list):
            bad("witnesses is not a list"); ws = []
        for i, w in enumerate(ws):
            ok = (isinstance(w, dict) and w.get("scheme") == "ed25519" and isinstance(w.get("public_key"), str) and HEX64.match(w["public_key"])
                  and isinstance(w.get("signature"), str) and HEX128.match(w["signature"]) and isinstance(w.get("witness_id"), str))
            if ok and isinstance(h, str) and ed25519_verify(bytes.fromhex(w["public_key"]), h.encode("ascii"), bytes.fromhex(w["signature"])):
                good += 1
            else:
                bad(f"witness {i} ({w.get('witness_id', '?') if isinstance(w, dict) else '?'}): signature does not verify")
        if st == "reconciled" and good == 0:
            bad("reconciled with no verifying witness")
        witnessed += 1 if good else 0
        # 7: the pair
        if t == "prospective":
            if b.get("verdict") not in VERDICTS: bad("verdict is not allow, block or escalate")
            c = b.get("credentials")
            if not (isinstance(c, dict) and set(c) == set(CREDS) and all(v in CRED_VALUES for v in c.values())):
                bad("credentials must name exactly Identity, Provenance, Consent, Authorization, Liability, each met, unmet or not_required")
            srs = b.get("sensor_reliability_state")
            if not (isinstance(srs, dict) and "floor" in srs and "lowest" in srs):
                bad("sensor_reliability_state must be an object with at least floor and lowest")
            if isinstance(b.get("action_id"), str):
                prospectives[b["action_id"]] = (h, b.get("verdict"), b.get("time"))
        else:
            if b.get("initiation_class") not in INIT: bad("initiation_class is not system, human or handoff")
            ref = prospectives.get(b.get("action_id"))
            if ref is None:
                bad("no earlier Prospective Receipt for this action_id")
            else:
                ph, pv, pt = ref
                if b.get("prospective_commitment") != ph: bad("prospective_commitment does not cite the Prospective Receipt's hash")
                if pv != "allow": bad(f"the act proceeded on a Prospective Receipt whose verdict was {pv}")
                if isinstance(b.get("time"), str) and isinstance(pt, str) and b["time"] < pt: bad("the act is earlier than its Prospective Receipt")
        # 8, 9, 10: the rest of the fields
        if policy and b.get("policy_hash") != policy: bad("policy_hash is not the fingerprint expected")
        if not (isinstance(b.get("policy_hash"), str) and HEX64.match(b["policy_hash"])): bad("policy_hash is not 64 hex characters")
        if not (isinstance(b.get("time"), str) and TIME.match(b["time"])): bad("time is not RFC 3339 UTC")
        for k in ("parameter_hashes",):
            if not (isinstance(b.get(k), list) and all(isinstance(x, str) and HEX64.match(x) for x in b[k])): bad(k + " must be a list of 64-hex hashes")
        for k in ("responsible_party", "person_refs"):
            if not (isinstance(b.get(k), list) and all(isinstance(x, str) for x in b[k])): bad(k + " must be a list of opaque references")
        prev_hash, prev_pos = (h if isinstance(h, str) else None), (pos if isinstance(pos, int) else prev_pos)
    return receipts, fails, notes, witnessed

def main():
    args = sys.argv[1:]
    policy = None
    if "--policy" in args:
        i = args.index("--policy"); policy = args[i + 1].strip().lower() if i + 1 < len(args) else ""; del args[i:i + 2]
    if not args:
        print(__doc__); sys.exit(2)
    if policy is None:
        seal = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "compiled", "bundle.sha256")
        if os.path.exists(seal):
            with open(seal) as fh:
                policy = fh.read().split()[0].strip().lower()
    receipts, fails, notes, witnessed = check(args[0], policy)
    print("receipts:", len(receipts), "| witnessed:", witnessed, "| policy:", (policy[:12] + "...") if policy else "not checked (pass --policy)")
    if fails:
        print("FAIL")
        for f in fails: print("  -", f)
        sys.exit(1)
    print("PASS (the chain is intact, signed and witnessed as it says; whose keys these are is the governance's to show)")

if __name__ == "__main__":
    main()
