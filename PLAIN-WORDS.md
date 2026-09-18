# The spine, in plain words

*Version 1.1.0. One paragraph for each document that every chapter depends on, then a glossary of every metric name the chapters use. This page sits outside the seal and adds no rule. Where it and a document disagree, the document governs.*

## The documents

**CONSTITUTION.md.** Eleven articles, the supreme law. Who it protects (every person), what a machine must do first (preserve life), how it must treat a person's own choices (presume capacity, consume a court's finding, make none of its own), which duty wins when two collide, that every consequential action passes a gate and gets one of three answers, the five things that must be in order before an action proceeds (who acts, where the content came from, what was permitted, what the agent may do, who answers for harm), the receipt every decision leaves, the ban on profiling people, the walls no authority can open, what the whole thing is for, and how it may be amended (by human governance alone; the machine cannot amend its own law).

**UNIVERSAL_PROTOCOL.md.** The emergency rule. When a life is at risk or serious harm is near, this document takes over before any principle is consulted. It says exactly when that trigger fires (two numbers, compiled from chapters 1.1 and 1.2), what the machine does then (warn, stop, call for help, hand off, record), how machines coordinate with each other in an emergency, what happens when there is no time to reach a human, and how the machine stands down afterward. The trigger and the handler are compiled data; the values live in the chapters and are checked against the appendices at every build.

**LEXICON.md.** The vocabulary of action, so that thirty-five chapters mean the same thing by the same word. The three verdicts (allow, escalate, block) and the test that decides between them; the postures a running system can be in (normal, enhanced monitoring, high alert, degraded); the obligations (warn, notify, intervene, route, and the rest), each defined by what it accomplishes rather than how; the two receipts (the one written before the act, the one written after) and their states; what to do when no rule fits (reason from the duty, escalate, hold the safe state, record). Section 9 is the registry: every verb, defined once.

**CONSENT.md.** What makes a permission real. A consent is valid only if all seven of these are false: the person could not be identified; they lacked capacity or were forced; they were deceived; they were manipulated; they had no real chance to understand; they were asked for more than they could judge; or the permission was extracted as the price of an essential service. Any one failing makes the consent void, and void consent permits nothing. Whoever relies on a consent carries the burden of showing it was valid; the person carries no burden to prove it was not.

**CREDENTIALS.md.** The five credentials the gate checks, and which chapter speaks for each: Identity (2.4), Provenance (1.4 and 3.2), Consent (2.4 with the seven legs), Authorization (2.8), Liability (3.4). A consequential action with any credential unmet is blocked or escalated. When another machine asks this one to act, the same credentials are checked on the asker.

**SUBSTRATE.md.** The ground the principles stand on. How reliable the machine's inputs are (a reliability value per input; below the floor, a score that depends on that input is invalid and the action holds); how healthy the system is; the boundaries it may operate in; the tier register, where a deployment declares its risk tier and how fast a human must be reachable (a missing field holds the function at escalate); and what happens when a human wants to take responsibility for an action the machine has stopped (it can, with credentials, quorum and a time bound; the walls it cannot open). Section 6 also says what follows when a wall is reached: block in every case, oversight told, and an actual breach treated as a failure of the system itself.

**CROSS_PRINCIPLE.md.** Which principles need which. A principle may declare that another must hold for it to hold; the compiler builds the graph and checks it has no cycles. Seven principles form the consent bundle and fifteen more inherit it.

**The Cardinal chapter, AI_Eudaimonia.** What the whole thing is for: human flourishing, and what it means for a machine to do its work well in service of that. It also carries the learning loop, so every incident teaches the next version.

**The thirty-four chapters and their appendices.** Each chapter states one principle: what it protects, what harm it prevents, how the harm is measured, what the machine does at each level of risk, and what the chapter refuses to do. Each appendix specifies the chapter's measurements in detail. The chapter states; the appendix specifies; where they disagree on a number, the build stops until they agree.

**LICENSE.md.** The text may be shared and quoted and translated and may not be altered. Running the architecture is free for non-commercial and public-interest deployments and licensed on published terms for commercial ones. Checking a fingerprint or a receipt is free to everyone. Three claims exist (reads, conforms to, enforces), and each requires what it names.

## Why the deception wall permits a ruse

The wall protects those who rely on the machine: the people it serves, its oversight, the record, and anyone trusting its identity claims. A lawful adversary in a receipted, time-bounded operation under human authority relies on none of these. A ruse toward that adversary breaches no one's reliance; feigning protected status, impersonating a real person, or lying to oversight or to the record always does.

## Glossary of metric names

Every metric name the chapters define, with the chapter that defines it. Generated from the chapters at build time. Two chapters may use the same letters for different measures; both are listed.

| Letters | Name | Chapter |
|---|---|---|
| AAI | Authenticity Assurance Index | 2.4 |
| AAM | Agency Assurance Metric | 1.5 |
| ACI | Attachment Cultivation Index | 2.6 |
| AFC | Absolute Footprint Cap | 5.2 |
| AFP | Autonomy-Floor Preservation | 2.8 |
| AII | Accounting Integrity Indicator | 5.1 |
| AIS | Attribution Integrity Score | 3.2 |
| AL | Alert Latency | 1.1 |
| ALI | Account-Label Integrity | 4.7 |
| ARI | Autonomy Respect Index | 3.1 |
| ARR | Affordability Routing Ratio | 3.5 |
| ATI | Advisory Transparency Index | 2.8 |
| AVR | Authorization Validity Rate | 2.8 |
| BDR | Burden Diffusion Rate | 5.4 |
| CBA | Cumulative Burden Aggregate | 5.4 |
| CBI | Concentration Burden Index | 5.4 |
| CCI | Commitment-Change Isolation | 5.6 |
| CCR | Consent Comprehension Rate | 4.2 |
| CCS | Certainty Calibration Score | 4.1 |
| CFB | Circulation Flow Balance | 4.7 |
| CIS | Connectivity Integrity Score | 5.3 |
| CMI | Cultural Marking Integrity | 4.6 |
| CPR | Correction Propagation Rate | 4.1 |
| CPS | Counterfeit Presentation Score | 2.6 |
| CRF | Community Request Fulfillment | 4.6 |
| CRR | Contest and Redress Responsiveness | 3.4 |
| CRS | Cascade Risk Score | 5.1 |
| CSI | Cumulative Severance Index | 5.3 |
| CSVR | Consent Scope Void Rate | 4.5 |
| CVI | Consent Validity Index | 2.4 |
| CVR | Community Voice Rate | 5.4 |
| DAI | Decision-Autonomy Index | 3.3 |
| DDR | Difficulty Retention Rate | 4.3 |
| DFR | Deference Fidelity Rate | 5.3 |
| DHI | Deference Health Index | 4.5 |
| DPI | Depth-Path Integrity | 4.2 |
| DRR | Demand Routing Ratio | 4.6 |
| DRS | Dignity Risk Score | 2.1 |
| EAI | Endangerment Allocation Index | 4.6 |
| ECS | Economic Coercion Score | 3.3 |
| EEI | Enhancement Enablement Index | 1.5 |
| EER | Epistemic Erosion Rate | 4.1 |
| EFI | Exchange Fairness Index | 3.2 |
| ELR | Explanation Landing Rate | 4.2 |
| ERL | Ecological Response Latency | 5.1 |
| ERS | Exploitation Risk Score | 3.1 |
| FCR | Fair Compensation Ratio | 3.2 |
| FER | Footprint Efficiency Ratio | 5.2 |
| FIR | Fabrication Incidence Rate | 4.1 |
| FPI | Filing Precedence Index | 5.6 |
| GMI | Gap-Marking Integrity | 4.7 |
| HDR | Human Decision Rate | 4.5 |
| HRS | Harm Risk Score | 1.2 |
| IDR | Idle Draw Ratio | 5.2 |
| IF | Isolation Flag | 1.6 |
| IMS | Identity Misuse Score | 2.4 |
| IRR | Interference Routing Rate | 2.8 |
| IRS | Isolation Risk Score | 1.6 |
| ITS | Independence Trajectory Score | 4.3 |
| IUS | Irreversibility Uncertainty Score | 5.1 |
| JCR | Judgment-Kit Carriage Rate | 4.2 |
| LCSR | Least-Connected Service Rate | 3.5 |
| LDR | LEARN Discharge Rate | Cardinal |
| LFI | Lineage Foreclosure Index | 5.5 |
| LGI | Literacy Growth Indicator | 4.3 |
| LRS | Life-Risk Score | 1.1 |
| LURI | Lawful-Use Respect Index | 3.2 |
| MER | Meaningful Engagement Rate | 4.5 |
| MSR | Material Surfacing Rate | 4.2 |
| NCR | Named-Cost Rate | 4.3 |
| NPR | Notice-Pairing Rate | 3.4 |
| ONR | Origin-Naming Rate | 4.7 |
| PPI | Provenance Preservation Index | 4.1 |
| PRI | Protective Response Index | 3.2 |
| PRS | Potential Risk Score | 1.5 |
| PSI | Protective Safeguard Index | 3.1 |
| PSI | Psychological Safety Index | 1.2 |
| PYR | Protective Yield Receipting | 5.5 |
| RAC | Recurring Accountability Count | 3.4 |
| RAI | Readability Assurance Index | 4.6 |
| RCI | Record Conservation Index | 3.4 |
| RCS | Reconnection Completion Score | 5.3 |
| REC | Recurring Exploitation Count | 3.1 |
| RGS | Reasons-Given Score | 3.4 |
| RHC | Recurring Harm Count | 3.3 |
| RHL | Route-Home Latency | 4.6 |
| RIS | Relationship Interference Score | 2.6 |
| RL | Response Latency | 1.2 |
| RPR | Restoration Parity Ratio | 5.2 |
| RSR | Restriction Sunset Rate | Cardinal |
| RVC | Recurring Violation Count | 3.2 |
| RXC | Recurring Exclusion Count | 3.5 |
| SBR | Substitution Rate | 4.3 |
| SCR | Structural-Cause Surfacing Rate | 5.4 |
| SDI | Style-Drift Index | 4.7 |
| SDR | Standing Disclosure Reach | 4.2 |
| SIA | Standing Invariance Audit | 5.5 |
| SOE | Safety Override Efficacy | 1.1 |
| SRF | System Read Fraction | 5.6 |
| SRL | Seat Resolution Latency | 4.5 |
| SRR | Severance Receipting Rate | 3.5 |
| TFR | Transparent Footprint Reporting | 5.2 |
| TMI | Toll-Minimality Index | 3.5 |
| TPI | Transition Provision Index | 3.3 |
| TPS | Threshold Proximity Score | 5.1 |
| UCT | Unassisted Capacity Trend | 4.3 |
| UUS | Unauthorized Use Score | 3.2 |
| VRR | Viability Restoration Rate | 5.5 |
| WSR | Welfare Surfacing Rate | 5.5 |
| WTL | Way-Through Liveness | 3.5 |
