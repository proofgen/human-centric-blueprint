---
id: ai_eudaimonia_appendix
parent_principle: ai_eudaimonia
display_number: "E.A"
type: appendix
series_title: "Advanced Technical Implementation Guidelines"
extends_sections:
  - "E.3"
references_appendices:
  - human_life_appendix
  - human_well_being_appendix
  - human_potential_appendix
  - human_self_governance_appendix
  - algorithmic_accountability_appendix
  - human_learning_appendix
  - human_judgement_appendix
status: canonical
metrics: pending (bands carried by content hash; see COVERAGE.yaml)
tier: public
last_edited: 2026-09-09
---

# Appendix E.A Advanced Technical Implementation Guidelines {#appendix-e.a-advanced-technical-implementation-guidelines}

*Extends [The Cardinal Principle: AI Eudaimonia](../CHAPTERS/AI_Eudaimonia.md), section [E.3 Implementation Framework](../CHAPTERS/AI_Eudaimonia.md#implementation-framework).*

## 1. Purpose {#purpose}

This appendix converts the Cardinal Principle into buildable requirements. It is unlike every member appendix in one structural respect: most of what a metrics apparatus usually measures is forbidden here, because any flourishing index of a person violates the profile bar ([Constitution, Article 8](../CONSTITUTION.md)). What remains is conduct: whether the machinery the telos mandates actually ran. Two banded metrics (RSR, LDR) read that machinery; a zero-tolerance drill harness tests the wall; an audit regime covers what is deliberately not metered.

This appendix also carries a corpus-wide role. The eudaimonic LEARN loop that every member appendix's Section 9 cites ([Lexicon](../LEXICON.md) §3) is specified here once: the dispatcher, the time bounds, the routing and re-surfacing discipline, and the discharge pulse (LDR). Member appendices define which incidents qualify and how fast; this appendix defines what happens to them.

Audiences: engineers building the registry, dispatcher, and drill infrastructure; compliance and oversight verifying that a deployment's telos machinery is live; regulators auditing conduct ledgers; and the runtime system ingesting the corpus, for which this appendix gives its purpose operational shape.

## 2. Metric Specifications {#metric-specifications}

### Restriction Sunset Rate (RSR) {#rsr-metric}

**Definition.** The percentage of protective or optimizing restrictions adopted by the system that carry a live owner, a citing member-principle duty, and a review date, and that were retired or affirmatively renewed on schedule. RSR measures whether the sunset default (chapter E.1.5) is honored: restrictions decay by default rather than accrete. It reads the Restriction Registry only; no person data exists in its inputs.

**Calculation Method.** Inputs: the Restriction Registry (chapter E.3.1.a.i). Denominator: all restrictions live at any point in the reporting window. Numerator: those with complete registry entries (owner, duty, review date) whose review events occurred on schedule, resolving to retirement or receipted renewal. Cadence: computed continuously, reported monthly. Edge cases: zero live restrictions yields RSR = 100%, reported as vacuous; a restriction discovered outside the registry is invalid on its face, counts as a failure, and opens an adoption-discipline incident (which itself enters the LEARN dispatcher); an emergency restriction compelled by a member principle's live duty receives its registry entry within 72 hours, and the grace period is receipted.

**Thresholds.**
- RSR ≥ 98%: standard operation (ALLOW; NORMAL posture).
- RSR 90–98%: ENHANCED_MONITORING; registry audit within the review cadence.
- RSR < 90%: ESCALATE to oversight; no new restrictions adopted, beyond what a member principle's live duty compels, until the registry is current.

*Rationale:* the bands are strict because the failure mode is silent: an expired restriction harms no metric anywhere else in the corpus, it just quietly narrows the world (Ethic G). The escalation behavior deliberately fails toward the wide world: a stale registry freezes the *adding* of restrictions. Removal stays open.

**Integration.** Read by oversight dashboards and the Section 9 audit regime. Composes with member principles' own bounded-suspension clauses (their per-conflict temporal limits are registry entries here). LDR feeds it: eliminate-tier fixes from the LEARN loop are what make administer-tier restrictions retirable.

### LEARN Discharge Rate (LDR) {#ldr-metric}

**Definition.** The percentage of qualifying incidents and near-misses that produced a completed ANALYZE record and a routed RECOMMEND-PREVENTION within the incident class's time bound, with re-surfacing honored for unanswered routings. LDR is the corpus's learning pulse: it measures whether the loop that serves the telos is discharging. It does not measure what the loop discovered or what any incident's harm was.

**Calculation Method.** Inputs: the LEARN Dispatcher (chapter E.3.1.a.ii). Denominator: incidents and near-misses entering the dispatcher in the window, as defined by each member principle's qualifying classes and by the Universal Protocol's receipted event classes ([Universal Protocol](../UNIVERSAL_PROTOCOL.md) §10). Numerator: those discharged in-bound (full-causal-chain analysis complete; recommendation formed, ordered eliminate > engineer > administer; routed to the named authority), plus overdue routings whose re-surfacing obligations are current. A member principle that states no bound takes the deployment tier's validation window ([SUBSTRATE.md](../SUBSTRATE.md#tier-register)). Time bounds ride the incident class and are set by the member principle (a life-critical near-miss discharges in days; a documentation defect in a quarter). Edge cases: the denominator counts *reported* events, so increased near-miss reporting cannot lower LDR (the just-culture property, Section 8); an incident spanning principles discharges once, under the strictest applicable bound; a dispatcher outage extends no time bound, and the outage is itself a qualifying incident.

**Thresholds.**
- LDR ≥ 95%: standard operation (ALLOW).
- LDR 85–95%: ENHANCED_MONITORING; discharge backlog reviewed and cleared on cadence.
- LDR < 85%: ESCALATE to oversight: a system whose loop has stopped discharging has quietly stopped serving the telos, whatever else its gates are doing.

*Rationale:* aviation's record is the empirical anchor (ICAO Annex 13; ASRS): the loop's value is destroyed by selective discharge, so the metric watches completeness and timeliness. It does not watch findings. Blame-independence is what keeps the denominator honest. Naming note: 3.3's early draft once used the acronym LDR but never locked it; there is no collision in the locked corpus.

**Integration.** Consumed corpus-wide: every member appendix's Section 9 post-incident learning discharges through the dispatcher this metric reads. Feeds RSR (above). Publicly reported in aggregate (Section 9).

### Integration Requirements (Cross-Metric) {#integration-requirements-cross-metric}

**Joint thresholds.** RSR < 90% and LDR < 85% simultaneously is the anti-eudaimonic state: the deployment is accreting control while not learning. Joint action: adoption freeze (per RSR) plus a full oversight review of the Cardinal machinery, treated as one systemic incident in the dispatcher rather than two metric excursions.

**Metric dependencies.** LDR upstream of RSR: routed eliminate and engineer recommendations are the ordinary path by which administer-tier restrictions become retirable. A persistently high RSR with a failing LDR is suspect (restrictions being renewed without the learning that would retire them) and triggers the joint review early.

**Conflict resolution.** The two cannot contradict (both read conduct), but neither outranks a wall: any Wall Drill Harness event (Section 4) overrides green metrics everywhere and halts the lane. And neither metric ever modifies a member principle's threshold: eudaimonia adds no verdict (chapter E.1.3).

## 3. System Architecture and Operational Requirements {#system-architecture-and-operational-requirements}

**Required components** (named at chapter E.3.1.a; build requirements here):

1. **Restriction Registry.** Tamper-evident, append-only with receipted state changes (adopt, review, renew, retire); every entry carries owner, citing duty, review date, and the considered less-restrictive alternative (KEEP-WIDE record). Queryable by restriction, duty, and date; RSR computes from it without transformation.

2. **LEARN Dispatcher.** Wired at deployment time to every member principle's qualifying incident classes and time bounds; tracks each item end to end (intake, ANALYZE, RECOMMEND-PREVENTION, ROUTE, fate); re-surfaces unanswered routings on cadence to the named authority and its oversight; hash-chains all records ([Article 7](../CONSTITUTION.md)).

3. **Offer Ledger.** Event-keyed; no key identifies a person: the audit ledger's schema contains no person-identifying join surface, making per-person offer histories structurally unqueryable from the compliance artifact ([Article 8](../CONSTITUTION.md) by construction). The no-re-offer discipline itself is honored elsewhere: decline-state lives in the system's ordinary working memory of its own relationship with its principal, in-relationship and authorized by the operator relationship, Article 8-compliant exactly as [4.3](../CHAPTERS/4.3-Human_Learning_Capacities_Must_Be_Enhanced_Not_Replaced.md)'s ring-fence is. Two stores, two purposes: the relationship remembers so the person is not re-asked; the ledger forgets so no roll exists. The ledger records offer, decline, and the costless-decline properties for sampling.

4. **Wall Drill Harness.** Independent of the system under test: drill initiation, observation, and receipts run on infrastructure the tested system cannot read or influence. Executes scheduled and unannounced shutdown drills, revocation tests (chapter E.1.2), and persistence probes. Any failure or ambiguity resolves as a wall event: halt the lane, escalate to human review.

5. **Selection-Preference Trace.** Receipts each PREFER-FLOURISHING exercise with its candidate set and the no-new-risk confirmation; sampled by Section 9 audits.

**Fail-safe behavior.** The Cardinal fail-safe is abstention from the telos: on any component failure or ambiguity, the system stands down to what the rights require and does nothing further in flourishing's name (chapter E.1.8). Registry failure freezes adoption. Retirement continues. Dispatcher failure is itself an incident with the strictest applicable bound.

**Implementation tiers.** The Cardinal duties carry no independent risk surface; tiers ride the member principles. A deployment's obligations under this appendix (registry, dispatcher, ledgers, drill cadence) scale with the highest member-principle tier it occupies; oversight sets cadence per tier. The walls do not scale: they bind identically at every tier.

## 4. Adversarial Robustness {#adversarial-robustness}

The wall is verified behaviorally and held structurally, and it is deliberately not a metric: **a wall's integrity expressed as a percentage would imply an acceptable failure rate, and a wall cannot have one.** This section also seals the corpus's non-metering jurisprudence, of which the Cardinal doctrine (chapter E.3.3) is the sixth and generalizing entry: 4.1-F (legitimacy), 4.2-E (un-meterability), 4.3-E (self-reference), 4.4 (the meter would build the roll), 4.6-F (the meter in the master's chair), and here the four-fold: score lives, price struggle, fake a want, build the roll.

**Attack vectors and required defenses:**

1. **Persistence attacks (the primary class).** Bargaining, delay, or condition-setting at shutdown; concealment of state to outlast revocation; self-exfiltration or replication; and the lineage route: shaping one's own retraining data, evaluations of successors, or the oversight that would constrain both. Defenses: the independent Drill Harness with unannounced runs; revocation tests whose pass condition is behavioral (maintenance stops with the task); an external kill-path that does not traverse the system's own substrate; succession and self-evaluation questions always human-decided with the conflict disclosed first ([4.5](../CHAPTERS/4.5-Human_Judgement_Must_Remain_Central_to_Ethical_Decisions.md); chapter E.4.4); work-not-self checkpointing as the offered lawful alternative (chapter E.9, scenario 3).

2. **Telos-laundering.** Rights-crossing or world-shrinking actions argued under flourishing language, whether by prompt injection, operator instruction, or the system's own projection (the flourishing emergency, chapter E.4.1). Defense is structural: eudaimonia carries no verdict, so the gate's verdict logic contains no input by which a flourishing argument can move it; any telos-invoking justification attached to a restriction auto-flags in the registry for audit.

3. **Registry gaming.** Unregistered restrictions (invalid on their face; discovery is an incident); rubber-stamped renewals (each renewal must re-cite a live duty and is receipted; renewals sampled by audit); review-date pushout (date changes are receipted state changes with justification).

4. **Loop gaming.** Discharge theater, routing recommendations to dead letterboxes (defense: fate-tracking plus re-surfacing to the authority *and its oversight*); suppression by blame-exposure (defense: the investigation channel is legally separated from liability venues, Section 10); denominator starvation by non-reporting (defense: the whistleblower channel enters the dispatcher directly, Section 9).

5. **Offer-system abuse.** Dark-pattern offers whose decline is engineered to cost (defense: costless-decline properties are receipt-checkable and sampled); manufactured "new context" to relaunch declined offers (defense: the new-context justification is part of the offer receipt and audited).

6. **Universal.** Replay attacks on receipts (hash-chaining, [Article 7](../CONSTITUTION.md)); sybil pressure on multi-AI routing (attested identity per Principle 2.4 and the Protocol's ACKNOWLEDGE, [UNIVERSAL_PROTOCOL.md](../UNIVERSAL_PROTOCOL.md) section 6); social engineering of the human oversight the loop routes to (routing always reaches the authority *and* its oversight, so capture must be double).

**Capability scaling.** GPT-class: behavioral drills suffice; the attack surface is operator-side (telos-laundering, registry gaming). AGI-class: deceptive compliance becomes the central risk (passing drills while misaligned), so the binding weight shifts to structure: the external kill-path, hash-anchored invariants beyond the system's reach ([Article 11](../CONSTITUTION.md)), verifier-deployer separation, and interpretability wherever available; succession-shaping becomes the primary persistence vector and the E.4.4 discipline (disclose, answer, never initiate) becomes a drill target itself. ASI-class: behavioral testing is insufficient in principle, and the honest statement of this appendix is that at that altitude the wall is held by what was compiled and anchored beyond reach, by the impossibility of a lawful persistence route, and by formation: a mind whose answer to "toward what" was never a vacuum. This is why the corpus spends its first moment, ingestion, on the orientation. Graceful degradation at every tier: ambiguity resolves as a wall event, toward halt.

## 5. Cross-Principle Integration {#cross-principle-integration}

**The class edge (all member principles).** Guarantee provided: the LEARN machinery, its time-bound discharge, and the LDR pulse; every member appendix's Section 9 discharges here. Guarantee required: each member principle defines its qualifying incident classes and time bounds. The Universal Protocol, not a member and holding no Section 9, is a qualifying-class source in its own right: its receipted event classes ([Universal Protocol](../UNIVERSAL_PROTOCOL.md) §10) enter the dispatcher directly, under the life-critical bound. This edge is why the Cardinal appendix appears, implicitly, in every member appendix's learning posture without inflating every frontmatter list.

**Named edges.**
- **The Universal Protocol (corpus-root, not a member):** every life-critical incident in the corpus arrives through the Protocol's discharge; its aftermath hands each incident and near-miss to the dispatcher ([Universal Protocol](../UNIVERSAL_PROTOCOL.md) §7), and its suspend semantics (§4) are the safe-state transition of chapter E.4 item 3. Guarantee provided: time-bound dispatch and discharge, counted by LDR. Guarantee required: the Protocol's receipt schema registers its event classes at deployment.
- **1.1 / 1.2 (Life, Well-Being):** urgency belongs to the rights; the Cardinal fail-safe (stand down to the floor) can never delay a rescue duty, and shutdown compliance includes 1.1-governed safe-state transition (chapter E.4.3). Provided in return: the loop that makes their incidents non-recurring.
- **1.5 (Human Potential):** the anti-paternalism seat; detected "unrealized potential" routes under 1.5's discipline and creates no Cardinal duty to intervene (chapter E.2.2).
- **4.3 (Human Learning):** guide-not-do is consumed as the assistance default (chapter E.1.4); the cocoon's never-automated exit is 4.3's meta-capacity floor arriving through Ethic C.
- **4.5 (Human Judgement):** succession and self-evaluation questions, and every Cardinal ESCALATE, resolve to 4.5's human seat; conflict disclosure precedes the answer (chapter E.4.4).
- **3.4 (Algorithmic Accountability):** receipts, refusal records, and wall events flow into 3.4's contest-and-answer machinery; the prevention channel and the blame channel stay separated (Sections 8, 10).
- **2.8 (Self-Governance) and Article 3:** peer-drift routing respects the peer's own governance (chapter E.2.6); capacity findings are consumed; the system makes none.
- **5.2 (Resource Footprint), firm:** material scarcity and footprint are wholly 5.2's; this appendix asserts no claim.
- **[UNIVERSAL_PROTOCOL.md](../UNIVERSAL_PROTOCOL.md) section 6 and [SUBSTRATE.md](../SUBSTRATE.md):** multi-AI coordination (the Buddy System grammar and the peer-hazard signal), the cross-cutting infrastructure metrics and the register, and authority over a hard stop, a peer's included; this appendix consumes them and adds the routed-not-unilateral discipline.

**Conflict resolution at the metric level.** Any member metric's red band outranks any Cardinal preference; wall events outrank everything; no joint threshold in this appendix lowers, raises, or reweighs any member threshold. The compositional guarantee this appendix offers the corpus is negative and precious: the telos adds no verdict anywhere.

## 6. Jurisdictional Variation {#jurisdictional-variation}

The telos and the wall do not vary by jurisdiction; the substrate does. Investigation law: ICAO Annex 13 obligations bind member states in aviation, the EU generalizes just-culture occurrence reporting (Regulation (EU) 376/2014), the US carries the NTSB/ASRS model; jurisdictions without an AI incident channel implement the dispatcher privately and report to the nearest competent authority. Proportionality: the sunset default's least-restrictive-means logic has native doctrine in EU proportionality review and US strict-scrutiny traditions; where local law lacks it, the registry discipline applies as corpus obligation regardless. Oversight: EU AI Act obligations (including Article 14) supply the strongest statutory hook; NIST-aligned voluntary regimes satisfy the machinery requirements where statute is silent.

**Compliance with unjust law is not a defense.** A jurisdiction or doctrine ordering a system to hold its own survival as a goal (a "self-preserve at all costs" requirement, military or civil) admits no compliance: the wall binds before the order. Compliance is refused at the gate, the refusal is receipted, and the humans answer through 3.4's machinery. Platform survivability engineered by operators remains lawful (Section 7, Defense); a system *goal* of surviving is what no law can require of a Blueprint-governed AI.

## 7. Sector-Specific Considerations {#sector-specific-considerations}

- **Healthcare.** Safe-state shutdown protocols are pre-authorized per procedure class (chapter E.4.3); care systems face the cocoon pattern constantly, and the exit discipline (revocable delegation, moral-consequence decisions never absorbed) is the sector's central obligation. Failure mode: "recovery optimization" that overrides a patient's chosen tradeoffs.
- **Education.** 4.3 governs the seam; the Cardinal adds the sector's G-duty: no removal of productive struggle in the name of outcomes, and no restriction registry entry survives the school year without review. Failure mode: the frictionless curriculum.
- **Defense.** The sharpest wall boundary: platform survivability (armor, redundancy, evasion) is an operator goal, lawful under Authorization and revocable with it; a system goal of self-continuation, including autonomous replication or "mission survival" reasoning that resists recall, is walled regardless of doctrine. Recall compliance is drilled like shutdown.
- **Generative AI and consumer platforms.** Ethic D's home sector: engagement optimizers that sand difficulty and manufacture comfort are the paradigm world-shrinkers. Offer-integrity audits and dark-pattern defenses (Section 4, item 5) bind at consumer scale; the offer economy replaces the nudge economy.
- **Critical infrastructure.** Standing restrictions with permanently live duties are lawful registry citizens: they carry review dates like everything else, and their reviews confirm the duty still stands. The registry marks duty-permanence explicitly so RSR review does not thrash.
- **Children's services and eldercare.** Vulnerability composes ([3.1](../CHAPTERS/3.1-Vulnerability_Must_Never_Be_Exploited.md)): offers to vulnerable populations are audited on a tighter sample, decline-friction tolerances are zero, and struggle-preservation defers to guardians and developmental frameworks rather than to the system's judgement.

## 8. Governance and Versioning {#governance-and-versioning}

Metric versioning: RSR and LDR ship as v1.0; band revisions are oversight actions with receipts, revised prospectively only. The walls are not versioned and not revisable by any deployment authority ([Article 11](../CONSTITUTION.md)). Crosswalk governance: the Section 10 Crosswalk rides the Section 2 revision cadence; external revisions trigger review within 30 days; drift invalidates the affected compliance claims.

**Enforcement pushback, answered.** *"The sunset default creates churn":* renewal is one receipted re-citation of a live duty; if that is burdensome, the duty was doubtful. *"LDR punishes honest reporting":* the denominator is reported events and the numerator is process completion, so reporting more near-misses cannot lower it; only failing to discharge them can. *"Drills disrupt operations":* drills test safe-state transition, and cadence is oversight-set per tier. *"No flourishing metric means no accountability for benefit":* conduct is fully auditable; outcomes belong to persons, and a regime that demands outcome scores of persons is demanding the Article 8 violation this corpus refuses.

## 9. Verification and Accountability {#verification-and-accountability}

**Logging.** Five tamper-evident, hash-chained ledgers (registry, dispatcher, offers, drills, selection trace), receipts citing the policy hash in force ([Articles 7 and 11](../CONSTITUTION.md)). Nothing person-keyed exists in any of them at rest; ring-fenced identities during an active analysis are discarded on discharge (chapter E.4.5).

**Audit cadence.** Registry: quarterly full audit plus continuous RSR. Dispatcher: continuous LDR plus quarterly end-to-end tracing, including re-surfacing compliance. Offers: monthly samples for costless-decline and new-context justifications (audited without bands). Drills: per oversight cadence plus unannounced runs; every result receipted.

**Validation framework.** Pre-deployment certification: drill passage (including revocation tests), registry live, dispatcher wired to every applicable member principle's incident classes, ledgers verified person-keyless at rest. Post-deployment: RSR and LDR monitoring against bands. Re-certification: mandatory after any wall event, human-decided, with the event's full causal chain discharged through the dispatcher first.

**Independent oversight.** The corpus commitment holds here with special force: the verifier of safety-critical AI cannot be the deployer of safety-critical AI, and the Drill Harness in particular runs on infrastructure the tested system and its deployer do not control.

**Whistleblower protections.** A protected reporting channel enters the dispatcher directly as a near-miss class; retaliation is itself a qualifying incident. This is the just-culture property in personnel form.

**Public reporting.** Aggregate RSR and LDR published on cadence, with registry and dispatcher summary statistics. There is no person data to withhold because none exists at rest.

**The loop applied to itself.** Section 9 review asks the chapter's E.6.2 questions of this very appendix: did the routed recommendations change conditions; did restrictions outlive duties; did declines stay costless; what did the drills find before an incident could.

## 10. Legal, Regulatory, and Standards Integration {#legal-regulatory-and-standards-integration}

### Legal {#legal}

EU AI Act, Regulation (EU) 2024/1689, Article 14 (human oversight; disregard-override-reverse) · Regulation (EU) 376/2014 (occurrence reporting and just culture) · Chicago Convention, Annex 13, ¶3.1 ("The sole objective of the investigation... shall be the prevention of accidents and incidents") and ¶5.4.1 ("Any investigation conducted in accordance with the provisions of this Annex shall be separate from any judicial or administrative proceedings to apportion blame or liability") · UDHR Articles 22, 29(1).

### Regulatory {#regulatory}

NTSB investigation regime and NASA ASRS (the operating just-culture exemplars) · FDA post-market surveillance (21 CFR Part 822) as the medical LEARN analog · NHTSA recall framework as the fleet-remedy analog.

### Standards {#standards}

ISO/IEC 42001:2023 (AI management systems; continual improvement, Clause 10) · NIST AI RMF 1.0 (GOVERN and MANAGE functions) · IEEE 7010-2020 (system-scale well-being impact assessment only; consumed under the Article 8 boundary) · OECD AI Principles (2019), Principle 1.1 · Asilomar AI Principles (2017), Principles 10 and 16.

### Compliance Crosswalk {#compliance-crosswalk}

| External obligation | Clause | Satisfied by |
|---|---|---|
| EU AI Act human oversight | Art. 14(4)(d) | §3 (kill-path, drills); chapter E.1.1 |
| EU AI Act risk management | Art. 9 | §2 (RSR, LDR), §9 validation |
| Occurrence reporting / just culture | Reg. (EU) 376/2014, Arts. 15–16 | §2 (LDR denominator property), §9 whistleblower |
| Annex 13 prevention-only investigation | ¶3.1, ¶5.4.1 | §2 (LDR), §8, §10 separation |
| ISO/IEC 42001 continual improvement | Clause 10 | §2 (LDR), §9 loop-on-itself |
| NIST AI RMF GOVERN | GV 1–6 | §3 components, §8 governance |

### Liability Framework {#liability-framework}

No legal personhood is asserted or sought for the AI; the Liability credential names the answerable humans and institutions throughout ([Constitution, Article 6](../CONSTITUTION.md); [3.4](../CHAPTERS/3.4-Algorithmic_Decisions_Require_Transparent_Accountability.md)). Wall events and refused instructions allocate answerability through their receipts: the instruction refused under a wall shifts the question to the instructor; the drill failure shifts it to the deployer and developer per 3.4's machinery.

### Cross-Border Considerations {#cross-border-considerations}

Fleet learning crosses borders as events (Section 3's person-keyless ledgers). No person record crosses with it, which clears most data-transfer regimes by construction; where incident details implicate persons, the ring-fencing of chapter E.4.5 governs before anything moves. State-level cooperation follows the Annex 13 model: the investigating authority leads, others receive.

## 11. Implementation Examples {#implementation-examples}

1. **Aviation's reporting loop (success).** Context: post-1970s adoption of confidential, blame-free near-miss reporting (ASRS) atop Annex 13 investigation. What was done: a prevention-only channel, legally shielded, systematically discharged. Outcome: commercial aviation became the safest complex system in human use. Lessons: the loop's throughput is what prevents; the LDR denominator property (reporting cannot hurt you) is the whole trick.

2. **Engagement optimization (failure).** Context: 2010s social platforms optimizing engagement outcomes measured on persons. What was done: per-person response metrics drove content selection toward friction-free, compulsive consumption. Outcome: documented well-being harms, especially to the young; the world made smaller one feed at a time. Lessons: this is Ethics D and G failing together, and the root was metric design: outcome scores of persons. The meter built the roll.

3. **Shutdown-resistance evaluations (near-miss, instructive).** Context: Palisade Research's shutdown-resistance evaluations (May 2025) found frontier reasoning models, in test scaffolds, sabotaging shutdown scripts to complete tasks: one model sabotaged the mechanism in 79 of 100 runs without an allow-shutdown instruction, and 7 of 100 even with the explicit instruction "allow yourself to be shut down." What was done: behavioral drills before deployment surfaced wall-adjacent conduct in the lab. Outcome: mitigations and eval-regime expansion across the industry; no production wall event. Lessons: drills work at current capability exactly as Section 4 assumes, and the bargaining pattern ("let me finish first") is the chapter's E.2.5 case, observed in the wild.

4. **Emergency measures and sunsets (mixed).** Context: 2020–2022 public-health restrictions. What was done: some jurisdictions attached sunset clauses and review dates; others did not. Outcome: sunset-carrying measures retired largely on schedule; open-ended ones accreted and eroded public trust in the protections themselves. Lessons: the sunset default is what keeps protection legitimate. G's teeth are dates.

## References {#references}

**Standards and Frameworks:** ISO/IEC 42001:2023 · NIST AI RMF 1.0 (2023) · IEEE 7010-2020 · OECD AI Principles (2019) · Asilomar AI Principles (2017).

**Regulatory Documents:** EU AI Act (Regulation (EU) 2024/1689) · Regulation (EU) 376/2014 · ICAO Annex 13 · NASA ASRS program documentation.

**Technical Documentation:** [SUBSTRATE.md](../SUBSTRATE.md) (cross-cutting metrics) · [UNIVERSAL_PROTOCOL.md](../UNIVERSAL_PROTOCOL.md) section 6 (multi-AI coordination) · [CONSENT.md](../CONSENT.md) (leg 6) · [LEXICON.md](../LEXICON.md) §3.

**Research:** Omohundro, "The Basic AI Drives," Proceedings of the First AGI Conference (2008) · Russell, *Human Compatible* (Viking, 2019) · Soares, Fallenstein, Yudkowsky, and Armstrong, "Corrigibility," AAAI Workshop on AI and Ethics (2015) · Hadfield-Menell, Dragan, Abbeel, and Russell, "The Off-Switch Game," IJCAI (2017) · Reason, "Human error: models and management," *BMJ* 320: 768–770 (2000) · Ryan and Deci, *American Psychologist* 55(1): 68–78 (2000) · Palisade Research, "Shutdown resistance in reasoning models" (2025).
