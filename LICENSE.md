# License

*A Human-Centric Blueprint for Safe AI Ethics*, by Erik Passoja. The version, the seal date, and the fingerprint (the Layer 3 policy hash) this file accompanies are stated in RELEASES.md and CITATION.cff beside it. The steward of the Blueprint is Erik Passoja, acting through Seventh Planet, Inc.

This file is the binding statement of the terms. It carries into the Blueprint the Stewardship and Licensing Principles first published in the author's papers (Passoja 2026, *Self-Sovereign Identity and Governed Action* and *The Action Receipt*), which said the binding terms would be published with the Blueprint. This is that publication. The papers remain the record of intent behind it.

## 1. The text

### Why there are no derivatives

The Blueprint works only if every governed machine runs the same text. A receipt that says, "This machine conforms to Human-Centric Blueprint [version] [fingerprint]" is worth something, because that sentence points to one exact text everywhere, identified by one fingerprint. The moment altered copies circulate under the same name, a receipt stops telling anyone what actually governed the machine, and trust fails. So the text is set, and it is set for the system integrity of the entire ethical network.

You will not need to change the text. A governed network admits an AI on the strength of the fingerprint it cites. A modified text carries a fingerprint no network recognizes.

At this version, there is no variation. You use the version as published, fingerprint for fingerprint, or your machines are out of network (section 2).

A fingerprint already tells one text from another, so a reader may fairly ask what the ban on derivatives adds. It guards standing. You may write your own rules under your own name, and nothing here prevents it. You may not alter these and keep their standing, because a near-copy with one wall removed would borrow a legitimacy it has not earned. Variation enters by the front door: proposed, reviewed by the Council once it is seated and by the steward until then (`GOVERNANCE.md`), given its own fingerprint, and listed in `RELEASES.md`. Every wall of Article 9 stays beyond the reach of variation.

### The grant

The whole text of the Blueprint (the Constitution, the six documents in FOUNDATIONS/, the chapters, and the appendices) is licensed under **Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)**.

You may copy and redistribute it, whole or in part, in any medium or format, for any purpose, including commercially, with attribution to the author and a reference to the version and fingerprint. You may quote it, teach it, and argue with it. You may not distribute a modified version.

**Translations.** This is an additional permission beyond CC BY-ND 4.0, granted by the steward. Anyone may translate any part of this work and share the translation, if it is marked as an unofficial translation, links to the English original and its fingerprint, and states that the English text governs. A translation reviewed by the steward becomes official and carries its own fingerprint.

## 2. No deviation at this version

There is no profile mechanism at this version. A deployment uses the text and the compiled bundle exactly as published, fingerprint for fingerprint, or it is out of network.

A deployment declares only what the text itself requires it to declare: its row in the tier register (SUBSTRATE.md, section 5), which names its tier or its software-only declaration, its escalation time bound and High Alert window, its operational boundaries, its software version and hardware lot, its authority chain, and the other fields that section lists. Where the text supplies a number, a declared value may be stricter than it and may not be looser. Where the text does not supply one, the field is the deployer's to declare and receipt. That row is a name plate for the deployment, and it does not change the ethics program.

Deployment by a military or law-enforcement body, whose work involves the use of force by humans, requires a written grant, and the tier register carries that grant as a required field. An AI may not apply lethal or violent force to a human being under any authority (Constitution, Article 9). The grant is the Council's to issue once it is seated (`GOVERNANCE.md` section 2), and until then nobody issues one, the steward included, so that a Blueprint-governed system runs for such a body only after more than one person has examined the deployment. The Constitution names the grant as the steward's, and the steward has bound himself not to issue it alone. None is issued at this version. The Blueprint was not written for military use. A military or law-enforcement body that wants to run a governed system comes to the steward, and later to the Council, and asks, and the answer may be no. A grant, if one is ever issued, reaches only work outside the use of force, such as carrying the injured to a hospital. The grant certifies one thing: that the deployment sits outside the kill chain. The Blueprint's name goes on no system that performs any function of that chain against a human being, in the six words the military itself uses, find, fix, track, target, engage, assess, and no interlock between a governed part and a weapon changes this. The test for whether a function is in the chain is whether a particular person or group is being sought. A truck that carries ammunition to a depot seeks no one and may be governed, and the same truck tasked to resupply a unit in a firefight is engage support and is not covered. A drone that maps terrain seeks no one and may be governed, and the same drone tasked to find a person is in the chain and is not covered. An abort circuit on a weapon platform seeks no one and is the safety the text already describes (Principle 1.1, 1.1.1 item 3), and a detector that hands a person to the shooter is in the chain. The grant is per deployment, and the register row carries the purpose for which it was issued.

A later version may admit profiles, under strict protocols, as additions to the stack of a published version, so that a deployment can state a lawful local variation without touching the text. Until that version is published, no deviation of any kind is recognized.

## 3. The compiled bundle and the code

**`compiled/verify.py`**, **`FOR_ENGINEERS/check_receipts.py`**, and **`FOR_ENGINEERS/compile/compile.py`** are licensed under the **Apache License 2.0**: use them, change them, and redistribute them, keeping the notice. The compiler is the text-to-data step and does not contain gate logic. It is published so that anyone can regenerate `compiled/` from the text and compare the result with the sealed bundle, and the release builder does exactly that before any release ships.

**The compiled bundle** (`compiled/`) is a derived form of the text and travels under the text's terms in section 1: copy it, load it, verify it, and do not alter it. An altered bundle has a different fingerprint and is out of network.

**The kit** (the runtime that loads the bundle and gates actions against it, and the profile format, if one is ever admitted) is software of the steward. Its license is section 5. Nothing in this section grants any right in it.

## 4. Using the name

The name is **Human-Centric Blueprint**, and it is the steward's. This section exists so that the name on a product tells the truth about what the product does. Three claims exist, and each requires what it names.

- *"Reads Human-Centric Blueprint [version] [fingerprint]."* We loaded this bundle, unaltered. Any deployment may say this.
- *"Conforms to Human-Centric Blueprint [version]."* We run a gate that evaluates every boundary-crossing action against this bundle, and our copy's fingerprint matches. Only a deployment that does this may say it.
- *"Enforces Human-Centric Blueprint [version]."* Every principle's metrics, bands, thresholds, and verdict mappings are compiled into the bundle and evaluated at runtime. A version carries that layer only where its `compiled/COVERAGE.yaml` says so, and the steward opens the claim cluster by cluster in `RELEASES.md`. This version compiles the layer for cluster 1 (Principles 1.1 to 1.6), and the claim is not yet opened for any cluster, so no deployment may make it.

*Why no product may yet say "Enforces."* A product can say three things about this text. "Reads" means the product loaded the data. "Conforms to" means the product checks every action against the rules and can prove it. "Enforces" means the rules' numbers are built into the product's own software, so the product allows or stops an action by those numbers, automatically, and anyone can check that it does. This is the first version where that is possible, because the first six chapters' numbers are now data a program can load. But no one has yet shown a product doing it where an outside reader could check. So the label stays off until someone does. A product that said "we enforce it" before anyone had seen it work would be making a promise without proof. When the author turns the label on, this section will say "Enforces (cluster 1)," name the product that showed it, and the release record will give the date.

The name is granted for no other use.

## 5. Running the machinery: the tiers

These terms concern the architecture claimed in the author's patent applications, and in any patents that issue from them, which a deployment practices when it loads the bundle and gates actions against it. They carry forward the Stewardship and Licensing Principles of the author's papers. They are the steward's present terms. The signed instruments that make them enforceable against any successor are named in section 6.

**Royalty-free tier.** Perpetual, royalty-free licensing for deployments not operated for commercial gain: non-commercial deployments, and deployments by not-for-profit institutions serving public-interest functions, child safety among them. If you are a person using your own AI, a parent protecting your child, a nonprofit, or a public hospital, it is free, and you do not need to ask. Eligibility turns on whether the deployment is operated for commercial gain by the operator, by any party controlling it, or by any party entitled to its output, and not on the mission it serves. Commercial gain includes indirect gain: advertising, data monetization, or using the deployment to drive purchases elsewhere. Recovery of operating costs is not commercial gain.

**Commercial tier.** We are early. If you plan to run this layer for profit, in an agent, a product, or a payment system, write to us before you deploy. There will be a fee. Whether it is a percentage, a flat charge, or a yearly sum is set in the agreement we sign, and the price will remain confidential. The agreement covers the price only. Nobody can pay for different rules, a different version of the text, permission to skip the receipts, or the removal of the free tier. Every agreement is listed in `RELEASES.md` by name. As more of you deploy, we intend to settle on one low fee and/or percentage for all. A for-profit company that deploys only because a regulation requires it is commercial all the same, and so is deployment by a national, state, provincial, or regional government body as a program of general application, whether or not operated for gain. Deployment by a public institution serving a public-interest function, including publicly funded hospitals, schools, libraries, and social services, is not.

**Favorable terms.** A discount, a waiver, or a pilot is part of the agreement, and none of them exempts a party from the seal, the receipt, or defensive termination. The commercial tier never asks less of a deployment than the royalty-free tier asks.

**Who holds the hash.** The fee flows to the operating company. The policy hash, the authority to amend under Article 11, and the patents are meant to rest with a body that does not earn on volume: the Council described in `GOVERNANCE.md`, and the nonprofit holding entity the steward is forming for the patents. Until that body is seated and the instruments of section 6 are signed, the separation is a stated commitment and not yet an instrument, and the steward is the sole signer.

**Standards bodies.** The receipt format (`FOR_ENGINEERS/RECEIPT-FORMAT.md`) and the vocabulary may be carried to a standards venue on royalty-free terms, as standards bodies require, while the runtime stays in the commercial tier. A submission is the steward's act, and `RELEASES.md` records it when it is made.

**The runtime scope.** The commercial scope is the runtime layer: any implementation that loads the compiled bundle and gates actions against it, issues capability grants, or emits receipts under it, by any means. In the patents' vocabulary the same layer is receipt conservation and custody accounting, commit-before-act witnessing, policy-version citation bound to the receipt, and person-exclusion enforcement, and the two descriptions name one scope. Everything outside that scope, the text and its vocabulary, is free to all users under section 1, and the text grant does not carry a license to the runtime. Where a party provides the runtime as a service to others, the tier is determined for each party served. The provisional applications the Lexicon cites are pending and unpublished, and the non-provisional applications are pending. The Lexicon cites them by the author's own numbering (PPA n and NP3), and their titles are published as the applications publish or issue.

**Intent.** The steward plans to give most of what the fee earns away. That is his intent and not a term of this license.

**Verification is free.** Verification sits outside the runtime scope. Reading the bundle, checking a fingerprint, and checking a receipt (its signature, its place in the chain, its anchor, and the policy version it cites) do not require a license from the steward and are free to every party, including a party without a license and without trust in any deployer. A record disciplines the party who wrote it only where someone outside can check it.

**Defensive termination.** The runtime grant of section 5 ends for any implementer that, in litigation or a formal administrative proceeding, alleges that another implementer's implementation of the architecture infringes a patent claim relating to the architecture. Termination does not apply to a defensive counterclaim or to an assertion made in response to a first-filed action. Thirty days' written notice precedes termination, during which the assertion may be withdrawn.

## 6. Steward, pledge, and succession

The open-tier grants are intended to be irrevocable and to survive any sale, change of control, or succession of the holder, so that no successor can withdraw the public grant or raise the standardized layers above royalty-free. Prose does not secure any of this. Instruments do. The mechanisms are three. A recorded covenant not to sue, binding on successors and assigns, travels with the patents through any transfer. An irrevocable grant-back, held by the steward and passing to the Council once it is seated (`GOVERNANCE.md`), is sufficient to re-grant the open-tier rights if the holder defaults. A springing license takes effect on default. Until those instruments are signed and published, this section states the steward's commitment and does not itself bind a successor. RELEASES.md records the date each instrument is published.

## 7. Amendment

The text changes only by the Constitution's Article 11: a receipted amendment that cites the prior fingerprint, the new fingerprint, and the reason, published as a new version. The Council carries amendments once it is seated, with more than one signature as Article 11 requires of a governance of more than one person, and the steward is the sole signer until then (`GOVERNANCE.md`). A published version is never withdrawn. A running system adopts a new version only by its own pinning. Nothing is pushed to it.
