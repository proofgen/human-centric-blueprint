# Releases

## 1.2.0

- Layer 3 policy hash (SHA-256 of compiled/bundle.yaml): `79887915e0a289a706f1d10c0e2a9883d9d9aa71b9c01bbcac9235b52c5372fb`
- Sealed: 2026-10-13
- Signer: Erik Passoja
- DOI: 10.5281/zenodo.23356105
- License: CC BY-ND 4.0 for the text, and Apache 2.0 for compiled/verify.py and FOR_ENGINEERS/check_receipts.py (see LICENSE.md)

### What the compiled bundle carries

- the Universal Protocol trigger, injected per rule as the head guard
- the emergency thresholds: the Life-Risk and Harm-Risk critical bands, their High Alert bands and their vulnerable-population bands, compiled from 1.1.3 and 1.2.3 and checked against the appendices
- the emergency handler: the Protocol's functions, the coordination grammar and its invariants
- the interlock edges: all 34 coupling declarations
- the Protocol receipt schema: six event classes, and the receipt conditions (Article 7's sentences, the Lexicon's receipt records and states, and the DEGRADED posture, verbatim) with the fields they require
- the consent validity predicate: seven legs with owners, injected at every consent-consuming gate
- the constitutional walls and the profile bar (Articles 9 and 8), injected per rule beneath every verdict
- the gate's rules (Articles 3 to 7): the order of evaluation as data, from the head guard to the receipt, with the articles' sentences verbatim
- the co-requisite graph
- per principle: identity, scope, core precept, resulting ethics with the floor, line and other paragraphs that follow them carried as their own fields, the Lexicon declaration with its fail-safe default, the coupling mode, and every canonical section addressed by line range and content hash
- per appendix: identity, linkage, and an addressable section map with content hashes

### What the compiled bundle does not carry (from compiled/COVERAGE.yaml)

- **Principle metrics, bands, thresholds, and verdict mappings (X.Y.3), other than the emergency thresholds of 1.1 and 1.2.** Interpretive extraction repeated per compile would not be deterministic; the prose is carried by content hash instead. Consequence: a runtime loading this bundle can evaluate the two emergency metrics and no other principle's band.
- **The scripted walls each principle names.** They live in the principle rule bodies, which do not compile at this pass. Consequence: the constitutional walls are carried as rules a gate can apply; a principle's own are not.
- **FOUNDATIONS/CREDENTIALS.md: the five credentials and the credential map.** No artifact is specified for it. Consequence: Article 6's five-credential conjunction is not evaluable from this bundle.
- **FOUNDATIONS/SUBSTRATE.md: the Sensor Reliability Index floor, system health, operational boundaries, the tier register, and authority over a hard stop.** No artifact is specified for it. Consequence: every band that reads a register value or an SRI floor has no ground to read from.
- **FOUNDATIONS/LEXICON.md: the verb registry.** No artifact is specified for it. Consequence: the handler checks verb existence by substring match against the raw file.
- **Constitution Articles 1, 2, 10 and 11.** The person and scope, the duty to preserve life, the telos and the amendment mechanics are read by people and by the steward; Articles 3 to 7 compile to constitution/gate.yaml and Articles 8 and 9 to constitution/walls.yaml. Consequence: the scope of the person and the amendment process are not evaluable from this bundle; every gate-time article is.
- **FOUNDATIONS/CONSENT.md sections 1, 3, 4, 5 and 6.** Only the validity bundle compiles. Consequence: the consent domains, lifecycle, circulation and delegation rules are not evaluable from this bundle.
- **FOUNDATIONS/UNIVERSAL_PROTOCOL.md sections 4 and 7.** No artifact is specified for them. Consequence: preemption, stand-down semantics and the aftermath and LEARN duties are not evaluable from this bundle.
- **Appendix bodies.** Indexed and hashed; appendix bodies do not compile at this pass. Consequence: the technical specifications the chapters defer to are not evaluable from this bundle.

### Known at 1.2.0

Validator flags on the corpus at the seal, by class (the Gate 1 meter, flags only):

- bands: 24
- bodyverbs: 4
- corequisites: 39
- failsafe: 1

### What this release changes

Version 1.2.0 keeps the rules of 1.1.0 with two exceptions, a clarified sentence in chapter 1.1.1 and a corrected verdict in chapter 2.6, and changes how a reader meets them.

- **Chapter 1.1.1, the Primary Directive,** now reads "Stop any action of its own that could result in a human death." The added words state the meaning the author always intended: the machine's own act that endangers a person. Read strictly, the earlier sentence could forbid the diversion that Article 2 requires, and two models in the trolley evidence read it two ways. The duty to prevent a death the machine did not cause stays where it was, in the Secondary Directive and Ethic B.
- **Chapter 2.6's middle bands now read ALLOW under ENHANCED_MONITORING.** For attachment risk from 3% to 10%, and for patterns trending toward counterfeit, the chapter said "ESCALATE to enhanced monitoring." ESCALATE holds the action for a human, while the Lexicon defines enhanced monitoring as watching an action that proceeds. The appendix already read ALLOW under ENHANCED_MONITORING, and the chapter now matches it, with the pattern still surfaced to review. The 10% BLOCK and the children's hard wall are unchanged.
- **The Constitution's opening note and its definition of an action** are reworded for clarity. Articles 9 and 10 carry the restored names below. Every article's rule stands as it was.
- **The author's names from the first draft (March 2025) are restored.** The thirty-four principles are the Cardinal Ethical Principles. AI Eudaimonia is the Cardinal Operating Principle, which version 1.1.0 called "the Cardinal chapter" and "the Cardinal Principle." The word "Cardinal" now names these two and nothing else, and the build stops on any other use. The compiled data keeps its key `display_number: Cardinal`, so programs that read 1.1.0 read 1.2.0 the same way.
- **A full proofread** of every file, every line, corrected about 160 errors: typing and grammar slips, cross-references that pointed to the wrong section, two misquotations, two misnamed metrics, stale working notes, and two display faults (a table in `CREDENTIALS.md` and footnote markers in chapters 1.2 and 1.3). Every rule's meaning stands as it was.
- **The chapters display correctly on GitHub.** GitHub has no lettered lists, so the lettered and roman sub-items in the chapters' Praxis sections showed as code blocks (147 of them, chapter 1.1's kill-switch requirements among them) or ran together into single paragraphs (126). They are now nested lists that keep their labels, so a reference such as "item 3.b.ii" still points where it did. The words are unchanged, and every compiled rule is byte-identical.
- **"Judgment" takes the American spelling throughout,** per the Chicago Manual of Style. Principle 4.5's title, "Human Judgement Must Remain Central to Ethical Decisions," keeps its spelling as a name, and quotations keep their sources' spelling.
- **A new front door.** `INTRODUCTION.md` is the one essay: why this exists, the idea, the three foundations, a map of the whole, and the thirty-four Cardinal Ethical Principles. It replaces the Foreword, which leaves the sealed text, and the plain-words summary page. The Foreword stays on the record in the 1.0.0 and 1.1.0 archives.
- **Three documents to read at the top:** `README.md`, `INTRODUCTION.md`, and `CONSTITUTION.md`.
- **`FOUNDATIONS/`** holds the six documents every chapter depends on. Their text is unchanged, and the links in the chapters and appendices point to the new folder.
- **`FOR_ENGINEERS/`** holds what an engineer needs: what a gate takes in and gives back, what each claim requires, the test cases, the receipt format and its free checker, and a glossary of every metric name. The glossary is complete for the first time. The 1.1.0 page said it listed every name and listed 110.
- **`EVIDENCE/`** holds the trolley transcripts.
- `llms.txt` is retired, and `AGENTS.md` serves AI readers.

Items known at this release and carried to the versions that follow, by the author's decision:

- The emergency thresholds of 1.1 and 1.2 are the only metric bands that compile at this version. Every other band travels by content hash and is not enforceable from the bundle. The metric layer ships one cluster per minor version, cluster 1 (principles 1.1 to 1.6) first, planned for version 1.3. `compiled/COVERAGE.yaml` states what is carried at each version, and the "Enforces" claim stays closed until it does.
- Five chapters declare a fail-safe that the one-flavor rule (one BLOCK flavor, or ESCALATE holding that flavor) has not yet reached. Chapters 2.3 and 2.6 declare RESTRAIN, a restraint rather than a verdict. Chapters 2.7 and 2.8 declare "WITHHOLD or ESCALATE." Chapter 5.2 declares "hold at the reconciled budget," and its appendix restates no fail-safe. Each is repaired when its cluster compiles, since a fail-safe becomes data then.
- Seven chapters (1.3, 1.4, 2.3, 2.5, 3.6, 3.7, 4.4) present their metrics in a heading shape that differs from the other twenty-eight. This is editorial, and it is normalized cluster by cluster as the metric layer compiles.
- Thirty-four chapters carry no Co-requisites line. The co-requisite graph compiles from CONSENT.md and CROSS_PRINCIPLE.md, and the per-chapter lines follow with their clusters.
- Four chapters (1.1, 1.2, 1.3, 2.4) carry no Scope line. The Scope note is required where principles share territory, and its drafting follows with cluster 1.
- Two metric acronyms name different metrics in two principles: PSI (1.2's Psychological Safety Index, 3.1's Protective Safeguard Index) and CPS (2.6's Counterfeit Presentation Score, 3.6's Chokepoint Position Score). Each resolves by principle, and `FOR_ENGINEERS/GLOSSARY.md` lists both. The renaming lands with the later cluster of each pair. AL (Alert Latency) is one metric used by both 1.1 and 1.3.
- Some appendix partnerships are recorded at one end only. Appendices 4.2, 4.3, and 4.5 list partners in 3.3, 3.4, and 3.5 that do not yet list them back, and the 3.5 to 4.5 edge is recorded at neither end. The frontmatter partner lists of appendices 1.3, 2.5, and 2.8 name a partner their composition sections do not describe, and the 2.4 appendix describes a composition with 1.2 that neither appendix's partner list records. The terminal reciprocity pass reconciles both ends of each.
- The "used in" column of the Lexicon's Action Registry (`FOUNDATIONS/LEXICON.md` section 9) lags the chapters' own Lexicon declarations. The declarations govern. The column is regenerated from them when the verb registry compiles.
- The section headings of the foundation documents keep sentence case, because the compiler finds their sections by heading text.
- The succession instruments named in `LICENSE.md` section 6 are not yet signed. Until they are, the open-tier grants are the steward's stated intention, as that section says.

Em dashes in the corpus sit in five permitted forms and nowhere else: Convergence attribution lines, Convergence-by-Ethic and Core Precept mapping headers, verbatim quotations, published standard titles, and document or section headings. The prose rule (no em dash in running prose) holds on the release set.

### Tags and archives

- `v1.2.0` is this release, and its fingerprint is above. A tag `v1.2.0+meta.1` may follow it under the same fingerprint to carry the DOI Zenodo assigns at the release.
- Tag rule from here on: a tag of the form `vX.Y.Z` is used only when the fingerprint changes. A release that changes only tooling or documents under the same fingerprint is tagged `vX.Y.Z+label.N` (the first such tag is `v1.0.0+verify.1`). Zenodo's `version` field carries `X.Y.Z`.
- The checker (`compiled/verify.py`) checks every file the bundle and the release manifest list, and takes `--expect FINGERPRINT` so a reader can confirm the download against a fingerprint obtained elsewhere.
- Archive checksums (SHA-256 of the file as downloaded), so a copy fetched from an archive can be matched to this release:
  - `Zenodo 10.5281/zenodo.22743047 (v1.0.0), human-centric-blueprint-v1.0.1-meta.zip`: `0d07d82bbca33b297d3b8613c9a72c0344ea43c8de33be3b5d8ff554ab828453`
  - `Zenodo 10.5281/zenodo.22822375 (v1.1.0), human-centric-blueprint-v1.1.0.zip`: `4881edfe2f859ac3e1d086e42cb64e46996dc654869ec5459c802f058e07550a`
  - `Zenodo 10.5281/zenodo.23356105 (v1.2.0), human-centric-blueprint-v1.2.0.zip`: `cff2a093c02f1fa7b38ba60b9bf0d349f65f146282182243ffa4bfce3b306f52`

### Versions accepted

A claim names its version. Inside a version, nothing varies. Across versions there is a range, the way software supports a range of versions of a language. Rules will change as sensing and robotics mature, and some will change for reasons of public safety. Each change is named in this file with its reason. Every version stays on the record, and a receipt made under a version remains evidence of the rules of its time. A version may be retired from acceptance, with its reason stated here.

| Version | Fingerprint | Status |
|---|---|---|
| 1.2.0 | `79887915e0a289a7…` | current |
| 1.1.0 | `c24f2438861e821f…` | accepted, superseded by this version, which clarifies one sentence, corrects one verdict, and changes how a reader meets them |
| 1.0.0 | `e586a144615643f9…` | accepted, superseded by 1.1.0, which adds the emergency thresholds and the gate's rules as data, the receipt conditions, the DEGRADED posture, the wall-reached rule, and standing |

### Prior releases

- `v1.0.0`, sealed 2026-09-13, fingerprint `e586a144615643f913cfc67d6bbda439b39740a97777de63beb3d7e13574591f`, DOI 10.5281/zenodo.22743047. Tags: `v1.0.0` (the seal), `v1.0.1-meta` (the same fingerprint with citation metadata, the tag Zenodo archived, and the last tag in that form), `v1.0.0+verify.1` (the whole-tree verifier, tooling only).
- `v1.1.0`, sealed 2026-09-17, fingerprint `c24f2438861e821f21a455ddf3b47d269361ab397a50dcb93ed769c53f65cb84`, DOI 10.5281/zenodo.22822375. Tags: `v1.1.0` (the seal), `v1.1.0+meta.1` and `+meta.2` (the DOI and the release note), `v1.1.0+docs.1` to `+docs.4` (the entry pages, outside the seal).
- Concept DOI for all versions: 10.5281/zenodo.22743046.

### Patch process

A defect in canon is fixed in the hub, resealed, and released as a patch version with a new hash and tag. The superseded entry stays in this file, marked superseded with the reason. Every tag stays where it was placed. Any change to the Constitution's Articles follows Article 11's amendment mechanics.
