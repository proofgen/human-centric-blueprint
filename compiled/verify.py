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

# 6. the fingerprint you brought with you
if expect is not None:
    if not expect:
        fails.append("--expect was given with no fingerprint")
    elif expect != seal:
        fails.append("the tree's fingerprint (" + seal[:12] + "...) is not the one you expected (" + expect[:12] + "...)")

print("fingerprint (Layer 3, compiled/bundle.sha256):", seal)
print("checked: bundle listings", len(listed), "| manifest files", manifest_count, "| walls", len(prohibitions), "| Article headings", len(set(articles)))
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
