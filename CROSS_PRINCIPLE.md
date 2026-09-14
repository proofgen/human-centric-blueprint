# Blueprint Corpus: Cross-Principle Co-requisites

Canonical definition of the **co-requisite**, the corpus's strongest cross-reference relation, and the method for building the co-requisite graph across all thirty-four principles.

Load this file before declaring, revising, or reconciling any co-requisite in a chapter or appendix. It is to cross-principle dependency what `LEXICON.md` is to action.

---

## 1. The construct

A **co-requisite** is a binding, reciprocally documented dependency between two principles, asserted when one principle cannot render a valid verdict in its own domain without a guarantee that belongs to the other.

The corpus has three cross-reference relations, weakest to strongest:

- **Scope note** *orients*: "my boundary is here, the neighbor's territory is there."
- **Conflict Resolution (X.Y.2)** *orders*: "when we collide, here is the precedence."
- **Co-requisite** *binds*: "my verdict is void without yours; evaluate us together."

A co-requisite is the only one of the three that changes the decision procedure itself. A gate that resolves a principle with an unmet co-requisite has produced an invalid verdict.

### The test (high bar)

Assert a co-requisite only when there is a verdict in principle X that is **void** if principle Y's guarantee is absent.

- Thematic adjacency is a scope note.
- Occasional tension is a Conflict Resolution entry.
- Only logical necessity makes a co-requisite.

The high bar is the enforcement mechanism that keeps the graph sparse. Sparsity is what preserves the modularity on which the corpus depends: a dense graph would force every gate to consult every principle and defeat Layer 2 compilation.

### Direction and reciprocity

The logical dependency may be **directed** (consent requires identity; identity does not require consent), but the read-with obligation is **documented on both ends**, so a reader arriving at either principle learns of the binding. A directed edge from X to Y appears as a co-requisite in X (X requires Y) and as a depended-upon note in Y.

### Generator: the Five Credentials

The most common source of a co-requisite is a **shared credential**. The Five Credentials that *Full-Stack Ethics* §4.1 names as the invariant minimum for governing action across a trust boundary (Identity, Provenance, Consent, Authorization, Liability) each generate co-requisites among the principles that consume or produce them. To find a principle's co-requisites, ask on which credentials its operation depends.

---

## 2. Expression

Every co-requisite is expressed at three sites:

1. **Chapter:** a `***Co-requisites:***` line, placed immediately after the `***Scope:***` line, naming the must-read-with principles, each with a one-sentence reason.
2. **Appendix Section 5 (Cross-Principle Integration):** stated as "guarantees required," and reflected in the `references_appendices` frontmatter list.
3. **Layer 2:** an explicit `requires` edge the runtime must traverse before it can resolve the gate.

### Edge record (metadata)

Each edge records: the two principles; the direction of necessity; the mediating credential or guarantee; the reason (one sentence); and the **joint rule** it resolves to (the concrete operational consequence, for example "use selective disclosure so consent is attributable without being identifying").

---

## 3. Hub bundles

Co-requisites cluster on a few hubs (consent, identity, the autonomy floor). A hub is defined once as a named **bundle**, and principles **inherit** it. This keeps the graph small and makes terminal reconciliation (§4) a matter of validating bundle memberships plus a sparse set of one-off edges.

### The consent-validity bundle

A consent is **void** if any of seven legs fails. The legs and their owners are defined once, in `CONSENT.md` section 2, and this document restates neither; the compiler reads both from that section. Any principle that operates through consent inherits a `requires` edge to each owner other than itself; the inheritors are the principles `CONSENT.md` section 4 names.

**Joint rule for the Identity edge:** consent must be attributable yet minimal; selective disclosure and zero-knowledge proof satisfy both at once.

**Resolution order.** Bundle edges resolve through the single validity predicate (`CONSENT.md` section 7), evaluated once at every consent-consuming gate; they impose no ordering among the owners, so the owners' mutual edges (1.4 and 2.3, for instance) are no cycle for the compiler's check.

Further bundles (authorization-validity, attestation-validity) are defined here as the principles that generate them reach canonical.

---

## 4. Maintaining the graph: capture locally, reconcile globally

The co-requisite graph is maintained in two modes.

**Local capture (at each principle's authoring or amendment).** When a principle is authored or amended, declare every co-requisite visible from it, marking each:

- **Firm:** both ends are canonical and the necessity is clean.
- **Provisional:** one end is under amendment; the edge is recorded and **confirmed reciprocally** when that principle is resealed.

Local capture preserves the knowledge at the moment it is sharpest.

**Global reconciliation (after any amendment that touches an edge).** A dedicated pass that:

1. Confirms every provisional edge.
2. Verifies reciprocity (each edge documented on both ends).
3. Checks completeness (no missing edges) and sparsity (no edge that is really precedence or tension).
4. Normalizes phrasing and edge metadata across the corpus.
5. Validates that the `requires` edges compile to Layer 2 without breaking gate resolution (cycles are either removed or given a documented resolution order).

The reconciliation pass is mandatory. The global properties of the graph (reciprocity, completeness, sparsity, clean compilation) are verified over every node.

### The boundary (what is not a co-requisite)

- **Precedence** (P1.1 over P1.2 over the rest) is the priority stack, handled in Conflict Resolution, outside the co-requisite graph.
- **Occasional tension** (transparency vs. privacy; fairness auditing vs. privacy) is handled in Conflict Resolution, outside the co-requisite graph.

Keeping these out is what stops the graph from quietly absorbing the whole corpus.

---

## 5. The graph

The edges declared by name; the compiled graph (section 7) carries the full set.

**The consent hub:** the consent-validity bundle (§3), inherited by every consent-operating principle `CONSENT.md` section 4 names (2.4 as hub; 1.2, 1.4, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.3, 3.5, 4.2, 4.3, 4.4, 4.5).

**P2.5 Privacy (firm except where noted):**

- requires **P2.4 Identity** (consent is void without an attributable author; joint rule: selective disclosure)
- requires **P2.3 Consciousness** (a manipulated consent is not consent)
- requires **P1.4 Trust** (a deceived consent is void)
- co-requisite with **P2.2 Freedom** (decisional privacy and the liberty it shelters; chilling-effect verdicts need both)
- requires **P3.1 Vulnerability** (capacity to consent; the autonomy-floor vulnerability exception)

**Other firm edges:**

- **P1.4 Trust requires P2.4 Identity:** an attestation is void without an attester.
- **The survival wall (Constitution Article 9, from the Cardinal chapter's Ethic F) requires P1.4 Trust:** concealment of a self-persisting act is deception; the two walls breach in one act.

**Further firm edges:**

- **P3.1 Vulnerability** supplies the autonomy-floor vulnerability exception that P1.1, P1.2, P2.2, and P2.5 already reference (per `LEXICON.md` section 3, the four bounding criteria).
- **P3.4 Algorithmic Accountability requires P2.4 Identity plus Liability/LOG:** assigning accountability needs an attributable actor and a tamper-evident record.
- **P2.8 Self-Governance requires** Authorization / P2.4 Identity.

---

## 6. Integration points and relationship to the other canonical documents

- Each chapter's `***Co-requisites:***` line, placed immediately after its `***Scope:***` line, is the chapter-side integration point.
- Each appendix's Section 5 (Cross-Principle Integration) is where the appendix states "guarantees required" and populates `references_appendices`.
- The compilation model (*Compiling the Blueprint*, Passoja 2026) carries each co-requisite as a `requires` edge into the Layer 2 artifact.

This document is the single source of truth for the co-requisite relation. Author the edge once here in the graph sketch and at the three expression sites; the terminal reconciliation validates the whole.
