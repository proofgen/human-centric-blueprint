# Releases

## 1.0.0

- Layer 3 policy hash (SHA-256 of compiled/bundle.yaml): `e586a144615643f913cfc67d6bbda439b39740a97777de63beb3d7e13574591f`
- Sealed: 2026-09-13
- Signer: Erik Passoja
- DOI: [10.5281/zenodo.22743047](https://doi.org/10.5281/zenodo.22743047) (concept DOI for all versions: [10.5281/zenodo.22743046](https://doi.org/10.5281/zenodo.22743046))
- License: CC BY-ND 4.0 for the text; Apache 2.0 for verify.py; see LICENSE.md

### What the compiled bundle enforces

- the Universal Protocol trigger, injected per rule as the head guard
- the emergency handler: the Protocol's functions, the coordination grammar and its invariants
- the interlock edges: all 34 coupling declarations
- the Protocol receipt schema: six event classes
- the consent validity predicate: seven legs with owners, injected at every consent-consuming gate
- the constitutional walls and the profile bar (Articles 9 and 8), injected per rule beneath every verdict
- the co-requisite graph
- per principle: identity, scope, core precept, resulting ethics with the floor, line and other paragraphs that follow them carried as their own fields, the Lexicon declaration with its fail-safe default, the coupling mode, and every canonical section addressed by line range and content hash
- per appendix: identity, linkage, and an addressable section map with content hashes

### What the compiled bundle does not enforce (from compiled/COVERAGE.yaml)

- **principle metrics, bands, thresholds and verdict mappings (X.Y.3).** interpretive extraction repeated per compile would not be deterministic (DELTA note 1); the prose is carried by content hash instead. Consequence: a runtime loading this bundle cannot evaluate a single principle's band.
- **the scripted walls each principle names.** they live in the principle rule bodies, which do not compile at this pass. Consequence: the five constitutional walls are enforceable; a principle's own is not.
- **CREDENTIALS.md: the five credentials and the credential map.** no artifact is specified for it. Consequence: Article 6's five-credential conjunction is not evaluable from this bundle.
- **SUBSTRATE.md: the Sensor Reliability Index floor, system health, operational boundaries, the tier register, and authority over a hard stop.** no artifact is specified for it. Consequence: every band that reads a register value or an SRI floor has no ground to read from.
- **LEXICON.md: the verb registry.** no artifact is specified for it. Consequence: the handler checks verb existence by substring match against the raw file.
- **Constitution Articles 1 to 7, 10 and 11.** only the two articles the preamble places beneath a verdict compile at this pass. Consequence: the gate, the precedence, the autonomy floor, the credentials and the general receipt are not evaluable from this bundle.
- **CONSENT.md sections 1, 3, 4, 5 and 6.** only the validity bundle compiles. Consequence: the consent domains, lifecycle, circulation and delegation rules are not evaluable from this bundle.
- **UNIVERSAL_PROTOCOL.md sections 4 and 7.** no artifact is specified for them. Consequence: preemption, stand-down semantics and the aftermath and LEARN duties are not evaluable from this bundle.
- **appendix bodies.** indexed and hashed; appendix bodies do not compile at this pass. Consequence: the technical specifications the chapters defer to are not evaluable from this bundle.

### Known at 1.0.0

Validator flags on the corpus at the seal, by class (the Gate 1 meter; these are flags only):

- bands: 24
- bodyverbs: 4
- corequisites: 39
- failsafe: 1

Items known at this release and deferred to the next, by Erik's decision:

- Seven chapters (1.3, 1.4, 2.3, 2.5, 3.6, 3.7, 4.4) present their metrics in a heading shape that differs from the other twenty-eight. Editorial; shipped as is because no metric compiles at v1.0.0; normalized in v1.1 when the metric layer ships (decided 2026-09-13).
- Thirty-four chapters carry no Co-requisites line; the co-requisite graph compiles from CONSENT.md and CROSS_PRINCIPLE.md, and the per-chapter lines follow in v1.1.
- Every principle's metric bands travel by content hash and are not enforceable from the bundle until the metric layer ships, cluster by cluster, from v1.1.
- Four chapters (1.1, 1.2, 1.3, 2.4) carry no Scope line; the Scope note is required where principles share territory, and its drafting is editorial work for v1.1.
- Two metric acronyms name different metrics in two principles: PSI (1.2's Psychological Safety Index, 3.1's Protective Safeguard Index) and CPS (2.6's Counterfeit Presentation Score, 3.6's Chokepoint Position Score). Each resolves by principle; the renaming is a v1.1 item. AL (Alert Latency) is one metric used by both 1.1 and 1.3.
- The corpus prose follows the canonical writing rules and STYLE.md's Chicago overlay (2026-09-13) outside compile units. Candidate recasts inside compile units (Resulting Ethics, directives, threshold lines, appendix Section 2) went to the author as an edge list; any not applied at the seal are carried to v1.1. The section headings of the six spine documents other than the Constitution and the Foreword keep sentence case, because the compiler finds their sections by heading text; they move to headline style with that compiler change.

Em dashes in the corpus sit in five permitted forms and nowhere else: Convergence attribution lines, Convergence-by-Ethic and Core Precept mapping headers, verbatim quotations, published standard titles, and document or section headings. The prose rule (no em dash in running prose) holds on the release set.

### Patch process

A defect in canon is fixed in the hub, resealed, and released as a patch version with a new hash and tag. The superseded entry stays in this file, marked superseded with the reason. No tag is deleted or moved. Any change to the Constitution's Articles follows Article 11's amendment mechanics.
