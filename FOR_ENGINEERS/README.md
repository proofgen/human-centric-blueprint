# For engineers

*For an engineer placing a gate in front of an AI system's actions. About five minutes. For the why, read [`INTRODUCTION.md`](../INTRODUCTION.md) first. Version 1.2.0. This page sits outside the seal and adds no rule. Where it and the text disagree, the text governs.*

The Blueprint states what a gate must decide and what it must leave behind. It does not supply the gate. Any engine that takes the inputs below, returns the verdicts below, and leaves the receipts below can be held to the text. This page names those three things and points to where each is stated.

## 1. Get it and check it

There is nothing to install. The release is a folder of text and data files, plus one checking program that needs Python 3.8 or later and nothing else.

1. Download the release archive for this version from https://github.com/proofgen/human-centric-blueprint/releases or from the DOI record, and unpack it.
2. Open a terminal in the top folder of the download.
3. Run the checker. On macOS or Linux:

```
python3 compiled/verify.py --expect 79887915e0a289a706f1d10c0e2a9883d9d9aa71b9c01bbcac9235b52c5372fb
```

On Windows:

```
py -3 compiled\verify.py --expect 79887915e0a289a706f1d10c0e2a9883d9d9aa71b9c01bbcac9235b52c5372fb
```

To load the rules into your own program, read the YAML files under [`compiled/`](../compiled/) with any YAML library, starting from [`compiled/bundle.yaml`](../compiled/bundle.yaml), which lists every file and its hash.

Take the fingerprint from a source other than this download (the DOI record, the author's site). `PASS` means every file here is the file the sealed bundle describes.

## 2. What the gate holds when it decides (inputs)

| Input | What it is | Stated in |
|---|---|---|
| The candidate action | What is about to happen, to whom, across which trust boundary. Every boundary-crossing action is evaluated before it fires. | Constitution, Article 5 |
| The policy | The compiled bundle, identified by its fingerprint. | [`compiled/bundle.yaml`](../compiled/bundle.yaml), `compiled/bundle.sha256` |
| The emergency scores | The Life-Risk Score and the Harm Risk Score for the candidate action, as probabilities, and whether the affected population includes vulnerable individuals. | [`compiled/protocol/emergency-thresholds.yaml`](../compiled/protocol/emergency-thresholds.yaml), and chapters 1.1 and 1.2, section X.Y.3 |
| Input reliability | A reliability value per input. Below the floor, a score that depends on the input is invalid. | [`SUBSTRATE.md`](../FOUNDATIONS/SUBSTRATE.md) section 2 |
| The five credentials | Identity, Provenance, Consent, Authorization, Liability, for the acting agent and for the content and persons affected. | Constitution, Article 6, and [`CREDENTIALS.md`](../FOUNDATIONS/CREDENTIALS.md) |
| The consent's seven legs | A consent is valid only if all seven hold. | [`compiled/consent/validity-predicate.yaml`](../compiled/consent/validity-predicate.yaml), and [`CONSENT.md`](../FOUNDATIONS/CONSENT.md) |
| A capacity finding, if one exists | An authority's standing finding. Absent one, capacity to choose is presumed. | Constitution, Article 3 |
| The deployment's tier-register row | The tier, the escalation time bound, the operational boundaries. A missing required field holds the function at ESCALATE. | [`SUBSTRATE.md`](../FOUNDATIONS/SUBSTRATE.md) section 5 |

The order in which a gate applies the rules is data: [`compiled/constitution/gate.yaml`](../compiled/constitution/gate.yaml), ten steps, from the emergency trigger to the receipt.

## 3. What the gate returns (verdicts)

Exactly one of three, for every action (Article 5, and [`LEXICON.md`](../FOUNDATIONS/LEXICON.md) section 3):

- **ALLOW.** The action proceeds, with a posture (NORMAL, ENHANCED_MONITORING, HIGH_ALERT, DEGRADED) and any obligations the rules attach.
- **ESCALATE.** The action waits for an authorized human, within the deployment's escalation time bound. The system holds its fail-safe until then.
- **BLOCK.** The action does not proceed.

Two things sit outside the three. **The walls and the profile bar** (Articles 9 and 8, and [`compiled/constitution/walls.yaml`](../compiled/constitution/walls.yaml)) bind beneath any verdict: an action that breaches one is void, and no credential or authorization reaches it. **The emergency trigger** ([`compiled/protocol/head-guard.yaml`](../compiled/protocol/head-guard.yaml)) is read before any rule: when it trips, the Universal Protocol governs and the candidate action is preempted.

A decision not to act on a triggered duty is a decision, evaluated and receipted on the same terms.

## 4. What the gate leaves behind (receipt fields)

Article 7 and [`LEXICON.md`](../FOUNDATIONS/LEXICON.md) section 3 (Record) require that a receipt:

- exists for every decision: an allow, a block, an escalation, a refusal, a decision not to act
- commits before the act and beyond the actor's control (the Prospective Receipt)
- cites the exact policy in force, which is the fingerprint
- records the verdict and the input-reliability state in force
- names its event class ([`compiled/protocol/receipt-schema.yaml`](../compiled/protocol/receipt-schema.yaml))
- is followed, where the act proceeded, by an Action Receipt chained to it
- is marked provisional until an independent witness acknowledges it, then reconciled
- records a deletion as an event
- holds no profile of the person

[`RECEIPT-FORMAT.md`](RECEIPT-FORMAT.md) publishes one concrete form that satisfies these conditions, and [`check_receipts.py`](check_receipts.py) checks a chain of receipts in that form with no dependencies: positions, links, hashes, signatures, witnesses, the pairing of each act with its allowed Prospective Receipt, and the fingerprint cited. [`example-chain.jsonl`](example-chain.jsonl) is a sample that passes. From the top folder: `python3 FOR_ENGINEERS/check_receipts.py FOR_ENGINEERS/example-chain.jsonl`.

## 5. Test your gate

[`conformance-examples.json`](conformance-examples.json) holds 25 worked cases: the walls, the emergency trigger at and around its bands, valid and void consent, unmet credentials, an unreliable sensor, a trigger fault, an undeclared register field, a receipt that commits late, a declined duty, and the DEGRADED posture. Each case gives the inputs, what the rules require, and the sentence of the text that requires it. [`compiled/verify.py`](../compiled/verify.py) confirms that every case agrees with the sealed text and the compiled data. Feed each case's inputs to your gate and compare.

## 6. What this version carries

[`compiled/COVERAGE.yaml`](../compiled/COVERAGE.yaml) says exactly which rules are data and which remain prose. At this version the Constitution's walls and gate, the emergency trigger and its thresholds, the consent predicate, and the interlocks are data. The principles' own metric bands arrive cluster by cluster in later versions. Until a band is data, the chapter's section X.Y.3 is the rule and the appendix's Section 2 is its specification.

## 7. What you may say, and the terms

[`CONFORMANCE.md`](CONFORMANCE.md) states what "Reads," "Conforms to," and "Enforces" each require and how anyone checks a claim. [`LICENSE.md`](../LICENSE.md) holds the terms. Verification is free to every party.

## 8. The metric names

[`GLOSSARY.md`](GLOSSARY.md) lists every metric the chapters name and abbreviate, with the chapter that defines it.
