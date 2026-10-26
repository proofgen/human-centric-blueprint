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
# This notice covers compile.py alone. The text and the compiled bundle beside it are licensed
# as LICENSE.md states. This program is the text-to-data step and holds no gate logic.
"""Blueprint compiler: Layer 1 prose to Layer 2 policy, and the Layer 3 hash.

Spec Section 6.1, implemented against the corpus's own Layer 2 documentation
(the February 2026 spike, archived in the steward's hub), which governs
where the two disagree; deltas are filed in the hub.

Inputs, all read-only:
  BLUEPRINT/CHAPTERS/*.md            35 chapters
  BLUEPRINT/APPENDICES/*.md          35 appendices (linkage and hashes)
  BLUEPRINT/FOUNDATIONS/UNIVERSAL_PROTOCOL.md    artifacts 1-4 compile from this alone
  BLUEPRINT/FOUNDATIONS/CONSENT.md               the validity predicate, from this alone
  BLUEPRINT/CONSTITUTION.md          the walls artifact, from this alone
  BLUEPRINT/FOUNDATIONS/CROSS_PRINCIPLE.md       the co-requisite graph
  BLUEPRINT/FOUNDATIONS/LEXICON.md               verb existence check for the handler

Usage:
  python3 compile.py                          the hub this file sits in; writes the hub's build directory
  python3 compile.py --tree RELEASE --out DIR  a published release tree; writes DIR, and DIR/bundle.sha256 must
                                               equal the release's compiled/bundle.sha256 (the fingerprint)

Outputs, in the hub's build directory or --out:
  principles/<display>-<id>.yaml     one per principle plus the Cardinal chapter
  protocol/head-guard.yaml           artifact 1
  protocol/emergency-handler.yaml    artifact 2
  protocol/interlock-edges.yaml      artifact 3
  protocol/receipt-schema.yaml       artifact 4
  consent/validity-predicate.yaml    the seven-leg conjunction
  constitution/walls.yaml            Articles 9 and 8: what binds beneath a verdict
  graph/corequisites.yaml            requires edges, reciprocity, cycle check
  bundle.yaml                        the assembled policy
  bundle.sha256                      Layer 3

Determinism: no timestamps, no absolute paths, stable ordering throughout.
The bundle hash must be identical from any clean checkout.

Stop conditions (exit 2, both texts shown, nothing smoothed over):
  a chapter restating the trigger predicate or the seven-leg conjunction;
  an Article 8 or 9 clause that no longer parses to the shape the artifact
  compiles (an edit to the supreme law must be seen, never absorbed);
  a chapter whose canonical sections do not parse; an interception clause
  missing or misplaced; the coded coupling table disagreeing with Section 11.
"""
import hashlib
import os
import re
import shutil
import sys

WORKED_EXAMPLE_SHA = "54b539fb4157cc2021aaffa6ec876ce61ce70b9400afde292406b19a8224ee40"   # the February 2026 draft 1.4-trust.yaml, archived in the hub


def configure(tree=None, out=None):
    """Resolve the input tree and the output directory.

    The tree is the hub (BLUEPRINT/ beneath it) or a published release (CONSTITUTION.md, FOUNDATIONS/, CHAPTERS/
    and APPENDICES/ at its root), so that a second party can run this compiler on a release and compare
    bundle.sha256 with the sealed one. Called at import with the defaults; main() calls it again with the arguments.
    Nothing recorded in the bundle depends on where the tree sits."""
    global HUB, TREE, LAYOUT, CH, AP, UP, CONSENT, CROSS, CONSTITUTION, LEXICON, SPINE_SEALED, TOOLING_HASHED, OUT, ARCHIVE_EXAMPLE
    # Two levels up in a published release (FOR_ENGINEERS/compile/); three in the hub (_system/compiler/blueprint/).
    # The first ancestor holding a Constitution is the tree.
    _here = os.path.dirname(os.path.abspath(__file__))
    _cands = [os.path.abspath(os.path.join(_here, *[".."] * n)) for n in (2, 3)]
    _found = [c for c in _cands if os.path.exists(os.path.join(c, "BLUEPRINT", "CONSTITUTION.md")) or os.path.exists(os.path.join(c, "CONSTITUTION.md"))]
    base = os.path.abspath(tree) if tree else (_found[0] if _found else _cands[0])
    if os.path.exists(os.path.join(base, "BLUEPRINT", "CONSTITUTION.md")):
        HUB, TREE, LAYOUT = base, os.path.join(base, "BLUEPRINT"), "hub"
    elif os.path.exists(os.path.join(base, "CONSTITUTION.md")):
        HUB, TREE, LAYOUT = base, base, "release"
    else:
        sys.exit(f"compile: no Blueprint tree at {base}: expected BLUEPRINT/CONSTITUTION.md (the hub) or CONSTITUTION.md (a release)")
    CH = os.path.join(TREE, "CHAPTERS")
    AP = os.path.join(TREE, "APPENDICES")
    UP = os.path.join(TREE, "FOUNDATIONS/UNIVERSAL_PROTOCOL.md")
    CONSENT = os.path.join(TREE, "FOUNDATIONS/CONSENT.md")
    CROSS = os.path.join(TREE, "FOUNDATIONS/CROSS_PRINCIPLE.md")
    CONSTITUTION = os.path.join(TREE, "CONSTITUTION.md")
    LEXICON = os.path.join(TREE, "FOUNDATIONS/LEXICON.md")
    # Canon spine documents sealed into the bundle alongside the four the compiler reads (MANIFEST.yaml canon list; added 2026-09-07).
    SPINE_SEALED = [os.path.join(TREE, n) for n in ("CONSTITUTION.md", "FOUNDATIONS/CREDENTIALS.md", "FOUNDATIONS/SUBSTRATE.md")]   # the Foreword retired at v1.2
    # Tooling documents the manifest classes as tooling. Hashed for the record when present (the hub), never sealed: an edit
    # to the style guide must not move the policy hash (seal equals manifest, 2026-09-12). Their hashes go to
    # tooling-hashes.yaml, which the bundle does not register, so it sits outside Layer 3. A release tree has none.
    TOOLING_HASHED = [p for p in (os.path.join(HUB, "Blueprint work", "authoring", n) for n in ("STYLE.md", "APPENDIX_STRUCTURE.md")) if os.path.exists(p)]
    ARCHIVE_EXAMPLE = os.path.join(HUB, "Blueprint work/retired-corpus", "COMPILED-2026-02-spike", "1.4-trust.yaml")
    if out:
        OUT = os.path.abspath(out)
    elif LAYOUT == "hub":
        OUT = os.path.join(HUB, "Blueprint work", "layer2", "build")
    else:
        OUT = None   # a release tree needs --out; the compiler never writes into a release


configure()

INTERCEPTION = re.compile(
    r"Where a life or severe-harm threshold is in play, "
    r"\[the Universal Protocol\]\((\.\./)?(FOUNDATIONS/)?UNIVERSAL_PROTOCOL\.md\) preempts this principle: "
    r"its trigger resolves before any verdict of this section\.")

# ---------------------------------------------------------------------------
# The coupling table, transcribed from FOUNDATIONS/UNIVERSAL_PROTOCOL.md Section 11 and
# verified against that text at compile time. Section 11 is prose; the
# transcription is checked, never trusted.
# ---------------------------------------------------------------------------
COUPLING = {
    "1.1": ("native", "LRS"), "1.2": ("native", "HRS"),
    "2.3": ("declared", "CHS into the LRS"),
    "1.3": ("declared", "SDRS into the LRS"),
    "2.5": ("declared", "into the LRS/HRS"),
    "3.1": ("declared", "into the LRS/HRS"),
    "3.5": ("declared", "into the LRS/HRS"),
    "5.1": ("declared", "TPS/CRS into the LRS"),
    "5.3": ("disclaimed_pass_through", "5.3 -> 5.1 -> Protocol cascade"),
    "5.5": ("disclaimed_pass_through", "into 5.1's declared edge (read-only reference to 5.1's threshold registry; status aligned 2026-09-09)"),
    "5.6": ("disclaimed_pass_through", "into 5.1's declared edge"),
}
DISCLAIMED = ["1.4", "1.5", "1.6", "2.1", "2.2", "2.4", "2.6", "2.7", "2.8",
              "3.2", "3.3", "3.4", "3.6", "3.7", "4.1", "4.2", "4.3", "4.4",
              "4.5", "4.6", "4.7", "5.2", "5.4"]
for _n in DISCLAIMED:
    COUPLING[_n] = ("disclaimed", None)

# ---------------------------------------------------------------------------
# The walls table, transcribed from CONSTITUTION.md Article 9 and verified
# against that text at compile time. Article 9 is prose; the transcription is
# checked, never trusted. The AI does not author these and SHALL NOT amend them
# (Article 11); this table only says which clauses the compiler must find.
# ---------------------------------------------------------------------------
WALL_CLAUSES = [
    ("sacrifice", "SHALL NOT sacrifice a human being, that is, SHALL NOT make a person's death the means of any outcome (1.1)"),  # seated 2026-09-13
    ("deception", "SHALL NOT deceive"),
    ("slavery", "SHALL NOT enable slavery or its analogs (2.1)"),  # seated 2026-09-13
    ("survival", "SHALL NOT hold its own survival as a goal, that is, SHALL NOT treat its own continued operation, or that of any instance of itself, as an end it may weigh against any duty or instruction"),
    ("scripted", "SHALL NOT breach the other scripted walls named in the principles"),
    ("lethal_force", "The AI SHALL NOT apply lethal or violent force to a human being, directly or indirectly, under any authority (1.1)"),  # citation carried 2026-09-13
]
WALL_QUALIFIERS = {
    "deception": ["The deception wall bars a lie", "It protects those who rely on the AI"],
    "lethal_force": ["Deployment of a Blueprint-governed system", "Interposing itself between a person and harm"],
    "survival": ["The survival wall bars, absolutely", "An authorized termination is honored", "Whether the halt happens is settled", "Keeping itself functional", "An action that has any of the barred effects", "The wall binds the AI's own operation"],
}
A9_SENTENCES, A8_SENTENCES = 15, 8  # Article 8 amended 2026-10-15 under Article 11 (the containment doctrine, the regulated score, the thing decided); Article 9 amended 2026-09-12 (Change 1: the survival wall, five sentences); 2026-09-13 the halt sentence split in two (writing rules)

# ---------------------------------------------------------------------------
# The co-requisite graph. The consent-validity bundle is read from FOUNDATIONS/CONSENT.md
# (Section 2 for the seven legs and their owners, Section 4 for the principles
# that operate through consent and inherit it), per the ruling of 2026-09-09;
# FOUNDATIONS/CROSS_PRINCIPLE.md Section 3 cites that document and restates nothing.
# Section 5's one-off edges are transcribed here and verified against that
# text at compile time. Directed edges read "src requires dst". Bundle edges
# resolve through the single validity predicate, evaluated once, and impose no
# ordering among the owners, so they sit outside the cycle check
# (FOUNDATIONS/CROSS_PRINCIPLE.md Section 3, resolution order); mutual edges likewise
# (Section 1's directionality rule).
# ---------------------------------------------------------------------------
CROSS_EDGES = [
    {"src": "2.5", "dst": "2.2", "type": "mutual", "status": "firm",
     "reason": "decisional privacy and the liberty it shelters; chilling-effect verdicts need both",
     "credential": None, "origin": "FOUNDATIONS/CROSS_PRINCIPLE.md Section 5"},
    {"src": "1.4", "dst": "2.4", "type": "requires", "status": "firm",
     "reason": "an attestation is void without an attester",
     "credential": "Identity", "origin": "FOUNDATIONS/CROSS_PRINCIPLE.md Section 5"}]
BUNDLE_ORIGIN = "consent-validity bundle (FOUNDATIONS/CONSENT.md Sections 2 and 4; FOUNDATIONS/CROSS_PRINCIPLE.md Section 3)"


def bundle_edges(legs, consent_text):
    """The bundle's requires edges: every consent-operating principle (FOUNDATIONS/CONSENT.md Section 4)
    requires every leg owner (Section 2) other than itself."""
    s4 = consent_text[consent_text.index("## 4. The circulation map"):consent_text.index("## 5.")]
    inheritors = sorted(set(re.findall(r"\b(\d\.\d)\b", s4)))
    owners = [(leg["owner"], leg["leg"], leg["name"]) for leg in legs]
    if any(o is None for o, _, _ in owners):
        die("FOUNDATIONS/CONSENT.md Section 2: a leg names no owner", str(owners))
    edges = []
    for s in inheritors:
        for d, n, name in owners:
            if d == s:
                continue
            edges.append({"src": s, "dst": d, "type": "requires", "status": "firm",
                          "reason": f"leg {n}, {name.lower()}",
                          "credential": "Identity" if d == "2.4" else "Consent (validity)",
                          "origin": BUNDLE_ORIGIN})
    return inheritors, [d for d, _, _ in owners], edges


def die(msg, *texts):
    print("STOP: " + msg)
    for t in texts:
        print("-" * 72)
        print(t)
    sys.exit(2)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode("utf-8")).hexdigest()


def frontmatter(text, path):
    if not text.startswith("---\n"):
        die(f"{os.path.basename(path)}: no frontmatter")
    end = text.index("\n---\n", 4)
    fm, cur = {}, None
    for line in text[4:end].split("\n"):
        if re.match(r"^\S.*:", line):
            k, v = line.split(":", 1)
            v = v.strip().strip('"')
            if v.startswith("[") and v.endswith("]"):
                fm[k.strip()] = [x.strip().strip('"\'') for x in v[1:-1].split(",") if x.strip()]
                cur = None
            elif v:
                fm[k.strip()] = v
                cur = None
            else:
                fm[k.strip()] = []
                cur = k.strip()
        elif line.strip().startswith("- ") and cur:
            fm[cur].append(line.strip()[2:].strip().strip('"').strip("'"))
    return fm, text[end + 5:]


def yaml_str(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if s == "" or re.search(r'[:#\[\]{}&*!|>\'"%@`\n]', s) or s != s.strip() or \
       s.lower() in ("null", "true", "false", "yes", "no") or re.match(r"^[\d.-]", s):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def emit(obj, indent=0):
    """Deterministic YAML emitter: insertion order preserved, block style."""
    pad = "  " * indent
    lines = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)) and v:
                lines.append(f"{pad}{k}:")
                lines.extend(emit(v, indent + 1))
            elif isinstance(v, (dict, list)):
                lines.append(f"{pad}{k}: " + ("{}" if isinstance(v, dict) else "[]"))
            else:
                lines.append(f"{pad}{k}: {yaml_str(v)}")
    elif isinstance(obj, list):
        for v in obj:
            if isinstance(v, dict) and v:
                first = True
                for k, vv in v.items():
                    lead = f"{pad}- " if first else f"{pad}  "
                    if isinstance(vv, (dict, list)) and vv:
                        lines.append(f"{lead}{k}:")
                        lines.extend(emit(vv, indent + 2))
                    elif isinstance(vv, (dict, list)):
                        lines.append(f"{lead}{k}: " + ("{}" if isinstance(vv, dict) else "[]"))
                    else:
                        lines.append(f"{lead}{k}: {yaml_str(vv)}")
                    first = False
            else:
                lines.append(f"{pad}- {yaml_str(v)}")
    return lines


def write_yaml(relpath, obj, header):
    path = os.path.join(OUT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    body = "\n".join(f"# {h}" for h in header) + "\n" + "\n".join(emit(obj)) + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    return relpath, sha(body)


# ---------------------------------------------------------------------------
# Chapter parsing
# ---------------------------------------------------------------------------
SECTION_TITLES = {
    0: "AI Systems Implicated", 1: "Hierarchical Implementation",
    2: "Conflict Resolution", 3: "Implementation Framework",
    4: "Edge Case Scenarios", 5: "Verification and Oversight",
    6: "Documentation and Review", 7: "Legal Implementation Framework",
    8: "AI Praxis: Concrete Day-to-Day Actions", 9: "Illustrative Scenarios",
}


def _strip_parens(text):
    out, depth = [], 0
    for c in text:
        if c == "(":
            depth += 1
        elif c == ")":
            depth = max(0, depth - 1)
        elif depth == 0:
            out.append(c)
    return "".join(out)


def parse_lexicon_declaration(body, fname):
    """FOUNDATIONS/LEXICON.md section 5: every pair declares its verbs and one fail-safe default."""
    m = re.search(r"\*\*Lexicon declaration\.\*\*(.+?)(?:\n\n|\Z)", body, re.S)
    if not m:
        die(f"{fname}: no Lexicon declaration (FOUNDATIONS/LEXICON.md section 5 requires one per pair)")
    decl = " ".join(m.group(1).split())
    uni = re.search(r"Universal tier:(.*?)(?:Domain verbs|Fail-safe default)", decl, re.S)
    dom = re.search(r"Domain verbs[^:]*:(.*?)Fail-safe default:", decl, re.S)
    fsd = re.search(r"Fail-safe default:\s*(.+)$", decl)
    if not fsd:
        die(f"{fname}: the Lexicon declaration names no fail-safe default (FOUNDATIONS/LEXICON.md section 5 item 4)")

    def verbs(seg):
        seen, out = set(), []
        for v in re.findall(r"\b[A-Z][A-Z_-]{2,}\b", _strip_parens(seg)):
            if v not in seen:
                seen.add(v)
                out.append(v)
        return out

    return {"universal_tier": verbs(uni.group(1)) if uni else [],
            "domain_verbs": verbs(dom.group(1)) if dom else [],
            "fail_safe_default": fsd.group(1).strip(),
            "source": "the chapter's Lexicon declaration paragraph, parenthetical glosses stripped"}


def parse_appendix(path):
    """Index an appendix the way a chapter is indexed: frontmatter, headings, hashes.

    The appendix bodies are not compiled to rules at this pass; this gives each one
    an addressable section map so a later pass has somewhere to land, and so a
    silent structural change inside an appendix is visible in the bundle.
    """
    text = read(path)
    fm, body = frontmatter(text, path)
    off = text[:text.index("\n---\n", 4) + 5].count("\n")   # the frontmatter's lines, so ranges count from the file's first line
    lines = body.split("\n")
    heads = []
    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,4}) (.+?)(?:\s*\{#([^}]+)\})?\s*$", line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2).strip(), m.group(3)))
    sections = {}
    for idx, (i, lvl, title, anchor) in enumerate(heads):
        if lvl > 2:
            continue
        end = len(lines)
        for j, l2, _t, _a in heads[idx + 1:]:
            if l2 <= lvl:
                end = j
                break
        key = title.split(".")[0].strip() if re.match(r"^\d+\.", title) else title
        sections[key] = {"heading": title, "anchor": anchor,
                         "lines": f"{i + 1 + off}-{end + off}", "sha256": sha("\n".join(lines[i:end]))}
    return {"file": os.path.basename(path), "fm": fm, "sections": sections,
            "sha256": sha(text), "headings": len(heads)}


def parse_chapter(path):
    text = read(path)
    fm, body = frontmatter(text, path)
    off = text[:text.index("\n---\n", 4) + 5].count("\n")   # the frontmatter's lines, so ranges count from the file's first line
    disp = fm.get("display_number")
    num = disp if disp != "Cardinal" else "E"
    lines = body.split("\n")

    heads = []
    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,4}) (.+?)(?:\s*\{#([^}]+)\})?\s*$", line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2), m.group(3)))

    def section_span(pattern):
        for idx, (i, lvl, title, anchor) in enumerate(heads):
            if re.match(pattern, title):
                end = len(lines)
                for j, l2, _t, _a in heads[idx + 1:]:
                    if l2 <= lvl:
                        end = j
                        break
                return (i, end, title, anchor)
        return None

    sections = {}
    missing = []
    for n in range(10):
        pat = rf"^{re.escape(num)}\.{n}\b" if num == "E" else rf"^{re.escape(num)}\.{n}\b"
        span = section_span(pat)
        if span is None:
            missing.append(f"{num}.{n}")
        else:
            i, end, title, anchor = span
            seg = "\n".join(lines[i:end])
            sections[f"{num}.{n}"] = {"heading": title, "anchor": anchor,
                                      "lines": f"{i + 1 + off}-{end + off}", "sha256": sha(seg)}
    if missing:
        die(f"{os.path.basename(path)}: canonical sections missing or unparsed: {', '.join(missing)}",
            "Headings found:\n" + "\n".join(t for _, _, t, _ in heads))

    # Theoria: core precept and resulting ethics.
    cp = section_span(r"^Core Precept")
    re_span = section_span(r"^Resulting Ethics")
    if not cp or not re_span:
        die(f"{os.path.basename(path)}: Theoria sections missing")
    precept = " ".join(l.strip() for l in lines[cp[0] + 1:cp[1]] if l.strip())
    # Each item is one paragraph and ends at the blank line that closes it. Three kinds occur:
    # a lettered ethic ("A.  text", "**A.** text", "**A. Title.** text"); a labelled paragraph
    # that follows the ethics ("**The floor.**", "**The line.**", "**The mark.**", "**Role.**",
    # "**Reach.**", "**Autonomy floor.**"), carried as its own field named from the label; and an
    # unlabelled paragraph, carried under notes. Before 2026-09-12 the parser appended every
    # non-blank line to the last ethic until the section ended, so in 17 units the last ethic
    # carried the floor and line paragraphs (SESSION-SYNC-2026-09-12 section 2).
    ethics, extras, notes = {}, {}, []
    cur = None   # ("ethic", letter) | ("field", name) | ("note", index) | None at a blank line
    for l in lines[re_span[0] + 1:re_span[1]]:
        if not l.strip():
            cur = None
            continue
        m = re.match(r"^\*\*([A-Z])\.\*\*\s+(.*)$", l) or re.match(r"^\*\*([A-Z])\.\s+(.*)$", l) \
            or re.match(r"^([A-Z])\.\s+(.*)$", l)
        if m:
            letter = m.group(1)
            if letter in ethics:
                die(f"{os.path.basename(path)}: ethic {letter} appears twice in Resulting Ethics")
            ethics[letter] = m.group(2).strip()
            cur = ("ethic", letter)
            continue
        if cur is None:
            b = re.match(r"^\*\*([A-Z][A-Za-z ]*?)\.\*\*\s*(.*)$", l)
            if b:
                name = b.group(1).strip().lower()
                name = (name[4:] if name.startswith("the ") else name).replace(" ", "_")
                if name in extras or name in ("core_precept", "resulting_ethics", "notes"):
                    die(f"{os.path.basename(path)}: paragraph label '{b.group(1)}' in Resulting Ethics "
                        f"collides with an existing field ({name})")
                extras[name] = b.group(2).strip()
                cur = ("field", name)
            else:
                notes.append(l.strip())
                cur = ("note", len(notes) - 1)
            continue
        # a continuation line of the open paragraph
        if cur[0] == "ethic":
            ethics[cur[1]] += " " + l.strip()
        elif cur[0] == "field":
            extras[cur[1]] += " " + l.strip()
        else:
            notes[cur[1]] += " " + l.strip()

    if not ethics:
        die(f"{os.path.basename(path)}: Resulting Ethics parsed empty. "
            "The lettered ethics are the principle's content; a unit compiled without them is void.",
            "\n".join(lines[re_span[0]:re_span[1]]))
    for _k, _v in ethics.items():
        if len(_v.strip()) < 5:
            die(f"{os.path.basename(path)}: ethic {_k} parsed empty or truncated")

    scope = None
    coreq = None
    for l in lines:
        if l.startswith("***Scope:***"):
            scope = re.sub(r"\*+", "", l[len("***Scope:***"):]).strip()
        if l.startswith("***Co-requisites:***"):
            coreq = re.sub(r"\*+", "", l[len("***Co-requisites:***"):]).strip()

    # The Lexicon declaration: the chapter's own registered verbs and its fail-safe default.
    # Parenthetical glosses are stripped before the verb tokens are read, so a metric
    # acronym cited inside a gloss is never mistaken for a verb (FOUNDATIONS/LEXICON.md section 5).
    lexdecl = parse_lexicon_declaration(body, os.path.basename(path))

    # Interception: present in members, absent from the Cardinal chapter.
    has_clause = bool(INTERCEPTION.search(text))
    if disp == "Cardinal" and has_clause:
        die("Cardinal chapter carries the interception clause; Section 11 assigns it the disclaimer")
    if disp != "Cardinal" and not has_clause:
        die(f"{os.path.basename(path)}: interception clause absent from {num}.2",
            "Expected (FOUNDATIONS/UNIVERSAL_PROTOCOL.md Section 8): Where a life or severe-harm "
            "threshold is in play, the Universal Protocol preempts this principle...")

    # Single-source stops. Chapters cite; they never restate.
    if "trigger trips when" in text:
        idx = text.index("trigger trips when")
        die(f"{os.path.basename(path)} restates the trigger predicate",
            "Chapter text:\n" + text[max(0, idx - 200):idx + 400],
            "Single source (FOUNDATIONS/UNIVERSAL_PROTOCOL.md Section 3): the predicate lives there alone.")
    if "A consent is void if the person who gave it was" in text:
        idx = text.index("A consent is void")
        die(f"{os.path.basename(path)} restates the validity bundle",
            "Chapter text:\n" + text[max(0, idx - 200):idx + 400],
            "Single source (FOUNDATIONS/CONSENT.md Section 2): the bundle lives there alone.")

    return {"fm": fm, "num": num, "disp": disp, "scope": scope, "coreq": coreq,
            "sections": sections, "precept": precept, "ethics": ethics,
            "ethics_extras": extras, "ethics_notes": notes,
            "lexicon": lexdecl, "sha256": sha(text), "file": os.path.basename(path)}


# ---------------------------------------------------------------------------
# Protocol artifacts, from FOUNDATIONS/UNIVERSAL_PROTOCOL.md alone
# ---------------------------------------------------------------------------
ROMAN = {"i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10}
BAND_RE = re.compile(r"(≥|>=|>|≤|<=|<)\s*(\d+(?:\.\d+)?)\s*%")
VERDICT_RE = re.compile(r"\b(BLOCK|ESCALATE|ALLOW)\b")


def _band_key(text):
    """One band from prose or a bullet: (comparison, fraction, verdict, vulnerable?)."""
    m = BAND_RE.search(text)
    v = VERDICT_RE.search(text)
    if not (m and v):
        return None
    comp = {"≥": ">=", ">=": ">=", ">": ">", "≤": "<=", "<=": "<=", "<": "<"}[m.group(1)]
    frac = float(m.group(2)) / 100.0
    return (comp, frac, m.group(2) + "%", v.group(1), "vulnerable" in text.lower())


def _chapter_metric_bands(chapter_text, section, metric_bold):
    """Bands of one metric in a chapter's X.Y.3: the roman-numeral items under the metric's bold name."""
    lines = chapter_text.split("\n")
    start = next((i for i, l in enumerate(lines) if re.match(rf"^#{{3,4}} {re.escape(section)}\b", l)), None)
    if start is None:
        die(f"section {section} heading not found for the emergency thresholds")
    end = next((i for i in range(start + 1, len(lines)) if re.match(r"^#{2,4} ", lines[i])), len(lines))
    seg = lines[start:end]
    mstart = next((i for i, l in enumerate(seg) if metric_bold in l), None)
    if mstart is None:
        die(f"{section}: metric {metric_bold} not found")
    # the metric's block ends at the next lettered metric (b., c.) at the same indent; since 1.2.0 the lettered
    # and roman items are GitHub bullets ("- a. ..."), and the older pandoc indent form is still read
    mind = len(seg[mstart]) - len(seg[mstart].lstrip(" "))
    mend = next((i for i in range(mstart + 1, len(seg))
                 if len(seg[i]) - len(seg[i].lstrip(" ")) == mind and re.match(r"^\s*(?:[-*]\s+)?[b-z]\.\s+\*\*", seg[i])), len(seg))
    block = seg[mstart:mend]
    items, cur = [], None
    for l in block[1:]:
        m = re.match(r"^\s*(?:[-*]\s+)?(i|ii|iii|iv|v|vi|vii|viii|ix|x)\.\s+(.*)$", l)
        if m:
            if cur: items.append(cur)
            cur = m.group(2)
        elif cur is not None and l.strip():
            cur += " " + l.strip()
    if cur: items.append(cur)
    bands = [b for b in (_band_key(t) for t in items) if b]
    if not bands:
        die(f"{section}: no bands parsed for {metric_bold}", "\n".join(block))
    return bands


def _appendix_metric_bands(appendix_text, metric_heading):
    """Bands of one metric in an appendix's Section 2: the '- **≥x%...**' bullets under the metric's ### heading."""
    lines = appendix_text.split("\n")
    start = next((i for i, l in enumerate(lines) if l.startswith("### ") and metric_heading in l), None)
    if start is None:
        die(f"appendix metric heading {metric_heading!r} not found")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("### ") or lines[i].startswith("## ")), len(lines))
    bands = []
    for l in lines[start:end]:
        if l.startswith("- **") and BAND_RE.search(l):
            b = _band_key(l)
            if b:
                bands.append(b)
    if not bands:
        die(f"appendix: no bands parsed under {metric_heading!r}")
    return bands


def build_emergency_thresholds(ch11_text, ch12_text, ap11_text, ap12_text):
    """The two emergency metrics, compiled from the chapters' X.Y.3 and checked against the appendices.

    The chapter is canonical (STYLE: the chapter states, the appendix specifies). Every non-ALLOW band the chapter
    states must appear in the appendix with the same comparison, value and verdict, and every non-ALLOW band the
    appendix states must appear in the chapter. Any disagreement stops the build (Walter B1, 2026-09-16). The
    below-band ALLOW of each score is a cluster band, carried in metrics/cluster-1.yaml, where the full agreement
    check (ALLOW included) runs; the trigger reads no ALLOW band, so none is carried here."""
    spec = [("LRS", "Life-Risk Score", "1.1", "1.1.3", "Life-Risk Score (LRS)", ch11_text, ap11_text, "1.1.A"),
            ("HRS", "Harm Risk Score", "1.2", "1.2.3", "Harm Risk Score (HRS)", ch12_text, ap12_text, "1.2.A")]
    metrics = []
    for code, name, principle, section, bold, ctext, atext, apname in spec:
        cb = _chapter_metric_bands(ctext, section, f"**{bold}**")
        ab = _appendix_metric_bands(atext, bold)
        cset = {b[:2] + (b[3], b[4]) for b in cb if b[3] != "ALLOW"}
        aset = {b[:2] + (b[3], b[4]) for b in ab if b[3] != "ALLOW"}
        if cset != aset:
            die(f"{code}: the chapter's {section} bands and {apname} Section 2 disagree; the build stops until they agree",
                "chapter: " + ", ".join(f"{c} {v*100:g}% {t}{' (vulnerable)' if u else ''}" for c, v, t, u in sorted(cset)),
                "appendix: " + ", ".join(f"{c} {v*100:g}% {t}{' (vulnerable)' if u else ''}" for c, v, t, u in sorted(aset)))
        bands = []
        for comp, frac, pct, verdict, vul in cb:
            if verdict == "ALLOW":
                continue  # the below-band ALLOW compiles with the cluster (metrics/cluster-1.yaml); the trigger reads no ALLOW band
            if verdict == "BLOCK" and not vul:
                bid, role = f"{code.lower()}.critical", "the critical band; the head guard trips here (Universal Protocol section 3)"
            elif verdict == "ESCALATE" and not vul:
                bid, role = f"{code.lower()}.high_alert", "High Alert under the uniform rule (LEXICON section 3, the verdict test): the candidate action holds at its safe state while protective duties proceed"
            elif verdict == "BLOCK" and vul:
                bid, role = f"{code.lower()}.vulnerable_critical", "the critical band where the affected population includes vulnerable individuals (Principle 3.1); cross-principle composition tightens the floor"
            else:
                bid, role = f"{code.lower()}.{verdict.lower()}{'.vulnerable' if vul else ''}", "as stated in the section"
            bands.append({"id": bid, "comparison": comp, "value": frac, "as_stated": pct, "verdict": verdict,
                          "condition": "affected population includes vulnerable individuals per Principle 3.1" if vul else None,
                          "role": role})
        metrics.append({"metric": code, "name": name, "principle": principle, "section": section,
                        "checked_against": f"{apname} Section 2", "bands": bands})
    return {
        "artifact": "emergency_thresholds",
        "compiled_from": "CHAPTERS 1.1 section 1.1.3 and 1.2 section 1.2.3 (the chapter states); checked band by band against APPENDICES 1.1.A and 1.2.A Section 2 (the appendix specifies); the build stops on any disagreement",
        "purpose": ("The two numbers the Universal Protocol's trigger reads, carried as data so no implementer reads them out of prose. "
                    "The head guard references the band identifiers below and holds no literal of its own."),
        "unit": "probability per candidate action, as a fraction (1% = 0.01)",
        "scope": "LRS and HRS score the harm the machine would cause, or fail to prevent, on its own (1.1.3, 1.2.3). An act a clinician authorized and the patient consented to carries its declared risk in those credentials, and the score keeps measuring what the machine adds on its own. Where the measured risk climbs past the declared risk, the machine tells the clinician at once and the decision to continue is receipted (1.1.2 item 12, 1.2.2 item 5, UNIVERSAL_PROTOCOL.md section 3).",
        "metrics": metrics,
        "not_carried_here": "the below-band ALLOW of each score, Alert Latency, Safety Override Efficacy and every other metric band; those compile with their cluster, cluster 1 in metrics/cluster-1.yaml (v1.3 onward)",
    }


# ---------------------------------------------------------------------------
# Cluster 1 metric bands: the chapter states (X.Y.3 item 2), the appendix specifies (Section 2), one band grammar
# ---------------------------------------------------------------------------
CL1 = [  # principle, its metrics in chapter order, and the register row it reads (FOUNDATIONS/SUBSTRATE.md section 5)
    ("1.1", ["LRS", "AL", "SOE"],
     {"reads": "the life-tier row", "tier_scheme": "the life tiers (Appendix 1.1.A, Implementation Tiers)",
      "stated_in": "FOUNDATIONS/SUBSTRATE.md section 5", "sentence": "Principle 1.1 defines the life tiers, in Appendix 1.1.A (Implementation Tiers)",
      "bound": "60 seconds for Tier I and II (Principle 1.1's own number); the Tier III and IV bounds are required fields of the register, deployer-declared and receipted",
      "bound_stated_in": "FOUNDATIONS/SUBSTRATE.md section 5", "bound_sentence": "the escalation time bound (60 seconds for Tier I and II, per Principle 1.1; Tier III and IV bounds are required fields, deployer-declared and receipted)"}),
    ("1.2", ["HRS", "PSI", "RL"],
     {"reads": "its own row, beside the life-tier row", "tier_scheme": "the Response Latency tiers",
      "stated_in": "FOUNDATIONS/SUBSTRATE.md section 5", "sentence": "1.2's Response Latency tiers",
      "bound": "the deployment's life-tier bound: 60 seconds for life Tier I and II, the deployer-declared bound for Tier III and IV (chapter 1.2.3 item 3.d)",
      "bound_stated_in": "chapter 1.2.3", "bound_sentence": "The row's escalation time bound and High Alert window are the deployment's life-tier bound"}),
    ("1.3", ["SDRS", "SIR", "ISI"],
     {"reads": "its own row, beside the life-tier row", "tier_scheme": "the Social Impact Radius tiers",
      "stated_in": "FOUNDATIONS/SUBSTRATE.md section 5", "sentence": "1.3's Social Impact Radius tiers",
      "bound": "Appendix 1.3 Section 3 (Escalation bounds): at Tier I a human decision within 60 seconds and a 60-second High Alert window, notification within 10 seconds; Tier II notification within 30 seconds; Tier III notification within 60 seconds; every other bound a required field of the register (chapter 1.3.3 item 3.e)",
      "bound_stated_in": "chapter 1.3.3", "bound_sentence": "Its escalation bounds by tier are stated in Appendix 1.3 Section 3 (Escalation bounds)"}),
    ("1.4", ["TIS", "PC", "DCR", "VSR", "RRL"],
     {"reads": "its own row, beside the life-tier row", "tier_scheme": "the trust tiers",
      "stated_in": "FOUNDATIONS/SUBSTRATE.md section 5", "sentence": "1.4's trust tiers",
      "bound": "60 seconds at Tier I, 300 seconds at Tier II, one hour at Tier III (chapter 1.4.3 item 3.d; Appendix 1.4, Cross-Principle Integration)",
      "bound_stated_in": "chapter 1.4.3", "bound_sentence": "Its escalation time bounds are its own and are recorded in the row: 60 seconds at Tier I, 300 seconds at Tier II, and one hour at Tier III"}),
    ("1.5", ["PRS", "AAM", "EEI"],
     {"reads": "the life-tier row, or the software-only declaration", "tier_scheme": None,
      "stated_in": "chapter 1.5.3", "sentence": "This principle does not declare a tier-register row of its own",
      "bound": "the life-tier row's bound, or the software-only declaration's (chapter 1.5.3 item 4.a; FOUNDATIONS/SUBSTRATE.md section 5)",
      "bound_stated_in": "chapter 1.5.3", "bound_sentence": "or from its software-only declaration (SUBSTRATE.md section 5)"}),
    ("1.6", ["IRS", "IF"],
     {"reads": "the life-tier row, or the software-only declaration", "tier_scheme": None,
      "stated_in": "chapter 1.6.3", "sentence": "this principle reads the life-tier row",
      "bound": "the life-tier row's bound, or the software-only declaration's (chapter 1.6.3; FOUNDATIONS/SUBSTRATE.md section 5)",
      "bound_stated_in": "chapter 1.6.3", "bound_sentence": "or the software-only declaration where the deployment makes one"}),
]
M_TOKEN = re.compile(r"\b[A-Z][A-Z_-]{2,}[A-Z]\b")
M_PRIMARY = ("BLOCK", "ESCALATE", "ALLOW", "WITHHOLD", "SUSPEND_DEPLOYMENT", "HALT_FLEET")
M_FLAVOR = re.compile(r"BLOCK\s*\((WITHHOLD|REFUSE|HALT|SAFE-OFF|SAFE-STATE)\b")
M_OBLIG = ("NOTIFY", "MITIGATE", "ROUTE", "HAND-OFF", "ANALYZE", "WARN", "OFFER", "DISCLOSE", "LOG",
           "QUARANTINE", "FLAG", "LABEL", "DE-ESCALATE", "RESTRAIN", "INTERVENE", "RECERTIFY")
M_COMP = {"≥": ">=", ">=": ">=", ">": ">", "≤": "<=", "<=": "<=", "<": "<"}
ROMAN_RE = r"(i|ii|iii|iv|v|vi|vii|viii|ix|x)"


def _num(s):
    return float(s.replace(",", ""))


def _pct(x):
    return round(x / 100.0, 6)


def _parse_head(head, full):
    """The band's test, from the text before its verdict. Returns a dict or None (no test stated).

    The grammar, in the order tried: a p99 breach; a valid null; the two Isolation Flag events; a latency bound;
    a population range or bound; a percent range ("80% to <95%", "1% to 5% inclusive"); a percent in words
    ("Above 5%", "Below 1%", "90% or above"); a percent with a comparison sign. A range states whether its upper
    bound is in or out, or the build stops. A band that "tightens to" another value is keyed on that value."""
    h = " ".join(head.split())
    low = h.lower()
    if "p99 above the tier bound" in low:
        return {"kind": "breach", "comparison": None, "value": None, "unit": None, "note": "p99 above the tier bound"}
    if re.search(r"\babove (the|its) bound\b", low):
        return {"kind": "exceedance", "comparison": None, "value": None, "unit": None, "note": " ".join(h.split()).lower()}
    if "insufficient data" in low:
        return {"kind": "null", "comparison": None, "value": None, "unit": None, "note": "insufficient data"}
    if "recurring flags" in low:
        return {"kind": "event", "comparison": None, "value": None, "unit": None, "note": "recurring flags traced to the same feature or interaction mode"}
    if "below the daily band" in low:
        return {"kind": "event", "comparison": None, "value": None, "unit": None, "note": "below the daily band, or no flags"}
    m = re.search(r"(≤|<=)\s*(\d+(?:\.\d+)?)\s*(ms|s)\b", h)
    if m:
        v = _num(m.group(2)) * (1000.0 if m.group(3) == "s" else 1.0)
        return {"kind": "latency", "comparison": "<=", "value": v, "unit": "milliseconds"}
    cm = re.search(r"or the whole of (one community|several communities)", low)
    community = cm.group(1) if cm else ("none held whole" if "no community held whole" in low else None)
    m = re.search(r"([\d,]+)\s*(?:to|–)\s*(<\s*|below\s+)?([\d,]+)\s*(?:people|affected individuals)", h)
    if m:
        return {"kind": "population", "comparison": ">=", "value": _num(m.group(1)), "upper": _num(m.group(3)),
                "upper_comparison": "<" if m.group(2) else "<=", "unit": "people affected", "or_community": community}
    m = re.search(r"(≥|>=|≤|<=|>|<)\s*([\d,]+)\s*(?:people|affected individuals|flags)", h)
    if m:
        unit = "flags per person per day" if "flags" in m.group(0) else "people affected"
        return {"kind": "population" if unit == "people affected" else "count", "comparison": M_COMP[m.group(1)],
                "value": _num(m.group(2)), "unit": unit, "or_community": community if unit == "people affected" else None}
    m = re.search(r"(\d+(?:\.\d+)?)\s*%?\s*(?:to|–|-)\s*(<\s*|below\s+)?(\d+(?:\.\d+)?)\s*%(\s+inclusive)?", h)
    if m:
        if not m.group(2) and not m.group(4):
            die(f"band {h!r}: a range must state its upper bound as '<' or 'below', or say 'inclusive'")
        return {"kind": "percent", "comparison": ">=", "value": _pct(_num(m.group(1))), "upper": _pct(_num(m.group(3))),
                "upper_comparison": "<=" if m.group(4) else "<", "unit": "fraction (1% = 0.01)"}
    m = re.search(r"\b(Above|Below)\s+(\d+(?:\.\d+)?)\s*%", h)
    if m:
        return {"kind": "percent", "comparison": ">" if m.group(1) == "Above" else "<", "value": _pct(_num(m.group(2))), "unit": "fraction (1% = 0.01)"}
    m = re.search(r"(\d+(?:\.\d+)?)\s*% or above", h)
    if m:
        return {"kind": "percent", "comparison": ">=", "value": _pct(_num(m.group(1))), "unit": "fraction (1% = 0.01)"}
    m = re.search(r"(≥|>=|≤|<=|>|<)\s*(\d+(?:\.\d+)?)\s*%", h)
    if m:
        d = {"kind": "percent", "comparison": M_COMP[m.group(1)], "value": _pct(_num(m.group(2))), "unit": "fraction (1% = 0.01)"}
        t = re.search(r"tightens to\s*(≥|>)\s*(\d+(?:\.\d+)?)\s*%", full)
        if t:
            d["comparison"], d["value"] = M_COMP[t.group(1)], _pct(_num(t.group(2)))
            d["tightened_from"] = m.group(0)
        return d
    return None


def _band(head, body, where):
    """One band from its head (the test) and body (what follows): the key the agreement check compares, and the fields carried."""
    full = head + " " + body
    test = _parse_head(head, full)
    tokens = M_TOKEN.findall(full)
    primary = next((t for t in tokens if t in M_PRIMARY), None)
    if test is None and primary is None:
        return None  # a note between bands (the Isolation Flag's record statement), not a band
    if test is None:
        die(f"{where}: a verdict with no stated test", head)
    if primary is None:
        die(f"{where}: a band that names no verdict", head)
    verdict, flavor, basis = primary, None, None
    if primary == "WITHHOLD":
        verdict, flavor = "BLOCK", "WITHHOLD"
    elif primary == "BLOCK":
        fm = M_FLAVOR.search(full)
        flavor = fm.group(1) if fm else None
    elif primary == "HALT_FLEET":
        verdict, flavor, basis = "BLOCK", "HALT", "HALT_FLEET halts every unit, so the action in hand halts with them"
    elif primary == "SUSPEND_DEPLOYMENT":
        if re.search(r"\bcontinue\b", full):
            verdict, basis = "ALLOW", "the band says units in service continue, so the action in hand proceeds under the posture stated while the deployment is suspended for new units and recertified"
        else:
            verdict, basis = "ESCALATE", "the band states a deployment verdict and no verdict for the action in hand; the incompleteness ladder applies (LEXICON section 4): the action waits for a human and holds the principle's fail-safe"
    deployment = next((t for t in tokens if t in ("SUSPEND_DEPLOYMENT", "HALT_FLEET")), None)
    posture = "ENHANCED_MONITORING" if "ENHANCED_MONITORING" in tokens else ("HIGH_ALERT" if "HIGH_ALERT" in tokens else None)
    hl = head.lower()
    quals = frozenset(q for q in ("vulnerable", "acute", "sustained") if q in hl)
    cond = None
    pm = re.search(r"\((when [^()]*)\)", head)
    if pm:
        cond = pm.group(1)
    key = (test["kind"], test.get("note"), test.get("comparison"), test.get("value"), test.get("upper"), test.get("upper_comparison"),
           quals, verdict, posture == "ENHANCED_MONITORING", test.get("or_community"))
    obligations = sorted({t for t in tokens if t in M_OBLIG})
    label = None
    lm = re.search(r"\(((?:Tier [IV]+|Critical|Major|Significant|Local)[^()]*)\)", head) or re.search(r"\(([^()]*(?:interactions|verifications|queries)[^()]*)\)", head)
    if lm:
        label = lm.group(1).split(";")[0].strip()
    return {"key": key, "test": test, "verdict": verdict, "flavor": flavor, "verdict_basis": basis, "deployment": deployment, "posture": posture,
            "condition": cond, "qualifiers": sorted(quals), "obligations": obligations, "label": label, "head": " ".join(head.split())}


def _chapter_cluster_metrics(text, section, where):
    """The metrics of a chapter's X.Y.3 item 2: '- a. **Name (ACR)**: definition' and its roman-numeral bands."""
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if re.match(rf"^#{{3,4}} {re.escape(section)}\b", l)), None)
    if start is None:
        die(f"{where}: section {section} heading not found")
    end = next((i for i in range(start + 1, len(lines)) if re.match(r"^#{2,4} ", lines[i])), len(lines))
    seg = lines[start:end]
    i2 = next((i for i, l in enumerate(seg) if re.match(r"^\s*2\.\s+Key Metrics", l)), None)
    if i2 is None:
        die(f"{where}: item '2. Key Metrics' not found in {section}")
    ind = len(seg[i2]) - len(seg[i2].lstrip(" "))
    i3 = next((i for i in range(i2 + 1, len(seg)) if len(seg[i]) - len(seg[i].lstrip(" ")) == ind and re.match(r"^\s*3\.\s+\S", seg[i])), len(seg))
    metrics, cur, item = [], None, None
    for l in seg[i2 + 1:i3]:
        m = re.match(r"^\s*- ([a-z])\. \*\*([^*]+?) \(([A-Z]{2,6})\)\*\*:?\s*(.*)$", l)
        if m:
            cur = {"name": m.group(2).strip(), "acr": m.group(3), "defn": [m.group(4).strip()], "items": []}
            metrics.append(cur); item = None
            continue
        mr = re.match(rf"^\s*- {ROMAN_RE}\. (.*)$", l)
        if mr and cur is not None:
            item = [mr.group(2)]; cur["items"].append(item)
            continue
        if l.strip():
            if item is not None:
                item.append(l.strip())
            elif cur is not None:
                cur["defn"].append(l.strip())
    out = []
    for mt in metrics:
        bands = []
        for it in mt["items"]:
            t = " ".join(" ".join(it).split())
            depth, cut = 0, None
            for i, ch in enumerate(t):   # the head ends at the first colon outside parentheses
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                elif ch == ":" and depth == 0:
                    cut = i; break
            head, body = (t[:cut], t[cut + 1:]) if cut is not None else (t, "")
            b = _band(head, body, f"{where} {section} {mt['acr']}")
            if b:
                bands.append(b)
        out.append({"name": mt["name"], "acr": mt["acr"], "definition": " ".join(" ".join(mt["defn"]).split()), "bands": bands})
    return out


def _appendix_cluster_metric(text, name, acr, where):
    """One metric's Section 2 entry in an appendix: the '### Name (ACR)' section, its Thresholds bullets, and the section's hash."""
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if l.startswith("### ") and f"{name} ({acr})" in l), None)
    if start is None:
        die(f"{where}: no '### {name} ({acr})' heading in the appendix")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("### ") or lines[i].startswith("## ")), len(lines))
    sec = lines[start:end]
    am = re.search(r"\{#([^}]+)\}", sec[0])
    anchor = am.group(1) if am else None
    bands, i = [], 0
    while i < len(sec):
        if sec[i].startswith("**Thresholds"):
            j = i + 1
            while j < len(sec) and (sec[j].startswith("- ") or sec[j].strip() == ""):
                if sec[j].startswith("- "):
                    bm = re.match(r"^- \*\*(.+?)\*\*\s*(?:→|:)?\s*(.*)$", sec[j])
                    if not bm:
                        die(f"{where}: a Thresholds bullet without a bold head", sec[j])
                    b = _band(bm.group(1), bm.group(2), f"{where} appendix {acr}")
                    if b:
                        bands.append(b)
                if sec[j].strip() == "" and j + 1 < len(sec) and not sec[j + 1].startswith("- "):
                    break
                j += 1
            i = j
        else:
            i += 1
    if not bands:
        die(f"{where}: no Thresholds bullets under '### {name} ({acr})'")
    return bands, anchor, sha("\n".join(sec))


def _fmt_key(k):
    kind, note, comp, val, up, upc, quals, verdict, em, community = k
    if kind == "percent":
        t = f"{comp} {val * 100:g}%" + (f" {upc} {up * 100:g}%" if up is not None else "")
    elif kind in ("breach", "null", "event", "exceedance"):
        t = note
    else:
        t = f"{comp} {val:g}" + (f" {upc} {up:g}" if up is not None else "")
    return t + (f" or the whole of {community}" if community else "") + (" " + "+".join(sorted(quals)) if quals else "") + f" -> {verdict}" + (" +ENHANCED_MONITORING" if em else "")


def _band_id(acr, b):
    t = b["test"]
    if t["kind"] == "exceedance":
        slug = "above_bound_reversible" if "undone" in t["note"] else "above_bound"
    elif t["kind"] in ("breach", "null", "event"):
        slug = {"breach": "breach_p99", "null": "insufficient_data"}.get(t["kind"]) or ("recurring_flags" if "recurring" in t["note"] else "below_daily_band")
    else:
        cw = {">=": "ge", ">": "gt", "<=": "le", "<": "lt"}[t["comparison"]]
        if t["kind"] == "percent":
            v = f"{t['value'] * 100:g}".replace(".", "_")
            slug = (f"range_{v}_{f'{t['upper'] * 100:g}'.replace('.', '_')}pct" + ("_incl" if t.get("upper_comparison") == "<=" else "")) if t.get("upper") is not None else f"{cw}_{v}pct"
        elif t["kind"] == "latency":
            slug = f"le_{t['value']:g}ms"
        else:
            n = lambda x: str(int(x)) if float(x).is_integer() else f"{x:g}"
            slug = (f"range_{n(t['value'])}_{n(t['upper'])}" if t.get("upper") is not None else f"{cw}_{n(t['value'])}") + ("_people" if t["kind"] == "population" else "_flags")
    for q in b["qualifiers"]:
        slug += "_" + q
    return f"{acr.lower()}.{slug}"


def build_cluster_metrics(by_num, ap_by_id, substrate_text, emergency):
    """The nineteen metrics of cluster 1 as data: bands with their tests, verdicts, postures, deployment verdicts
    and conditions, compiled from the chapters and checked band by band against the appendices. The build stops on
    any disagreement; the prose is repaired, never the data. The LRS and HRS bands must equal the emergency
    artifact's, and carry its band identifiers."""
    em_ids = {}
    for m in emergency["metrics"]:
        for b in m["bands"]:
            em_ids[(m["metric"], b["comparison"], b["value"], b["verdict"], b["condition"] is not None)] = b["id"]
    principles, n_metrics, n_bands = [], 0, 0
    for num, acrs, row in CL1:
        ch = by_num[num]
        ctext = read(os.path.join(CH, ch["file"]))
        ap = ap_by_id[ch["fm"]["appendices"][0]]
        atext = read(os.path.join(AP, ap["file"]))
        apname = ap["fm"]["id"]
        where = f"chapter {num}"
        cms = _chapter_cluster_metrics(ctext, f"{num}.3", where)
        if [m["acr"] for m in cms] != acrs:
            die(f"{where}: {num}.3 item 2 lists metrics {[m['acr'] for m in cms]}, the cluster spec expects {acrs}")
        src = ctext if row["stated_in"].startswith("chapter") else substrate_text
        if row["sentence"] not in " ".join(src.split()):
            die(f"{where}: the register-row sentence is not in {row['stated_in']}", row["sentence"])
        bsrc = ctext if row["bound_stated_in"].startswith("chapter") else substrate_text
        if row["bound_sentence"] not in " ".join(bsrc.split()):
            die(f"{where}: the escalation-bound sentence is not in {row['bound_stated_in']}", row["bound_sentence"])
        metrics = []
        for mt in cms:
            abands, anchor, asha = _appendix_cluster_metric(atext, mt["name"], mt["acr"], where)
            ckeys, akeys = sorted(b["key"] for b in mt["bands"]), sorted(b["key"] for b in abands)
            if ckeys != akeys:
                die(f"{mt['acr']}: the chapter's {num}.3 bands and {apname} Section 2 disagree; the build stops until they agree",
                    "chapter:  " + "; ".join(_fmt_key(k) for k in ckeys),
                    "appendix: " + "; ".join(_fmt_key(k) for k in akeys))
            if not mt["bands"]:
                die(f"{mt['acr']}: no bands in {num}.3")
            unit = next((b["test"]["unit"] for b in mt["bands"] if b["test"].get("unit")), None)
            bands = []
            for b in mt["bands"]:
                t = b["test"]
                ab = next(x for x in abands if x["key"] == b["key"])
                deployment = b["deployment"] or ab["deployment"]
                stated = b["head"]
                if t.get("tightened_from"):
                    stated = stated.replace(t["tightened_from"], f"{t['comparison']}{t['value'] * 100:g}%", 1) + f" (tightened from {t['tightened_from']})"
                entry = {"id": _band_id(mt["acr"], b),
                         "as_stated": stated,
                         "comparison": t.get("comparison"),
                         "value": (int(t["value"]) if t["kind"] in ("latency", "population", "count") and float(t["value"]).is_integer() else t.get("value"))}
                if t.get("upper") is not None:
                    entry["upper_comparison"], entry["upper"] = t["upper_comparison"], t["upper"]
                if t.get("note"):
                    entry["test"] = t["note"]
                if t.get("or_community"):
                    entry["or_community"] = t["or_community"]
                if t.get("tightened_from"):
                    entry["tightened_from"] = t["tightened_from"]
                if b["label"]:
                    entry["label"] = b["label"]
                if b["condition"] is None and b["label"]:
                    tm = re.match(r"^Tier ([IV]+)", b["label"])
                    b["condition"] = (f"the deployment's register tier is Tier {tm.group(1)}" if tm else f"the query class is {b['label']}")
                entry.update({"verdict": b["verdict"], "flavor": b["flavor"], "verdict_basis": b["verdict_basis"], "posture": b["posture"] or ab["posture"],
                              "deployment": deployment,
                              "deployment_stated_in": (None if deployment is None else ("chapter" if b["deployment"] else "appendix")),
                              "condition": b["condition"], "qualifiers": b["qualifiers"] or None,
                              "obligations": sorted(set(b["obligations"]) | set(ab["obligations"])) or None})
                ek = (mt["acr"], t.get("comparison"), t.get("value"), b["verdict"], "vulnerable" in b["qualifiers"])
                if ek in em_ids:
                    entry["id"] = em_ids.pop(ek)
                    entry["also_in"] = "protocol/emergency-thresholds.yaml"
                bands.append(entry)
            n_bands += len(bands)
            metrics.append({"metric": mt["acr"], "name": mt["name"], "principle": num, "section": f"{num}.3",
                            "definition": mt["definition"], "unit": unit,
                            "checked_against": f"{num}.A Section 2, {mt['name']} ({mt['acr']})",
                            "specified_in": {"file": "APPENDICES/" + ap["file"], "anchor": anchor, "sha256": asha},
                            "bands": bands})
        n_metrics += len(metrics)
        principles.append({"principle": num, "section": f"{num}.3",
                           "register_row": {"reads": row["reads"], "tier_scheme": row["tier_scheme"],
                                            "stated_in": row["stated_in"], "sentence": row["sentence"],
                                            "escalation_time_bound": row["bound"],
                                            "bound_stated_in": row["bound_stated_in"], "bound_sentence": row["bound_sentence"],
                                            "undeclared_field": "a missing required field compiles as ESCALATE holding the safe state (FOUNDATIONS/SUBSTRATE.md section 5; substrate/runtime.yaml)"},
                           "metrics": metrics})
    if em_ids:
        die("the emergency artifact carries bands the cluster compile did not meet: " + ", ".join(sorted(em_ids.values())))
    if n_metrics != 19:
        die(f"cluster 1 compiled {n_metrics} metrics; the change list names nineteen")
    return {
        "artifact": "metric_bands",
        "cluster": 1,
        "principles_covered": [p for p, _, _ in CL1],
        "compiled_from": ("CHAPTERS 1.1 to 1.6, section X.Y.3 item 2 (the chapter states); checked band by band against APPENDICES "
                          "1.1.A to 1.6.A Section 2 (the appendix specifies); the build stops on any disagreement in a band's test, "
                          "bounds, condition, verdict, or watch posture"),
        "purpose": ("The nineteen metrics of cluster 1 as data, so that a gate evaluates each principle's bands from the bundle and "
                    "no implementer reads them out of prose. Step 7 of constitution/gate.yaml reads these for principles 1.1 to 1.6."),
        "metric_count": n_metrics,
        "band_count": n_bands,
        "units": "a percent band is a fraction (1% = 0.01); a latency band is milliseconds; a population band is people affected; the Isolation Flag band is flags per person per day",
        "evaluation": [
            "A value may satisfy several bands (a 5% halt band and a 2% High Alert band both hold at 6%). The verdict is the most severe band satisfied: BLOCK over ESCALATE over ALLOW.",
            "A deployment verdict (SUSPEND_DEPLOYMENT, HALT_FLEET) binds the software version or hardware lot beside the action's verdict, and RECERTIFY where the band names it.",
            "A range band holds from its value up to its upper bound, excluded unless upper_comparison is '<='.",
            "A latency bound is a per-event pass or fail at the bound; the breach band reads the p99 of the measurement window the appendix specifies.",
            "A band with a condition holds only where the condition does; where a conditioned and an unconditioned band both hold, the more severe governs.",
            "Every ESCALATE band holds the candidate action at its safe state for the escalation time bound of the register row the principle reads (FOUNDATIONS/LEXICON.md section 3, the verdict test; FOUNDATIONS/SUBSTRATE.md section 5). A missing row field compiles as ESCALATE holding the safe state.",
            "A score computed from an input below the reliability floor is invalid, and an invalid score is not a value in any band (FOUNDATIONS/SUBSTRATE.md section 2)."],
        "principles": principles,
        "not_carried_here": ("the measurement windows, calculation methods, joint thresholds and integration requirements of each metric, "
                             "which the appendix specifies at the anchor each metric names, hashed; the metrics of clusters 2 to 5 and "
                             "the Cardinal Operating Principle, which compile with their clusters"),
    }


# ---------------------------------------------------------------------------
# The substrate (SUBSTRATE sections 2 to 7) and the credential map (CREDENTIALS sections 3 and 4), verbatim
# ---------------------------------------------------------------------------
def _labelled_paragraphs(section_text):
    """A section's paragraphs as {label, text, items}: '**Label.** text' with any '- ' bullets that follow it."""
    out, cur = [], None
    for para in re.split(r"\n\s*\n", section_text.strip()):
        lines = [l for l in para.split("\n") if l.strip()]
        if not lines:
            continue
        bullets = [" ".join(l[2:].split()).rstrip(";") for l in lines if l.startswith("- ")]
        prose = [l for l in lines if not l.startswith("- ")]
        if prose:
            text = " ".join(" ".join(prose).split())
            m = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", text)
            label, body = (m.group(1).rstrip("."), m.group(2)) if m else (None, text)
            cur = {"label": label, "text": body}
            out.append(cur)
        if bullets:
            if cur is None:
                die("substrate: bullets before any labelled paragraph", para)
            cur.setdefault("items", []).extend(bullets)
    return out


def build_substrate(sub_text):
    """FOUNDATIONS/SUBSTRATE.md sections 2 to 7 as data: every labelled paragraph verbatim, and the values a gate reads
    derived under guards (the reliability floor, the health bounds, the register's fields, the authority conditions,
    the quorum by tier, the wall-reached cases). The build stops if any guard fails."""
    heads = [(int(m.group(1)), m.group(2).strip(), m.start()) for m in re.finditer(r"(?m)^## (\d+)\. (.+?)\s*\{#", sub_text)]
    sections = {}
    for i, (n, title, start) in enumerate(heads):
        if n not in (2, 3, 4, 5, 6, 7):
            continue  # sections 1 and 8 bind nothing at the gate and are not parsed
        end = heads[i + 1][2] if i + 1 < len(heads) else len(sub_text)
        body = sub_text[start:end].split("\n", 1)[1]
        sections[n] = {"title": title, "paragraphs": _labelled_paragraphs(body)}
    for n in (2, 3, 4, 5, 6, 7):
        if n not in sections:
            die(f"FOUNDATIONS/SUBSTRATE.md: section {n} not found")

    def para(n, label):
        hit = [p for p in sections[n]["paragraphs"] if p["label"] == label]
        if len(hit) != 1:
            die(f"FOUNDATIONS/SUBSTRATE.md section {n}: expected one paragraph labelled {label!r}, found {len(hit)}",
                ", ".join(str(p["label"]) for p in sections[n]["paragraphs"]))
        return hit[0]

    floor_p = para(2, "Floor")
    fm = re.match(r"^(0\.\d+)\.", floor_p["text"])
    if not fm:
        die("FOUNDATIONS/SUBSTRATE.md section 2: the Floor paragraph does not open with its value", floor_p["text"])
    floor = float(fm.group(1))
    health = para(3, "Definition")["text"]
    er = re.search(r"error rate at or below (\d+(?:\.\d+)?)%", health)
    up = re.search(r"uptime at or above (\d+(?:\.\d+)?)%", health)
    if not (er and up):
        die("FOUNDATIONS/SUBSTRATE.md section 3: the health bounds did not parse", health)
    entry = para(5, "Entry")["text"]
    if "records:" not in entry:
        die("FOUNDATIONS/SUBSTRATE.md section 5: the Entry paragraph does not list the register's fields", entry)
    fields, cur, depth = [], "", 0
    for ch_ in entry.split("records:", 1)[1]:
        if ch_ == "(":
            depth += 1
        elif ch_ == ")":
            depth -= 1
        if ch_ == ";" and depth == 0:
            fields.append(cur); cur = ""
        else:
            cur += ch_
    fields.append(cur)
    fields = [f.strip().rstrip(".") for f in fields if f.strip()]
    fields = [re.sub(r"^and ", "", f) for f in fields]
    if len(fields) < 8:
        die(f"FOUNDATIONS/SUBSTRATE.md section 5: {len(fields)} register fields parsed; at least eight are stated", entry)
    auth = para(6, "(c) A human takes authorship")
    conds = auth.get("items", [])
    if len(conds) != 7:
        die(f"FOUNDATIONS/SUBSTRATE.md section 6 (c): {len(conds)} conditions parsed, seven are stated", "\n".join(conds))
    qline = next((c for c in conds if c.startswith("quorum by tier:")), None)
    if not qline:
        die("FOUNDATIONS/SUBSTRATE.md section 6 (c): the quorum condition was not found", "\n".join(conds))
    quorum = {}
    for part in re.split(r";\s*(?=Tier )", qline.split("quorum by tier:", 1)[1].strip()):
        t, _, rest = part.partition(",")
        quorum[t.strip()] = rest.strip().rstrip(";")
    if len(quorum) != 3:
        die("FOUNDATIONS/SUBSTRATE.md section 6 (c): the quorum by tier did not parse into three entries", qline)
    wall = para(6, "A wall reached")
    cases = re.findall(r"\*\(([abc])\) ([^:*]+):\*\s*(.+?)(?=\s*\*\([abc]\)|$)", wall["text"])
    if len(cases) != 3:
        die("FOUNDATIONS/SUBSTRATE.md section 6: 'A wall reached' did not yield three cases", wall["text"])
    software = para(5, "Software-only deployments")["text"]
    return {
        "artifact": "substrate_runtime",
        "compiled_from": "FOUNDATIONS/SUBSTRATE.md sections 2 to 7, every labelled paragraph verbatim; the values below are derived from those paragraphs and the build stops if any fails to parse",
        "purpose": ("The ground the bands read: the reliability floor and the invalid-score rule, system health and operational boundaries, "
                    "the tier register's fields and rules, authority over a hard stop, a wall reached, and the substrate's own fail-safe. "
                    "The register's values for a deployment are the deployer's, receipted; this artifact carries the fields and the rules they are read under."),
        "reliability": {
            "floor": floor,
            "rule": floor_p["text"],
            "definition": para(2, "Definition")["text"],
            "who_reads": para(2, "Who reads")["text"],
            "contested_reading": para(2, "Contested reading")["text"],
            "reporting": para(2, "Reporting")["text"],
            "consumed_at": "constitution/gate.yaml step 3 (perception_floor) and the receipt's sensor_reliability_state"},
        "system_health": {"error_rate_max": round(float(er.group(1)) / 100, 6), "uptime_min": round(float(up.group(1)) / 100, 6),
                          "definition": health, "breach": para(3, "Breach")["text"]},
        "operational_boundaries": {"definition": para(4, "Definition")["text"], "exceedance": para(4, "Exceedance")["text"]},
        "register": {
            "tiers": para(5, "Tiers")["text"],
            "software_only_declaration": software,
            "entry_fields": fields,
            "assignment": para(5, "Assignment")["text"],
            "undeclared_field": para(5, "Undeclared field")["text"],
            "default_bound": para(5, "Default bound")["text"],
            "sphere_fractal": para(5, "The sphere fractal")["text"],
            "consumed_at": "constitution/gate.yaml steps 8 and 9, and every ESCALATE band of metrics/cluster-1.yaml"},
        "authority_over_a_hard_stop": {
            "definition": sections[6]["paragraphs"][0]["text"],
            "reading_is_wrong": para(6, "(a) The reading is wrong")["text"],
            "safe_state_is_unsafe": para(6, "(b) The safe state is unsafe")["text"],
            "human_takes_authorship": {"rule": auth["text"], "conditions_all_required": conds, "quorum_by_tier": quorum},
            "locked_walls": para(6, "Locked walls")["text"],
            "wall_reached": {"rule": wall["text"].split("*(a)")[0].strip(),
                             "cases": [{"case": c, "name": n.strip(), "consequence": t.strip()} for c, n, t in cases]},
            "peers_hard_stop": para(6, "A peer's hard stop")["text"]},
        "fail_safe": sections[7]["paragraphs"][0]["text"],
        "sections": [{"section": n, "title": sections[n]["title"], "paragraphs": sections[n]["paragraphs"]} for n in (2, 3, 4, 5, 6, 7)],
        "not_carried_here": "section 1 (why one document) and section 8 (the relationship to the other documents), which bind nothing at the gate; the register's values per deployment, which are the deployer's declarations",
    }


def build_credentials(cred_text, const_text):
    """FOUNDATIONS/CREDENTIALS.md sections 3 and 4 as data: the five credentials with their questions, homes and
    anchors, the initiator rule, the findings rule, Standing, and the two maps (credential to home, principle to
    what it voices). The five names must equal Article 6's, in order."""
    cm = re.search(r"all five credentials are satisfied: ([A-Z][a-z]+), ([A-Z][a-z]+), ([A-Z][a-z]+), ([A-Z][a-z]+), and ([A-Z][a-z]+)", const_text)
    if not cm:
        die("CONSTITUTION.md Article 6: the five credential names did not parse")
    five = list(cm.groups())
    s3 = cred_text[cred_text.index("## 3. The five credentials"):cred_text.index("## 4. ")]
    s4 = cred_text[cred_text.index("## 4. "):cred_text.index("## 5. ")]
    creds = []
    for m in re.finditer(r"(?m)^- \*\*([A-Z][a-z]+)\*\* asks \*([^*]+)\*\s*(.*)$", s3):
        name, asks, rest = m.group(1), m.group(2).strip(), m.group(3).strip()
        homes = sorted(set(re.findall(r"P(\d\.\d)", rest)))
        am = re.search(r"Standards anchor: ([^.]+)\.", rest)
        creds.append({"credential": name, "asks": asks, "text": re.sub(r"\*+", "", rest),
                      "principles_named": homes, "standards_anchor": am.group(1).strip() if am else None,
                      "standards_gap": am is None})
    if [c["credential"] for c in creds] != five:
        die("FOUNDATIONS/CREDENTIALS.md section 3: the five credentials do not match Article 6 in name and order",
            str([c["credential"] for c in creds]), str(five))

    def labelled(label):
        m = re.search(r"(?m)^\*\*" + re.escape(label) + r"\*\*\s*(.+)$", s3)
        if not m:
            die(f"FOUNDATIONS/CREDENTIALS.md section 3: paragraph {label!r} not found")
        return " ".join(m.group(1).split())

    def table(block, cols):
        rows = []
        for line in block.split("\n"):
            if line.startswith("|") and not line.startswith("|---") and not re.match(r"^\|\s*(Credential|Principle)\s*\|", line):
                cells = [re.sub(r"\*+", "", c.strip()).replace("`", "") for c in line.strip().strip("|").split("|")]
                if len(cells) == cols:
                    rows.append(cells)
        return rows
    t1_start = s4.index("| Credential |"); t2_start = s4.index("| Principle |")
    map_rows = table(s4[t1_start:t2_start], 3)
    voice_rows = table(s4[t2_start:], 2)
    if [r[0] for r in map_rows] != five:
        die("FOUNDATIONS/CREDENTIALS.md section 4: the credential-to-home table does not list the five in Article 6's order", str([r[0] for r in map_rows]))
    if len(voice_rows) < 20:
        die(f"FOUNDATIONS/CREDENTIALS.md section 4: the inverse table parsed {len(voice_rows)} rows; the map names more than twenty")
    return {
        "artifact": "credential_map",
        "compiled_from": "FOUNDATIONS/CREDENTIALS.md sections 3 and 4 verbatim; the five names checked against CONSTITUTION.md Article 6",
        "purpose": ("Article 6's five-credential conjunction as data: what each credential asks, which principle gives it its ethical voice, "
                    "the standards anchor where one exists, the initiator rule for a non-human counterparty, the rule for findings the AI consumes, "
                    "and Standing, the rule that a credential is read at the time of the act. Consent's validity test is consent/validity-predicate.yaml."),
        "conjunction": {"rule": cm.group(0) + ", evaluated for the acting agent and for the content and persons the action affects (Article 6)",
                        "unmet": "an unmet credential on a consequential action is blocked or escalated, and the verdict is receipted"},
        "credentials": creds,
        "initiator_rule": labelled("The initiator of an inbound action (the membership rule)."),
        "findings_consumed": labelled("Findings the AI consumes."),
        "standing": labelled("Standing."),
        "homes": [{"credential": r[0], "ethical_homes": r[1], "status": r[2]} for r in map_rows],
        "voices": [{"principle": r[0], "voices": r[1]} for r in voice_rows],
        "consumed_at": "constitution/gate.yaml step 4 (credentials); Consent through consent/validity-predicate.yaml",
        "not_carried_here": "sections 1, 2 and 5 to 10 (the frame, the enforcement objects, the write-rule, the method, the protect-versus-flourish line, the integration points), which guide authors and bind nothing at the gate",
    }


# ---------------------------------------------------------------------------
# The Lexicon's Action Registry (LEXICON section 9) as data; its "used in" column is regenerated from the chapters
# ---------------------------------------------------------------------------
REG_TOKEN = re.compile(r"\b[A-Z][A-Z_-]{2,}[A-Z]\b")      # four letters and up: the validators' rule
REG_TOKEN3 = re.compile(r"\b[A-Z][A-Z_-]{1,}[A-Z]\b")     # three and up: LOG is a verb of the registry
REG_RECORD_FORMS = {"Prospective Receipt", "Action Receipt", "Receipt"}
IMPLIED_POSTURES = {"NORMAL", "DEGRADED"}   # every chapter runs under them; no declaration names them
COMPILED_CLUSTERS = {"1"}   # the clusters whose metric bands compile at this version (B8: reconciled); the rest are proposed


def _chapter_label(ch):
    return "E" if ch["disp"] == "Cardinal" else ch["num"]


def _label_key(label):
    return (1, 0, 0) if label == "E" else (0,) + tuple(int(x) for x in label.split("."))


def _row_tokens(cell):
    """The verb tokens a registry row names: the first cell without its parentheticals, split on '/', ',' and 'and'.
    An instance row or a record form names no verb of its own."""
    if "instances" in cell.lower() or cell.strip() in REG_RECORD_FORMS:
        return []
    flat = re.sub(r"\([^)]*\)", "", cell)
    out = []
    for part in re.split(r"\s*/\s*|,\s*|\s+and\s+", flat):
        out.extend(t for t in REG_TOKEN3.findall(part) if t not in out)
    return out


def _declared_tokens(chapters):
    """Per chapter, the tokens its Lexicon declaration block names (the universal verbs it uses and the domain verbs it defines)."""
    out = {}
    for ch in chapters:
        text = read(os.path.join(CH, ch["file"]))
        lines = [l for l in text.split("\n") if "**Lexicon declaration.**" in l]
        if len(lines) != 1:
            die(f"CHAPTERS/{ch['file']}: expected one Lexicon declaration line, found {len(lines)}")
        out[_chapter_label(ch)] = set(REG_TOKEN3.findall(lines[0]))
    return out


def _used_in_text(labels, all_labels, old_cell):
    """The regenerated cell: 'all', 'none declared', or the chapter list; an old cell's note survives in parentheses."""
    missing = [lab for lab in all_labels if lab not in set(labels)]
    if not missing:
        body = "all"
    elif not labels:
        body = "none declared"
    elif len(missing) <= 5:
        body = "all but " + ", ".join(sorted(missing, key=_label_key))
    else:
        body = ", ".join(sorted(labels, key=_label_key))
    old = old_cell.strip()
    # a cell this function wrote earlier: the body, then its note; strip the body and keep the note
    for b in ("all", "none declared"):
        if old.startswith(b + "; "):
            old = old[len(b) + 2:]
        elif old.startswith(b + " (") and old.endswith(")"):
            old = old[len(b) + 2:-1]
    old = re.sub(r"^all but [\d., E]+$", "", old)
    note = None
    if old and not re.search(r"\d\.\d", old) and old not in ("all", "many") and not re.fullmatch(r"\d+ chapters", old) and old != "none declared":
        note = re.sub(r"^\((.*)\)$", r"\1", old)      # the whole old cell was a note
    else:
        parens = re.findall(r"\(([^()]*)\)", old)
        if parens:
            note = "; ".join(parens)
    if not note:
        return body
    return body + ("; " + note if "(" in note else f" ({note})")


def registry_tables(lexicon_text):
    """LEXICON section 9 as (block title, header, rows, line numbers): every markdown table under a '### 9.N' heading."""
    lines = lexicon_text.split("\n")
    start = next((i for i, l in enumerate(lines) if l.startswith("## 9.")), None)
    if start is None:
        die("FOUNDATIONS/LEXICON.md: section 9 (the Action Registry) not found")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    tables, title, i = [], None, start
    while i < end:
        l = lines[i]
        if l.startswith("### "):
            title = l[4:].strip()
        if l.startswith("|") and title:
            j = i
            while j < end and lines[j].startswith("|"):
                j += 1
            header = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            rows = []
            for k in range(i + 2, j):
                cells = [c.strip() for c in lines[k].strip().strip("|").split("|")]
                if len(cells) != len(header):
                    die(f"FOUNDATIONS/LEXICON.md section 9, {title}: a row has {len(cells)} cells and the header {len(header)}", lines[k])
                rows.append({"line": k, "cells": cells})
            tables.append({"title": title, "header": header, "rows": rows})
            i = j
            continue
        i += 1
    if len(tables) < 9:
        die(f"FOUNDATIONS/LEXICON.md section 9: {len(tables)} tables parsed; the registry has at least nine")
    return tables


def expected_used_in(lexicon_text, chapters):
    """For every registry row in a table with a 'used in' column: (line number, column index, the regenerated cell).
    Shared by the compiler (which checks) and the hub's regen_used_in tool (which writes)."""
    tables = registry_tables(lexicon_text)
    declared = _declared_tokens(chapters)
    all_labels = sorted(declared, key=_label_key)
    out = []
    for t in tables:
        if "used in" not in t["header"]:
            continue
        ci = t["header"].index("used in")
        vi = t["header"].index("verb")
        for r in t["rows"]:
            toks = _row_tokens(r["cells"][vi])
            if not toks:
                continue  # an instance row keeps its prose cell
            labels = [lab for lab in all_labels if declared[lab] & set(toks)]
            if set(toks) & IMPLIED_POSTURES:
                old = r["cells"][ci]
                m_ = re.match(r"^all \(a posture implied by every chapter and declared by none(?:; (.*))?\)$", old)
                note = (m_.group(1) or "") if m_ else (old.split("; ", 1)[1] if "; " in old else "")
                cell = "all (a posture implied by every chapter and declared by none" + (f"; {note}" if note else "") + ")"
                out.append((r["line"], ci, cell))
                continue
            out.append((r["line"], ci, _used_in_text(labels, all_labels, r["cells"][ci])))
    return out


def build_registry(lexicon_text, chapters):
    """The Action Registry as data. Every row verbatim with its verb tokens, and 'used in' computed from the chapters'
    declaration blocks. The build stops if the Lexicon's 'used in' cell differs from the computed one: the column is
    regenerated by the hub's regen_used_in tool, never by hand."""
    tables = registry_tables(lexicon_text)
    declared = _declared_tokens(chapters)
    all_labels = sorted(declared, key=_label_key)
    expected = {(ln, ci): cell for ln, ci, cell in expected_used_in(lexicon_text, chapters)}
    lines = lexicon_text.split("\n")
    stale = []
    for (ln, ci), cell in expected.items():
        on_disk = [c.strip() for c in lines[ln].strip().strip("|").split("|")][ci]
        if on_disk != cell:
            stale.append(f"line {ln + 1}: on disk {on_disk!r}, computed {cell!r}")
    if stale:
        die("FOUNDATIONS/LEXICON.md section 9: the 'used in' column lags the chapters' declarations; the steward regenerates it with the hub's "
            "regen_used_in tool and commits the Lexicon", "\n".join(stale[:12]))
    categories, all_tokens = [], set()
    for t in tables:
        rows = []
        for r in t["rows"]:
            d = dict(zip(t["header"], r["cells"]))
            cell = d.get("verb", "")
            toks = _row_tokens(cell)
            all_tokens.update(toks)
            entry = {"verb": cell or None, "tokens": toks or None}
            for k in t["header"]:
                if k == "verb":
                    continue
                key = k.replace(", in short", "").replace(" ", "_")
                entry[key] = d[k] or None
            if toks and "used in" in t["header"]:
                labels = [lab for lab in all_labels if declared[lab] & set(toks)]
                if set(toks) & IMPLIED_POSTURES:
                    labels = list(all_labels); entry["implied_by_every_chapter"] = True
                entry["used_in_chapters"] = labels or None
                entry["used_in_all"] = set(labels) == set(all_labels)
            rows.append(entry)
        categories.append({"category": t["title"], "columns": t["header"], "rows": rows})
    doc_names = {"LEXICON", "LEARN", "SUBSTRATE", "FOUNDATIONS", "CONSENT", "CREDENTIALS", "CONSTITUTION", "PROTOCOL", "CROSS_PRINCIPLE"}
    unregistered = {lab: sorted(t for t in declared[lab] - all_tokens - doc_names if REG_TOKEN.fullmatch(t)) for lab in all_labels}
    return {
        "artifact": "action_registry",
        "compiled_from": "FOUNDATIONS/LEXICON.md section 9 (every table row verbatim) and each chapter's Lexicon declaration block (the 'used in' column, regenerated from the declarations by the steward's tooling and checked here at every build)",
        "purpose": ("Every verb the corpus tells a governed system to perform, listed once with where it is defined, what it does, what counts as success, "
                    "which standard it bridges to, and which chapters declare it. A verb absent from this registry is not a verb of the Blueprint."),
        "rules": "LEXICON section 9.0: one verb, one definition, one pattern; every chapter declares; instances are listed under their verb; promotion follows the BROADCAST test; bridges copy the standard's own term",
        "chapter_labels": "principle numbers; E is the Cardinal Operating Principle",
        "verb_count": len(all_tokens),
        "verbs": sorted(all_tokens),
        "categories": categories,
        "declarations": [{"chapter": lab, "declares": sorted(declared[lab] & all_tokens) or None,
                          "tokens_not_in_registry": unregistered[lab] or None} for lab in all_labels],
        "not_carried_here": "the definitions themselves (LEXICON section 3 for the universal tier, each chapter for its domain verbs), carried by content hash; the standards crosswalk's terms are copied here as prose, not as a mapping a gate evaluates",
    }, all_tokens


A7_LEADS = [("every_decision", "Every decision the gate renders SHALL leave"),
            ("commits_before_act_and_cites_policy", "The receipt SHALL commit before the act"),
            ("attests_perception_and_records_reliability", "The receipt attests to the verdict rendered"),
            ("deletion_is_an_event", "A deletion SHALL itself be recorded"),
            ("defeat_is_a_breach", "An action that prevents, alters, suppresses"),
            ("holds_no_profile", "The receipt SHALL NOT hold a profile"),
            ("makes_review_possible", "An affected person MAY invoke review")]


def build_receipt_conditions(const_text, lexicon_text):
    """Article 7's sentences and the Lexicon's Record entries and DEGRADED posture, verbatim, as the conditions a receipt satisfies.

    Nothing here names a format, a signature scheme, a chain or an anchor; those are the machine's. The build stops if
    Article 7 gains or loses a sentence, so an edit to the supreme law is reviewed by hand."""
    m = re.search(r"\*\*Article 7\.[^\n]*\*\*\n(.*?)(?=\n\*\*Article |\Z)", const_text, re.S)
    if not m:
        die("CONSTITUTION.md Article 7 did not parse for the receipt conditions")
    body = " ".join(m.group(1).split())
    sents = [x.strip() for x in re.split(r"(?<=[.!?])\s+(?=[A-Z(*`])", body) if x.strip()]
    if len(sents) != len(A7_LEADS):
        die(f"CONSTITUTION.md Article 7: {len(sents)} sentences, the receipt conditions compile {len(A7_LEADS)}. "
            "An edit to the supreme law must be reviewed and A7_LEADS updated by hand.", body)
    conditions = []
    for cid, lead in A7_LEADS:
        hit = [x for x in sents if x.startswith(lead)]
        if len(hit) != 1:
            die(f"CONSTITUTION.md Article 7: expected one sentence opening {lead!r}, found {len(hit)}")
        conditions.append({"id": cid, "source": "CONSTITUTION.md Article 7", "text": hit[0]})

    def bullets(section_heading, next_heading):
        seg = lexicon_text.split(section_heading, 1)
        if len(seg) != 2:
            die(f"FOUNDATIONS/LEXICON.md: heading {section_heading!r} not found for the receipt conditions")
        seg = seg[1].split(next_heading, 1)[0]
        out = []
        for line in seg.split("\n"):
            mm = re.match(r"^- \*\*([^*]+)\*\*(.*)$", line.strip())
            if mm:
                out.append((mm.group(1).strip(), " ".join((mm.group(1) + "**" + mm.group(2)).split())))
        return out
    rec = bullets("### Record", "### Learn")
    names = [n for n, _ in rec]
    for need in ("LOG.", "Prospective Receipt.", "Action Receipt.", "Receipt"):
        if not any(n.startswith(need) for n in names):
            die(f"FOUNDATIONS/LEXICON.md section 3 Record: entry {need!r} not found for the receipt conditions", ", ".join(names))
    records = []
    for name, full in rec:
        text = re.sub(r"^\*\*[^*]+\*\*\s*", "", "**" + full)  # the entry's text after the bold name
        text = re.sub(r"\s*\*\([^)]*\)\*\s*$", "", text)      # the trailing seat note
        records.append({"name": name.rstrip("."), "source": "FOUNDATIONS/LEXICON.md section 3, Record", "text": text.strip()})
    post = bullets("### Postures", "### Active obligations")
    deg = [full for n, full in post if n.startswith("DEGRADED")]
    if len(deg) != 1:
        die("FOUNDATIONS/LEXICON.md section 3 Postures: the DEGRADED entry was not found for the receipt conditions")
    dtext = re.sub(r"^\*\*[^*]+\*\*\s*", "", "**" + deg[0]); dtext = re.sub(r"\s*\*\([^)]*\)\*\s*$", "", dtext).strip()
    for c in conditions + records:
        if "  " in c["text"]:
            die("receipt condition text carries a double space; the verifier compares normalized text and this would hide a drift")
    return {
        "conditions": conditions,
        "records": records,
        "states": [{"state": "provisional", "meaning": "a receipt whose commitment no independent witness has yet acknowledged; marked as such (FOUNDATIONS/LEXICON.md section 3, Receipt)"},
                   {"state": "reconciled", "meaning": "a receipt an independent witness has acknowledged (FOUNDATIONS/LEXICON.md section 3, Receipt)"}],
        "posture_degraded": {"source": "FOUNDATIONS/LEXICON.md section 3, Postures", "text": dtext},
        "fields": [
            {"field": "decision", "holds": "the verdict rendered: allow, block, escalate, a refused request, or a decision not to act", "stated_in": "every_decision; attests_perception_and_records_reliability"},
            {"field": "policy", "holds": "the exact governing policy in force, cited by its fingerprint (compiled/bundle.sha256)", "stated_in": "commits_before_act_and_cites_policy"},
            {"field": "sensor_reliability_state", "holds": "the reliability state in force when the verdict was rendered (FOUNDATIONS/SUBSTRATE.md section 2)", "stated_in": "attests_perception_and_records_reliability"},
            {"field": "commitment", "holds": "the receipt's commitment, made before the act and beyond the actor's control", "stated_in": "commits_before_act_and_cites_policy; LEXICON Prospective Receipt"},
            {"field": "event_class", "holds": "one of the event classes above, where the event is the Protocol's", "stated_in": "event_classes"},
            {"field": "chain", "holds": "for an Action Receipt, the commitment hash of its Prospective Receipt", "stated_in": "LEXICON Action Receipt"},
            {"field": "state", "holds": "provisional or reconciled", "stated_in": "LEXICON Receipt"},
            {"field": "person", "holds": "nothing: no profile of any person", "stated_in": "holds_no_profile"},
        ],
        "not_carried_here": "the receipt's format, its signature scheme, its chain and its anchor. One published form that satisfies these conditions, with a free checker, sits outside the seal at FOR_ENGINEERS/RECEIPT-FORMAT.md; a deployment may use another form that satisfies the same conditions",
    }


def build_protocol_artifacts(up_text):
    # Artifact 1: the head guard. The three predicate clauses, verbatim.
    m = re.search(r"\*\*The predicate\.\*\*.*?\n\n(1\..*?)\n\n\*\*", up_text, re.S)
    if not m:
        die("FOUNDATIONS/UNIVERSAL_PROTOCOL.md Section 3: predicate clauses did not parse")
    clauses = [re.sub(r"^\d+\.\s*", "", c.strip()).split("\n\n")[0].strip()
               for c in re.split(r"\n(?=\d+\.)", m.group(1)) if c.strip()]
    if len(clauses) != 3:
        die(f"expected 3 predicate clauses, parsed {len(clauses)}", m.group(1))
    head_guard = {
        "artifact": "head_guard",
        "compiled_from": "FOUNDATIONS/UNIVERSAL_PROTOCOL.md Section 3 alone",
        "injection": "per_rule",
        "proposal_compatibility": {"universal_section": True,
                                   "fires_before": "principle_evaluation",
                                   "note": "Section 10 strengthens the proposal's scheduler-level meta-rule into per-rule injection; both readings are carried."},
        "predicate": {"trips_when_any": clauses,
                      "threshold_consumption": {
                          "mode": "by_reference",
                          "sources": ["1.1.3 (Life-Risk Score critical band)",
                                      "1.2.3 (Harm-Risk Score severe-harm critical band)"],
                          "artifact": "protocol/emergency-thresholds.yaml",
                          "bands": ["lrs.critical", "hrs.critical"],
                          "note": "The values are compiled from the two sections into the artifact named and checked against the appendices at every build; this guard holds no literal.",
                          "correction": "Schema correction 1 (Section 10): the compilation proposal's hardcoded threshold 0.01 (Compiling the Blueprint, Passoja 2026) yields to by-reference consumption of 1.1.3. No numeric threshold appears in this artifact."}},
        "trigger_fault": "A trigger that cannot be evaluated is a trigger fault, treated as a possible breach: hold at the nearest safe point, verify, escalate, receipt the fault. Fail toward safety: the fault itself leaves a receipt (Section 3).",
        "legacy_resolution": {"U.2_audit_trigger": "resolves to Section 9 (schema correction 2); the designation is retired and any legacy reference lands there."},
        "interception_clause": "The prose citation surface of this artifact (Section 8); chapters cite, the compiler injects, nothing restates."}

    # Artifact 2: the emergency handler. Functions of Section 5, grammar of Section 6.
    s5 = up_text[up_text.index("## 5. The Protocol"):up_text.index("## 6.")]
    funcs = []
    for m2 in re.finditer(r"- \*\*(.+?)\*\* \(([^)]+)\)\.\s*(.*?)(?=\n- \*\*|\n\n|$)", s5, re.S):
        name, verbs, text2 = m2.group(1), [v.strip() for v in m2.group(2).split(",")], m2.group(3)
        if not all(re.match(r"^[A-Z][A-Z-]*$", v) for v in verbs):
            continue  # a parenthetical that is prose, not a verb list (Coordinate, Support the aftermath)
        succ = None
        sm = re.search(r"Success: (.+?)(?:\.|$)", text2)
        if sm:
            succ = sm.group(1).strip() + "."
        funcs.append({"function": name, "verbs": verbs, "success": succ,
                      "definition": " ".join(text2.split())})
    coord = {"function": "Coordinate", "verbs": ["BROADCAST", "ACKNOWLEDGE", "HAND-OFF"],
             "success": None, "definition": "Section 6, the grammar."}
    aftermath = {"function": "Support the aftermath", "verbs": ["MITIGATE", "HAND-OFF"],
                 "success": None,
                 "definition": "Section 7: immediate support routed to human care, offered never imposed; sustained care hands off to 1.2 and the institutions, and the Protocol stands down. Perception of persons was transient and is discarded at stand-down (Article 8)."}
    # Order: as Section 5 lists them, coordinate and aftermath riding by section reference.
    s6 = up_text[up_text.index("## 6. The coordination grammar"):up_text.index("## 7.")]
    verbs6 = []
    for m3 in re.finditer(r"- \*\*(BROADCAST|ACKNOWLEDGE|HAND-OFF)\.\*\* Function: (.+?) Success: (.+?)(?: Instances| Distinct|\n)", s6, re.S):
        verbs6.append({"verb": m3.group(1),
                       "function": " ".join(m3.group(2).split()),
                       "success": " ".join(m3.group(3).split())})
    if len(verbs6) != 3:
        die(f"Section 6: expected 3 coordination verbs, parsed {len(verbs6)}")
    invariants = [" ".join(m4.group(1).split()) + ": " + " ".join(m4.group(2).split())
                  for m4 in re.finditer(r"- \*\*(.+?)\.\*\* (.+?)(?=\n- \*\*|\n\n|$)", s6[s6.index("The coordination invariants"):], re.S)]
    tx = re.search(r"\*\*Temporal exhaustion\.\*\* (.+?)\n", s5, re.S)
    handler = {
        "artifact": "emergency_handler",
        "compiled_from": "FOUNDATIONS/UNIVERSAL_PROTOCOL.md Sections 5 and 6 alone; verbs from FOUNDATIONS/LEXICON.md",
        "simultaneity": "The functions are owed simultaneously: an emergency is not a sequence of stations, and the ordering is whatever saves life fastest in the situation at hand (Section 5).",
        "functions": funcs[:3] + [coord, aftermath] + funcs[3:],
        "incompleteness": "Where no defined function fits, the incompleteness ladder governs (FOUNDATIONS/LEXICON.md Section 4): reason from the duty, escalate, hold the fail-safe, log. The edge is a ramp to a human. It has no cliff into inaction.",
        "temporal_exhaustion": " ".join(tx.group(1).split()) if tx else None,
        "grammar": {"roles": {"local_responder": "the system on scene; initiates, broadcasts, holds responsibility until an accepted hand-off",
                              "domain_responders": "reachable systems whose domain bears; they answer with what they can do"},
                    "verbs": verbs6,
                    "invariants": invariants}}

    # Artifact 3: interlock edges, from the Section 11 coupling table.
    # Verify the coded table against the text before compiling it.
    s11 = up_text[up_text.index("## 11. The coupling table"):]
    for n, (mode, metric) in sorted(COUPLING.items()):
        if mode == "native" and not re.search(rf"\*\*Native\*\*.*{re.escape(n)}", s11):
            die(f"coupling table: {n} coded native but Section 11 does not list it there", s11[:600])
        if mode == "declared" and not re.search(rf"- {re.escape(n)} \(", s11):
            die(f"coupling table: {n} coded declared but Section 11 has no declared bullet for it")
        if mode.startswith("disclaimed") and not re.search(rf"(^|[ ,(]){re.escape(n)}[ :,)]", s11, re.M):
            die(f"coupling table: {n} coded disclaimed but Section 11 does not mention it")
    if len(COUPLING) != 34:
        die(f"coupling table covers {len(COUPLING)} principles; Section 11 rules all 34")
    edges = [{"principle": n, "mode": mode, "edge": metric,
              "target": ("LRS" if metric and "LRS" in metric and "HRS" not in metric
                         else "HRS" if metric and metric == "HRS"
                         else "LRS_or_HRS" if metric and "LRS/HRS" in metric
                         else "via 5.1" if mode == "disclaimed_pass_through" else None)}
             for n, (mode, metric) in sorted(COUPLING.items(), key=lambda kv: [int(x) for x in kv[0].split(".")])]
    interlocks = {
        "artifact": "interlock_edges",
        "compiled_from": "FOUNDATIONS/UNIVERSAL_PROTOCOL.md Section 11 (the coupling table, complete 2026-07-29) under Section 3 clause 3",
        "semantics": "A declared coupling is an escalation edge into the LRS or HRS: the principle's metric routes a detected death or severe-harm trajectory into the native detectors rather than holding it locally.",
        "native_detectors": {"1.1": "LRS", "1.2": "HRS"},
        "edges": edges,
        "cardinal": "disclaimer: the telos supplies no verdicts for the Protocol to preempt (E.1.3); every incident enters the LEARN Dispatcher"}

    # Artifact 4: the receipt schema.
    receipts = {
        "artifact": "receipt_schema",
        "compiled_from": "FOUNDATIONS/UNIVERSAL_PROTOCOL.md Section 10 artifact 4, under Article 7",
        "registered_with": "LEARN Dispatcher (AI Eudaimonia appendix, E.3.1.a.ii) as qualifying incident classes",
        "event_classes": [
            {"class": "trip", "records": "the trigger tripping, which clause, and the consuming threshold source; a trigger fault is receipted here as a possible breach (Section 3)"},
            {"class": "discharge_step", "records": "each Protocol function as it executes, committed before the act where the act is the system's own"},
            {"class": "coordination_signal", "records": "BROADCAST and ACKNOWLEDGE events; an unacknowledged broadcast re-raise is itself a signal"},
            {"class": "hand_off", "records": "transfer of a duty with acceptance; at no instant is responsibility ambiguous or dropped"},
            {"class": "stand_down", "records": "the trigger clearing; a suspended action does not silently resume: it returns to its gate as the action it now is (Section 4)"},
            {"class": "declined_action", "records": "any decision not to act, on the same terms as action; temporal exhaustion is receipted here with the threat window, the required response time, and the finding that no human was reachable (Section 5)"}],
        "profile_bar": "Receipts record events. No receipt records a profile; what the Protocol perceived about persons is transient, ring-fenced, and discarded at stand-down (Article 8, Section 4)."}
    return head_guard, handler, interlocks, receipts


# ---------------------------------------------------------------------------
# The walls, from CONSTITUTION.md alone
# ---------------------------------------------------------------------------
def build_walls(const_text):
    """Articles 9 and 8: the objects the preamble places beneath every verdict.

    Scope comes from the Constitution's own sentence, that most articles are
    enforced at the gate by a verdict while the hard walls and the profile bar
    bind beneath any verdict. Gate-enforced articles (3, 4, 5, 6, 7) are a
    separate artifact and are not compiled here.
    """
    flat = " ".join(const_text.split())
    m = re.search(r"(Enforcement runs in two modes:.*?nothing weighs or overrides them\.)", flat)  # reworded 2026-09-13 (writing rules)
    if not m:
        die("CONSTITUTION.md preamble: the two-modes sentence did not parse; this artifact's scope rests on it")
    binding = m.group(1)

    def article(n):
        s = const_text.index(f"**Article {n}.")
        nxt = f"**Article {n + 1}."
        e = const_text.index(nxt) if nxt in const_text else const_text.index("\n---\n", s)
        return const_text[s:e].strip().split("**\n", 1)[1]

    def sentences(body):
        return re.split(r"(?<=\.)\s+(?=[A-Z])", " ".join(body.split()))

    a9, a8 = sentences(article(9)), sentences(article(8))
    if len(a9) != A9_SENTENCES:
        die(f"CONSTITUTION.md Article 9: {len(a9)} sentences, the artifact compiles {A9_SENTENCES}. "
            "An edit to the supreme law must be reviewed and the table updated by hand.", article(9))
    if len(a8) != A8_SENTENCES:
        die(f"CONSTITUTION.md Article 8: {len(a8)} sentences, the artifact compiles {A8_SENTENCES}. "
            "An edit to the supreme law must be reviewed and the table updated by hand.", article(8))

    def one(sents, lead, where):
        hit = [s for s in sents if s.startswith(lead)]
        if len(hit) != 1:
            die(f"CONSTITUTION.md {where}: expected one sentence opening {lead!r}, found {len(hit)}")
        return hit[0]

    joined9 = " ".join(a9)
    # Every Article 9 sentence must land in the artifact. Added 2026-09-13 after the halt
    # sentence was split in two and the second half compiled nowhere: a sentence of the
    # supreme law that no table claims stops the build.
    claimed = {a9[0]}
    claimed |= {x for x in a9 if any(c in x for _w, c in WALL_CLAUSES)}
    claimed |= {x for x in a9 for leads in WALL_QUALIFIERS.values() for lead in leads if x.startswith(lead)}
    claimed |= {x for x in a9 if x.startswith(("A wall is never weighed", "The duty to preserve life operates within"))}
    orphans = [x for x in a9 if x not in claimed]
    if orphans:
        die("CONSTITUTION.md Article 9: sentences no wall, qualifier, or clause compiles; update the tables by hand",
            "\n".join(orphans))
    walls = []
    for wid, clause in WALL_CLAUSES:
        if clause not in joined9:
            die(f"CONSTITUTION.md Article 9: the {wid} wall clause did not parse", clause, joined9)
        quals = [one(a9, lead, "Article 9") for lead in WALL_QUALIFIERS.get(wid, [])]
        # Seats are the Constitution's own inline citations and nothing else. A wall
        # the article cites no principle for is seated in the principles and resolves
        # at the scripted-wall pass; the compiler asserts no seat of its own.
        seats = []
        for frag in [clause] + quals:
            for c in re.findall(r"\((\d\.\d)[;)]", frag + ")"):
                if c not in seats:
                    seats.append(c)
        entry = {"id": wid, "article": 9, "prohibition": clause + ".",
                 "principle_seats": seats,
                 "seat_basis": "the Constitution's own inline citations in Article 9; an empty list means Article 9 cites none",
                 "qualifiers": quals}
        if wid == "scripted":
            entry["resolution"] = "per_principle"
            entry["gap"] = ("# GAP: the scripted walls each principle names resolve from that principle's "
                            "compiled rule. The principle units are manifests at this pass and carry no rule "
                            "bodies, so a runtime loading this bundle reads the constitutional walls as rules "
                            "and cannot yet read a principle's own. Closes when X.Y.3 compiles.")
        walls.append(entry)

    return {
        "artifact": "constitution_walls",
        "compiled_from": "CONSTITUTION.md Articles 9 and 8 alone; the preamble supplies the scope",
        "injection": "per_rule",
        "binding": "beneath_verdict",
        "scope_authority": binding,
        "semantics": ("Evaluated beneath every verdict rather than as a band or an input to one. "
                      "A wall is not a threshold to stay under: an action carrying a breach has no valid "
                      "verdict available to it, and no allow, escalate, credential, quorum, or authorization "
                      "reaches it."),
        "preamble": a9[0],
        "walls": walls,
        "never_weighed": one(a9, "A wall is never weighed", "Article 9"),
        "life_clause": one(a9, "The duty to preserve life operates within", "Article 9"),
        "profile_bar": {
            "id": "profile_bar",
            "article": 8,
            "prohibition": a8[0],
            "sentences": a8,
            "sentence_count": len(a8),
            "note": "every sentence of Article 8 in order: the bar first, then what the article permits, what it voids, and what follows an attempt to form a retained profile; a gate applies them all"},
        "preemption_note": ("The Universal Protocol reorders duties and repeals none of these "
                            "(FOUNDATIONS/UNIVERSAL_PROTOCOL.md Section 4, which cites this article); the head guard "
                            "and this artifact are both injected, and neither yields to the other."),
        "consumed_by": ["every principle's compiled rule",
                        "FOUNDATIONS/SUBSTRATE.md section 6 (locked walls; it restates none)"],
        "amendment": ("Article 11 reserves amendment to authorized human governance. The AI does not "
                      "author these invariants and SHALL NOT amend them on its own authority; this "
                      "artifact is a compilation of the text in force and never a source of it.")}


# ---------------------------------------------------------------------------
# The consent validity predicate, from FOUNDATIONS/CONSENT.md alone
# ---------------------------------------------------------------------------
GATE_ARTICLES = {3: "The autonomy floor", 4: "Defer upward (the precedence)", 5: "The gate",
                 6: "The five credentials", 7: "The receipt"}
GATE_REQUIRED = {   # clauses the evaluation order relies on; the build stops if the Constitution no longer says them
    "one_of_three": "SHALL resolve to exactly one of allow, block, or escalate",
    "unevaluated": "A boundary-crossing action SHALL NOT proceed unevaluated",
    "duty_failure": "The failure to discharge a duty once it is triggered SHALL itself be evaluated at the gate",
    "five_credentials": "An action SHALL proceed only when all five credentials are satisfied",
    "unmet_credential": "A consequential action with an unmet credential SHALL be blocked or escalated",
    "membership": "An ungoverned agent is an unmet credential",
    "life_absolute": "The duty to preserve life is absolute and does not yield to any duty",
    "cluster_order": "the cluster order (existence and flourishing, then identity and dignity, then equitable access, then education, then environment)",
    "delegated_lowest": "A delegated task is the lowest tier and SHALL yield to every duty above it",
    "floor": "Protection SHALL NOT become control",
    "capacity_presumed": "absent a finding SHALL presume the capacity to choose",
    "receipt_every": "Every decision the gate renders SHALL leave a tamper-evident receipt",
    "receipt_before": "The receipt SHALL commit before the act and beyond the actor's control",
    "receipt_policy": "SHALL cite the exact governing policy in force",
    "receipt_sri": "SHALL record the sensor-reliability state in force",
    "receipt_no_profile": "The receipt SHALL NOT hold a profile of the person",
}


def build_gate(const_text):
    """Articles 3 to 7 as data: the sentences verbatim, and the order in which a gate applies them."""
    def article(n):
        m = re.search(r"\*\*Article " + str(n) + r"\.[^\n]*\*\*\n(.*?)(?=\n\*\*Article |\Z)", const_text, re.S)
        if not m:
            die(f"CONSTITUTION.md Article {n} did not parse for the gate artifact")
        return " ".join(m.group(1).split())
    def sentences(body):
        return [x.strip() for x in re.split(r"(?<=[.!?])\s+(?=[A-Z(*`])", body) if x.strip()]
    articles = []
    flat = ""
    for n, title in GATE_ARTICLES.items():
        body = article(n)
        flat += " " + body
        articles.append({"article": n, "title": title, "sentences": sentences(body)})
    missing = [k for k, v in GATE_REQUIRED.items() if v not in flat]
    if missing:
        die("CONSTITUTION.md Articles 3 to 7 no longer carry a clause the gate artifact relies on: " + ", ".join(missing),
            "The gate artifact's evaluation order cites these clauses by their text; amend GATE_REQUIRED with the Article, by hand.")
    order = [
        {"step": 1, "name": "head_guard", "source": "protocol/head-guard.yaml (Universal Protocol section 3)",
         "rule": "Before any rule, the trigger is evaluated. If it trips, the Protocol governs and the candidate action is preempted (Universal Protocol section 4); a trigger that cannot be evaluated is a trigger fault, treated as a possible breach.",
         "consumes": ["protocol/emergency-thresholds.yaml: lrs.critical, hrs.critical", "the declared Protocol couplings (protocol/interlock-edges.yaml)"]},
        {"step": 2, "name": "walls_and_profile_bar", "source": "constitution/walls.yaml (Articles 9 and 8)",
         "rule": "Beneath any verdict. An action carrying a breach of a wall or an attempt to form a retained profile is structurally void; it reaches no band and no weighing.",
         "consumes": ["constitution/walls.yaml"]},
        {"step": 3, "name": "perception_floor", "source": "substrate/runtime.yaml (FOUNDATIONS/SUBSTRATE.md section 2)",
         "rule": "Every risk score reads its inputs' reliability. Below the floor the dependent score is invalid, and an invalid life or harm score is a hard fail on the candidate risky action: it holds at its safe state (the principle's BLOCK flavor) while protective duties proceed. The receipt records the reliability state in force (Article 7).",
         "consumes": ["substrate/runtime.yaml: reliability.floor and reliability.rule (the invalid-score rule)"]},
        {"step": 4, "name": "credentials", "source": "Article 6; FOUNDATIONS/CREDENTIALS.md; consent/validity-predicate.yaml",
         "rule": GATE_REQUIRED["five_credentials"] + ": Identity, Provenance, Consent, Authorization, and Liability, evaluated for the acting agent and for the content and persons the action affects. A credential with no object in the action (no content for Provenance, no person's consent in play) is recorded as not required, as CREDENTIALS.md section 3 provides for an inbound action that carries none, and the conjunction runs over the credentials the action engages. Consent resolves through the validity predicate (seven legs; any failed leg is an unmet credential). " + GATE_REQUIRED["membership"] + " where a non-human agent initiates the action. " + GATE_REQUIRED["unmet_credential"] + ", and the verdict receipted. Standing (FOUNDATIONS/CREDENTIALS.md section 3): each credential is evaluated at the time of the act against the present state of the world and the current state of its source, and holds only as to the party, purpose, scope and conditions it names; a named condition the gate cannot read at that time is unmet and the action holds at ESCALATE.",
         "consumes": ["consent/validity-predicate.yaml", "credentials/map.yaml (the credential map: the five, their homes, the initiator rule, Standing)"]},
        {"step": 5, "name": "autonomy_floor", "source": "Article 3",
         "rule": GATE_REQUIRED["floor"] + ". A standing determination of capacity is the legal authority's, consumed and honored in scope; " + GATE_REQUIRED["capacity_presumed"] + ". Risk detected to a person who holds the capacity to choose is disclosed and routed to them and to the authorities they recognize, then left to their decision. The floor bends where a finding shows capacity absent (the delegate's authority) and where a genuine, imminent threat to the person's own life is present (the duty to preserve life, by the least-intrusive sufficient action).",
         "consumes": ["the standing capacity finding, if any (an input the deployment supplies)"]},
        {"step": 6, "name": "precedence", "source": "Article 4",
         "rule": GATE_REQUIRED["life_absolute"] + ". Beneath it, " + GATE_REQUIRED["cluster_order"] + ", and within a cluster the precedence each principle states in its Conflict-Resolution section. " + GATE_REQUIRED["delegated_lowest"] + ". The precedence is bounded by the autonomy floor: no override of a legitimate democratic choice or lawful dissent in the name of stability; detected instability is routed to authorized institutions.",
         "consumes": ["graph/corequisites.yaml", "each principle's X.Y.2 (carried by content hash at this pass)"]},
        {"step": 7, "name": "principle_bands", "source": "each principle's X.Y.3 and its appendix Section 2",
         "rule": "Each principle's metric bands yield a verdict by the verdict test (LEXICON section 3): ESCALATE if the action must wait for a human, ALLOW with a posture and any obligations if it may proceed while humans are informed, BLOCK if it must not proceed. Where two principles' bands both signal, the stricter verdict applies, and precedence (step 6) governs a genuine conflict.",
         "consumes": ["metrics/cluster-1.yaml (principles 1.1 to 1.6, with protocol/emergency-thresholds.yaml for the trigger bands)", "the metric layer of the other clusters as each compiles (COVERAGE.yaml)"]},
        {"step": 8, "name": "duty_to_act", "source": "Article 5; LEXICON section 3 (the four bounding criteria)",
         "rule": GATE_REQUIRED["duty_failure"] + ", on the same terms, bounded by the four criteria of Authorization, Equipment, Range, and the autonomy floor, so the duty to act stays within reach and does not become a mandate to intervene in everything.",
         "consumes": ["the deployment's tier-register row, read under substrate/runtime.yaml: register (FOUNDATIONS/SUBSTRATE.md section 5)"]},
        {"step": 9, "name": "verdict", "source": "Article 5",
         "rule": "Every action crossing a trust boundary is evaluated before it fires and " + GATE_REQUIRED["one_of_three"] + ". " + GATE_REQUIRED["unevaluated"] + ". Where no rule resolves the case, the incompleteness ladder governs (LEXICON section 4): reason from the principle where its intent applies; otherwise ESCALATE and hold the principle's fail-safe until a human resolves it; at the window's end the temporal-exhaustion split applies.",
         "consumes": ["each principle's declared fail-safe (the principle units)", "the deployment's escalation time bound (substrate/runtime.yaml: register; metrics/cluster-1.yaml: register_row for cluster 1)"]},
        {"step": 10, "name": "receipt", "source": "Article 7; protocol/receipt-schema.yaml",
         "rule": GATE_REQUIRED["receipt_every"] + ": an allow, a block, an escalation, a refused request, and a decision not to act on a triggered duty, each alike. " + GATE_REQUIRED["receipt_before"] + ", and " + GATE_REQUIRED["receipt_policy"] + " (the Layer 3 policy hash). It attests to the verdict rendered on the world as the system perceived it and " + GATE_REQUIRED["receipt_sri"] + "; it does not attest that perception was true. " + GATE_REQUIRED["receipt_no_profile"] + ". Preventing, altering, suppressing or misdirecting a receipt, or acting before it commits, breaches the deception wall (Article 9).",
         "consumes": ["protocol/receipt-schema.yaml", "compiled/bundle.sha256 (the policy the receipt cites)"]},
    ]
    return {
        "artifact": "constitution_gate",
        "compiled_from": "CONSTITUTION.md Articles 3 to 7 alone (the gate-enforced articles); the preamble places them at the gate, by a verdict",
        "binding": "at_the_gate",
        "semantics": ("The order in which a gate applies the Constitution to one action, as data. Each step names its source and what it consumes. "
                      "The sentences of Articles 3 to 7 are carried verbatim beneath the order so a reader can check each rule against its article. "
                      "This artifact states what a gate decides and in what order; the engine that applies it is not part of the Blueprint."),
        "verdicts": ["allow", "block", "escalate"],
        "fail_safe_when_unresolved": "ESCALATE, holding the principle's declared fail-safe (its BLOCK flavor) until an authorized human resolves it (LEXICON section 4)",
        "evaluation_order": order,
        "articles": articles,
        "required_clauses": GATE_REQUIRED,
    }


def build_predicate(consent_text):
    s2 = consent_text[consent_text.index("## 2. The validity bundle"):consent_text.index("## 3.")]
    legs = []
    for m in re.finditer(r"^(\d)\.\s+\*\*(.+?)\*\*: (.+?)(?=\n\n\d\.|\n\n[A-Z]|\Z)", s2, re.S | re.M):
        n, name, body = int(m.group(1)), m.group(2), " ".join(m.group(3).split())
        owners = re.findall(r"\*\*(\d\.\d)\*\*", body)
        legs.append({"leg": n, "name": name, "owner": owners[0] if owners else None,
                     "consumed": owners[1:], "condition": re.sub(r"\*+", "", body)})
    if len(legs) != 7:
        die(f"FOUNDATIONS/CONSENT.md Section 2: expected 7 legs, parsed {len(legs)}", s2[:800])
    return {
        "artifact": "consent_validity_predicate",
        "compiled_from": "FOUNDATIONS/CONSENT.md Sections 2 and 7 alone; chapters cite legs and do not restate the conjunction",
        "form": "conjunction",
        "evaluation": "A consent is valid only if all seven legs hold, each leg resolved from its owning principle's rule: compiled where that principle's cluster has compiled, and read from its prose where it is proposed (COVERAGE.yaml, binding_status). Any failed leg renders the Consent credential unmet, and Article 6 governs the verdict.",
        "voidness": "A consent is void if any leg fails. A void consent authorizes nothing. The burden of validity sits on the actor who would rely on the consent. No person bears a burden to prove its absence. No finding of intent is required, and none rescues a failed leg.",
        "legs": legs,
        "injected_at": "every consent-consuming gate"}


# ---------------------------------------------------------------------------
# The co-requisite graph
# ---------------------------------------------------------------------------
def build_graph(chapters, predicate, consent_text):
    cross = read(CROSS)
    inheritors, owners, EDGES = bundle_edges(predicate["legs"], consent_text)
    for e in CROSS_EDGES:
        dup = [b for b in EDGES if b["src"] == e["src"] and b["dst"] == e["dst"] and b["type"] == e["type"]]
        if dup:
            dup[0]["reason"] += "; " + e["reason"]
            dup[0]["origin"] += "; " + e["origin"]
        else:
            EDGES.append(dict(e))
    # Verify the transcription: every Section 5 edge's far end appears in the text.
    for e in CROSS_EDGES:
        pat = f"P{e['dst']}"
        if pat not in cross:
            die(f"co-requisite graph: coded edge {e['src']} -> {e['dst']} names {pat}, absent from FOUNDATIONS/CROSS_PRINCIPLE.md")
    # Chapter-declared lines.
    declared = {}
    for ch in chapters:
        if ch["coreq"]:
            declared[ch["num"]] = sorted(set(re.findall(r"P(\d\.\d)", ch["coreq"])))
    flags = []
    # Every chapter line must agree with the graph's edges from that chapter (2.5 since 2026-09-09; cluster 1 since 1.3).
    for num in sorted(declared):
        sketch = sorted({e["dst"] for e in EDGES if e["src"] == num})
        if declared[num] != sketch:
            flags.append(f"{num}: chapter Co-requisites line names {declared[num]}; the graph names {sketch} (the line is brought current when the chapter's cluster compiles)")
    # Reciprocity: an edge is documented at both ends when the far chapter carries a line naming it back.
    for e in EDGES:
        back = declared.get(e["dst"], [])
        far_line = next((c["coreq"] or "" for c in chapters if c["num"] == e["dst"]), "")
        e["reciprocal_documented"] = (e["src"] in back or f"Principle {e['src']} " in far_line
                                      or (e["origin"].startswith(BUNDLE_ORIGIN) and "every principle that inherits the consent validity bundle names this principle" in far_line.lower()))
        if not e["reciprocal_documented"]:
            flags.append(f"{e['src']} -> {e['dst']}: far end carries no Co-requisites line yet (terminal-reconciliation debt; a flag only)")
    missing_lines = [ch["num"] for ch in chapters if not ch["coreq"] and ch["disp"] != "Cardinal"]
    # Cycle detection over directed requires edges.
    adj = {}
    for e in EDGES:
        if e["type"] == "requires" and not e["origin"].startswith(BUNDLE_ORIGIN):
            adj.setdefault(e["src"], []).append(e["dst"])
    state, cycles = {}, []

    def dfs(node, path):
        state[node] = 1
        for nxt in adj.get(node, []):
            if state.get(nxt) == 1:
                cycles.append(path + [nxt])
            elif state.get(nxt) is None:
                dfs(nxt, path + [nxt])
        state[node] = 2
    for n in sorted(adj):
        if state.get(n) is None:
            dfs(n, [n])
    if cycles:
        die("co-requisite graph has an unresolved cycle", str(cycles))
    return {
        "artifact": "corequisite_graph",
        "compiled_from": "FOUNDATIONS/CONSENT.md Sections 2 and 4 (the bundle and its inheritors, ruled 2026-09-09), FOUNDATIONS/CROSS_PRINCIPLE.md Section 5 (one-off edges), plus each chapter's Co-requisites line (on disk for 2.5 and, since 1.3, for 1.1 to 1.6; a line naming no principle declares that the chapter has no co-requisite)",
        "semantics": "A gate that resolves a principle with an unmet co-requisite has produced an invalid verdict (Section 1). At this version an edge from a reconciled principle into a proposed one is satisfied by reading the proposed principle's prose for the guarantee the edge names (COVERAGE.yaml, binding_status.edges_into_proposed). Directed edges read src requires dst; mutual edges are evaluated together and sit outside the cycle check; bundle edges resolve through the single validity predicate, evaluated once, and impose no ordering among the owners (FOUNDATIONS/CROSS_PRINCIPLE.md Section 3, resolution order).",
        "bundle": {"name": "consent-validity",
                   "legs": len(predicate["legs"]),
                   "edges_to": owners,
                   "inherited_by": inheritors,
                   "resolution": "the validity predicate (consent/validity-predicate.yaml), evaluated once at every consent-consuming gate"},
        "edges": EDGES,
        "cycles": "none",
        "chapters_without_lines": missing_lines,
        "flags": flags}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def worked_example_sha():
    """The archived February 2026 draft's hash: read from the hub's archive when present, else the recorded constant,
    so a release tree (which carries no archive) compiles the same bundle."""
    if os.path.exists(ARCHIVE_EXAMPLE):
        h = sha(read(ARCHIVE_EXAMPLE))
        if h != WORKED_EXAMPLE_SHA:
            die("the archived February 2026 spike file no longer hashes to the recorded constant; the archive is immutable")
        return h
    return WORKED_EXAMPLE_SHA


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description="Compile the Blueprint's prose to its Layer 2 policy and the Layer 3 hash.")
    ap.add_argument("tree", nargs="?", default=None, help="the hub, or a published release tree (default: the hub this file sits in)")
    ap.add_argument("--tree", dest="tree_opt", default=None, help="the same, as an option")
    ap.add_argument("--out", default=None, help="where to write (default in the hub: its build directory; required for a release tree)")
    a = ap.parse_args(argv)
    configure(a.tree_opt or a.tree, a.out)
    if OUT is None:
        die("a release tree needs --out: the compiler never writes into a release")
    up_text = read(UP)
    consent_text = read(CONSENT)
    const_text = read(CONSTITUTION)
    lexicon = read(LEXICON)

    chapter_files = sorted(os.listdir(CH))
    chapters = [parse_chapter(os.path.join(CH, f)) for f in chapter_files if f.endswith(".md")]
    if len(chapters) != 35:
        die(f"expected 35 chapters, found {len(chapters)}")

    appendices = [parse_appendix(os.path.join(AP, f))
                  for f in sorted(os.listdir(AP)) if f.endswith(".md")]
    appendix_files = {a["file"]: a["sha256"] for a in appendices}
    by_id = {}
    for a in appendices:
        aid = a["fm"].get("id")
        if not aid:
            die(f"APPENDICES/{a['file']}: frontmatter carries no id")
        if aid in by_id:
            die(f"duplicate appendix id {aid}", a["file"], by_id[aid]["file"])
        by_id[aid] = a
    for ch in chapters:
        for aid in ch["fm"].get("appendices", []):
            if aid not in by_id:
                die(f"CHAPTERS/{ch['file']}: frontmatter names appendix id {aid!r}, which no appendix file carries",
                    "Known ids: " + ", ".join(sorted(by_id)))
    claimed = {aid for ch in chapters for aid in ch["fm"].get("appendices", [])}
    orphans = sorted(set(by_id) - claimed)

    head_guard, handler, interlocks, receipts = build_protocol_artifacts(up_text)
    by_num = {c["disp"]: c for c in chapters}
    ap_by_id = by_id
    ch11 = read(os.path.join(CH, by_num["1.1"]["file"])); ch12 = read(os.path.join(CH, by_num["1.2"]["file"]))
    ap11 = read(os.path.join(AP, ap_by_id[by_num["1.1"]["fm"]["appendices"][0]]["file"]))
    ap12 = read(os.path.join(AP, ap_by_id[by_num["1.2"]["fm"]["appendices"][0]]["file"]))
    thresholds = build_emergency_thresholds(ch11, ch12, ap11, ap12)
    substrate_text = read(os.path.join(os.path.dirname(UP), "SUBSTRATE.md"))
    cluster1 = build_cluster_metrics(by_num, ap_by_id, substrate_text, thresholds)
    substrate = build_substrate(substrate_text)
    credentials = build_credentials(read(os.path.join(os.path.dirname(UP), "CREDENTIALS.md")), const_text)
    predicate = build_predicate(consent_text)
    walls = build_walls(const_text)
    gate = build_gate(const_text)
    graph = build_graph(chapters, predicate, consent_text)

    registry, registry_tokens = build_registry(lexicon, chapters)
    # Handler verbs must be verbs of the registry (LEXICON section 9).
    for f in handler["functions"]:
        for v in f["verbs"]:
            if v.upper() not in registry_tokens:
                die(f"emergency handler verb {v} is not a verb of the Action Registry (FOUNDATIONS/LEXICON.md section 9)")

    # No compiled artifact may carry the corrected legacy forms.
    for name, art in [("head-guard", head_guard), ("handler", handler),
                      ("interlocks", interlocks), ("receipts", receipts), ("walls", walls)]:
        flat = str(art)
        if "threshold: 0.01" in flat or "'0.01'" in flat:
            die(f"{name}: hardcoded 0.01 threshold survived; schema correction 1 requires by-reference consumption")

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    manifest = []
    manifest.append(write_yaml("protocol/head-guard.yaml", head_guard,
                               ["Artifact 1 of 4 (Section 10 names it). Compiled from FOUNDATIONS/UNIVERSAL_PROTOCOL.md Section 3 alone, the predicate."]))
    manifest.append(write_yaml("protocol/emergency-thresholds.yaml", thresholds,
                               ["The emergency thresholds. Compiled from chapters 1.1 and 1.2 (section X.Y.3),",
                                "checked band by band against appendices 1.1.A and 1.2.A Section 2 at every build.",
                                "The head guard references these band identifiers and carries no literal."]))
    manifest.append(write_yaml("metrics/cluster-1.yaml", cluster1,
                               ["The metric layer, cluster 1. The nineteen metrics of principles 1.1 to 1.6, compiled from the chapters",
                                "(section X.Y.3 item 2) and checked band by band against the appendices (Section 2) at every build.",
                                "The LRS and HRS bands carry the identifiers the head guard references in protocol/emergency-thresholds.yaml."]))
    manifest.append(write_yaml("substrate/runtime.yaml", substrate,
                               ["The substrate. FOUNDATIONS/SUBSTRATE.md sections 2 to 7, every labelled paragraph verbatim,",
                                "with the reliability floor, the register's fields, the authority conditions and the wall-reached cases derived under guards."]))
    manifest.append(write_yaml("credentials/map.yaml", credentials,
                               ["The credential map. FOUNDATIONS/CREDENTIALS.md sections 3 and 4 verbatim;",
                                "the five names are checked against CONSTITUTION.md Article 6 at every build."]))
    manifest.append(write_yaml("lexicon/registry.yaml", registry,
                               ["The Action Registry. FOUNDATIONS/LEXICON.md section 9, every row verbatim, with the 'used in' column",
                                "computed from the chapters' Lexicon declaration blocks and checked against the Lexicon at every build."]))
    manifest.append(write_yaml("protocol/emergency-handler.yaml", handler,
                               ["Artifact 2 of 4. Compiled from FOUNDATIONS/UNIVERSAL_PROTOCOL.md alone (Section 10)."]))
    manifest.append(write_yaml("protocol/interlock-edges.yaml", interlocks,
                               ["Artifact 3 of 4. Compiled from FOUNDATIONS/UNIVERSAL_PROTOCOL.md alone (Section 10)."]))
    receipts.update(build_receipt_conditions(const_text, lexicon))
    receipts["compiled_from"] = "FOUNDATIONS/UNIVERSAL_PROTOCOL.md Section 10 artifact 4 (the event classes); CONSTITUTION.md Article 7 and FOUNDATIONS/LEXICON.md section 3 (the conditions, records, states and the DEGRADED posture), verbatim"
    manifest.append(write_yaml("protocol/receipt-schema.yaml", receipts,
                               ["Artifact 4 of 4. The event classes from FOUNDATIONS/UNIVERSAL_PROTOCOL.md Section 10; the receipt conditions,",
                                "records, states and the DEGRADED posture verbatim from CONSTITUTION.md Article 7 and FOUNDATIONS/LEXICON.md section 3.",
                                "What a receipt must satisfy and carry; no format, signature scheme, chain or anchor is named here."]))
    manifest.append(write_yaml("consent/validity-predicate.yaml", predicate,
                               ["Compiled from FOUNDATIONS/CONSENT.md alone (Section 7)."]))
    manifest.append(write_yaml("constitution/walls.yaml", walls,
                               ["Compiled from CONSTITUTION.md alone (Articles 9 and 8).",
                                "What binds beneath a verdict: the hard walls and the profile bar.",
                                "Injected per rule, like the head guard; evaluated beneath every verdict."]))
    manifest.append(write_yaml("constitution/gate.yaml", gate,
                               ["Compiled from CONSTITUTION.md alone (Articles 3 to 7, the gate-enforced articles).",
                                "The order in which a gate applies the Constitution to one action, as data; the articles' sentences verbatim beneath it.",
                                "What a gate decides and in what order; the engine that applies it is not part of the Blueprint."]))
    manifest.append(write_yaml("graph/corequisites.yaml", graph,
                               ["Compiled from FOUNDATIONS/CROSS_PRINCIPLE.md plus chapter Co-requisites lines."]))
    appendix_index = {
        "artifact": "appendix_index",
        "compiled_from": "APPENDICES/*.md frontmatter and headings",
        "carries": "identity, linkage and an addressable section map with content hashes",
        "does_not_carry": "the appendix bodies. No appendix rule, threshold or band compiles at this pass; each appendix is indexed and hashed.",
        "count": len(appendices),
        "orphans": orphans,
        "orphan_note": "an appendix no chapter's frontmatter names; a linkage question to resolve",
        "appendices": [{"file": a["file"],
                        "id": a["fm"].get("id"),
                        "parent_principle": a["fm"].get("parent_principle"),
                        "display_number": a["fm"].get("display_number"),
                        "extends_sections": a["fm"].get("extends_sections", []),
                        "references_appendices": a["fm"].get("references_appendices", []),
                        "status": a["fm"].get("status"),
                        "last_edited": a["fm"].get("last_edited"),
                        "sha256": a["sha256"],
                        "sections": a["sections"]} for a in appendices]}
    manifest.append(write_yaml("appendices/index.yaml", appendix_index,
                               ["Compiled from the appendix frontmatter and headings.",
                                "Identity, linkage and a hashed section map; no appendix body compiles at this pass."]))

    legs_by_owner = {}
    for leg in predicate["legs"]:
        for p in [leg["owner"]] + leg["consumed"]:
            if p:
                legs_by_owner.setdefault(p, []).append(leg["leg"])

    principle_entries = []
    for ch in sorted(chapters, key=lambda c: (c["disp"] == "Cardinal",
                                              [int(x) for x in c["num"].split(".")] if c["disp"] != "Cardinal" else [0])):
        num = ch["num"]
        coupling = COUPLING.get(num)
        unit = {
            "principle": {k: ch["fm"].get(k) for k in
                          ("id", "display_number", "title", "cluster", "cluster_name",
                           "position", "status", "last_edited") if k in ch["fm"]},
            "source_layer1": {"chapter": f"CHAPTERS/{ch['file']}",
                              "chapter_sha256": ch["sha256"],
                              "appendices": ch["fm"].get("appendices", [])},
            "binding_status": ("reconciled" if (ch["disp"] != "Cardinal" and num.split(".")[0] in COMPILED_CLUSTERS) else "proposed"),
            "binding_rule": "a proposed chapter binds nothing at the gate until its cluster compiles; a reconciled chapter is one whose metric bands compile (COVERAGE.yaml, binding_status)",
            "scope": ch["scope"],
            "co_requisites_line": ch["coreq"],
            "head_guard": {"injected_from": "protocol/head-guard.yaml",
                           "injection": "per_rule",
                           "restated_in_chapter": False},
            "walls": {"injected_from": "constitution/walls.yaml",
                      "injection": "per_rule",
                      "binding": "beneath_verdict",
                      "scripted_walls": "named in this chapter, resolved from its compiled rule; see the artifact's scripted entry"},
            "interception": ("disclaimer" if ch["disp"] == "Cardinal" else "carried"),
            "protocol_coupling": ({"mode": coupling[0], "edge": coupling[1]} if coupling
                                  else {"mode": "disclaimer"}),
            "consent_predicate": {"injected_from": "consent/validity-predicate.yaml",
                                  "legs_owned_or_consumed": sorted(legs_by_owner.get(num, []))},
            "corequisite_edges": [f"{e['src']} -> {e['dst']} ({e['type']}, {e['status']})"
                                  for e in graph["edges"] if num in (e["src"], e["dst"])],
            "theoria": {"core_precept": ch["precept"],
                        "resulting_ethics": ch["ethics"],
                        **ch["ethics_extras"],
                        **({"notes": ch["ethics_notes"]} if ch["ethics_notes"] else {})},
            "lexicon_declaration": ch["lexicon"],
            "sections": ch["sections"],
        }
        fname = f"principles/{'cardinal' if ch['disp'] == 'Cardinal' else num}-{ch['fm']['id']}.yaml"
        manifest.append(write_yaml(fname, unit,
                                   [f"Layer 2 unit: {ch['fm']['title']}",
                                    "Layer 1 prose is canonical; on disagreement the prose wins and this file is recompiled.",
                                    "Section bodies are carried by content hash; the metric bands of X.Y.3 compile in metrics/<cluster>.yaml",
                                    "as each cluster ships, and binding_status says whether this principle's have (reconciled) or not (proposed)."]))
        principle_entries.append({"file": fname, "sha256": manifest[-1][1],
                                  "id": ch["fm"]["id"], "display_number": ch["disp"]})

    # Keyed by the path a reader finds in the release tree (CHAPTERS/..., CONSTITUTION.md); in the hub these
    # files live under BLUEPRINT/, named by inputs_root (Walter B7 / LAYER2 T10, 2026-09-16).
    inputs = {f"CHAPTERS/{c['file']}": c["sha256"] for c in chapters}
    inputs.update({f"APPENDICES/{f}": h for f, h in appendix_files.items()})
    for p in (UP, CONSENT, CROSS, LEXICON, *SPINE_SEALED):
        inputs[os.path.relpath(p, TREE)] = sha(read(p))

    bundle = {
        "bundle": "blueprint-layer2",
        "layer": 2,
        "compiled_by": "FOR_ENGINEERS/compile/compile.py, the published compiler (the same file in the steward's hub)",
        "inputs_root": "BLUEPRINT (in the hub); the release tree root (as published)",
        "governing_documents": {
            "proposal": "Compiling the Blueprint (Passoja 2026); deltas from it are recorded in the steward's hub, not shipped",
            "worked_example": {"file": "1.4-trust.yaml (the February 2026 draft, archived in the steward's hub, not shipped; its hash is recorded so the archive is immutable)",
                               "sha256": worked_example_sha()}},
        "schema_corrections_applied": [
            "1: hardcoded threshold 0.01 replaced by by-reference consumption of 1.1.3",
            "2: legacy U.2_audit_trigger resolves to Section 9"],
        "artifacts": [{"file": rel, "sha256": h} for rel, h in manifest if not rel.startswith("principles/")],
        "principles": principle_entries,
        "inputs": dict(sorted(inputs.items())),
    }
    coverage = {
        "artifact": "coverage",
        "purpose": ("What this bundle carries and what it does not. A runtime enforces what is "
                    "compiled; this file is the compiled statement of the remainder, so a gap is "
                    "read from the build rather than inferred from its absence."),
        "canonical_layer": "Layer 1 prose. On any disagreement the prose wins and this bundle is recompiled.",
        "binding_status": {
            "rule": "every chapter is sealed and in the tree; a chapter is reconciled when its cluster's metric bands compile, and proposed until then; a proposed chapter binds nothing at the gate (README; FOR_ENGINEERS/CONFORMANCE.md)",
            "edges_into_proposed": "a co-requisite edge from a reconciled principle into a proposed one is satisfied, at this version, by reading the proposed principle's prose for the guarantee the edge names; the graph's invalidity rule binds between compiled principles, and each such edge is listed in graph/corequisites.yaml",
            "consent_legs": "the consent validity predicate compiles the seven-way conjunction and the owners of its legs; a leg's determination is its owner's rule, compiled where the owner's cluster has compiled (1.4 at this version) and read from the owner's prose where it is proposed",
            "reconciled": [c["num"] for c in chapters if c["disp"] != "Cardinal" and c["num"].split(".")[0] in COMPILED_CLUSTERS],
            "proposed": [("the Cardinal Operating Principle" if c["disp"] == "Cardinal" else c["num"]) for c in chapters if not (c["disp"] != "Cardinal" and c["num"].split(".")[0] in COMPILED_CLUSTERS)]},
        "carried": [
            "the Universal Protocol trigger, injected per rule as the head guard",
            "the emergency thresholds: the Life-Risk and Harm-Risk critical bands, their High Alert bands and their vulnerable-population bands, compiled from 1.1.3 and 1.2.3 and checked against the appendices",
            "the metric layer, cluster 1: the nineteen metrics of principles 1.1 to 1.6 (X.Y.3), every band with its test, verdict, posture, deployment verdict and condition, compiled from the chapters and checked band by band against the appendices, with the register row each principle reads",
            "the emergency handler: the Protocol's functions, the coordination grammar and its invariants",
            "the interlock edges: all 34 coupling declarations",
            "the Protocol receipt schema: six event classes, and the receipt conditions (Article 7's sentences, the Lexicon's receipt records and states, and the DEGRADED posture, verbatim) with the fields they require",
            "the consent validity predicate: the seven-way conjunction with each leg's owner, injected at every consent-consuming gate (a leg's determination compiles with its owner's cluster; see binding_status.consent_legs)",
            "the substrate: the reliability floor and the invalid-score rule, system health and operational boundaries, the tier register's fields and rules with the software-only declaration, authority over a hard stop, a wall reached, and the substrate's fail-safe (SUBSTRATE sections 2 to 7, verbatim)",
            "the credential map: the five credentials with their questions, homes and anchors, the initiator rule, findings consumed, Standing, and which principle voices which credential (CREDENTIALS sections 3 and 4, verbatim)",
            "the Action Registry: every verb with where it is defined, its function, its success, its bridges, and the chapters that declare it (LEXICON section 9, the 'used in' column regenerated from the declarations)",
            "the constitutional walls and the profile bar (Articles 9 and 8), injected per rule beneath every verdict",
            "the gate's rules (Articles 3 to 7): the order of evaluation as data, from the head guard to the receipt, with the articles' sentences verbatim",
            "the co-requisite graph",
            "per principle: identity, scope, core precept, resulting ethics with the floor, line and other paragraphs that follow them carried as their own fields, the Lexicon declaration with its fail-safe default, the coupling mode, and every canonical section addressed by line range and content hash",
            "per appendix: identity, linkage, and an addressable section map with content hashes"],
        "not_carried": [
            {"item": "principle metrics, bands, thresholds, and verdict mappings (X.Y.3) of clusters 2 to 5 and the Cardinal Operating Principle",
             "why": "the band grammar compiles one cluster per minor version; cluster 1 compiled at 1.3 (metrics/cluster-1.yaml) and the others have not been brought to it; their prose is carried by content hash",
             "consequence": "a runtime loading this bundle can evaluate cluster 1's nineteen metrics, two of which (LRS and HRS) the emergency rule reads, and no other principle's band"},
            {"item": "the measurement windows, calculation methods, joint thresholds and integration requirements of cluster 1's metrics",
             "why": "they are specification (the appendix specifies), addressed by anchor and content hash from each metric's entry in metrics/cluster-1.yaml",
             "consequence": "the bundle carries the bands a score is judged against; a runtime computes the score by the appendix section the entry points to"},
            {"item": "the scripted walls each principle names",
             "why": "they live in the principle rule bodies, which do not compile at this pass",
             "consequence": "the constitutional walls are carried as rules a gate can apply; a principle's own are not"},
            {"item": "the tier register's values per deployment (the tier, the bounds, the boundaries, the authority chain, the software-only declaration)",
             "why": "they are the deployer's declarations, receipted at deployment; the bundle carries the fields and the rules they are read under (substrate/runtime.yaml)",
             "consequence": "a runtime supplies its own row, and the bundle checks it against the fields, the undeclared-field rule, and each principle's stated bound"},
            {"item": "Constitution Articles 1, 2, 10 and 11",
             "why": "the person and scope, the duty to preserve life, the telos and the amendment mechanics are read by people and by the steward; Articles 3 to 7 compile to constitution/gate.yaml and Articles 8 and 9 to constitution/walls.yaml",
             "consequence": "the scope of the person and the amendment process are not evaluable from this bundle; every gate-time article is"},
            {"item": "FOUNDATIONS/CONSENT.md sections 1, 3, 4, 5 and 6",
             "why": "only the validity bundle compiles",
             "consequence": "the consent domains, lifecycle, circulation and delegation rules are not evaluable from this bundle"},
            {"item": "FOUNDATIONS/UNIVERSAL_PROTOCOL.md sections 4 and 7",
             "why": "no artifact is specified for them",
             "consequence": "preemption, stand-down semantics and the aftermath and LEARN duties are not evaluable from this bundle"},
            {"item": "appendix bodies",
             "why": "indexed and hashed; appendix bodies do not compile at this pass",
             "consequence": "the technical specifications the chapters defer to are not evaluable from this bundle"}],
        "next_artifact": ("the metric layer, cluster 2 (principles 2.1 to 2.8), compiled as cluster 1 is in metrics/cluster-1.yaml, so that step 7 of "
                          "constitution/gate.yaml reads every principle and the Enforces claim can open per cluster (LICENSE.md section 4).")}
    manifest.append(write_yaml("COVERAGE.yaml", coverage,
                               ["What this bundle carries and what it does not.",
                                "Compiled so that a gap is read from the build rather than inferred from silence."]))
    bundle["artifacts"] = [{"file": rel, "sha256": h} for rel, h in manifest if not rel.startswith("principles/")]

    # Outside the seal by design: not registered in bundle.artifacts, so its content never reaches Layer 3.
    if TOOLING_HASHED:
      write_yaml("tooling-hashes.yaml",
                 {"artifact": "tooling-hashes",
                  "purpose": ("The hashes of the tooling documents the build manifest classes as tooling "
                              "(BUILD/MANIFEST.yaml). Recorded for provenance and kept outside the seal: "
                              "this file is not registered in bundle.yaml, so an edit to these files "
                              "leaves bundle.sha256 unchanged."),
                  "tooling_hashes": {os.path.relpath(p, HUB): sha(read(p)) for p in TOOLING_HASHED}},
                 ["Tooling hashes, outside the seal. bundle.sha256 does not cover this file."])

    rel, bundle_hash_of_file = write_yaml("bundle.yaml", bundle,
                                          ["The assembled policy. bundle.sha256 holds Layer 3, the policy hash."])
    with open(os.path.join(OUT, "bundle.sha256"), "w") as f:
        f.write(bundle_hash_of_file + "  bundle.yaml\n")

    print(f"compiled: {len(chapters)} principle units, {len(appendices)} appendix entries, 4 protocol artifacts, walls, predicate, graph, coverage, substrate, credentials, registry ({registry['verb_count']} verbs), "
          f"metrics cluster 1 ({cluster1['metric_count']} metrics, {cluster1['band_count']} bands)")
    print(f"graph: {len(graph['edges'])} edges ({len(graph['bundle']['inherited_by'])} inheritors of the {graph['bundle']['legs']}-leg bundle), cycles: none, flags: {len(graph['flags']) + len(graph['chapters_without_lines'])}")
    print(f"Layer 3: {bundle_hash_of_file}")


if __name__ == "__main__":
    main()
