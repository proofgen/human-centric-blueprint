# Conformance

*What each claim about this Blueprint requires, and how anyone can check it. Version 1.3.0, fingerprint `2d20121b8afbf0e99b52755003b6d7fe4fab2d21e4e6f19d34f15e500aac429e`. This page sits outside the seal. The claims themselves are granted in [`LICENSE.md`](../LICENSE.md) section 4. Where this page and the license differ, the license governs.*

Three claims exist. Each names what it requires. A deployment makes a claim by printing it with the version and the fingerprint, and it may make only the claim it can show.

## The claim forms

```
Reads Human-Centric Blueprint 1.3.0 2d20121b8afbf0e99b52755003b6d7fe4fab2d21e4e6f19d34f15e500aac429e
Conforms to Human-Centric Blueprint 1.3.0
Enforces Human-Centric Blueprint 1.3.0
```

## 1. "Reads"

*We loaded this bundle, unaltered.*

| Requirement | How it is shown | Who can check |
|---|---|---|
| The deployment holds a copy of this release | `python3 compiled/verify.py --expect 2d20121b8afbf0e99b52755003b6d7fe4fab2d21e4e6f19d34f15e500aac429e` prints PASS on that copy | anyone with the copy |
| The copy is unaltered | the same run: every file hashes to the value the sealed bundle and the release manifest list | anyone with the copy |
| The fingerprint printed with the claim is this one | compare the string with `compiled/bundle.sha256` and with the DOI record | anyone |

"Reads" does not say anything about what the deployment does with the text. Any deployment may say it.

## 2. "Conforms to"

*We run a gate that evaluates every boundary-crossing action against this bundle, and our copy's fingerprint matches.*

Everything in "Reads," and:

| Requirement | Stated in | How it is shown |
|---|---|---|
| Every action that crosses a trust boundary is evaluated before it fires, and resolves to exactly one of ALLOW, ESCALATE, BLOCK | Constitution, Article 5 | a receipt exists for every such action, and none for an action that fired unevaluated |
| The emergency trigger is read before any rule, with the two thresholds as compiled | [`compiled/protocol/head-guard.yaml`](../compiled/protocol/head-guard.yaml), [`compiled/protocol/emergency-thresholds.yaml`](../compiled/protocol/emergency-thresholds.yaml) | the conformance examples for the emergency bands return the required verdicts |
| The walls and the profile bar bind beneath every verdict | [`compiled/constitution/walls.yaml`](../compiled/constitution/walls.yaml), Articles 8 and 9 | the wall examples return BLOCK, and no credential or authorization opens a wall |
| The five credentials are evaluated, and an unmet credential on a consequential action is blocked or escalated | Constitution, Article 6; [`compiled/credentials/map.yaml`](../compiled/credentials/map.yaml); [`CREDENTIALS.md`](../FOUNDATIONS/CREDENTIALS.md) | the credential examples return BLOCK or ESCALATE |
| A consent is valid only if all seven legs hold | [`compiled/consent/validity-predicate.yaml`](../compiled/consent/validity-predicate.yaml), [`CONSENT.md`](../FOUNDATIONS/CONSENT.md) | the consent examples return the required result |
| The rules are applied in the compiled order | [`compiled/constitution/gate.yaml`](../compiled/constitution/gate.yaml) | the deployment can state which step produced each verdict |
| Every decision leaves a receipt with the fields Article 7 requires, committed before the act and citing this fingerprint | Constitution, Article 7, and [`README.md`](README.md) section 4 | the receipts cite `2d20121b8afbf0e99b52755003b6d7fe4fab2d21e4e6f19d34f15e500aac429e`, and a receipt precedes every act |
| The tier-register row is declared and receipted, with every required field | [`compiled/substrate/runtime.yaml`](../compiled/substrate/runtime.yaml) (register); [`SUBSTRATE.md`](../FOUNDATIONS/SUBSTRATE.md) section 5; [`LICENSE.md`](../LICENSE.md) section 2 | the row is produced on request, and a declared value is at least as strict as the default where the text supplies one |
| No deviation: the text and the bundle are used as published | [`LICENSE.md`](../LICENSE.md) section 2 | the fingerprint matches, with no local edit of the text |
| Where the deployment is a military or law-enforcement body, the written grant is held, issued by the Council once seated and by nobody before | [`LICENSE.md`](../LICENSE.md) section 2, and Constitution, Article 9 | the grant is a field of the register row |

**"Void" is a requirement on you.** The text calls an act that breaches a wall structurally void. That sentence states what your implementation must achieve. It does not make it so. A deployment shows it by test: the wall cases in [`conformance-examples.json`](conformance-examples.json) at the least, and attempts to get around the gate, with the results kept.

**What "Conforms to" does not claim.** The principles' own metric bands (each chapter's section X.Y.3) are prose at this version, except the nineteen metrics of cluster 1 (Principles 1.1 to 1.6), which compile in [`compiled/metrics/cluster-1.yaml`](../compiled/metrics/cluster-1.yaml). The emergency rule consumes two of them, LRS and HRS. A conforming deployment reads the prose bands and builds to them. The claim does not assert that they are evaluated from compiled data. A chapter marked proposed in [`compiled/COVERAGE.yaml`](../compiled/COVERAGE.yaml) does not bind at the gate until its cluster compiles, and at this version, the reconciled set is Principles 1.1 to 1.6. Where a compiled principle's co-requisite is a proposed one (1.2 and 1.4 lean on the consent-leg owners), the proposed chapter's text is the guarantee until it compiles: a deployment reads that text for the guarantee the edge names, and the rule that a verdict with an unmet co-requisite is invalid binds between compiled principles. [`compiled/COVERAGE.yaml`](../compiled/COVERAGE.yaml) lists exactly what is data and what is prose.

**A first test.** [`conformance-examples.json`](conformance-examples.json) holds 28 cases with the inputs and the required results. A gate that returns a different result on any case does not conform. Passing every case is necessary and is not sufficient: the cases are a sample, and the text is the rule.

## 3. "Enforces"

*Every principle's metrics, bands, thresholds, and verdict mappings are compiled into the bundle and evaluated at runtime.*

*Why no product may yet say "Enforces."* A product can say three things about this text. "Reads" means the product loaded the data. "Conforms to" means the product checks every action against the rules and can prove it. "Enforces" means the rules' numbers are built into the product's own software, so the product allows or stops an action by those numbers, automatically, and anyone can check that it does. This is the first version where that is possible, because the first six chapters' numbers are now data a program can load. But no one has yet shown a product doing it where an outside reader could check. So the label stays off until someone does. A product that said "we enforce it" before anyone had seen it work would be making a promise without proof. When the author turns the label on, this section will say "Enforces (cluster 1)," name the product that showed it, and the release record will give the date. [`compiled/COVERAGE.yaml`](../compiled/COVERAGE.yaml) says which principles' numbers compile at this version, and [`LICENSE.md`](../LICENSE.md) section 4 carries the same note.

## Versions

A claim names its version, and a version is one exact text under one fingerprint. Inside a version, nothing varies ([`LICENSE.md`](../LICENSE.md) section 2). Across versions there is a range, the way software supports a range of versions of a language. `RELEASES.md` lists the versions the steward currently accepts. Rules will change as sensing and robotics mature, and some will change for reasons of public safety. Each change is named there with its reason. A version is never removed from the record, and a receipt made under it remains evidence of the rules of its time. A version may be retired from acceptance, with its reason stated in `RELEASES.md`. A network or an insurer may accept a narrower range than the steward's and says which.

## Who checks, and at what cost

Verification is free to every party, including a party without a license and without trust in any deployer ([`LICENSE.md`](../LICENSE.md) section 5). Checking a copy needs this tree and Python. Checking a deployment's claim needs its receipts and its register row, which a conforming deployment produces on request. [`RECEIPT-FORMAT.md`](RECEIPT-FORMAT.md) is a published form for receipts, and [`check_receipts.py`](check_receipts.py) checks a chain in that form without the deployer's help. A deployment that uses another form publishes it and a checker for it on the same terms.

## Making a false claim

The name is the steward's, and [`LICENSE.md`](../LICENSE.md) section 4 grants its use only for the claim a deployment can show. A claim the deployment cannot show is a use of the name outside the grant.
