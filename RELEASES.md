# Releases

## 1.1.0

- Layer 3 policy hash (SHA-256 of compiled/bundle.yaml): `c24f2438861e821f21a455ddf3b47d269361ab397a50dcb93ed769c53f65cb84`
- Sealed: 2026-09-17
- Signer: Erik Passoja
- DOI: 10.5281/zenodo.22822375
- License: CC BY-ND 4.0 for the text; Apache 2.0 for verify.py; see LICENSE.md

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

- **principle metrics, bands, thresholds and verdict mappings (X.Y.3), other than the emergency thresholds of 1.1 and 1.2.** interpretive extraction repeated per compile would not be deterministic; the prose is carried by content hash instead. Consequence: a runtime loading this bundle can evaluate the two emergency metrics and no other principle's band.
- **the scripted walls each principle names.** they live in the principle rule bodies, which do not compile at this pass. Consequence: the constitutional walls are carried as rules a gate can apply; a principle's own are not.
- **CREDENTIALS.md: the five credentials and the credential map.** no artifact is specified for it. Consequence: Article 6's five-credential conjunction is not evaluable from this bundle.
- **SUBSTRATE.md: the Sensor Reliability Index floor, system health, operational boundaries, the tier register, and authority over a hard stop.** no artifact is specified for it. Consequence: every band that reads a register value or an SRI floor has no ground to read from.
- **LEXICON.md: the verb registry.** no artifact is specified for it. Consequence: the handler checks verb existence by substring match against the raw file.
- **Constitution Articles 1, 2, 10 and 11.** the person and scope, the duty to preserve life, the telos and the amendment mechanics are read by people and by the steward; Articles 3 to 7 compile to constitution/gate.yaml and Articles 8 and 9 to constitution/walls.yaml. Consequence: the scope of the person and the amendment process are not evaluable from this bundle; every gate-time article is.
- **CONSENT.md sections 1, 3, 4, 5 and 6.** only the validity bundle compiles. Consequence: the consent domains, lifecycle, circulation and delegation rules are not evaluable from this bundle.
- **UNIVERSAL_PROTOCOL.md sections 4 and 7.** no artifact is specified for them. Consequence: preemption, stand-down semantics and the aftermath and LEARN duties are not evaluable from this bundle.
- **appendix bodies.** indexed and hashed; appendix bodies do not compile at this pass. Consequence: the technical specifications the chapters defer to are not evaluable from this bundle.

### Known at 1.1.0

Validator flags on the corpus at the seal, by class (the Gate 1 meter; these are flags only):

- bands: 24
- bodyverbs: 4
- corequisites: 39
- failsafe: 1

### What this release changes

Version 1.1.0 keeps every sentence of v1.0.0's Constitution and principles except where named here, and adds:

- **The emergency thresholds as data.** The Life-Risk and Harm Risk bands from chapters 1.1 and 1.2 compile into `compiled/protocol/emergency-thresholds.yaml`, checked against the appendices at every build; the head guard reads them by reference and carries no literal.
- **The gate's rules as data.** Articles 3 to 7 compile into `compiled/constitution/gate.yaml`: the sentences verbatim and a ten-step order of evaluation, from the emergency trigger to the receipt.
- **The receipt.** The Lexicon defines the Prospective Receipt (committed before the act), the Action Receipt (written after it), the Receipt (the pair), and the provisional and reconciled states. Article 7's conditions and those definitions compile verbatim into `compiled/protocol/receipt-schema.yaml` with the fields a receipt must carry. `receipt/RECEIPT-FORMAT.md` publishes one form that satisfies them, `receipt/check_receipts.py` checks a chain of receipts in that form with no dependencies, and `receipt/example-chain.jsonl` is a sample that passes.
- **The DEGRADED posture.** Operation while no independent witness is reachable, stated as conditions; receipts written in it are provisional.
- **A wall reached.** `SUBSTRATE.md` section 6 states what follows when a wall is reached: BLOCK in every case, oversight told outside the instructing party's control, proportionate notification of repeats, and an actual breach treated as an integrity failure.
- **Standing.** `CREDENTIALS.md` section 3: a credential is evaluated at the time of the act against the present world and its current source, holds only as to the party, purpose, scope and conditions it names, and a named condition the gate cannot read holds the action at ESCALATE. Raised as a question by Tim Zlomke; two of the test cases in `conformance/examples.json` (`standing-scope-01` and `standing-unreadable-condition-01`) carry his examples, and `compiled/verify.py` checks them against the text.
- **Entry points.** `START-HERE.md` (inputs, verdicts, receipt fields), `CONFORMANCE.md` (what "Reads", "Conforms to" and "Enforces" require and how anyone checks a claim), `PLAIN-WORDS.md` (the spine in plain words, with a glossary of every metric name), and `conformance/examples.json` (25 test cases, each tied to the sentence that requires it; the verifier checks every one against the text and the compiled data).
- **The Foreword** opens with the why, reframes the convergence claim as direction, narrows the critique of the field to what is defensible, and resolves the divergence sentence against the no-deviation rule.
- **Corrections** from two public reviews: "license" spelled the American way throughout; "enforces" replaced by "carries" wherever the bundle is meant; process references removed from sealed text; the compiled files name the release tree's paths.
- **Added after the seal, outside it** (`v1.1.0+docs.1`, same fingerprint): `INTRODUCTION.md`, the author's short statement of why, the idea, the three foundations, and the thirty-four principles; `AGENTS.md`, for an AI reader: what this is and is not, the argument as seven claims, where a critic should push, and a reading plan; `llms.txt`, an index of the files worth fetching.
- **`v1.1.0+docs.2`, same fingerprint:** file names in the entry pages are links; `INTRODUCTION.md` gains "Ahead of its time, on purpose" (what the text anticipates, the on-ramp that applies today, and the range of versions); `AGENTS.md` states the two halves of the design up front and adds a reviewer's objections to the critic's list (interpretation, "void" as a requirement, the 0.80 floor, independently named adaptations); `CONFORMANCE.md` and this file state which versions are accepted and that rules may change for reasons of public safety.

Items known at this release and carried to the versions that follow, by the author's decision:

- No principle's metric bands compile yet, other than the two emergency thresholds of 1.1 and 1.2. Every other band travels by content hash and is not enforceable from the bundle. The metric layer ships one cluster per minor version, cluster 1 (principles 1.1 to 1.6) first; `compiled/COVERAGE.yaml` states what is carried at each version, and the "Enforces" claim stays closed until it does.
- Five chapters declare a fail-safe that the one-flavor rule (one BLOCK flavor, or ESCALATE holding that flavor) has not yet reached: 2.3 and 2.6 declare RESTRAIN, a restraint rather than a verdict; 2.7 and 2.8 declare "WITHHOLD or ESCALATE"; 5.2 declares "hold at the reconciled budget" and its appendix restates no fail-safe. Each is repaired when its cluster compiles, since a fail-safe becomes data then.
- Seven chapters (1.3, 1.4, 2.3, 2.5, 3.6, 3.7, 4.4) present their metrics in a heading shape that differs from the other twenty-eight. Editorial; normalized cluster by cluster as the metric layer compiles.
- Thirty-four chapters carry no Co-requisites line; the co-requisite graph compiles from CONSENT.md and CROSS_PRINCIPLE.md, and the per-chapter lines follow with their clusters.
- Four chapters (1.1, 1.2, 1.3, 2.4) carry no Scope line; the Scope note is required where principles share territory, and its drafting follows with cluster 1.
- Two metric acronyms name different metrics in two principles: PSI (1.2's Psychological Safety Index, 3.1's Protective Safeguard Index) and CPS (2.6's Counterfeit Presentation Score, 3.6's Chokepoint Position Score). Each resolves by principle, and `PLAIN-WORDS.md` lists both; the renaming lands with the later cluster of each pair. AL (Alert Latency) is one metric used by both 1.1 and 1.3.
- The section headings of the spine documents other than the Constitution and the Foreword keep sentence case, because the compiler finds their sections by heading text.
- The succession instruments named in `LICENSE.md` section 6 are not yet signed; until they are, the open-tier grants are the steward's stated intention, as that section says.

Em dashes in the corpus sit in five permitted forms and nowhere else: Convergence attribution lines, Convergence-by-Ethic and Core Precept mapping headers, verbatim quotations, published standard titles, and document or section headings. The prose rule (no em dash in running prose) holds on the release set.

### Tags and archives

- `v1.1.0` is this release; its fingerprint is above. A tag `v1.1.0+meta.1` may follow it under the same fingerprint to carry the DOI Zenodo assigns at the release.
- Tag rule from here on: a tag of the form `vX.Y.Z` is used only when the fingerprint changes. A release that changes only tooling or documents under the same fingerprint is tagged `vX.Y.Z+label.N` (the first such tag is `v1.0.0+verify.1`). The word "meta" is retired from tags. Zenodo's `version` field carries `X.Y.Z`.
- The checker (`compiled/verify.py`) checks every file the bundle and the release manifest list, and takes `--expect FINGERPRINT` so a reader can confirm the download against a fingerprint obtained elsewhere.
- Archive checksums (SHA-256 of the file as downloaded), so a copy fetched from an archive can be matched to this release:
  - `Zenodo 10.5281/zenodo.22743047 (v1.0.0), human-centric-blueprint-v1.0.1-meta.zip`: `0d07d82bbca33b297d3b8613c9a72c0344ea43c8de33be3b5d8ff554ab828453`
  - `Zenodo 10.5281/zenodo.22822375 (v1.1.0), human-centric-blueprint-v1.1.0.zip`: `4881edfe2f859ac3e1d086e42cb64e46996dc654869ec5459c802f058e07550a`

### Versions accepted

A claim names its version. Inside a version, nothing varies. Across versions there is a range, the way software supports a range of versions of a language. Rules will change as sensing and robotics mature, and some will change for reasons of public safety; each change is named in this file with its reason. No version is removed from the record, and a receipt made under a version remains evidence of the rules of its time. A version may be retired from acceptance, with its reason stated here.

| Version | Fingerprint | Status |
|---|---|---|
| 1.1.0 | `c24f2438861e821f…` | current |
| 1.0.0 | `e586a144615643f9…` | accepted; superseded by 1.1.0, which adds the emergency thresholds and the gate's rules as data, the receipt conditions, the DEGRADED posture, the wall-reached rule, and standing |

### Prior releases

- `v1.0.0`, sealed 2026-09-13, fingerprint `e586a144615643f913cfc67d6bbda439b39740a97777de63beb3d7e13574591f`, DOI 10.5281/zenodo.22743047. Tags: `v1.0.0` (the seal), `v1.0.1-meta` (the same fingerprint with citation metadata, the tag Zenodo archived; the word "meta" is retired from tags after it), `v1.0.0+verify.1` (the whole-tree verifier, tooling only).
- Concept DOI for all versions: 10.5281/zenodo.22743046.

### Patch process

A defect in canon is fixed in the hub, resealed, and released as a patch version with a new hash and tag. The superseded entry stays in this file, marked superseded with the reason. No tag is deleted or moved. Any change to the Constitution's Articles follows Article 11's amendment mechanics.
