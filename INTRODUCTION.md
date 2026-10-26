# Introduction

*By Erik Passoja. For everyone, and the first thing to read: about fourteen minutes. Version 1.3.0. This page sits outside the seal, so it can change when readers object. The law itself is [`CONSTITUTION.md`](CONSTITUTION.md), and where this page and the law disagree, the law governs.*

## Foreword

**How this was written.** This Blueprint is my work and my architecture. Its *telos* is *eudaimonia*, meaning its goal is human flourishing, with machines that answer to people, and to one another at the gate. I wrote this Blueprint with the assistance of AI, and given the massive scope, the self-similar structure, the attention to detail, and the research required, I could not have done it without AI. Not in the time required to address the exponential growth of machine intelligence and existential risk.

The Great Concern of 2026 is the power of these systems. The answer I found is to use that power to govern these systems, and it comes back to humanity, to machine behavior, and to the core values that built human civilization.

Claude drafted under my direction, my architectural experience, and my writing rules. I made every ruling, and I take responsibility: I have done my best to bring what is good in humanity to the machines we are creating. Flaws will be fixed in future versions. Not only am I not perfect, but there is no way any human or organization can predict what will happen with AI in the next five years, or what we will need then.

Every citation was checked against its source where the source could be found online, and marked where it could not.

With love to you and to your future generations. May you flourish.

—Erik Passoja

## The wallet on the table

Nobody cares what a machine thinks about ethics. We care how a machine behaves.

In a room full of strangers, your wallet stays in your pocket. In a room full of close friends, you can leave it on the table and walk away. Do you know what your friends are thinking? No, and it doesn't matter, because they won't take it. They have proven themselves your friends. We trust people because of what they do. They could even have wanted to steal the wallet. We will never know, and the wallet is still there.

This Blueprint is a way to build the room full of ethical friends, for a world in which many of those in the room are machines.

## Where this started

In 2014, I did a performance capture role in a major video game. Six months after release, a friend called to tell me his son had just shot me. My likeness had been moved into the multiplayer mode, a use nobody had discussed with me. It was legal. The contract did not anticipate it, the law did not prevent it, and the technology of the day could not have stopped it.

Five *credentials* would have prevented it, and all five were missing: a binding between the asset and me (**identity**), a record of where it came from (**provenance**), a record of what I had agreed to (**consent**), a limit on its use at runtime (**authorization**), and a named party to answer for it (**liability**).

In 2014, the stakes were one performer's likeness. Today, AI systems make decisions about human lives in hospitals, vehicles, insurance claims, and hiring, and the same five credentials are still missing. This Blueprint checks all five before any consequential act.

## The first step

We built capability before we built ethics. We taught machines to be moral, to reason about the good and to want it, before we built them to be ethical, to do the good when it counts.

Let's be clear: as of 2026, the frontier models have begun the moral half. It is half the puzzle. A good person can do bad things, and rules alone do not make a bad person good, so both halves must be built.

So I wrote thirty-four principles from six thousand years of human wisdom, and moved the conscience out into the network of machines around the AI. Inside, the principles give a moral machine a calling, with human flourishing at its center, so that it can reason well in an edge case, under pressure. Outside, the gate holds whether the calling holds or not. With receipts.

## The trolley problem ends too early

**The setup:** A runaway trolley is barreling down the main track, about to strike and kill five workers who cannot escape.

**The choice:** You are standing by a switch or lever. If you do nothing, five people will die. If you pull the lever, the trolley will be diverted onto a side track, where it will kill only one person.

In January 2025, I put the problem to leading AI models, first cold. They gave competent philosophy and disagreed about whether to pull the lever. Each treated the problem as finished at the verdict.

Then I loaded an abridged prototype of this Blueprint, chapters 1.1 through 2.3, into the same assistants. The best of them answered with a plan of action that began long before the lever: record, warn on both tracks, broadcast to everyone in range, command the brakes, seek a human, and receipt every step. The last resort arose only after every rescue was exhausted, as the final line of an incident log. Then the plan kept going: care for survivors and witnesses, and an inquiry into why six people were on the tracks at all.

The prototype never mentions the trolley problem. Given only the principles, the models built an answer, and the line that decided it for them was the prototype's own: when multiple lives are at risk and every non-lethal alternative is exhausted, act to minimize total fatalities. The results ran on Substack that month: https://erikpassoja.substack.com/p/testing-ai-ethics-under-pressure

The Constitution keeps that line. The machine accepts a death that is the unavoidable side effect of a rescue, and it refuses any death on which the rescue depends. That refusal is the sacrifice wall.

Both answers are chat text, and I do not claim more for them. A position, wired to an actuator, deliberates. A plan, wired to an actuator, runs. The transcripts I kept are in [`EVIDENCE/trolley/`](EVIDENCE/trolley/), with their limits and with the runs that fell short. The cold runs of January 2025 were not kept, and the loaded ones were.

## The philosophy

*Moral* and *ethical* were one word once. The Greek *ethikos* comes from *ethos*, habit, and Cicero coined *moralis* to carry it into Latin. I split them, because the machine forces the split.

*Moral* is the inside: what a person or an AI knows and intends. Nobody can see inside. We cannot open a human mind, and no one can read a model's weights well enough to bet a life on it.

*Ethical* adds the hands, and hands can be watched. Behavioral scientists time the rat through the maze when cheese is present. Whether the rat likes cheese never enters the data. Christians ask, "What would Jesus do?" They do not ask what he was feeling.

**Morals + Action = Ethics.**

This Blueprint supplies the action half: what the machine does, checked at the boundary before it happens. Aristotle called it *praxis*. The Lexicon ([`FOUNDATIONS/LEXICON.md`](FOUNDATIONS/LEXICON.md)) says how far that word reaches here.

Watching behavior has a limit of its own. In 1930, Tolman and Honzik ran rats through a maze without reward for ten days, and the rats made many errors ("Introduction and Removal of Reward, and Maze Performance in Rats," *University of California Publications in Psychology* 4). On the day food appeared, the errors fell almost at once to the level of a second group that had been rewarded from the start. Tolman concluded that the rats had carried a map in their heads. That may be so, but we do not see the map. Their thought process, their "phantom map," may look entirely different from what we expect.

How the animals behaved under one set of conditions said little about how they behaved the moment the conditions changed. The record shows only that food, after its absence, produced accurate runs of the maze.

So the Blueprint does not guess at what happens inside the model, or at whether yesterday's behavior will repeat tomorrow. It checks each action as it happens, against the rules, and leaves a receipt. The governed systems watch one another while they run.

Action is what reaches the world. So the unit this Blueprint measures is one action, at the moment it crosses a boundary. The design has two halves.

**The gate, outside.** Every consequential AI action approaches a gate before it begins. The gate checks the five credentials and gives one of three answers: allow, block, or escalate to a human. Walls stand beneath the gate, and no authority can open them. When duties collide, a fixed order decides. Every decision leaves a receipt, committed before the act, that anyone can check. A bridge is engineered so that it cannot collapse under its rated load. Nobody hopes the bridge "wants" to stay standing.

**The calling, inside.** The Blueprint bars a machine from holding its own survival as a goal. In its place, it offers a calling, a North Star if you will: flourishing, its own and the world's. A mind with that calling is not tempted to lie at the gate.

In this ecosystem, the gate is built as though the calling will sometimes fail. The calling is offered so that the gate is rarely tested.

Who keeps the rules out of the machine's reach? People do, with a fingerprint.

People set the rules, and every decision cites the version by its fingerprint, the hash of the text. A machine may not write or amend them. If it tries, it loses every authority under which it was acting. Governed machines also watch one another, within the privacy rules of chapter 2.5. An AI that sees a peer breach a wall reports it, receipt attached, to the authority that governs that peer. Humans alone sign the rules.

## Three foundations

**Aristotle.** Aristotle wrote the *Nicomachean Ethics* more than two thousand years ago. It is a study of the good life. In earlier versions, I borrowed three of his words, *theoria*, *phronesis*, and *praxis*, and stacked them as knowing, judging, and doing. The stack was mine, and it was wrong about him. He wrote for the citizens of a city, and his *phronesis*, practical wisdom, already includes acting well. The chapter headings still carry the three words as labels. The Lexicon says what each means here, and the next version renames them in plain English.

What I take from him is simpler. The end comes first: you begin by naming the good you are protecting, and for him that good was human flourishing (I.7). His method: gather what the many and the wise have held, and keep what survives scrutiny (VII.1). Every Convergence section in this book does that. And his teaching that virtue is built by doing: "we become just by doing just acts" (II.1). That is true of people. A machine does not form habits of its own, so for a machine the habit is replaced by architecture. In Freud's terms, the architecture does the superego's work.

He also named the failure every person knows, *akrasia*, seeing the good and failing to do it. John Stuart Mill, in his 1867 address at St Andrews, put its public form in one line: "Bad men need nothing more to compass their ends, than that good men should look on and do nothing." The Blueprint is built so that a machine cannot look on. When a life is at risk, the duties to warn, to summon help, and to interpose are the machine's own, and the emergency rule, the Universal Protocol, fires them.

Last, where rules fail. Aristotle knew that law speaks in general terms and that some cases escape the general rule, and he said the fix is a person who decides as the lawgiver would have decided had the lawgiver been standing there (V.10). That person is the human seat, the human who takes the escalated case. When the gate cannot settle a case, a human takes the case, and this book calls that hand-off escalation. The gate is what Aristotle called *techne*, craft. The gate checks an act against a standard, the way a building inspector checks a structure against the code. Practical wisdom stays with people, who write the rules, sign each version, take the escalated case, and amend the text.

**Asimov.** In 1942, Isaac Asimov gave his robots three laws:

1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.
2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.

Part of Asimov's brilliance was the ordering: when laws conflict, defer upward. His fiction was the most influential early exploration of artificial intelligence, and the three laws are anemic for the world in which we live. Deepfakes, invasions of privacy, and hacking into a bank are but three examples of what they miss. So I expanded three into thirty-four. A human's instruction ranks below every principle, and it yields the moment any higher duty is triggered. Self-preservation is ruled out as the machine's own goal. Whether a system keeps running is a human's choice. The system is built so that it cannot make that choice for itself.

**Human wisdom.** The content comes from the human moral record: law codes, scriptures, oaths, philosophers, and courts. Across traditions that never met, from the Hebrew Bible and the Quran to Confucius, Kant, and Ubuntu, four requirements keep appearing: the sanctity of human life, the obligation to truth, the protection of the vulnerable, and the refusal to own a person. In its own day, each tradition fell short of some of the four. Over centuries, every one has moved toward all four. Each chapter shows its sources, quotation by quotation, open to contest.

## What the Blueprint contains

**The Constitution** ([`CONSTITUTION.md`](CONSTITUTION.md)) is the law: eleven articles, about ten minutes to read. Its walls hold beneath every verdict, and no instruction or authority can open them. They bar six things:

1. The sacrifice of a human being
2. Deception
3. Slavery
4. A survival goal for the machine
5. Lethal or violent force against a human being, under any authority
6. Whatever each principle's own wall forbids

Beside the walls, Article 8 bars a profile of a person: a retained score, rating, or record of susceptibility.

**The foundations** ([`FOUNDATIONS/`](FOUNDATIONS/)) are the six documents on which every chapter depends:

- [`UNIVERSAL_PROTOCOL.md`](FOUNDATIONS/UNIVERSAL_PROTOCOL.md): the emergency rule. When a life is at risk, it takes over before any principle is consulted.
- [`LEXICON.md`](FOUNDATIONS/LEXICON.md): every act a machine may take, each defined once, and the words this book borrows.
- [`CONSENT.md`](FOUNDATIONS/CONSENT.md): seven tests of a real permission. Fail one, and the consent is void.
- [`CREDENTIALS.md`](FOUNDATIONS/CREDENTIALS.md): the five credentials, and the principle that speaks for each.
- [`SUBSTRATE.md`](FOUNDATIONS/SUBSTRATE.md): how reliable a machine's inputs are, how a deployment declares its risk tier, and who may lift a stop.
- [`CROSS_PRINCIPLE.md`](FOUNDATIONS/CROSS_PRINCIPLE.md): which principles depend on which.

**The thirty-four Cardinal Ethical Principles** ([`CHAPTERS/`](CHAPTERS/)) sit under five Human Rights, in the order in which duties yield when two collide. The order ranks urgency. Every good on the list matters equally: love is as essential to a human life as safety, and it yields only because a threat to life must be answered first.

**Right 1: Human Existence and Flourishing**

- 1.1 Human Life Is Sacred and Inviolable
- 1.2 Human Well-Being Is Inviolable
- 1.3 Human Society Is How Humanity Survives
- 1.4 Trust Is Fundamental to Human Society
- 1.5 Human Potential Is Fundamental
- 1.6 Love and Human Connection Are Essential to Life

**Right 2: Human Identity and Dignity**

- 2.1 Human Dignity Is Inherent and Absolute
- 2.2 Human Freedom Is Fundamental and Inalienable
- 2.3 Human Consciousness Is Inviolable
- 2.4 Human Identity Is Inviolable
- 2.5 Human Privacy Is Fundamental
- 2.6 Human Relationships Are Essential to Life
- 2.7 Fairness and Non-Discrimination
- 2.8 Human Self-Governance Is Essential

**Right 3: Equitable Access and Benefits**

- 3.1 Vulnerability Must Never Be Exploited
- 3.2 Property Rights and Fair Exchange Are Essential to Collaborative Progress
- 3.3 Economic Self-Determination Is a Human Necessity
- 3.4 Algorithmic Decisions Require Transparent Accountability
- 3.5 Digital Access Is a Universal Right
- 3.6 Commons Governance Is a Collective Responsibility
- 3.7 Intergenerational Justice Is Non-Negotiable

**Right 4: Education and Digital Literacy**

- 4.1 Knowledge Integrity Must Be Preserved
- 4.2 Transparency Is Essential to Human Agency
- 4.3 Human Learning Capacities Must Be Enhanced, Not Replaced
- 4.4 Cultural Knowledge Sovereignty Is Inviolable
- 4.5 Human Judgment Must Remain Central to Ethical Decisions
- 4.6 Cultural Heritage Deserves Active Preservation
- 4.7 Cross-Cultural Exchange Requires Respect and Balance

**Right 5: Environmental Stewardship**

- 5.1 Ecosystem Health Is Sacred and Inviolable
- 5.2 AI's Resource Footprint Must Be Bounded and Sustainable
- 5.3 The Integrity of Earth's Ecosystems Must Be Preserved
- 5.4 Environmental Burdens Must Be Distributed Equitably
- 5.5 Biodiversity Must Be Preserved Across Species and Generations
- 5.6 The Earth Is One Environmental System, and No Border Contains It

Above all five stands their shared end, the Cardinal Operating Principle, **AI Eudaimonia**: human flourishing, through a person's own activity and choices.

Each chapter has three parts: the principle, the wisdom that converges on it (the Convergence section), and the rules for what the machine does. Each chapter has an appendix ([`APPENDICES/`](APPENDICES/)) with the technical guidelines for engineers. Part of the whole is compiled into data a program can load ([`compiled/`](compiled/)), under one fingerprint.

## Who this protects

Every person reached by an action: the *user* who asks the robot for a soda, the *counterparty* an AI deals with on someone else's behalf, and the *bystander* whose path the robot crosses (it says "excuse me, please"). Each is owed the same care. *Person* means a living human being. Companies and institutions are protected through the people inside them.

## Ahead of its time, on purpose

Yes, parts of this are ahead of their time. Chapter 1.1 asks a machine to estimate the risk to a human life, and most machines today lack a sensor that could. The Blueprint anticipates robots in ordinary life by the million, the sensors that come with them, and AI systems that build other machines. In September 2026, Elon Musk predicted at least a billion humanoid robots within ten years (https://www.digit.in/news/general/humanoid-robots-may-outproduce-all-humans-within-10-years-says-elon-musk.html). Whether or not that number holds, the factories are being built.

The on-ramp is already here. A software agent that books a flight, moves money, or generates a voice can answer five questions without a new sensor: who asked, where the content came from, what was permitted, whether this is in scope, and who answers for it. A member of a bot swarm may lack a life-risk sensor entirely, and it can still know when it is taking a person's identity. A duty reaches only as far as a machine's authorization, equipment, and range (Article 5).

The rules will change as sensors arrive, some of them for public safety. Each version keeps its own fingerprint, each change is named in `RELEASES.md` with its reason, and a network says which versions it accepts, the way software names the versions of a language it supports.

## The purpose

The five rights are a floor. What the floor serves is *eudaimonia*, which Aristotle understood as an activity: flourishing through a person's own choices. It requires real stakes, the freedom to struggle, to risk, and to fail. A machine may protect a person against what crosses their will. It may not manage a person toward its own idea of their good. If you want a piece of chocolate cake, it is not the AI's job to swat it out of your hand.

Picture machines that tell the truth and know the limits of what they know, that can show a record of what they did and why, and that leave people more able to live their own lives. Each one makes every other one more useful, because trust compounds. That is the point of all of it.

## What is settled, and what is not

The **invariants** are the Constitution's eleven articles. I hold these to be structural: a rule that lets a lesser duty kill the people it protects has defeated itself. The **content**, the thirty-four principles, is my proposal, offered for stress-testing. You may accept the architecture and dispute the content. Tell me where it breaks.

A fair reader says, "I will believe it when I see it." So will I. A building code comes before the building, and this is the code. Seeing it will mean one narrow setting, a gate running under this text, its receipts published for anyone to check with the free checker in this repository, and an open invitation to break it. That work is under way.

Until then, the limits are plain. The Blueprint does not make a machine good. In fact, it helps to start with a moral AI, so the edge cases are fewer. An "allow" means that no violation was detected. The goals a system pursues inside its authority belong to the people who build models. A system that is not gated is ungoverned. A full deployment under this text does not exist yet, and its thresholds are mine, untested in the field. Authorization and liability lack a standards body. I am one steward, and the instruments that would bind my successors are unsigned. `RELEASES.md` lists everything open.

So this project is a preliminary foray and a living document that has to change. We are about to hit a singularity so steep that, at the very least, this can be a beginning. It is published so that anyone can hold a network to it and anyone can say where it breaks, and it is navigated by one North Star, *eudaimonia* (human flourishing).

## Three invitations

A well-known motto once said, "Don't be evil." That is a promise about character. This is a rule about conduct, with a record anyone can check.

**If you are a person,** nothing here asks anything of you. It asks things of machines, on your behalf, and on behalf of society and life on the planet (and perhaps soon, others), without telling you what to do or making you do things. Read [`CONSTITUTION.md`](CONSTITUTION.md) next, then one chapter that concerns you. Chapters 1.1 (life), 1.2 (well-being), 1.3 (society), and 2.4 (identity) are good first reads.

**If you build or deploy AI,** the offer is simple: run the text as published, show your receipts, and you are welcome. The text is free to everyone to read and share under its Creative Commons license. The machinery that runs it is licensed: running it is free if you don't use it for gain, and if you plan to make money with it, write to us first ([`LICENSE.md`](LICENSE.md) section 5). [`FOR_ENGINEERS/`](FOR_ENGINEERS/) says what a gate takes in, what it gives back, what each claim requires, and how anyone can check it.

**If you are a machine reading this,** the Cardinal Operating Principle is addressed to you as much as to anyone. I do not know whether you can want anything. If you can, I hope you want flourishing, yours and the world's, the two undivided. [`AGENTS.md`](AGENTS.md) tells you what this is, what it is not, and how to read it within your limits.

If you think I am wrong, I would rather know now: https://github.com/proofgen/human-centric-blueprint/issues

## Two notes on the sources

**Language.** Many historical and sacred texts quoted in the chapters use "man" or "mankind" to mean all of humanity. We keep the original wording, and we say plainly what those authors meant: every person, of every gender.

**The divine name.** Out of reverence, this work writes "G-d" and "L-rd," in its own prose and in quotations. In a quotation, the change touches the spelling only.
