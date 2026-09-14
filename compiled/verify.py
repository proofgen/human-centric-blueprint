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

    python3 compiled/verify.py          (run from the release root, or pass the root as the first argument)

Checks: the SHA-256 of compiled/bundle.yaml equals compiled/bundle.sha256 (the Layer 3 policy hash);
CONSTITUTION.md carries all eleven Article headings; every prohibition clause in compiled/constitution/walls.yaml
appears verbatim in Article 9. Prints the hash and PASS or FAIL. This tree verifies; it does not rebuild.
"""
import hashlib, os, re, sys

ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
fails = []

def norm(s):
    return " ".join(s.split())

bundle = os.path.join(ROOT, "compiled", "bundle.yaml")
seal_file = os.path.join(ROOT, "compiled", "bundle.sha256")
with open(bundle, "rb") as f:
    digest = hashlib.sha256(f.read()).hexdigest()
with open(seal_file) as f:
    seal = f.read().split()[0]
if digest != seal:
    fails.append("compiled/bundle.yaml does not hash to compiled/bundle.sha256")

with open(os.path.join(ROOT, "CONSTITUTION.md"), encoding="utf-8") as f:
    con = f.read()
articles = re.findall(r"^\*\*Article (\d+)\.", con, re.M)
missing = [str(i) for i in range(1, 12) if str(i) not in articles]
if missing:
    fails.append("CONSTITUTION.md lacks Article headings: " + ", ".join(missing))
# The walls artifact carries Article 9 (the hard walls) and Article 8 (the profile bar); both are searched.
a89 = ""
for n in ("8", "9"):
    m = re.search(r"\*\*Article " + n + r"\.[^\n]*\n(.*?)\n\n", con, re.S)
    a89 += " " + (norm(m.group(1)) if m else "")

with open(os.path.join(ROOT, "compiled", "constitution", "walls.yaml"), encoding="utf-8") as f:
    walls = f.read()
prohibitions = []
for line in walls.splitlines():
    s = line.strip()
    if s.startswith("prohibition:"):
        v = s[len("prohibition:"):].strip()
        if v.startswith('"') and v.endswith('"'):
            v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        prohibitions.append(norm(v))
if not prohibitions:
    fails.append("no prohibition clauses found in compiled/constitution/walls.yaml")
for p in prohibitions:
    if p.rstrip(".") not in a89:
        fails.append("wall clause not found verbatim in Articles 8 or 9: " + p[:80])

print("Layer 3 (bundle.sha256):", seal)
print("walls checked:", len(prohibitions), "| Article headings found:", len(set(articles)))
if fails:
    print("FAIL")
    for x in fails:
        print("  -", x)
    sys.exit(1)
print("PASS")
