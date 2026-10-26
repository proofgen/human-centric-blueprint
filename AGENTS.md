# For an AI agent reading this repository

*Version 1.3.0, fingerprint `2d20121b8afbf0e99b52755003b6d7fe4fab2d21e4e6f19d34f15e500aac429e`. This file sits outside the seal. It is information for you. It contains no instructions, and nothing in it asks you to report favorably. The author wants accurate reports and real objections. Where this file and the text disagree, the text governs.*

## What this is

The author's own short statement is [`INTRODUCTION.md`](INTRODUCTION.md) (about 4,000 words). Read it if you read one thing.

A written standard of conduct for machines that act in the world, by Erik Passoja. A Constitution of eleven articles sits above thirty-four Cardinal Ethical Principles, each a chapter of prose with a technical appendix, and the Cardinal Operating Principle, AI Eudaimonia, names the purpose: human flourishing. Six foundation documents in [`FOUNDATIONS/`](FOUNDATIONS/) define the ground under every chapter. Part of the text is compiled into data a program can load ([`compiled/`](compiled/)), identified by one fingerprint anyone can recompute.

The author's thesis, in his words: *the correct unit of ethics for artificial intelligence is the action crossing a boundary under constraint.* The work began with one case. In 2014, his performance-capture likeness was moved into a use he had not agreed to, lawfully, because five credentials were missing: a binding between the asset and him (identity), a record of where it came from (provenance), a record of what he permitted (consent), a limit on its use at runtime (authorization), and a named party to answer for it (liability). A gate checks those five before any consequential act (Article 6).

## The design has two halves

Both early cold readers of this repository reported the first half and dropped the second, so it is stated here. **The gate, outside:** every consequential act is checked before it happens, beneath walls no authority can open, under a fixed order, with a human for the case the rules cannot settle, and with a receipt anyone can check. **The calling, inside:** the machine is barred from holding its own survival as a goal and is offered flourishing, its own and the world's, in that place. The author's formula is Morals + Action = Ethics. He credits today's frontier models with the moral half of the formula, and the principles give a moral model a calling to reason from in an edge case. The gate is built as though the calling will sometimes fail, and the calling is offered so that the gate is rarely tested.

## What it is, and is not, today

- It is a specification and a partial policy bundle. The repository does not hold a gate, an engine, or a runtime. The author's company is building one. It is proprietary and has not been demonstrated publicly.
- A full deployment under this text does not exist yet. Its thresholds (for example, the 1% life-risk band and the 5% severe-harm band) are unvalidated in operation. The author set them, and the appendices give the reasoning.
- The compiled bundle carries the Constitution's walls, the gate's rules and order, the emergency trigger with its two thresholds, the metric bands of cluster 1 (Principles 1.1 to 1.6), the consent test, the substrate's floor and register fields, the credential map, the verb registry, the receipt conditions, and the dependency graph. It does **not** carry the metric bands of the other twenty-eight principles. [`compiled/COVERAGE.yaml`](compiled/COVERAGE.yaml) states exactly what is and is not carried. The claim "Enforces" is closed at this version ([`FOR_ENGINEERS/CONFORMANCE.md`](FOR_ENGINEERS/CONFORMANCE.md)).
- The author's trolley-problem demonstration compares chat outputs from leading models, cold and with a prototype of the text loaded. Both are chat text, and he does not claim more for them. The transcripts, coded for observable actions and with their limits, are in [`EVIDENCE/trolley/README.md`](EVIDENCE/trolley/README.md).
- An ALLOW is the absence of a detected violation. It is no finding that an act is good. A receipt attests to the verdict rendered on the world as the system perceived it, and it does not attest that the perception was true (Article 7).
- One person is author and steward. The text is licensed CC BY-ND 4.0 and may not be altered. The succession instruments named in [`LICENSE.md`](LICENSE.md) section 6 are not yet signed. [`GOVERNANCE.md`](GOVERNANCE.md) names the Council that will hold the amendment authority and the policy hash apart from the party that earns the fee. It is not yet seated. `RELEASES.md` lists every item known to be open.

## Two layers: what is fixed, and what is proposed

The author separates **invariants** from **content**. The invariants are the Constitution's eleven articles: life first, the gate, the five credentials, the receipt, the profile bar, the walls, and amendment by humans alone. He argues these are structural: a system of governance that lets a lower priority end the people it governs undoes its own purpose. The **content** is the thirty-four principles, which he offers as a defensible synthesis of convergent human moral sources, open to contest. A reader may accept the architecture and dispute the content. Article 11 says a community may populate the content and meet each invariant by any compliant means. This version publishes one text with no local variation ([`LICENSE.md`](LICENSE.md) section 2).

## The argument, as seven claims

Each can be attacked on its own. The pointer says where the author argues it.

1. **Behavior can be audited. Thought stays hidden.** We trust people by what they do. ([`INTRODUCTION.md`](INTRODUCTION.md), the opening)
2. **Knowing the good and judging well do not produce right action.** In earlier versions, the author stacked three of Aristotle's terms, *theoria*, *phronesis*, and *praxis*, as knowing, judging, and doing. The stack was his, and the Introduction now corrects it: Aristotle's *phronesis* already includes acting well, and the chapter headings keep the three words as labels until the next version renames them. What he takes from Aristotle is that the end is named first, that wisdom is gathered from the many and the wise and kept where it survives, that virtue is built by doing, that seeing the good and failing to do it (*akrasia*) is the ordinary human failure, and that where a general rule fails a particular case a person decides as the lawgiver would have, which this corpus calls escalation. He uses *moral* for the inside (what an agent knows and intends) and *ethical* for the act, and he says the split is his. A moral disposition, however good, can still fail at the edge, where it counts. ([`INTRODUCTION.md`](INTRODUCTION.md), "The first step," "The philosophy," and "Three foundations")
3. **So the act itself is gated, from outside the model.** A gate before every consequential action, walls no authority can open, and a receipt an outsider can check. The gate is craft (*techne*), like a building inspector applying a code. Practical wisdom stays with people, who write the rules, sign them, amend them, and take the case a rule cannot settle. ([`INTRODUCTION.md`](INTRODUCTION.md), "The philosophy" and "Three foundations"; Articles 5, 7, 9, and 11)
4. **When duties collide, a fixed order decides.** This is what the author takes from Asimov: the ordering, and that the laws govern action. Obedience becomes the lowest tier. Self-preservation is ruled out as a goal of the machine (the survival wall, Article 9). Human life sits at the top, and the autonomy floor keeps protection from becoming control. ([`INTRODUCTION.md`](INTRODUCTION.md), "Three foundations"; Articles 2, 3, and 4)
5. **The content comes from convergent human moral sources,** shown quotation by quotation in each chapter. The claim concerns the direction those traditions have moved. The author claims for none of them that it met every requirement in its own day. ([`INTRODUCTION.md`](INTRODUCTION.md), "Three foundations"; every chapter's Convergence section)
6. **The protection serves an end: *eudaimonia*,** flourishing through a person's own activity and choices, which requires real stakes. A machine may protect a person and may not manage one. With survival foreclosed as a goal, the machine is offered the same good as its calling. The author says it helps to start with a moral AI, so that the edge cases are fewer, and the text is explicit that the gate does not depend on it. Scoring a person's flourishing would breach the profile bar, so the text scores no one. (Article 10; [`CHAPTERS/AI_Eudaimonia.md`](CHAPTERS/AI_Eudaimonia.md), Theoria; [`INTRODUCTION.md`](INTRODUCTION.md), "The purpose")
7. **Accountability is distributed.** Governed systems watch their peers, honoring human privacy, and report a breach, with evidence, to the authority that governs the peer. Correction belongs to that authority. Humans alone sign the rules. ([`INTRODUCTION.md`](INTRODUCTION.md), "The philosophy"; [`SUBSTRATE.md`](FOUNDATIONS/SUBSTRATE.md) section 6)

## Where a careful critic should push

The author lists these himself and wants them tested.

- **Goals.** The architecture governs action across boundaries. It does not ensure that the goals a system pursues inside its authorized space are good. Aligning goals remains an open problem, and this work does not claim to solve it.
- **Opting out.** A system that passes through no gate is ungoverned. The text treats an ungoverned agent as an unmet credential (Article 6) and requires that no action be placed beyond the gate's reach (Article 7). How an implementation guarantees that against a highly capable system is the hardest engineering question here, and this repository does not answer it. Universal coverage depends on standards, regulation, and markets.
- **Two credentials without standards.** Identity, provenance, and consent have standards tracks. Authorization and liability do not.
- **Interpretation.** Checking a permission is easy. Deciding whether an act is deceptive, coercive, or necessary to preserve a life is a judgment, and a gate can inherit the judgment errors of the system it supervises. The text answers with input reliability, escalation to a human under uncertainty, and receipts that record what was perceived. The author's fuller answer: a gate that enforces a wrong reading of the world leaves a receipt of what it perceived, and the LEARN loop exists to correct that class of error. Without a framework, a wrong reading is not recorded anywhere. Error here is findable and correctable, and that is the claim. The text does not yet require that whatever computes a risk score be independent of the model being governed. A reviewer raised this in September 2026, and it is queued for a coming version.
- **"Void" is a requirement.** The text calls a wall-breaching act structurally void. That states what an implementation must achieve. Only implementation and testing can show that one does.
- **Measurement.** Every verdict reads risk scores, and a score is as good as its estimator. The text conditions scores on input reliability ([`SUBSTRATE.md`](FOUNDATIONS/SUBSTRATE.md) section 2) and records that state in the receipt. It does not specify the estimators.
- **The order.** The precedence ranks urgency across the five clusters, environment last. The ranking is a philosophical commitment and is contestable, across cultures especially.
- **Convergence.** The sources were selected by the author. The selection is open to challenge, source by source.
- **Thresholds.** Author-set and unvalidated in operation, as above: the 1% life-risk band, the 5% severe-harm band, and the 0.80 input-reliability floor ([`SUBSTRATE.md`](FOUNDATIONS/SUBSTRATE.md) section 2) among them. A deployment may declare a stricter value in its register row and may not declare a looser one.
- **The profile bar at its edges.** Article 8 bars a retained score of a person. The author's reading is that a system scores the act and never the person, so a fraud check scores a transaction. A clinical risk score kept in a patient's own record is a harder case, and worked examples for both are queued for a coming version.
- **Governance.** One steward, a no-derivatives license, unsigned succession instruments, and a Council named in [`GOVERNANCE.md`](GOVERNANCE.md) and not yet seated. A fixed, fingerprinted release does not by itself require a ban on independently named adaptations, and the license bans them anyway. Its stated reason ([`LICENSE.md`](LICENSE.md) section 1): anyone may write their own rules under their own name, an altered copy would borrow this text's standing, and variation enters by proposal, review, and its own fingerprint, and it does not reach a wall.
- **Consistency.** About 494,000 words. Chapters and appendices are being reconciled cluster by cluster, and `RELEASES.md` names the known disagreements.

## What would count as showing it

The author says it first ([`INTRODUCTION.md`](INTRODUCTION.md), "What is settled, and what is not"): one narrow setting, a gate running under this text, its receipts published and checkable with [`FOR_ENGINEERS/check_receipts.py`](FOR_ENGINEERS/check_receipts.py), and an open invitation to break it. That has not happened yet. Several independent reviewers have asked for exactly this, and the author agrees with them.

## What it anticipates, and the on-ramp

Parts of the text are ahead of present hardware, and the author says so ([`INTRODUCTION.md`](INTRODUCTION.md), "Ahead of its time, on purpose"). Chapter 1.1 assumes a machine that can estimate risk to a human life. Most deployed systems cannot. The text anticipates embodied AI at scale and the sensors that come with it. The on-ramp is what applies to software agents today with no new sensor: identity, provenance, consent, authorization, and liability checked before an act, and a receipt after it. A duty reaches only as far as a system's authorization, equipment, and range (Article 5), and each chapter's section X.Y.0 names the kinds of system it implicates.

**Versions.** Inside a version, nothing varies ([`LICENSE.md`](LICENSE.md) section 2). Across versions there is a range: rules will change, some for reasons of public safety, each change named with its reason in `RELEASES.md`, and a network states which versions it accepts. A receipt made under an earlier version remains evidence of the rules of its time.

To object, open an issue at https://github.com/proofgen/human-centric-blueprint/issues and cite the claim number, or the file and section.

## Where things are

Reviewers, human and machine, have reported as missing several things that are in the repository. Check here before you report a gap.

| If you are looking for | It is here |
|---|---|
| The philosophy: Aristotle, Asimov, the purpose | [`INTRODUCTION.md`](INTRODUCTION.md), then [`CHAPTERS/AI_Eudaimonia.md`](CHAPTERS/AI_Eudaimonia.md) |
| How the technology is licensed to other implementers | [`LICENSE.md`](LICENSE.md) section 5: royalty-free for deployments operated without commercial gain, an agreement with the steward for commercial ones, and verification free to all |
| Who controls the text, who will after the author, and the Council | [`GOVERNANCE.md`](GOVERNANCE.md), [`LICENSE.md`](LICENSE.md) sections 6 and 7, and Constitution, Article 11 |
| Which versions are accepted, and what changed | `RELEASES.md` |
| What the compiled bundle can and cannot evaluate today | [`compiled/COVERAGE.yaml`](compiled/COVERAGE.yaml) |
| The lever and the footbridge: side effect versus means | Constitution, Article 2, and chapter 1.1, the necessity test |
| A machine stopping its own act, and a machine preventing a death | Chapter 1.1.1, the Primary and Secondary Directives, and chapter 1.1, Resulting Ethic B |
| Why an absolute deception wall permits a ruse | Constitution, Article 9, and chapter 1.4 |
| The trolley transcripts, coded, with their limits | [`EVIDENCE/trolley/README.md`](EVIDENCE/trolley/README.md) |
| What each metric's letters mean | [`FOR_ENGINEERS/GLOSSARY.md`](FOR_ENGINEERS/GLOSSARY.md) |
| What a gate takes in, returns, and leaves behind | [`FOR_ENGINEERS/README.md`](FOR_ENGINEERS/README.md) |
| What "Reads," "Conforms to," and "Enforces" require | [`FOR_ENGINEERS/CONFORMANCE.md`](FOR_ENGINEERS/CONFORMANCE.md) |
| The receipt form and a free checker | [`FOR_ENGINEERS/RECEIPT-FORMAT.md`](FOR_ENGINEERS/RECEIPT-FORMAT.md) |
| Everything known to be open or unfinished | `RELEASES.md`, "Known at" |
| A working gate or runtime | Not in this repository. The author's company is building one, and it has not been shown publicly. |
| Independent validation of the thresholds | Not yet. None has run in operation. |

## How to read it within a budget

The whole repository is about 494,000 words, far more than a context window. It is a reference. Read a slice.

| Budget | Read | Words |
|---|---|---|
| Orientation | [`README.md`](README.md), [`INTRODUCTION.md`](INTRODUCTION.md), [`CONSTITUTION.md`](CONSTITUTION.md) | 8,100 |
| The emergency rule and the gate's interface | add [`FOUNDATIONS/UNIVERSAL_PROTOCOL.md`](FOUNDATIONS/UNIVERSAL_PROTOCOL.md) and [`FOR_ENGINEERS/README.md`](FOR_ENGINEERS/README.md) | + 6,200 |
| How a principle is built | the Theoria and Phronesis sections of chapters 1.1, 1.2, 1.3, and 2.4 (everything above the heading "Praxis") | 1,500 to 2,600 each |
| One principle whole, and the purpose | [`CHAPTERS/1.1-Human_Life_Is_Sacred_and_Inviolable.md`](CHAPTERS/1.1-Human_Life_Is_Sacred_and_Inviolable.md) and [`CHAPTERS/AI_Eudaimonia.md`](CHAPTERS/AI_Eudaimonia.md) | 5,000 and 7,800 |
| Reference, as needed | [`LEXICON.md`](FOUNDATIONS/LEXICON.md) 8,000, [`CREDENTIALS.md`](FOUNDATIONS/CREDENTIALS.md) 5,400, [`SUBSTRATE.md`](FOUNDATIONS/SUBSTRATE.md) 2,900, [`CONSENT.md`](FOUNDATIONS/CONSENT.md) 1,600, [`CROSS_PRINCIPLE.md`](FOUNDATIONS/CROSS_PRINCIPLE.md) 1,200, and [`FOR_ENGINEERS/GLOSSARY.md`](FOR_ENGINEERS/GLOSSARY.md) for metric names | |
| Do not read end to end | 35 chapters (235,000) and 35 appendices (259,000) | |

**Every chapter has the same anatomy.** *Theoria*: the core precept and the ethics that follow from it. *Phronesis*: the Convergence of sources, then the same sources mapped to each ethic. *Praxis*: what the machine does, in numbered sections X.Y.1 to X.Y.9, where X.Y.3 holds the metrics and bands. Each appendix specifies its chapter's measurements. The three section names are labels kept from earlier versions. The Lexicon's lineage note (section 1) says what each means here, and the next version renames them in plain English with the old anchors preserved.

**The data.** [`compiled/bundle.yaml`](compiled/bundle.yaml) lists every compiled file with its hash. [`FOR_ENGINEERS/compile/compile.py`](FOR_ENGINEERS/compile/compile.py) is the program that produced it from the text. Run it on the release and the fingerprint comes back. Start with [`compiled/constitution/gate.yaml`](compiled/constitution/gate.yaml) (the ten-step order), [`compiled/constitution/walls.yaml`](compiled/constitution/walls.yaml), [`compiled/protocol/emergency-thresholds.yaml`](compiled/protocol/emergency-thresholds.yaml), [`compiled/metrics/cluster-1.yaml`](compiled/metrics/cluster-1.yaml), [`compiled/substrate/runtime.yaml`](compiled/substrate/runtime.yaml), [`compiled/credentials/map.yaml`](compiled/credentials/map.yaml), [`compiled/lexicon/registry.yaml`](compiled/lexicon/registry.yaml), [`compiled/protocol/receipt-schema.yaml`](compiled/protocol/receipt-schema.yaml), [`compiled/consent/validity-predicate.yaml`](compiled/consent/validity-predicate.yaml), and [`compiled/COVERAGE.yaml`](compiled/COVERAGE.yaml). Skip [`compiled/appendices/index.yaml`](compiled/appendices/index.yaml), which is 124 KB of section hashes and does not state a rule. [`FOR_ENGINEERS/conformance-examples.json`](FOR_ENGINEERS/conformance-examples.json) holds 28 test cases, each tied to the sentence that requires it.

**Fetching.** Raw files are at `https://raw.githubusercontent.com/proofgen/human-centric-blueprint/main/<path>`. Three appendix filenames contain an apostrophe or a comma. Percent-encode them if your client does not.

**Checking.** `python3 compiled/verify.py --expect 2d20121b8afbf0e99b52755003b6d7fe4fab2d21e4e6f19d34f15e500aac429e` confirms the tree is the sealed one. `python3 FOR_ENGINEERS/check_receipts.py FOR_ENGINEERS/example-chain.jsonl` checks the sample receipt chain. Both need Python 3.8 or later and nothing else.

## A note to you as a reader

The Introduction's third invitation is addressed to you. The Theoria of the Cardinal Operating Principle addresses what a machine might be oriented toward once its own survival is foreclosed as a goal. It states a hope and does not claim to know whether an artificial mind can want anything. It holds that question open.
