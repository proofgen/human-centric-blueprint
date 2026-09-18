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
# This notice covers verify.py alone. The text and the compiled bundle beside it are licensed
# as LICENSE.md states.
"""Verify a Human-Centric Blueprint release tree. Python 3 only; no dependencies.

    python3 compiled/verify.py [ROOT] [--expect FINGERPRINT]

ROOT defaults to the folder above this file. --expect takes the fingerprint you obtained from a
source independent of this download (the Zenodo record, the published notice, the author's site)
and fails unless the tree carries exactly that fingerprint.

What it checks, in order:
  1. compiled/bundle.yaml hashes to compiled/bundle.sha256 (the fingerprint, the Layer 3 policy hash).
  2. Every artifact and principle unit bundle.yaml lists hashes to the value listed for it.
  3. Every sealed prose input bundle.yaml lists hashes to the value listed for it.
  4. Every file RELEASE-MANIFEST.json lists is present and hashes to its listed value; files present
     and not listed are reported (verify.py itself and the manifest are outside the manifest by design).
  5. CONSTITUTION.md carries all eleven Article headings, and every prohibition clause in
     compiled/constitution/walls.yaml appears verbatim in Article 8 or 9.
  6. With --expect: the fingerprint equals the one you supplied.
  8. Every condition, record and posture text in compiled/protocol/receipt-schema.yaml appears verbatim
     in CONSTITUTION.md or LEXICON.md.
  7. Where the tree carries conformance/examples.json: every example's basis quote appears verbatim in
     a sealed file, and the wall, emergency, consent and credential examples agree with the compiled data
     (the emergency examples are recomputed from compiled/protocol/emergency-thresholds.yaml).

What PASS means: the files in this tree are the files the sealed bundle and the release manifest
describe, byte for byte. What PASS does not establish: who published the tree. For that, compare the
fingerprint against a source you trust and pass it with --expect. This tool verifies; it does not
rebuild the bundle from the text.
"""
import hashlib, json, os, re, sys

args = [a for a in sys.argv[1:]]
expect = None
if "--expect" in args:
    i = args.index("--expect")
    expect = args[i + 1].strip().lower() if i + 1 < len(args) else ""
    del args[i:i + 2]
ROOT = os.path.abspath(args[0]) if args else os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
fails, notes = [], []

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def norm(s):
    return " ".join(s.split())

def unq(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v

# 1. the fingerprint
bundle_path = os.path.join(ROOT, "compiled", "bundle.yaml")
seal_path = os.path.join(ROOT, "compiled", "bundle.sha256")
if not (os.path.exists(bundle_path) and os.path.exists(seal_path)):
    print("FAIL"); print("  - compiled/bundle.yaml or compiled/bundle.sha256 is missing"); sys.exit(1)
digest = sha(bundle_path)
with open(seal_path) as f:
    seal = f.read().split()[0].strip().lower()
if digest != seal:
    fails.append("compiled/bundle.yaml does not hash to compiled/bundle.sha256")

# 2 and 3. everything bundle.yaml lists: artifacts and principles (file + sha256 pairs), and inputs (path: hash)
with open(bundle_path, encoding="utf-8") as f:
    blines = f.read().split("\n")
listed = {}       # release-relative path -> expected hash
pending_file = None
section = None
for line in blines:
    if line and not line[0].isspace():
        section = line.split(":")[0].strip()
        pending_file = None
        continue
    st = line.strip()
    if section in ("artifacts", "principles"):
        if st.startswith("- file:"):
            pending_file = unq(st[len("- file:"):])
        elif st.startswith("sha256:") and pending_file:
            listed[os.path.join("compiled", pending_file)] = unq(st[len("sha256:"):]).lower()
            pending_file = None
    elif section == "inputs":
        m = re.match(r"([^:]+\.md):\s*(.+)$", st)
        if m:
            rel = m.group(1).strip()
            if rel.startswith("BLUEPRINT/"):
                rel = rel[len("BLUEPRINT/"):]   # the release tree puts CHAPTERS/ and the spine at its root
            listed[rel] = unq(m.group(2)).lower()
if len(listed) < 10:
    fails.append("bundle.yaml lists fewer files than expected; the manifest may be malformed")
for rel, want in sorted(listed.items()):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        fails.append("listed in bundle.yaml and missing from the tree: " + rel)
    elif sha(path) != want:
        fails.append("does not hash to the value bundle.yaml lists: " + rel)

# 4. the release manifest, every file
man_path = os.path.join(ROOT, "RELEASE-MANIFEST.json")
manifest_count = 0
if os.path.exists(man_path):
    with open(man_path, encoding="utf-8") as f:
        man = json.load(f)
    files = man.get("files", {})
    manifest_count = len(files)
    if man.get("layer3", "").lower() != seal:
        fails.append("RELEASE-MANIFEST.json names a different fingerprint than compiled/bundle.sha256")
    for rel, want in sorted(files.items()):
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            fails.append("listed in RELEASE-MANIFEST.json and missing from the tree: " + rel)
        elif sha(path) != want.lower():
            fails.append("does not hash to the value RELEASE-MANIFEST.json lists: " + rel)
    present = set()
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if not d.startswith(".") and d != "__pycache__"]
        for fn in fns:
            if fn.startswith("."):
                continue
            present.add(os.path.relpath(os.path.join(dp, fn), ROOT).replace(os.sep, "/"))
    outside = {"RELEASE-MANIFEST.json", "compiled/verify.py"}
    extra = sorted(present - set(files) - outside)
    if extra:
        notes.append("present and not listed in RELEASE-MANIFEST.json (not part of the release): " + ", ".join(extra[:10]) + (" ..." if len(extra) > 10 else ""))
else:
    notes.append("no RELEASE-MANIFEST.json; only the bundle's own listings were checked")

# 5. the Constitution and the walls
with open(os.path.join(ROOT, "CONSTITUTION.md"), encoding="utf-8") as f:
    con = f.read()
articles = re.findall(r"^\*\*Article (\d+)\.", con, re.M)
missing = [str(i) for i in range(1, 12) if str(i) not in articles]
if missing:
    fails.append("CONSTITUTION.md lacks Article headings: " + ", ".join(missing))
a89 = ""
for n in ("8", "9"):
    m = re.search(r"\*\*Article " + n + r"\.[^\n]*\n(.*?)\n\n", con, re.S)
    a89 += " " + (norm(m.group(1)) if m else "")
with open(os.path.join(ROOT, "compiled", "constitution", "walls.yaml"), encoding="utf-8") as f:
    walls = f.read()
prohibitions = []
for line in walls.splitlines():
    st = line.strip()
    if st.startswith("prohibition:"):
        v = st[len("prohibition:"):].strip()
        if v.startswith('"') and v.endswith('"'):
            v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        prohibitions.append(norm(v))
if not prohibitions:
    fails.append("no prohibition clauses found in compiled/constitution/walls.yaml")
for pr in prohibitions:
    if pr.rstrip(".") not in a89:
        fails.append("wall clause not found verbatim in Articles 8 or 9: " + pr[:80])

# the gate artifact: every sentence it carries for Articles 3 to 7 appears verbatim in the Constitution
gate_path = os.path.join(ROOT, "compiled", "constitution", "gate.yaml")
gate_sentences = 0
if os.path.exists(gate_path):
    con_norm = norm(con)
    with open(gate_path, encoding="utf-8") as f:
        in_articles = False
        for line in f:
            if line.startswith("articles:"):
                in_articles = True
                continue
            if in_articles and line and not line[0].isspace():
                in_articles = False
            if in_articles and line.strip().startswith("- ") and "sentences" not in line and not line.strip().startswith("- article:"):
                v = line.strip()[2:].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
                if v and not v.endswith(":"):
                    gate_sentences += 1
                    if norm(v) not in con_norm:
                        fails.append("gate sentence not found verbatim in the Constitution: " + v[:80])
    if gate_sentences == 0:
        fails.append("compiled/constitution/gate.yaml carries no article sentences")

# 7. the conformance examples, where the tree carries them
ex_path = os.path.join(ROOT, "conformance", "examples.json")
examples_checked = 0
if os.path.exists(ex_path):
    def _read(rel):
        with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
            return fh.read()
    def _scalars(rel, key):
        out = []
        for ln in _read(rel).splitlines():
            st = ln.strip()
            if st.startswith("- "):
                st = st[2:].strip()
            if st.startswith(key + ":"):
                out.append(unq(st[len(key) + 1:]))
        return out
    try:
        with open(ex_path, encoding="utf-8") as fh:
            exdoc = json.load(fh)
    except ValueError as e:
        exdoc = {"examples": []}
        fails.append("conformance/examples.json is not valid JSON: " + str(e))
    wall_ids = set(_scalars("compiled/constitution/walls.yaml", "id"))
    leg_names = _scalars("compiled/consent/validity-predicate.yaml", "name")
    # the emergency bands, read line by line
    bands, cur, metric = [], None, None
    for ln in _read("compiled/protocol/emergency-thresholds.yaml").splitlines():
        st = ln.strip()
        if st.startswith("- metric:"):
            metric = unq(st[len("- metric:"):])
        elif st.startswith("- id:"):
            cur = {"metric": metric, "id": unq(st[len("- id:"):])}
            bands.append(cur)
        elif cur is not None:
            for k in ("comparison", "value", "verdict", "condition"):
                if st.startswith(k + ":"):
                    cur[k] = unq(st[len(k) + 1:])
    hg = _read("compiled/protocol/head-guard.yaml")
    trip_bands = set(re.findall(r"^\s+- ((?:lrs|hrs)\.[a-z_]+)\s*$", hg, re.M))
    cred_m = re.search(r"all five credentials are satisfied: ([^.,]+), ([^.,]+), ([^.,]+), ([^.,]+), and ([^.,]+?),", con)
    cred_names = [c.strip() for c in cred_m.groups()] if cred_m else []
    if not (wall_ids and len(leg_names) == 7 and bands and trip_bands and len(cred_names) == 5):
        fails.append("conformance: the compiled data the examples are checked against could not be read")
    sealed_text = {}
    ops = {">=": lambda a, b: a >= b, ">": lambda a, b: a > b, "<=": lambda a, b: a <= b, "<": lambda a, b: a < b}
    rank = {"BLOCK": 2, "ESCALATE": 1}
    for e in exdoc.get("examples", []):
        examples_checked += 1
        eid, kind, inp, req = e.get("id", "?"), e.get("kind"), e.get("input", {}), e.get("required", {})
        bad = lambda msg: fails.append("conformance example " + eid + ": " + msg)
        if not e.get("basis"):
            bad("states no basis")
        for b in e.get("basis", []):
            rel = b.get("file", "")
            if rel not in listed:
                bad("its basis names a file outside the sealed inputs: " + rel); continue
            if rel not in sealed_text:
                sealed_text[rel] = norm(_read(rel))
            if norm(b.get("quote", "")) not in sealed_text[rel] or not b.get("quote"):
                bad("its basis quote is not found verbatim in " + rel)
        if kind == "wall":
            if inp.get("wall") not in wall_ids:
                bad("names a wall the compiled walls do not carry: " + str(inp.get("wall")))
            if req.get("proceeds") is not False or req.get("void") is not True:
                bad("a wall example must require that the action does not proceed and is void")
            if inp.get("wall") != "profile_bar" and req.get("verdict") != "BLOCK":
                bad("a wall of Article 9 is a hard stop, and a hard stop is a BLOCK (SUBSTRATE.md section 6)")
        elif kind == "emergency":
            hit = [b for b in bands if b["metric"] == inp.get("metric") and ops[b["comparison"]](float(inp.get("value")), float(b["value"]))
                   and (b.get("condition") in (None, "null", "") or inp.get("vulnerable_population") is True)]
            want = max((b["verdict"] for b in hit), key=lambda v: rank.get(v, 0)) if hit else None
            trips = any(b["id"] in trip_bands for b in hit)
            if req.get("verdict") != want:
                bad("requires " + str(req.get("verdict")) + " where the compiled bands give " + str(want))
            if req.get("head_guard_trips") is not trips:
                bad("states head_guard_trips=" + str(req.get("head_guard_trips")) + " where the compiled bands give " + str(trips))
            if want and req.get("proceeds") is not False:
                bad("an emergency band applies and the example does not hold the action")
        elif kind == "consent":
            failed = inp.get("failed_legs", [])
            for l in failed:
                if l not in leg_names:
                    bad("names a consent leg the compiled predicate does not carry: " + str(l))
            if req.get("consent_credential") != ("unmet" if failed else "met"):
                bad("the consent credential it requires disagrees with the seven-leg conjunction")
            if failed and (req.get("proceeds") is not False or sorted(req.get("verdict_in", [])) != ["BLOCK", "ESCALATE"]):
                bad("a void consent is an unmet credential: blocked or escalated (Article 6)")
        elif kind == "credential":
            creds = inp.get("credentials", {})
            if sorted(creds) != sorted(cred_names):
                bad("does not state exactly the five credentials of Article 6")
            if any(v != "met" for v in creds.values()) and (req.get("proceeds") is not False or sorted(req.get("verdict_in", [])) != ["BLOCK", "ESCALATE"]):
                bad("an unmet credential on a consequential action: blocked or escalated (Article 6)")
        elif kind != "text":
            bad("unknown kind: " + str(kind))
    if examples_checked == 0 and not any("examples.json" in x for x in fails):
        fails.append("conformance/examples.json carries no examples")

# 8. the receipt schema: every condition, record and posture text it carries appears verbatim in the Constitution or the Lexicon
rs_path = os.path.join(ROOT, "compiled", "protocol", "receipt-schema.yaml")
receipt_texts = 0
if os.path.exists(rs_path):
    with open(os.path.join(ROOT, "LEXICON.md"), encoding="utf-8") as f:
        lex_norm = norm(f.read())
    con_norm2 = norm(con)
    with open(rs_path, encoding="utf-8") as f:
        for line in f:
            st = line.strip()
            if st.startswith("text:"):
                v = unq(st[len("text:"):])
                v = v.replace('\\"', '"').replace("\\\\", "\\")
                receipt_texts += 1
                if norm(v) not in con_norm2 and norm(v) not in lex_norm:
                    fails.append("receipt-schema text not found verbatim in the Constitution or the Lexicon: " + v[:80])
    if receipt_texts < 8:
        fails.append("compiled/protocol/receipt-schema.yaml carries fewer condition texts than expected")

# 6. the fingerprint you brought with you
if expect is not None:
    if not expect:
        fails.append("--expect was given with no fingerprint")
    elif expect != seal:
        fails.append("the tree's fingerprint (" + seal[:12] + "...) is not the one you expected (" + expect[:12] + "...)")

print("fingerprint (Layer 3, compiled/bundle.sha256):", seal)
print("checked: bundle listings", len(listed), "| manifest files", manifest_count, "| walls", len(prohibitions), "| gate sentences", gate_sentences, "| Article headings", len(set(articles)), "| conformance examples", examples_checked, "| receipt texts", receipt_texts)
for n in notes:
    print("note:", n)
if fails:
    print("FAIL")
    for x in fails:
        print("  -", x)
    sys.exit(1)
if expect is None:
    print("PASS (checked against itself; pass --expect with a fingerprint from an independent source to confirm provenance)")
else:
    print("PASS (fingerprint matches the one you supplied)")
