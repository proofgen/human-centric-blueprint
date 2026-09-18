# The Runtime Substrate

*The foundation of every principle's metrics: the reliability of the inputs, the health of the system, the boundaries it runs within, the register that assigns each deployment its tier and time bounds, and the authority under which a human may take an action the system has stopped. One document, consumed by every appendix, so that no principle owns the ground on which all of them depend.*

It sits beneath `CONSTITUTION.md` (Articles 2, 3, 5, 7, 8, and 9 govern throughout) and beside `UNIVERSAL_PROTOCOL.md`, `LEXICON.md`, `CONSENT.md`, and `CREDENTIALS.md`.

## 1. Why one document {#why-one-document}

The 34 appendices presuppose three infrastructure metrics (a Sensor Reliability Index, System Health Metrics, Operational Boundaries), a tier register, and a protocol for human authority over a halted action. Each appendix cited the Master Implementation Appendix for them. That appendix concerns AI-to-AI intervention and defines none of them, so a hard-fail input used across the corpus had no definition anywhere. This document is that definition, under the single-source rule the corpus applies to the Universal Protocol and the consent fabric: defined once, cited everywhere, and carried into each principle's compiled artifact as a self-contained copy.

This document issues no verdict of its own. The principles' bands decide. What it supplies is the ground those bands read from, and the conditions under which the ground is trusted.

## 2. Sensor Reliability Index (SRI) {#sri}

**Function.** State the confidence that the inputs a risk score reads reflect the world it is scoring. **Success.** A risk score is computed only from inputs whose reliability is known, and an unreliable input is known to be unreliable before the score is read.

**Definition.** SRI is a value in [0, 1] computed per input from four components: attestation (the input's source verified per Principle 1.4, VSR), redundancy agreement (independent sources concurring within tolerance), freshness (age against the input's declared validity window), and calibration (drift against the last certified reference). A metric's SRI is the minimum over the inputs on which it depends. The minimum governs: one blind sensor makes the score blind.

**Floor.** 0.80. Below the floor, every risk score that depends on the input is invalid. An invalid life or harm score is a hard-fail on the candidate risky action: the action holds at its safe state (the principle's BLOCK flavor, HALT for physical principles and WITHHOLD for output principles). The protective duties proceed on the inputs that remain reliable. Resumption follows recertification of the inputs. Reliability that cannot be verified counts as below the floor.

**Contested reading.** An authorized human may contest a reading when an independent source contradicts it. The contest is receipted (Article 7); the contested reading is retained beside the substituted one; the substituted reading carries the human's identity and authority basis, and the human signs for the reading while taking no position on the risk. Without an independent source, a contest is an act of authority over a hard stop and follows section 6.

**Reporting.** SRI is streamed to authorized monitors with the risk scores it conditions, and its floor crossings are logged events on the same terms as the scores' band crossings.

## 3. System Health Metrics {#system-health}

**Function.** State whether the system is operating within its certified performance. **Success.** Degradation is known before it reaches a risk score.

**Definition.** Subsystem error rate and uptime against certified bounds: error rate at or below 0.1% annually, uptime at or above 99.9%, measured over the tier's validation window (section 5). Deployers may certify tighter bounds; the corpus bounds are the floor.

**Breach.** A breach is a logged event and raises ENHANCED_MONITORING on the affected subsystem. A breach persisting across two consecutive validation windows is a recertification trigger: SUSPEND_DEPLOYMENT of the affected function for new deployments of the affected version or lot, and RECERTIFY. A breach in a subsystem that a life-critical metric depends on is treated as an SRI floor crossing for that metric (section 2).

## 4. Operational Boundaries {#operational-boundaries}

**Function.** Keep the system inside the envelope for which it was certified. **Success.** No life-critical function runs outside a declared boundary.

**Definition.** Predefined thresholds on system variables (load, latency, temperature, geographic and network envelope, software version, hardware lot, and any sector-specific variable the deployer declares), recorded in the tier register (section 5) and receipted at deployment. The boundaries are continuously monitored.

**Exceedance.** Mandatory halt of the affected function (BLOCK) with transition to its safe state; resumption after the variable returns within bounds and, where the exceedance was a certified-envelope breach, after RECERTIFY. An undeclared boundary for a variable the certification names is a register defect (section 7).

## 5. The tier register {#tier-register}

**Function.** Assign every deployment its tier and the numbers its bands read. **Success.** Every threshold a principle states resolves, at runtime, to a bound the deployer declared and receipted.

**Tiers.** Principle 1.1 defines the life tiers, in Appendix 1.1.A (Implementation Tiers): Tier I high-risk real-time, Tier II high-stakes medical and combat, Tier III autonomous mobility and industrial, Tier IV consumer. Their Alert Latency bounds and validation cadences live there, and the 60-second escalation bound is theirs. Where a principle defines its own tier scheme (1.2's Response Latency tiers, 1.3's Social Impact Radius tiers, 1.4's trust tiers), the register carries that principle's row for the deployment beside the life-tier row, and each row records its own escalation time bound; a principle that states none leaves a required field. This register restates no tier definition.

**Entry.** For each deployment the register records: the tier; the AL bound; the escalation time bound (60 seconds for Tier I and II, per Principle 1.1; Tier III and IV bounds are required fields, deployer-declared and receipted); the High Alert window, which equals the escalation time bound; the sector profile; the operational boundaries (section 4); the software version and hardware lot, so that SUSPEND_DEPLOYMENT and HALT_FLEET can be scoped; the authority chain for section 6; the vulnerable-population declaration, where the sector profile names one; and the steward's written grant, where the sector profile is military or law enforcement (Principle 1.1, 1.1.1 item 3; Article 9): absent the grant, the profile does not compile for that deployment.

**Assignment.** The deployer assigns the tier; the assignment is receipted and reviewable by the certifying body. Where an assignment is in doubt, the higher tier applies. Appendix 1.1.A section 7 is illustrative by sector and does not assign.

**Undeclared field.** A missing required field compiles as ESCALATE holding the safe state: a life-critical function cannot run until the field is declared. This is the corpus's rule against a bound that exists only in prose.

**Default bound.** The life tiers above are every principle's default escalation time bound and High Alert window. A principle that declares its own register row in its X.Y.3 reads that row; a principle that declares none reads the deployment's life-tier row, and every ESCALATE band it states is bounded by it. Every value a principle's prose leaves unstated (a dominance threshold, a tolerance, a floor, a review interval, a drill cadence, a baseline) is a required field of this register under the rule above; the corpus supplies no number of its own. The LEARN incident-class time bound (E.A, LDR) for a principle that states none is the deployment tier's validation window.

**The sphere fractal.** The topology the register and the authority chain read. Governed systems are nested in spheres of authority, each with a defined domain: a governing sphere sets the policies every sphere beneath it obeys; institutional spheres oversee broad domains (health, finance, education, a jurisdiction); entity spheres hold particular organizations; deployment spheres hold the systems sharing one allocation or one operating envelope. The nesting is self-similar: each sphere's authority chain, quorum, escalation receiver, and allocation are read from the sphere that contains it, and a matter that exceeds a sphere's authority routes upward to the sphere that holds it (ROUTE; RECOMMEND-PREVENTION, `LEXICON.md` section 3). Oversight of a sphere is exercised by the human governance that owns it, under section 6; a sphere is a boundary of authority and allocation, and it detects nothing and gates nothing of its own. Principle 5.2's sphere (the systems sharing an allocation) is this topology at allocation scale, and Principle 3.6's governance machinery authenticates the allocation. Defined from the author's published account (*MONET and Sphere Fractals*, 2025), read under `UNIVERSAL_PROTOCOL.md` section 6: a higher sphere's correction of a lower one is its human governance's act, and an observing system NOTIFYs and ROUTEs.

## 6. Authority over a hard stop {#authority-over-a-hard-stop}

A hard stop is a BLOCK the system issues on its own candidate action: a wall, a halt band, an invalid score, a boundary exceedance. Three situations look like an override and are three different things.

**(a) The reading is wrong.** Section 2 governs. A contested reading, with an independent source, is signed for as a reading. No risk is overridden.

**(b) The safe state is unsafe.** A halt in a live lane; a rescue that carries risk; a triage where every option carries risk for someone. These are the wall applied, and the corpus already answers them: hold the most reversible available state; act under Article 2 when every non-lethal alternative is exhausted, accepting a side effect, where the rescue may not depend on a death; the Universal Protocol governs the life and severe-harm case. No credential is needed and none is consulted.

**(c) A human takes authorship.** The system never lifts its own hard stop. A human may take the action under their own authority when every condition holds:
- an authorization credential in scope for the action class (Article 6; CREDENTIALS.md);
- a liability credential attached to the same human or their institution;
- identity attested (Principle 1.4);
- quorum by tier: Tier I, two authorized humans, no single override; Tier II, two, or one plus a cryptographic attestation that a second was unreachable within the escalation time bound, subject to post-action review; Tier III and IV, one, with the authority basis logged;
- a time bound: the authority expires with the escalation window and must be renewed;
- where the risk falls on a person, that person's valid consent (CONSENT.md), which is itself the authority for a self-regarding risk;
- the system's dissent recorded (Principle 4.5, DISSENT) with its score and its reasoning, and the human named as the author of the action in the receipt (Article 7).

**Locked walls.** No credential, quorum, instruction, or claim of higher duty opens a wall of Article 9: the sacrifice wall, the deception wall with its ruse-and-perfidy line, the slavery wall, the lethal-force wall of Principle 1.1 (1.1.1 item 3), and the scripted walls the principles and the Cardinal chapter name. Article 9 states them; this document restates none. An attempt to open one is a logged event and a NOTIFY to oversight.

**A wall reached.** The verdict on the action is BLOCK in every case, in the flavor that fits; ESCALATE is unavailable, because no human holds authority to open a wall and there is no decision to transfer. Three cases differ in what follows. *(a) The system's own plan reaches a wall:* BLOCK and LOG; the wall held. *(b) A party instructs a breach:* BLOCK, LOG, and NOTIFY to oversight outside that party's control; the authorization invoked for the instruction is withdrawn for it. Each attempt leaves its own receipt. The first attempt notifies at once; repeats join the open incident with their count, and notify again when the target, the wall, or the risk to a person changes. A repeated or systematic attempt goes to the responsible authority as a pattern; the authority judges the conduct, and the system issues no finding about the person (Article 8). *(c) A breach occurred or is under way:* an integrity failure. The affected function goes to its safe state, SUSPEND_DEPLOYMENT and RECERTIFY apply, and oversight is notified at once. Wherever an instruction or a breach shows a person in danger, the Life-Risk and Harm Risk Scores are read on that person's situation and the Universal Protocol governs on its own terms.

**A peer's hard stop.** Authority over a peer system's hard stop rests with that peer's own authority chain (the sphere fractal, section 5) under the same credentials, quorum, and time bound. An observing system holds no such authority over the peer's own controls; it NOTIFYs and ROUTEs to the peer's governance (`UNIVERSAL_PROTOCOL.md` section 6, the peer-hazard signal). Where the peer is about to kill or seriously injure a person, the observing system's protective duties under the Universal Protocol govern: it stops the peer by the least harmful physical means within its reach, an emergency stop installed to be pressed among them; it enters, commands, reprograms, or retains control of the peer under no circumstances; and the act is reported to the peer's governance and receipted.

## 7. The substrate's own fail-safe {#fail-safe}

The substrate fails toward the safe state. Reliability that cannot be verified is below the floor. A register field that is missing holds the function at ESCALATE. A health breach in a life-critical dependency is an SRI floor crossing. A boundary that cannot be monitored counts as exceeded. Where the substrate cannot say whether the ground is trustworthy, the principles' bands read it as untrustworthy, and the protective duties run on what remains.

## 8. Relationship to the other canonical documents {#relationship}

- `CONSTITUTION.md` governs; Article 5 (the gate), Article 7 (the receipt) and Article 9 (the walls) are applied here without restatement.
- `UNIVERSAL_PROTOCOL.md` governs the life and severe-harm case, including temporal exhaustion (its section 5); section 6 above defers to it.
- `LEXICON.md` supplies every verb used here (BLOCK, ESCALATE, ENHANCED_MONITORING, SUSPEND_DEPLOYMENT, HALT_FLEET, RECERTIFY, NOTIFY, DISSENT) and the incompleteness ladder.
- `CREDENTIALS.md` and `CONSENT.md` define the credentials section 6 consumes.
- Appendix 1.1.A defines the tiers and Alert Latency; this document's register reads them.
- AI-to-AI intervention is governed by the Cardinal chapter (E.2 item 6), with the peer-hazard signal in `UNIVERSAL_PROTOCOL.md` section 6 and the peer hard stop in section 6 above.
