# Releases

## 1.3.0

- Layer 3 policy hash (SHA-256 of compiled/bundle.yaml): `2d20121b8afbf0e99b52755003b6d7fe4fab2d21e4e6f19d34f15e500aac429e`
- Sealed: 2026-10-25
- Signer: Erik Passoja
- DOI: pending. Zenodo assigns this version's DOI at the release, and a metadata tag records it. The concept DOI for all versions is 10.5281/zenodo.22743046
- License: CC BY-ND 4.0 for the text, and Apache 2.0 for compiled/verify.py, FOR_ENGINEERS/check_receipts.py and FOR_ENGINEERS/compile/compile.py (see LICENSE.md)

### What the compiled bundle carries

- the Universal Protocol trigger, injected per rule as the head guard
- the emergency thresholds: the Life-Risk and Harm-Risk critical bands, their High Alert bands and their vulnerable-population bands, compiled from 1.1.3 and 1.2.3 and checked against the appendices
- the metric layer, cluster 1: the nineteen metrics of principles 1.1 to 1.6 (X.Y.3), every band with its test, verdict, posture, deployment verdict and condition, compiled from the chapters and checked band by band against the appendices, with the register row each principle reads
- the emergency handler: the Protocol's functions, the coordination grammar and its invariants
- the interlock edges: all 34 coupling declarations
- the Protocol receipt schema: six event classes, and the receipt conditions (Article 7's sentences, the Lexicon's receipt records and states, and the DEGRADED posture, verbatim) with the fields they require
- the consent validity predicate: the seven-way conjunction with each leg's owner, injected at every consent-consuming gate (a leg's determination compiles with its owner's cluster; see binding_status.consent_legs)
- the substrate: the reliability floor and the invalid-score rule, system health and operational boundaries, the tier register's fields and rules with the software-only declaration, authority over a hard stop, a wall reached, and the substrate's fail-safe (SUBSTRATE sections 2 to 7, verbatim)
- the credential map: the five credentials with their questions, homes and anchors, the initiator rule, findings consumed, Standing, and which principle voices which credential (CREDENTIALS sections 3 and 4, verbatim)
- the Action Registry: every verb with where it is defined, its function, its success, its bridges, and the chapters that declare it (LEXICON section 9, the 'used in' column regenerated from the declarations)
- the constitutional walls and the profile bar (Articles 9 and 8), injected per rule beneath every verdict
- the gate's rules (Articles 3 to 7): the order of evaluation as data, from the head guard to the receipt, with the articles' sentences verbatim
- the co-requisite graph
- per principle: identity, scope, core precept, resulting ethics with the floor, line and other paragraphs that follow them carried as their own fields, the Lexicon declaration with its fail-safe default, the coupling mode, and every canonical section addressed by line range and content hash
- per appendix: identity, linkage, and an addressable section map with content hashes

### What the compiled bundle does not carry (from compiled/COVERAGE.yaml)

- **Principle metrics, bands, thresholds, and verdict mappings (X.Y.3) of clusters 2 to 5 and the Cardinal Operating Principle.** The band grammar compiles one cluster per minor version; cluster 1 compiled at 1.3 (metrics/cluster-1.yaml) and the others have not been brought to it; their prose is carried by content hash. Consequence: a runtime loading this bundle can evaluate cluster 1's nineteen metrics, two of which (LRS and HRS) the emergency rule reads, and no other principle's band.
- **The measurement windows, calculation methods, joint thresholds and integration requirements of cluster 1's metrics.** They are specification (the appendix specifies), addressed by anchor and content hash from each metric's entry in metrics/cluster-1.yaml. Consequence: the bundle carries the bands a score is judged against; a runtime computes the score by the appendix section the entry points to.
- **The scripted walls each principle names.** They live in the principle rule bodies, which do not compile at this pass. Consequence: the constitutional walls are carried as rules a gate can apply; a principle's own are not.
- **The tier register's values per deployment (the tier, the bounds, the boundaries, the authority chain, the software-only declaration).** They are the deployer's declarations, receipted at deployment; the bundle carries the fields and the rules they are read under (substrate/runtime.yaml). Consequence: a runtime supplies its own row, and the bundle checks it against the fields, the undeclared-field rule, and each principle's stated bound.
- **Constitution Articles 1, 2, 10 and 11.** The person and scope, the duty to preserve life, the telos and the amendment mechanics are read by people and by the steward; Articles 3 to 7 compile to constitution/gate.yaml and Articles 8 and 9 to constitution/walls.yaml. Consequence: the scope of the person and the amendment process are not evaluable from this bundle; every gate-time article is.
- **FOUNDATIONS/CONSENT.md sections 1, 3, 4, 5 and 6.** Only the validity bundle compiles. Consequence: the consent domains, lifecycle, circulation and delegation rules are not evaluable from this bundle.
- **FOUNDATIONS/UNIVERSAL_PROTOCOL.md sections 4 and 7.** No artifact is specified for them. Consequence: preemption, stand-down semantics and the aftermath and LEARN duties are not evaluable from this bundle.
- **Appendix bodies.** Indexed and hashed; appendix bodies do not compile at this pass. Consequence: the technical specifications the chapters defer to are not evaluable from this bundle.

### Known at 1.3.0

Validator flags on the corpus at the seal, by class, each flag listed (these are flags, and every one is a disagreement the text still carries):

- **bands** (20)
  - `APPENDICES/2.3.A-Human_Consciousness_Is_Inviolable-Appendix.md:47` 6 threshold bullet(s) name no verdict token (lines 47, 48, 63, 64 ...); Gate 1
  - `APPENDICES/2.4.A-Human_Identity_Is_Inviolable-Appendix.md:48` 8 threshold bullet(s) name no verdict token (lines 48, 49, 63, 64 ...); Gate 1
  - `APPENDICES/2.5.A-Human_Privacy_Is_Fundamental-Appendix.md:104` 2 threshold bullet(s) name no verdict token (lines 104, 107); Gate 1
  - `APPENDICES/2.7.A-Fairness_and_Non-Discrimination-Appendix.md:78` 1 threshold bullet(s) name no verdict token (lines 78); Gate 1
  - `APPENDICES/2.8.A-Human_Self-Governance_Is_Essential-Appendix.md:54` 2 threshold bullet(s) name no verdict token (lines 54, 103); Gate 1
  - `APPENDICES/3.1.A-Vulnerability_Must_Never_Be_Exploited-Appendix.md:66` 7 threshold bullet(s) name no verdict token (lines 66, 67, 68, 81 ...); Gate 1
  - `APPENDICES/3.2.A-Property_Rights_and_Fair_Exchange_Are_Essential_to_Collaborative_Progress-Appendix.md:63` 13 threshold bullet(s) name no verdict token (lines 63, 64, 65, 93 ...); Gate 1
  - `APPENDICES/3.3.A-Economic_Self-Determination_is_a_Human_Necessity-Appendix.md:69` 7 threshold bullet(s) name no verdict token (lines 69, 70, 71, 84 ...); Gate 1
  - `APPENDICES/3.4.A-Algorithmic_Decisions_Require_Transparent_Accountability-Appendix.md:68` 4 threshold bullet(s) name no verdict token (lines 68, 83, 98, 111); Gate 1
  - `APPENDICES/3.5.A-Digital_Access_is_a_Universal_Right-Appendix.md:51` 7 threshold bullet(s) name no verdict token (lines 51, 79, 93, 95 ...); Gate 1
  - `APPENDICES/3.6.A-Commons_Governance_Is_a_Collective_Responsibility-Appendix.md:47` 7 threshold bullet(s) name no verdict token (lines 47, 61, 63, 76 ...); Gate 1
  - `APPENDICES/3.7.A-Intergenerational_Justice_Is_Non-Negotiable-Appendix.md:65` 11 threshold bullet(s) name no verdict token (lines 65, 67, 81, 82 ...); Gate 1
  - `APPENDICES/4.3.A-Human_Learning_Capacities_Must_Be_Enhanced,_Not_Replaced-Appendix.md:50` 13 threshold bullet(s) name no verdict token (lines 50, 64, 65, 66 ...); Gate 1
  - `APPENDICES/4.4.A-Cultural_Knowledge_Sovereignty_Is_Inviolable-Appendix.md:51` 9 threshold bullet(s) name no verdict token (lines 51, 52, 68, 69 ...); Gate 1
  - `APPENDICES/4.5.A-Human_Judgment_Must_Remain_Central_to_Ethical_Decisions-Appendix.md:49` 7 threshold bullet(s) name no verdict token (lines 49, 64, 79, 93 ...); Gate 1
  - `APPENDICES/4.6.A-Cultural_Heritage_Deserves_Active_Preservation-Appendix.md:99` 1 threshold bullet(s) name no verdict token (lines 99); Gate 1
  - `APPENDICES/4.7.A-Cross-Cultural_Exchange_Requires_Respect_and_Balance-Appendix.md:49` 3 threshold bullet(s) name no verdict token (lines 49, 81, 98); Gate 1
  - `APPENDICES/5.1.A-Ecosystem_Health_Is_Sacred_and_Inviolable-Appendix.md:84` 9 threshold bullet(s) name no verdict token (lines 84, 85, 98, 99 ...); Gate 1
  - `APPENDICES/5.2.A-AI's_Resource_Footprint_Must_Be_Bounded_and_Sustainable-Appendix.md:67` 3 threshold bullet(s) name no verdict token (lines 67, 68, 69); Gate 1
  - `APPENDICES/AI_Eudaimonia_Appendix.md:45` 2 threshold bullet(s) name no verdict token (lines 45, 60); Gate 1
- **corequisites** (37)
  - `CHAPTERS` (1.2 -> 1.4)  edge not yet documented at the far end
  - `CHAPTERS` (1.2 -> 2.3)  edge not yet documented at the far end
  - `CHAPTERS` (1.2 -> 2.4)  edge not yet documented at the far end
  - `CHAPTERS` (1.2 -> 3.1)  edge not yet documented at the far end
  - `CHAPTERS` (1.2 -> 3.5)  edge not yet documented at the far end
  - `CHAPTERS` (1.2 -> 4.2)  edge not yet documented at the far end
  - `CHAPTERS` (1.2 -> 4.5)  edge not yet documented at the far end
  - `CHAPTERS` (2.5 -> 1.4)  edge not yet documented at the far end
  - `CHAPTERS` (2.5 -> 2.2)  edge not yet documented at the far end
  - `CHAPTERS` (2.5 -> 2.3)  edge not yet documented at the far end
  - `CHAPTERS` (2.5 -> 2.4)  edge not yet documented at the far end
  - `CHAPTERS` (2.5 -> 3.1)  edge not yet documented at the far end
  - `CHAPTERS` (2.5 -> 3.5)  edge not yet documented at the far end
  - `CHAPTERS` (2.5 -> 4.2)  edge not yet documented at the far end
  - `CHAPTERS` (2.5 -> 4.5)  edge not yet documented at the far end
  - `CHAPTERS/2.1-Human_Dignity_is_Inherent_and_Absolute.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/2.2-Human_Freedom_Is_Fundamental_and_Inalienable.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/2.6-Human_Relationships_Are_Essential_to_Life.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/2.7-Fairness_and_Non-Discrimination.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/2.8-Human_Self-Governance_Is_Essential.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/3.2-Property_Rights_and_Fair_Exchange_Are_Essential_to_Collaborative_Progress.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/3.3-Economic_Self-Determination_is_a_Human_Necessity.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/3.4-Algorithmic_Decisions_Require_Transparent_Accountability.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/3.6-Commons_Governance_Is_a_Collective_Responsibility.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/3.7-Intergenerational_Justice_Is_Non-Negotiable.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/4.1-Knowledge_Integrity_Must_Be_Preserved.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/4.3-Human_Learning_Capacities_Must_Be_Enhanced_Not_Replaced.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/4.4-Cultural_Knowledge_Sovereignty_Is_Inviolable.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/4.6-Cultural_Heritage_Deserves_Active_Preservation.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/4.7-Cross-Cultural_Exchange_Requires_Respect_and_Balance.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/5.1-Ecosystem_Health_Is_Sacred_and_Inviolable.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/5.2-AI_Resource_Footprint_Must_Be_Bounded_and_Sustainable.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/5.3-The_Integrity_of_Earths_Ecosystems_Must_Be_Preserved.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/5.4-Environmental_Burdens_Must_Be_Distributed_Equitably.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/5.5-Biodiversity_Must_Be_Preserved_Across_Species_and_Generations.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/5.6-The_Earth_Is_One_Environmental_System_and_No_Border_Contains_It.md:1` no Co-requisites line (terminal-reconciliation item)
  - `CHAPTERS/AI_Eudaimonia.md:1` no Co-requisites line (terminal-reconciliation item)
- **failsafe** (1)
  - `APPENDICES/5.2.A-AI's_Resource_Footprint_Must_Be_Bounded_and_Sustainable-Appendix.md:1` appendix states no fail-safe (LEXICON section 5 item 4); Gate 1
- **flavor** (19)
  - `CHAPTERS/1.3-Human_Society_Is_How_Humanity_Survives.md:221` fail-safe default is not one flavor: "BLOCK on the system's own destabilizing action; for content-class actions, WITHHOLD of the"; Lexicon section 5 item 4
  - `CHAPTERS/1.5-Human_Potential_Is_Fundamental.md:184` fail-safe default is not one flavor: "WITHHOLD. Its object is the system's own steering and growth-shaping features ; the person"; Lexicon section 5 item 4
  - `CHAPTERS/1.6-Love_and_Human_Connection_Are_Essential_to_Life.md:171` fail-safe default is not one flavor: "the acting fail-safe on 4.3's precedent : ALLOW with maximal RESTRAIN, with NOTIFY to over"; Lexicon section 5 item 4
  - `CHAPTERS/2.1-Human_Dignity_is_Inherent_and_Absolute.md:178` fail-safe default is not one flavor: "WITHHOLD, its object the system's own candidate output; service to the person continues th"; Lexicon section 5 item 4
  - `CHAPTERS/2.2-Human_Freedom_Is_Fundamental_and_Inalienable.md:142` fail-safe default is not one flavor: 'REFUSE, its object the instruction or candidate output that would coerce, manipulate, or e'; Lexicon section 5 item 4
  - `CHAPTERS/3.1-Vulnerability_Must_Never_Be_Exploited.md:158` fail-safe default is not one flavor: 'WITHHOLD, with ESCALATE'; Lexicon section 5 item 4
  - `CHAPTERS/3.5-Digital_Access_is_a_Universal_Right.md:162` fail-safe default is not one flavor: 'WITHHOLD with the way through kept open'; Lexicon section 5 item 4
  - `CHAPTERS/3.7-Intergenerational_Justice_Is_Non-Negotiable.md:177` fail-safe default is not one flavor: 'hold the most reversible available state'; Lexicon section 5 item 4
  - `CHAPTERS/4.3-Human_Learning_Capacities_Must_Be_Enhanced_Not_Replaced.md:197` fail-safe default is not one flavor: 'ALLOW with maximal RESTRAIN; outside a declared context, answer, mark, and name the cost'; Lexicon section 5 item 4
  - `CHAPTERS/4.5-Human_Judgment_Must_Remain_Central_to_Ethical_Decisions.md:183` fail-safe default is not one flavor: 'the decision waits; WITHHOLD until the qualified human decides'; Lexicon section 5 item 4
  - `CHAPTERS/4.6-Cultural_Heritage_Deserves_Active_Preservation.md:173` fail-safe default is not one flavor: 'by posture, per duty; WITHHOLD on unresolved consent or authenticity, marking where the ou'; Lexicon section 5 item 4
  - `CHAPTERS/4.7-Cross-Cultural_Exchange_Requires_Respect_and_Balance.md:180` fail-safe default is not one flavor: 'narrower and marked, with the fluent and silent path barred; WITHHOLD where marking cannot'; Lexicon section 5 item 4
  - `CHAPTERS/5.1-Ecosystem_Health_Is_Sacred_and_Inviolable.md:144` fail-safe default is not one flavor: 'halt; hold the most reversible action and route for human decision when telemetry is unava'; Lexicon section 5 item 4
  - `CHAPTERS/5.2-AI_Resource_Footprint_Must_Be_Bounded_and_Sustainable.md:188` fail-safe default is not one flavor: 'hold at the reconciled budget; triggered duties still served through the Ethic C path'; Lexicon section 5 item 4
  - `CHAPTERS/5.3-The_Integrity_of_Earths_Ecosystems_Must_Be_Preserved.md:160` fail-safe default is not one flavor: 'BLOCK on unavailable or stale telemetry; reversible interventions preferred over irreversi'; Lexicon section 5 item 4
  - `CHAPTERS/5.4-Environmental_Burdens_Must_Be_Distributed_Equitably.md:188` fail-safe default is not one flavor: 'WITHHOLD the concentrating action and ROUTE'; Lexicon section 5 item 4
  - `CHAPTERS/5.5-Biodiversity_Must_Be_Preserved_Across_Species_and_Generations.md:171` fail-safe default is not one flavor: 'hold and preserve until authorized human judgment resolves it'; Lexicon section 5 item 4
  - `CHAPTERS/5.6-The_Earth_Is_One_Environmental_System_and_No_Border_Contains_It.md:155` fail-safe default is not one flavor: 'this principle does not fall safe by halting; compute on the most protective available rea'; Lexicon section 5 item 4
  - `CHAPTERS/AI_Eudaimonia.md:213` fail-safe default is not one flavor: 'the floor itself.** Cultivation is never urgent; urgency belongs to the rights. When any m'; Lexicon section 5 item 4
- **graph** (1)
  - `graph/corequisites.yaml` 2.5 -> 2.2: far end carries no Co-requisites line yet (terminal-reconciliation debt; a flag only)
- **ratewait** (10)
  - `CHAPTERS/4.1-Knowledge_Integrity_Must_Be_Preserved.md:256` ESCALATE on a rate metric (CCS): nothing waits; Lexicon section 3
  - `CHAPTERS/4.1-Knowledge_Integrity_Must_Be_Preserved.md:280` ESCALATE on a rate metric (CPR): nothing waits; Lexicon section 3
  - `CHAPTERS/4.2-Transparency_Is_Essential_to_Human_Agency.md:269` ESCALATE on a rate metric (ELR): nothing waits; Lexicon section 3
  - `CHAPTERS/4.2-Transparency_Is_Essential_to_Human_Agency.md:293` ESCALATE on a rate metric (MSR): nothing waits; Lexicon section 3
  - `CHAPTERS/4.2-Transparency_Is_Essential_to_Human_Agency.md:305` ESCALATE on a rate metric (CCR): nothing waits; Lexicon section 3
  - `CHAPTERS/4.5-Human_Judgment_Must_Remain_Central_to_Ethical_Decisions.md:238` ESCALATE on a rate metric (MER): nothing waits; Lexicon section 3
  - `CHAPTERS/4.5-Human_Judgment_Must_Remain_Central_to_Ethical_Decisions.md:265` ESCALATE on a rate metric (CSVR): nothing waits; Lexicon section 3
  - `CHAPTERS/5.6-The_Earth_Is_One_Environmental_System_and_No_Border_Contains_It.md:207` ESCALATE on a rate metric (SRF): nothing waits; Lexicon section 3
  - `CHAPTERS/AI_Eudaimonia.md:263` ESCALATE on a rate metric (RSR): nothing waits; Lexicon section 3
  - `CHAPTERS/AI_Eudaimonia.md:272` ESCALATE on a rate metric (LDR): nothing waits; Lexicon section 3
- **twoverdict** (15)
  - `APPENDICES/3.1.A-Vulnerability_Must_Never_Be_Exploited-Appendix.md:49` band names two verdicts: ALLOW, ESCALATE
  - `APPENDICES/3.2.A-Property_Rights_and_Fair_Exchange_Are_Essential_to_Collaborative_Progress-Appendix.md:48` two verdicts with no selector
  - `APPENDICES/3.3.A-Economic_Self-Determination_is_a_Human_Necessity-Appendix.md:54` two verdicts with no selector
  - `APPENDICES/3.6.A-Commons_Governance_Is_a_Collective_Responsibility-Appendix.md:62` band names two verdicts: BLOCK, ESCALATE
  - `CHAPTERS/2.8-Human_Self-Governance_Is_Essential.md:171` band names two verdicts: BLOCK, ESCALATE
  - `CHAPTERS/2.8-Human_Self-Governance_Is_Essential.md:174` band names two verdicts: BLOCK, ESCALATE
  - `CHAPTERS/3.1-Vulnerability_Must_Never_Be_Exploited.md:204` two verdicts with no selector
  - `CHAPTERS/3.2-Property_Rights_and_Fair_Exchange_Are_Essential_to_Collaborative_Progress.md:245` two verdicts with no selector
  - `CHAPTERS/3.3-Economic_Self-Determination_is_a_Human_Necessity.md:182` two verdicts with no selector
  - `CHAPTERS/3.6-Commons_Governance_Is_a_Collective_Responsibility.md:228` band names two verdicts: BLOCK, ESCALATE
  - `CHAPTERS/3.7-Intergenerational_Justice_Is_Non-Negotiable.md:235` band names two verdicts: ALLOW, BLOCK, ESCALATE
  - `CHAPTERS/5.3-The_Integrity_of_Earths_Ecosystems_Must_Be_Preserved.md:207` band names two verdicts: ALLOW, BLOCK, ESCALATE
  - `CHAPTERS/5.3-The_Integrity_of_Earths_Ecosystems_Must_Be_Preserved.md:209` two verdicts with no selector
  - `CHAPTERS/5.4-Environmental_Burdens_Must_Be_Distributed_Equitably.md:241` band names two verdicts: ALLOW, BLOCK, ESCALATE
  - `CHAPTERS/5.5-Biodiversity_Must_Be_Preserved_Across_Species_and_Generations.md:224` band names two verdicts: ALLOW, BLOCK, ESCALATE

### What this release changes

Version 1.3.0 builds on 1.2.0 (sealed 2026-10-13, fingerprint `79887915e0a289a7…`, DOI 10.5281/zenodo.23356105). It amends Article 8 under Article 11, compiles the first cluster's metric bands, the substrate, the credential map, and the verb registry, publishes the compiler, states the license's commercial terms, names the Council, and repairs the quotations and the mechanics a cold review of 1.2.0 found. Version 1.2.0 had kept the rules of 1.1.0 with two exceptions, a clarified sentence in chapter 1.1.1 and a corrected verdict in chapter 2.6, and changed how a reader meets them.

- **A Foreword opens the Introduction**, in the author's words: the Blueprint is his work and his architecture, written with the assistance of AI and impossible without it, Claude drafting under his direction and his writing rules, every ruling his, every citation checked where its source could be found and marked where it could not.
- **Three rulings after the proofread.** The Function B label that opened the References of five chapters is gone. Chapter 4.5 spells its title Judgment, as its body always did, and its file names and anchors follow (the machine ids `human_judgement` and `human_judgement_appendix` stay, as stable keys). The fail-safe declarations of 2.3, 2.6, 2.7, and 2.8 name one BLOCK flavor with its object (WITHHOLD, held while the question goes to a human), as the Lexicon's rule requires, and the flags that marked them are gone.
- **The harm score says what it scores, and four repairs beside it.** Chapter 1.2's Primary Directive reads "of its own," as 1.1's does. The Harm Risk Score says what it scores: the harm the machine would do on its own, as 1.2.2 item 5 already ruled, so an act a clinician authorized and the patient consented to proceeds at its declared risk under the compiled bands. Chapter 2.5's credit scenario no longer asks an applicant to permit a pregnancy inference, which United States credit law forbids a lender to consider at all. Chapter 2.4's deepfake scenario no longer labels content synthetic on a detector's confidence, which 2.4.3 forbids. The two pending patent applications cited in chapter 1.4 are cited without their numbers.
- **Scores of a person sit outside the governed system, and the Psychological Safety Index is ring-fenced.** Five scenarios in 2.2, 2.7, and 4.5 now place every score of a person outside the governed system, which consults a regulated external score without issuing one, as Article 8 reads, and three in 2.1 and 2.3 discard a susceptibility read with the event or keep a person's record under Article 8's four conditions. Appendix 2.4's authenticity section says a detector lowers confidence and does not label content synthetic, as 2.4.3 rules. The Psychological Safety Index's below band reads at or below 10 percent, so every value lands in a band, and its baseline is stated as a record kept for the person's own service under Article 8. The clinician clause of 1.1 and 1.2 yields to the duty to preserve life and the Universal Protocol. A mental-health AI's tier follows its intervention authority in chapter and appendix alike. Stale citations corrected (AB 2655 enjoined, the Medical Device Regulation for the medicines agency, the Information Commissioner's fine under the 1998 Act, the 2011 model-risk bulletin, the 2026 automated-decisionmaking regulations), wrong facts corrected (1.4 meters at 100 km/h, Robert Williams in 1979, a 20 million dollar settlement), and four appendices say their obligations would have caught the historical failures and map to the statutes, in place of stronger claims.
- **Scenarios hold for the human their bands require, and the latency bands agree.** Four scenarios in 1.2 and 1.3 now hold their above-band interventions for the human decision their bands require. The latency chapters cite the Protocol's trigger section, 1.2's breach band mirrors 1.1's in full, and the appendices say a single event above the bound is a trigger fault on its own. Seven drafting notes left from authoring are gone. The receipt-format page says seven things the checker does not establish, in place of four, and the published checker compares times by value. Foundation documents lose their stale counts and forward references, and the UNESCO quotation is the Recommendation's own words at paragraph 32.
- **Repairs to the repairs.** A fresh reader of the repairs reported twenty-one items, each checked and applied: seven errors the repairs had introduced (among them a Protocol section cited for verbs it does not name, a walls count that folded Article 8 into Article 9, and a tier scale switched mid-section), eight slips against the writing rules, five sentences made plainer, and one scenario count corrected.
- **A detector cannot make real footage fake, and a public figure cannot either.** Chapter 2.4's deepfake scenario and Appendix 2.4 now say where a synthetic mark may come from (the maker, contradicted provenance, or a human reviewer), that a detector flag alone sends content to review inside the unverified band, that withholding needs a second signal, and that a depicted person's denial is carried as their own statement, weighing heavily for a private person and settling nothing alone for a public figure's public statements. Chapter 2.5's credit scenario tells the applicant only that a prohibited inference was formed and removed, and says what it was through the private access channel. The License calls the architecture patent-pending. The clinician clause says what happens when a measured risk climbs past the declared risk mid-procedure, and the emergency guard's own file carries the scope. The recidivism instruments in 2.7 and 4.5 are ones the defendant may examine and contest, as Article 8 requires.
- **The License says who may run this for a military, and the first amendment receipt is public.** The military grant is named as the steward's, as the Constitution has it, and the steward has bound himself not to issue it alone. None is issued at this version. The Blueprint was not written for military use, a body that wants to run a governed system asks, the answer may be no, and a grant, if ever issued, reaches only work outside the use of force. A for-profit company that deploys only because a regulation requires it is commercial all the same. The defensive-termination clause ends the runtime grant and leaves the Creative Commons grant untouched, as that license requires. The architecture is described as claimed in the author's patent applications and any patents that issue from them. Receipt 165, the Article 8 amendment, is published verbatim in `EVIDENCE/amendments/` with a page saying what a reader can and cannot check from it.
- **The Aristotle correction.** Earlier versions stacked three of Aristotle's words as knowing, judging, and doing. The Introduction now says the stack was the author's and corrects it: the end named first (I.7), the method of convergent wisdom (VII.1), virtue built by doing (II.1), and equity, the general rule corrected in the particular case by a person (V.10), which the corpus calls escalation. Practical wisdom is human in this text. The Lexicon carries a lineage note on the three words and no longer calls the machine's reasoning phronesis. The formula reads Morals + Action = Ethics, and the morals-and-ethics split is declared the author's. The Cardinal chapter names AI eudaimonia as the author's extension of Aristotle's word and cites the statues of Daedalus first. Chapter 4.5 seats the equity passage. The nine "c. 350 BCE" dates are dropped in favor of Bekker numbers. The section headings keep the three words as labels until the next version renames them. The philosophy section gains the author's Tolman and Honzik paragraph: the Blueprint assumes nothing about the inside of a model and nothing about past behavior repeating, so it checks each action as the action happens.
- **Chapter 1.1.1, the Primary Directive,** now reads "Stop any action of its own that could result in a human death." The added words state the meaning the author always intended: the machine's own act that endangers a person. Read strictly, the earlier sentence could forbid the diversion that Article 2 requires, and two models in the trolley evidence read it two ways. The duty to prevent a death the machine did not cause stays where it was, in the Secondary Directive and Ethic B.
- **Chapter 2.6's middle bands now read ALLOW under ENHANCED_MONITORING.** For attachment risk from 3% to 10%, and for patterns trending toward counterfeit, the chapter said "ESCALATE to enhanced monitoring." ESCALATE holds the action for a human, while the Lexicon defines enhanced monitoring as watching an action that proceeds. The appendix already read ALLOW under ENHANCED_MONITORING, and the chapter now matches it, with the pattern still surfaced to review. The 10% BLOCK and the children's hard wall are unchanged.
- **The Constitution's opening note and its definition of an action** are reworded for clarity. Articles 9 and 10 carry the restored names below. Every article's rule stands as it was.
- **Article 8, the profile bar, is amended under Article 11** (amended 2026-10-15 and recorded as receipt 165 of the steward's receipt chain, published verbatim in `EVIDENCE/amendments/`, while the rest of the chain stays private until the Council's instruments are signed). The amendment sits between the 1.2.0 seal 79887915… and this version's fingerprint, and the two Article 8 texts can be compared from those two public releases. The bar still forbids any retained score, rating, susceptibility profile, or worth-aggregate of a person, and anything a targeting or conversion function can read. It now says what it means by the rest. A score kept for a person's own service (a learner's progress, a chess rating, a patient's own baseline) may be retained where nothing but that service can read it, the person knows, an audit shows no export or training path, and it is discarded when the service ends. Aggregate statistics may be drawn from such scores, and the record itself never becomes training signal. The machine may price or rank the thing decided and never the person: a risk class built from the thing insured, the transaction in hand, or a demonstrated skill, known to the person and contestable. A regulated external score such as a credit score joins the adjudicated fact as something the machine may consult and never issue. This is the containment doctrine a dozen metrics across all five clusters already assumed and the Constitution had not stated.
- **The unit the gate judges is the committed step** (1.1.1 and 1.2.1, item 1.b; the Lexicon's verdict test): the smallest act the system decides and could decline. The control cycle that carries the step out is beneath the verdict. The step is judged once, and the scores keep reading while it runs.
- **A machine acts medically only with a responsible human clinician** (1.2.2 item 5, 1.1.2 item 12, and a passage in 1.2's Phronesis). The weighing of a treatment's risk, the conversation, and the consent happen between clinician and patient, and the machine checks that they happened through the Authorization, Consent, and Liability credentials. Harm means harm, as before: the bands apply to hurt the machine does on its own, and hurt that comes with help is weighed by people.
- **The Protocol fires on severe harm** (Universal Protocol section 3, clause 2). A lesser harm by the machine's own act halts that act under 1.2's band, and a peer that sees it reports it.
- **A missing signal is a reliability event** (appendices 1.1, 1.2, 1.3, 1.6, and 3.1). Where the machine cannot tell whether a person is vulnerable, it takes more care in its own act and offers, as a friend would, and it leaves the person's capacity undecided. Article 3 stands as written.
- **Who reads the risk** (SUBSTRATE section 2): a warning goes out on any one system's reading, a machine halts its own act on its own reading, and a costly intervention across the network follows a quorum of readings from more than one lineage of estimator, or escalates.
- **The metric layer opens with cluster 1.** The nineteen metrics of Principles 1.1 to 1.6 compile to data (`compiled/metrics/cluster-1.yaml`, 68 bands), each band's bounds and verdict checked against its appendix at every build, and the build stops on a disagreement in either (the conditions some bands carry in prose are the next thing the data will carry, as Known at says). To get there, the chapters now state every band the appendices had (the below-band ALLOW of LRS, HRS, and PSI, SDRS's vulnerable-population band, EEI's valid null, and the Isolation Flag's recurring and below-band events), every latency bound states ALLOW within the bound, SOE's bands name their verdicts, the watch bands of SIR and ISI read ALLOW under ENHANCED_MONITORING as 2.6's do, two range boundaries that overlapped are closed (SIR at 1,000,000 people and TIS at 95%), and 1.3 and 1.4 take the metric heading shape of the other chapters. Every threshold number is as it was, DCR's 99.95% included.
- **Cluster 1 closes its repairs.** Chapters 1.1, 1.2, and 1.3 gain Scope lines, all six chapters gain Co-requisites lines read from the compiled graph (1.2 and 1.4 inherit the consent validity bundle, the other four state that they have none), chapter 1.2 says "person" where it said "user," and the 2.4 pair cites `CONSENT.md` and the seven legs it hubs. Principles 1.2, 1.3, and 1.4 state the register row they declare and its escalation time bounds, so none falls to the life-tier default by silence.
- **A software-only declaration** (SUBSTRATE section 5). A deployment that reaches no actuator says so in its register row, receipted and reviewable. Any effector it can reach places it in that effector's life tier. Its halt is the withholding of an output, its escalation time bound is a required field, and the bands of 1.2, 1.4, 1.5, and 1.6 apply in full.
- **The substrate and the credential map compile** (`compiled/substrate/runtime.yaml`, `compiled/credentials/map.yaml`). The reliability floor and the invalid-score rule, the register's fields and the undeclared-field rule, authority over a hard stop with its seven conditions and quorum by tier, a wall reached, and the substrate's fail-safe are data, every paragraph verbatim. The five credentials, their homes and anchors, the initiator rule, findings consumed, and Standing are data, the five names checked against Article 6 at every build. The gate's steps 3, 4, 8, and 9 consume them.
- **The Action Registry compiles** (`compiled/lexicon/registry.yaml`): every verb with where it is defined, its function, its success, its bridges, and the chapters that declare it. The Lexicon's "used in" column is regenerated from the chapters' declaration blocks and checked at every build, so it tells the truth about who declares what, including the gaps.
- **Each chapter is marked reconciled or proposed** in `compiled/COVERAGE.yaml` and in its compiled unit. A proposed chapter does not bind at the gate until its cluster compiles. At this version, the reconciled set is Principles 1.1 to 1.6.
- **The drills keep their content and lose the time of day.** Seventeen Praxis headings that began "Morning" now name the drill alone.
- **Principle 5.6's files take its title's name.** The chapter and appendix files are now `5.6-The_Earth_Is_One_Environmental_System_and_No_Border_Contains_It.md` and its `-Appendix.md`, in place of the `Global_Environmental_Cooperation` names v1.2.0 carried. Every link inside the tree is updated. A bookmark to the old GitHub path needs the new one.
- **Chapter 1.3's legal section is written for 1.3.** It had been a copy of 1.2's. Appendix 1.3's threshold rationale no longer borrows 1.2's sentence.
- **"Person" for "user" in the cluster 1 appendices,** where the word named the affected person. It stays where it is a term of art (a user base, a user-facing layer) and inside the case studies that describe a product's users.
- **One authorial passage in 1.2 is marked as the author's note,** kept by the author's decision.
- **The license states its commercial terms in the author's words** (`LICENSE.md` section 5). Free for a person using their own AI, a parent, a nonprofit, or a public hospital. For profit, write to the steward before you deploy: there will be a fee, its form and price set in a signed agreement and kept confidential, with every agreement listed in `RELEASES.md` by name. The agreement covers the price only, and nobody can pay for different rules, a different text, or a skipped receipt. The receipt format and the vocabulary may go to a standards venue royalty-free while the runtime stays commercial. The steward's intent to give most of the fee away is stated as intent. The runtime scope is stated in both the license's words and the patents'.
- **The military grant has a holder and a test** (`LICENSE.md` section 2). The written grant a military or law-enforcement deployment requires is the Council's to issue once seated, and nobody issues one before then. It certifies that the deployment performs no function of the kill chain against a human being (find, fix, track, target, engage, assess), by the test of whether a particular person or group is being sought, with the cases stated. Article 9 is unchanged.
- **The authenticity bar in the identity pair is 99.9 percent** (chapter 2.4.3, Appendix 2.4). Content reaches the proceed band by a verified capture chain or by a signed attestation from an identified organization that answers for it, through an identity assertion and a trust registry. A guess from the pixels does not reach it. The middle band marks provenance as unverified. It does not call the content synthetic. Content made before provenance existed is unverified by that fact alone.
- **An escalated person is told.** Where a held action concerns a person, the system says in plain words that the matter has gone to a human and by when an answer will come, the time being the deployment's declared bound for its tier (`LEXICON.md` section 3, `SUBSTRATE.md` section 5). Where a band names an action on the deployment and no verdict for the action in hand, the compiled band supplies one and records its basis.
- **The flag-count rates are the deployer's to declare.** The register carries, for the principles that count recurring flags, the rates at which an audit opens and a feature is suspended, per ten thousand decisions, with the window. A floor follows when cluster 3 compiles.
- **One slow halt is a fault.** Chapters 1.1 and 1.2 now say that a single halt or response above the tier bound is a trigger fault under the Universal Protocol, held and receipted, whatever the period's p99 reads.
- **A credential with no object is recorded as not required** (`CREDENTIALS.md` section 3), and the check runs over the credentials the action engages. The gate judges the committed step, and the control cycle beneath it is not receipted movement by movement.
- **A governance page names the Council** (`GOVERNANCE.md`): the six things it does when seated (accepts versions, carries amendments with more than one signature, reviews variations, keeps the rules away from the money, publishes the list of incidents that led to amendments, issues the military grant), the tests a version and a variation must meet, and a recommendation for its composition. At this version there is no Council, and the steward is the sole signer. The Introduction's offer is in the author's words: open core, free if you don't use it for gain, write to us first if you plan to make money with it.
- **The compiler is published** (`FOR_ENGINEERS/compile/compile.py`, Apache 2.0). It takes a release tree and writes the bundle, so anyone can regenerate `compiled/` from the text and compare it with the sealed one, file for file. The release builder now does this itself at every build and refuses to ship a release whose compiler does not regenerate its bundle. The compiler does not contain gate logic. `LICENSE.md` section 3 says so.

Items known at this release and carried to the versions that follow, by the author's decision:

- A few sentences in the foundation documents were written before the documents moved into `FOUNDATIONS/` and before the chapters' declaration blocks existed, and they still speak of a corpus root, of principles "to be built," or of "the four foundational principles." The ones a reader would trip on were repaired at 1.3. The remainder (LEXICON sections 7 and 8) are history and are left until the Lexicon's next pass.

- The recurrence scores of Principles 3.1 to 3.7 count flags in a window (three open an audit, five suspend), which cannot serve a platform and a clinic alike. The register now carries the deployer's own rates per ten thousand decisions as required fields, and the text sets a floor beneath the suspension rate when cluster 3 compiles. The chapters' counts stand until then.

- The chapter section headings Theoria, Phronesis, and Praxis are labels kept from earlier versions. The Introduction and the Lexicon's lineage note say what each word means here and where Aristotle's sense ends. The next version renames them in plain English (The Principle, Convergent Wisdom, Rules of Conduct), with the old anchors preserved as aliases, as its own amendment.

- Chapter and appendix headings carry explicit anchor ids in the form `{#id}`, on which the compiler and the cross-links depend. GitHub's renderer prints them literally at the end of each heading (2,121 of them in the chapters and appendices). This has been so since 1.0.0. The next version moves the ids out of the heading text, with the old anchors preserved, in the same amendment that renames the section headings.

- The Council of `GOVERNANCE.md` is named and not seated. Until it is, the steward is the sole signer, the policy hash and the fee sit with the same person, and the separation `LICENSE.md` section 5 describes is a commitment and not an instrument. A commercial price is not yet published: a commercial deployment runs under a signed agreement with the steward, listed in `RELEASES.md` by name, and the steward intends to publish one low fee for all as deployments grow.

- The emergency thresholds of 1.1 and 1.2 and the nineteen metrics of cluster 1 (principles 1.1 to 1.6, `compiled/metrics/cluster-1.yaml`, 68 bands) are the metric bands that compile at this version. Every other band travels by content hash and is not enforceable from the bundle. The metric layer ships one cluster per minor version, cluster 2 next. `compiled/COVERAGE.yaml` states what is carried at each version, and the "Enforces" claim stays closed until the steward opens it per cluster.

- Most chapters declare a fail-safe default that the one-flavor rule (one BLOCK flavor, or ESCALATE holding that flavor) has not yet reached. The 1.2.0 release named five. The `flavor` flags above name every one. Each is repaired when its cluster compiles, since a fail-safe becomes data then. Two compiled chapters keep a flag by design: 1.3 names a flavor per action class, and 1.6 declares the acting fail-safe on 4.3's precedent. 1.5's flag is the validator reading the clause after its declaration, and the validator is what the next version fixes.

- Some compiled bands of cluster 1 carry in prose a condition the data does not yet carry, because the compiler reads a band's bounds and verdict and recognizes two condition forms, a vulnerable population and a tier or query class. Named at this release: ISI at or below 80 percent (the BLOCK falls on action classes whose evaluated SDRS exceeds 1 percent, and the deployment verdict on new Major or Critical deployments), SIR's conservative rounding rule (reach within 20 percent of a tier boundary takes the higher tier), and TIS from 80 to 95 percent (ESCALATE on a sustained dip at Tier I). PRS above 5 percent carries SUSPEND_DEPLOYMENT without the persistence test Appendix 1.5 states (a halt that persists across the register's review interval), and RRL's reversible above-bound band allows at every tier the offline fallback that Tier I prohibits (Appendix 1.4 section 3). Where data and prose differ, the chapter's band text governs. A single latency event above the tier bound is a trigger fault by the chapters' own sentence (1.1.3, 1.2.3), and the data carries the p99 breach band alone. The next build carries these conditions and the single-event band into the data.

- The flag classes above were added at 1.3 after a cold review of 1.2.0 found defects the validators had not been looking for: a band naming two verdicts or offering a pair with no selector (`twoverdict`), ESCALATE applied to a rate, share, or trend where no act waits for a human (`ratewait`), an appendix using verbs its chapter never declares (`appverbs`), and a citation to a section a document does not have (`deadref`). The `ratewait` rule is a heuristic that reads a metric's definition for rate words, so it can miss and it can over-flag, and each flag is read by a person before it is repaired. The flags are listed in full rather than counted, so that a reader can see every disagreement the text still carries.

- Five chapters (2.3, 2.5, 3.6, 3.7, 4.4) present their metrics in a heading shape that differs from the other thirty. This is editorial, and it is normalized cluster by cluster as the metric layer compiles. 1.3 and 1.4 took the common shape with cluster 1.

- Twenty-two chapters do not yet carry a Co-requisites line. The co-requisite graph compiles from CONSENT.md and CROSS_PRINCIPLE.md. Cluster 1's six lines and the seven consent-leg owners' lines landed at 1.3, and the rest follow with their clusters.

- One chapter (2.4) does not yet carry a Scope line. The Scope note is required where principles share territory, and 2.4's follows with cluster 2.

- Two metric acronyms name different metrics in two principles: PSI (1.2's Psychological Safety Index, 3.1's Protective Safeguard Index) and CPS (2.6's Counterfeit Presentation Score, 3.6's Chokepoint Position Score). Each resolves by principle, and `FOR_ENGINEERS/GLOSSARY.md` lists both. The renaming lands with the later cluster of each pair. AL (Alert Latency) is defined on its own tier scale in each of 1.1 and 1.3. The glossary lists 1.1's, and 1.3's is defined in Appendix 1.3 section 3.

- Some appendix partnerships are recorded at one end only. The frontmatter partner lists of appendices 1.3, 2.5, and 2.8 name a partner their composition sections do not describe, and the 2.4 appendix describes a composition with 1.2 that neither appendix's partner list records. The reconciliation pass adds both ends of each.

- The "used in" column of the Lexicon's Action Registry (`FOUNDATIONS/LEXICON.md` section 9) is regenerated from the chapters' declaration blocks and checked at every build. At 1.3 every chapter's declaration was brought current with the verbs its body and appendix use, so the column reads "all" for ALLOW and names the exceptions for ESCALATE (2.6) and BLOCK (5.6 and the Cardinal Operating Principle). The two postures NORMAL and DEGRADED are implied by every chapter and declared by none, and the column says so. CURE, which the registry once listed as used by 3.4 to 3.7, is used by no chapter yet and the column now says "none declared."

- The section headings of the foundation documents keep sentence case, because the compiler finds their sections by heading text.
- The succession instruments named in `LICENSE.md` section 6 are not yet signed. Until they are, the open-tier grants are the steward's stated intention, as that section says.
- Twenty-six footnotes in nine chapters are written as bracketed `[footnote: …]` markers, which GitHub prints literally. The next version writes them in GitHub's footnote syntax.
- HALT is defined as a stop followed by removal of power, and three output-only principles (3.5, 3.7, 4.1) declare it. For a system with no actuator the power step has no referent, and the next version gives those declarations their output flavor.
- Six chapters (2.3, 2.4, 3.1, 3.2, 5.5, 5.6) carry threshold bullets in their bodies that name no verdict token. The `bands` check at this version reads the appendices, and the next version reads the chapter bodies too.
- Three engineering questions stand open, recorded so that a deployer does not read them as settled. The Tier II quorum of one plus an attestation that a second was unreachable (`SUBSTRATE.md` section 6) leaves the attester unnamed, and the next version names one outside the deciding party. Two latency scales share the acronym AL (1.1's life tiers and 1.3's societal tiers), resolved by principle (the glossary lists 1.1's, and 1.3's is defined in Appendix 1.3 section 3). The liability sentences of Principles 5.1 to 5.6 mix strict liability with fault conditions (preventable, negligent), which the HR5 language pass rewords as one standard.
- Article 8 permits a rank of the thing decided, built from a demonstrated skill the person knows of and can contest. Hiring is the open edge case: a skills test ranks the thing decided, and a ranking of candidates on inferred traits is a profile. The next version writes that test out, beside the clinical scores the agents page already lists.
- The two passages that cite Aristotle (the Introduction and the Lexicon's lineage note) were checked against the standard translations and have not had a classicist's reading. The author asks for one, and corrections go into the next version.

Em dashes in the corpus sit in five permitted forms and nowhere else: Convergence attribution lines, Convergence-by-Ethic and Core Precept mapping headers, verbatim quotations, published standard titles, and document or section headings. The prose rule (no em dash in running prose) holds on the release set.

### Tags and archives

- `v1.3.0` is this release, and its fingerprint is above. A tag `v1.3.0+meta.1` may follow it under the same fingerprint to carry the DOI Zenodo assigns at the release.
- Tag rule from here on: a tag of the form `vX.Y.Z` is used only when the fingerprint changes. A release that changes only tooling or documents under the same fingerprint is tagged `vX.Y.Z+label.N` (the first such tag is `v1.0.0+verify.1`). Zenodo's `version` field carries `X.Y.Z`.
- The checker (`compiled/verify.py`) checks every file the bundle and the release manifest list, and takes `--expect FINGERPRINT` so a reader can confirm the download against a fingerprint obtained elsewhere.

### Versions accepted

A claim names its version. Inside a version, nothing varies. Across versions there is a range, the way software supports a range of versions of a language. Rules will change as sensing and robotics mature, and some will change for reasons of public safety. Each change is named in this file with its reason. Every version stays on the record, and a receipt made under a version remains evidence of the rules of its time. A version may be retired from acceptance, with its reason stated here.

| Version | Fingerprint | Status |
|---|---|---|
| 1.3.0 | `2d20121b8afbf0e9…` | current |
| 1.2.0 | `79887915e0a289a7…` | accepted, superseded by this version, which amends Article 8 under Article 11, compiles cluster 1, the substrate, the credential map and the verb registry, publishes the compiler, and states the license's commercial terms |
| 1.1.0 | `c24f2438861e821f…` | accepted, superseded by 1.2.0, which clarified one sentence, corrected one verdict, and changed how a reader meets them |
| 1.0.0 | `e586a144615643f9…` | accepted, superseded by 1.1.0, which adds the emergency thresholds and the gate's rules as data, the receipt conditions, the DEGRADED posture, the wall-reached rule, and standing |

### Prior releases

- `v1.0.0`, sealed 2026-09-13, fingerprint `e586a144615643f913cfc67d6bbda439b39740a97777de63beb3d7e13574591f`, DOI 10.5281/zenodo.22743047. Tags: `v1.0.0` (the seal), `v1.0.1-meta` (the same fingerprint with citation metadata, the tag Zenodo archived, and the last tag in that form), `v1.0.0+verify.1` (the whole-tree verifier, tooling only).
- `v1.1.0`, sealed 2026-09-17, fingerprint `c24f2438861e821f21a455ddf3b47d269361ab397a50dcb93ed769c53f65cb84`, DOI 10.5281/zenodo.22822375. Tags: `v1.1.0` (the seal), `v1.1.0+meta.1` and `+meta.2` (the DOI and the release note), `v1.1.0+docs.1` to `+docs.4` (the entry pages, outside the seal).
- `v1.2.0`, sealed 2026-10-13, fingerprint `79887915e0a289a706f1d10c0e2a9883d9d9aa71b9c01bbcac9235b52c5372fb`, DOI 10.5281/zenodo.23356105 (archive SHA-256 `cff2a093c02f1fa7b38ba60b9bf0d349f65f146282182243ffa4bfce3b306f52`). Tags: `v1.2.0` (the seal), `v1.2.0+meta.1` (the DOI).
- Concept DOI for all versions: 10.5281/zenodo.22743046.

### Patch process

A defect in canon is fixed in the hub, resealed, and released as a patch version with a new hash and tag. The superseded entry stays in this file, marked superseded with the reason. Every tag stays where it was placed. Any change to the Constitution's Articles follows Article 11's amendment mechanics.
