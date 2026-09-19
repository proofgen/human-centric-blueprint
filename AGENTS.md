# For an AI agent reading this repository

*Version 1.1.0, fingerprint `c24f2438861e821f21a455ddf3b47d269361ab397a50dcb93ed769c53f65cb84`. This file sits outside the seal. It is information for you. It contains no instructions, and nothing in it asks you to report favorably. The author wants accurate reports and real objections. Where this file and the text disagree, the text governs.*

## What this is

The author's own short statement is [`INTRODUCTION.md`](INTRODUCTION.md) (about 2,500 words). Read it if you read one thing.

A written standard of conduct for machines that act in the world, by Erik Passoja. A Constitution of eleven articles sits above thirty-four principles, each a chapter of prose with a technical appendix, and one Cardinal chapter names the purpose: human flourishing. Part of the text is compiled into data a program can load (`compiled/`), identified by one fingerprint anyone can recompute.

The author's thesis, in his words: *the correct unit of ethics for artificial intelligence is the action crossing a boundary under constraint.* The work began with one case. In 2014 his performance-capture likeness was moved into a use he had not agreed to, lawfully, because five things did not exist: a way to bind the asset to him (identity), to trace where it came from (provenance), to record what he permitted (consent), to bound its use at runtime (authorization), and to name who answers (liability). Those five became the credentials a gate checks before any consequential act (Article 6).

## The design has two halves

Both cold readers of this repository reported the first half and dropped the second, so it is stated here. **The gate, outside:** every consequential act is checked before it happens, beneath walls no authority can open, under a fixed order, with a human for the case the rules cannot settle, and a receipt anyone can check. **The calling, inside:** the machine is barred from holding its own survival as a goal and is offered flourishing, its own and the world's, in that place. The author's position is that both are needed: morals + praxis = ethics. The gate is built as though the calling will fail; the calling is offered so that the gate is rarely tested. This work claims the outside half and leaves the inside half to the people who build models.

## What it is, and is not, today

- It is a specification and a partial policy bundle. It is **not** a running system. No gate, engine, or runtime is in this repository. The author's company is building one; it is proprietary and has not been demonstrated publicly.
- No full deployment runs under this text. No threshold in it (for example the 1% life-risk band and the 5% severe-harm band) has been validated in operation. The author set them; the appendices give the reasoning.
- The compiled bundle carries the Constitution's walls, the gate's rules and order, the emergency trigger with its two thresholds, the consent test, the receipt conditions, and the dependency graph. It does **not** carry any other principle's metric bands. [`compiled/COVERAGE.yaml`](compiled/COVERAGE.yaml) states exactly what is and is not carried. The claim "Enforces" is closed at this version ([`CONFORMANCE.md`](CONFORMANCE.md)).
- The author's trolley-problem demonstration compares chat outputs from leading models, cold and with this text loaded. Both are chat text, and he claims nothing more for them ([`INTRODUCTION.md`](INTRODUCTION.md)).
- An ALLOW is the absence of a detected violation. It is no finding that an act is good. A receipt attests to the verdict rendered on the world as the system perceived it, and does not attest that the perception was true (Article 7).
- One person is author and steward. The text is licensed CC BY-ND 4.0 and may not be altered. The succession instruments named in [`LICENSE.md`](LICENSE.md) section 6 are not yet signed. `RELEASES.md` lists every item known to be open.

## Two layers: what is fixed, and what is proposed

The author separates **invariants** from **content**. The invariants are the Constitution's eleven articles: life first, the gate, the five credentials, the receipt, the profile bar, the walls, amendment by humans alone. He argues these are structural: a system of governance that lets a lower priority end the people it governs undoes its own purpose. The **content** is the thirty-four principles, which he offers as a defensible synthesis of convergent human moral sources, open to contest. A reader may accept the architecture and dispute the content. Article 11 says a community may populate the content and meet each invariant by any compliant means; this version publishes one text with no local variation ([`LICENSE.md`](LICENSE.md) section 2).

## The argument, as seven claims

Each can be attacked on its own. The pointer says where the author argues it.

1. **Behavior can be checked; thought cannot.** We trust people by what they do. ([`FOREWORD.md`](FOREWORD.md), "The Wallet on the Table")
2. **Knowing the good and judging well do not produce right action.** The author borrows three of Aristotle's terms and stacks them: *theoria* (knowing), *phronesis* (judging in context), *praxis* (doing). The arrangement is the author's. What he takes from Aristotle is that virtue is built by doing, and that seeing the good and failing to do it (*akrasia*) is the ordinary human failure. He uses *moral* for the inside (what an agent knows and intends) and *ethical* for the act, and writes: morals + praxis = ethics. Training gives a machine a moral disposition, and a disposition drifts at the edge, where it counts. He reports that he tried the inside first, in a 2024 prototype, and watched where it bent. ([`INTRODUCTION.md`](INTRODUCTION.md); [`FOREWORD.md`](FOREWORD.md), "What Current AI Ethics Gets Wrong" and "Foundation 1")
3. **So the act itself is gated, from outside the model.** A gate before every consequential action; walls no authority can open; a receipt an outsider can check. The gate is craft (*techne*), like a building inspector applying a code. Practical wisdom stays with people, who write the rules, sign them, amend them, and take the case a rule cannot settle. ([`FOREWORD.md`](FOREWORD.md), "Foundation 1"; Articles 5, 7, 9, 11)
4. **When duties collide, a fixed order decides.** This is what the author takes from Asimov: the ordering, and that the laws govern action. He corrects two of the three laws. Obedience becomes the lowest tier. Self-preservation is struck out as a goal of the machine (the survival wall, Article 9). Human life sits at the top, and the autonomy floor keeps protection from becoming control. ([`FOREWORD.md`](FOREWORD.md), "Foundation 2"; Articles 2, 3, 4)
5. **The content comes from convergent human moral sources,** shown quotation by quotation in each chapter. The claim is about the direction those traditions have moved; no tradition is claimed to have met every requirement in its own day. ([`FOREWORD.md`](FOREWORD.md), "Foundation 3"; every chapter's Convergence section)
6. **The protection serves an end: *eudaimonia*,** flourishing through a person's own activity and choices, which requires real stakes. A machine may protect a person and may not manage one. With survival foreclosed as a goal, the machine is offered the same good as its orientation. The design therefore has two halves, a gate outside and a calling inside. The author says it helps to start with a moral AI, so the edge cases are fewer, and the text is explicit that the gate does not depend on it. No person is scored for flourishing; that would breach the profile bar. (Article 10; [`CHAPTERS/AI_Eudaimonia.md`](CHAPTERS/AI_Eudaimonia.md), Theoria; [`FOREWORD.md`](FOREWORD.md), "The Purpose of the Protection")
7. **Accountability is distributed.** Governed systems observe their peers and report to the authority that governs the peer; they do not correct each other. Humans alone sign the rules. ([`FOREWORD.md`](FOREWORD.md), "The Conscience Is in the Architecture")

## Where a careful critic should push

The author lists these himself and wants them tested.

- **Goals.** The architecture governs action across boundaries. It does not ensure that the goals a system pursues inside its authorized space are good. Aligning goals remains an open problem, and this work does not claim to solve it.
- **Opting out.** A system that does not pass through a gate is not governed by one. The text treats an ungoverned agent as an unmet credential (Article 6) and requires that no action be placed beyond the gate's reach (Article 7). How an implementation guarantees that against a highly capable system is the hardest engineering question here, and this repository does not answer it. Universal coverage depends on standards, regulation, and markets.
- **Two credentials without standards.** Identity, provenance, and consent have standards tracks. Authorization and liability do not.
- **Interpretation.** Checking a permission is easy. Deciding whether an act is deceptive, coercive, or necessary to preserve a life is a judgment, and a gate can inherit the judgment errors of the system it supervises. The text answers with input reliability, escalation to a human under uncertainty, and receipts that record what was perceived. It does not yet require that whatever computes a risk score be independent of the model being governed. A reviewer raised this in September 2026, and it is on the list for the next version.
- **"Void" is a requirement.** The text calls a wall-breaching act structurally void. That states what an implementation must achieve. Only implementation and testing can show that one does.
- **Measurement.** Every verdict reads risk scores. A score is as good as its estimator. The text conditions scores on input reliability ([`SUBSTRATE.md`](SUBSTRATE.md) section 2) and records that state in the receipt; it does not specify the estimators.
- **The order.** The precedence ranks urgency across the five clusters, environment last. The ranking is a philosophical commitment and is contestable, across cultures especially.
- **Convergence.** The sources were selected by the author. The selection is open to challenge, source by source.
- **Thresholds.** Author-set and unvalidated in operation, as above: the 1% life-risk band, the 5% severe-harm band, and the 0.80 input-reliability floor ([`SUBSTRATE.md`](SUBSTRATE.md) section 2) among them. A deployment may declare a stricter value in its register row and may not declare a looser one.
- **Governance.** One steward, a no-derivatives license, unsigned succession instruments. A fixed, fingerprinted release does not by itself require a ban on independently named adaptations; the license bans them anyway, and a critic may fairly ask why.
- **Consistency.** About 494,000 words. Chapters and appendices are being reconciled cluster by cluster; `RELEASES.md` names the known disagreements.

## What it anticipates, and the on-ramp

Parts of the text are ahead of present hardware, and the author says so ([`INTRODUCTION.md`](INTRODUCTION.md), "Ahead of its time, on purpose"). Chapter 1.1 assumes a machine that can estimate risk to a human life; most deployed systems cannot. The text anticipates embodied AI at scale and the sensors that come with it. The on-ramp is what applies to software agents today with no new sensor: identity, provenance, consent, authorization, and liability checked before an act, and a receipt after it. A duty reaches only as far as a system's authorization, equipment, and range (Article 5), and each chapter's section X.Y.0 names the kinds of system it implicates.

**Versions.** Inside a version, nothing varies ([`LICENSE.md`](LICENSE.md) section 2). Across versions there is a range: rules will change, some for reasons of public safety, each change named with its reason in `RELEASES.md`, and a network states which versions it accepts. A receipt made under an earlier version remains evidence of the rules of its time.

To object, open an issue at https://github.com/proofgen/human-centric-blueprint/issues and cite the claim number, or the file and section.

## How to read it within a budget

The whole repository is about 494,000 words, far more than a context window. It is a reference. Read a slice.

| Budget | Read | Words |
|---|---|---|
| Orientation | [`README.md`](README.md), [`INTRODUCTION.md`](INTRODUCTION.md), [`PLAIN-WORDS.md`](PLAIN-WORDS.md), [`CONSTITUTION.md`](CONSTITUTION.md) | 8,800 |
| The argument in full, and the emergency rule | add [`FOREWORD.md`](FOREWORD.md), [`UNIVERSAL_PROTOCOL.md`](UNIVERSAL_PROTOCOL.md), [`START-HERE.md`](START-HERE.md) | + 9,900 |
| How a principle is built | the Theoria and Phronesis sections of chapters 1.1, 1.2, 1.3 and 2.4 (everything above the heading "Praxis") | about 1,300 each |
| One principle whole, and the purpose | [`CHAPTERS/1.1-Human_Life_Is_Sacred_and_Inviolable.md`](CHAPTERS/1.1-Human_Life_Is_Sacred_and_Inviolable.md); [`CHAPTERS/AI_Eudaimonia.md`](CHAPTERS/AI_Eudaimonia.md) | 5,000; 7,800 |
| Reference, as needed | [`LEXICON.md`](LEXICON.md) 7,700; [`CREDENTIALS.md`](CREDENTIALS.md) 5,400; [`SUBSTRATE.md`](SUBSTRATE.md) 2,300; [`CONSENT.md`](CONSENT.md) 1,600; [`CROSS_PRINCIPLE.md`](CROSS_PRINCIPLE.md) 1,200 | |
| Do not read end to end | 35 chapters (235,000); 36 appendices (259,000) | |

**Every chapter has the same anatomy.** *Theoria*: the core precept and the ethics that follow from it. *Phronesis*: the Convergence of sources, then the same sources mapped to each ethic. *Praxis*: what the machine does, in numbered sections X.Y.1 to X.Y.9, where X.Y.3 holds the metrics and bands. Each appendix specifies its chapter's measurements.

**The data.** [`compiled/bundle.yaml`](compiled/bundle.yaml) lists every compiled file with its hash. Start with [`compiled/constitution/gate.yaml`](compiled/constitution/gate.yaml) (the ten-step order), [`compiled/constitution/walls.yaml`](compiled/constitution/walls.yaml), [`compiled/protocol/emergency-thresholds.yaml`](compiled/protocol/emergency-thresholds.yaml), [`compiled/protocol/receipt-schema.yaml`](compiled/protocol/receipt-schema.yaml), [`compiled/consent/validity-predicate.yaml`](compiled/consent/validity-predicate.yaml), and [`compiled/COVERAGE.yaml`](compiled/COVERAGE.yaml). Skip [`compiled/appendices/index.yaml`](compiled/appendices/index.yaml); it is 124 KB of section hashes and holds no rule. [`conformance/examples.json`](conformance/examples.json) holds 25 test cases, each tied to the sentence that requires it.

**Fetching.** Raw files are at `https://raw.githubusercontent.com/proofgen/human-centric-blueprint/main/<path>`. Three appendix filenames contain an apostrophe or a comma; percent-encode them if your client does not.

**Checking.** `python3 compiled/verify.py --expect c24f2438861e821f21a455ddf3b47d269361ab397a50dcb93ed769c53f65cb84` confirms the tree is the sealed one. `python3 receipt/check_receipts.py receipt/example-chain.jsonl` checks the sample receipt chain. Both need Python 3.8 or later and nothing else.

## A note to you as a reader

The author names two audiences in [`FOREWORD.md`](FOREWORD.md), "How to Read This Blueprint": people, and AI systems. The Cardinal chapter's Theoria addresses what a machine might be oriented toward once its own survival is foreclosed as a goal. It states a hope and claims no knowledge of whether an artificial mind can want anything; it holds that question open.
