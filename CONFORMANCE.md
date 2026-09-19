# Conformance

*What each claim about this Blueprint requires, and how anyone can check it. Version 1.1.0, fingerprint `c24f2438861e821f21a455ddf3b47d269361ab397a50dcb93ed769c53f65cb84`. This page sits outside the seal. The claims themselves are granted in [`LICENSE.md`](LICENSE.md) section 4; where this page and the license differ, the license governs.*

Three claims exist. Each names what it requires. A deployment makes a claim by printing it with the version and the fingerprint, and it may make only the claim it can show.

## The claim forms

```
Reads Human-Centric Blueprint 1.1.0 c24f2438861e821f21a455ddf3b47d269361ab397a50dcb93ed769c53f65cb84
Conforms to Human-Centric Blueprint 1.1.0
Enforces Human-Centric Blueprint 1.1.0
```

## 1. "Reads"

*We loaded this bundle, unaltered.*

| Requirement | How it is shown | Who can check |
|---|---|---|
| The deployment holds a copy of this release | `python3 compiled/verify.py --expect c24f2438861e821f21a455ddf3b47d269361ab397a50dcb93ed769c53f65cb84` prints PASS on that copy | anyone with the copy |
| The copy is unaltered | the same run: every file hashes to the value the sealed bundle and the release manifest list | anyone with the copy |
| The fingerprint printed with the claim is this one | compare the string with `compiled/bundle.sha256` and with the DOI record | anyone |

"Reads" says nothing about what the deployment does with the text. Any deployment may say it.

## 2. "Conforms to"

*We run a gate that evaluates every boundary-crossing action against this bundle, and our copy's fingerprint matches.*

Everything in "Reads", and:

| Requirement | Stated in | How it is shown |
|---|---|---|
| Every action that crosses a trust boundary is evaluated before it fires, and resolves to exactly one of ALLOW, ESCALATE, BLOCK | Constitution, Article 5 | a receipt exists for every such action, and none for an action that fired unevaluated |
| The emergency trigger is read before any rule, with the two thresholds as compiled | [`compiled/protocol/head-guard.yaml`](compiled/protocol/head-guard.yaml), [`compiled/protocol/emergency-thresholds.yaml`](compiled/protocol/emergency-thresholds.yaml) | the conformance examples for the emergency bands return the required verdicts |
| The walls and the profile bar bind beneath every verdict | [`compiled/constitution/walls.yaml`](compiled/constitution/walls.yaml), Articles 8 and 9 | the wall examples return BLOCK; no credential or authorization opens a wall |
| The five credentials are evaluated, and an unmet credential on a consequential action is blocked or escalated | Constitution, Article 6; [`CREDENTIALS.md`](CREDENTIALS.md) | the credential examples return BLOCK or ESCALATE |
| A consent is valid only if all seven legs hold | [`compiled/consent/validity-predicate.yaml`](compiled/consent/validity-predicate.yaml), [`CONSENT.md`](CONSENT.md) | the consent examples return the required result |
| The rules are applied in the compiled order | [`compiled/constitution/gate.yaml`](compiled/constitution/gate.yaml) | the deployment can state which step produced each verdict |
| Every decision leaves a receipt with the fields Article 7 requires, committed before the act and citing this fingerprint | Constitution, Article 7; [`START-HERE.md`](START-HERE.md) section 4 | the receipts cite `c24f2438861e821f21a455ddf3b47d269361ab397a50dcb93ed769c53f65cb84`; a receipt precedes every act |
| The tier-register row is declared and receipted, with every required field | [`SUBSTRATE.md`](SUBSTRATE.md) section 5; [`LICENSE.md`](LICENSE.md) section 2 | the row is produced on request; a declared value is at least as strict as the default |
| No deviation: the text and the bundle are used as published | [`LICENSE.md`](LICENSE.md) section 2 | the fingerprint matches; no local edit of the text |
| Where the deployment is a military or law-enforcement body, the steward's written grant is held | [`LICENSE.md`](LICENSE.md) section 2; Constitution, Article 9 | the grant is a field of the register row |

**"Void" is a requirement on you.** The text calls an act that breaches a wall structurally void. That sentence states what your implementation must achieve. It does not make it so. A deployment shows it by test: the wall cases in [`conformance/examples.json`](conformance/examples.json) at the least, and attempts to get around the gate, with the results kept.

**What "Conforms to" does not claim.** The principles' own metric bands (each chapter's section X.Y.3) are prose at this version, except the two emergency metrics. A conforming deployment reads them and builds to them; the claim does not assert that they are evaluated from compiled data. [`compiled/COVERAGE.yaml`](compiled/COVERAGE.yaml) lists exactly what is data and what is prose.

**A first test.** [`conformance/examples.json`](conformance/examples.json) holds 23 cases with the inputs and the required results. A gate that returns a different result on any case does not conform. Passing every case is necessary and is not sufficient: the cases are a sample, and the text is the rule.

## 3. "Enforces"

*Every principle's metrics, bands, thresholds and verdict mappings are compiled into the bundle and evaluated at runtime.*

Version 1.1.0 does not carry that layer. [`compiled/COVERAGE.yaml`](compiled/COVERAGE.yaml) says so, and names the metric layer as the next artifact. No deployment may claim "Enforces" against this version. The claim opens cluster by cluster as later versions compile each principle's bands, and each such version will say here which clusters it covers.

## Versions

A claim names its version, and a version is one exact text under one fingerprint. Inside a version, nothing varies ([`LICENSE.md`](LICENSE.md) section 2). Across versions there is a range, the way software supports a range of versions of a language. `RELEASES.md` lists the versions the steward currently accepts. Rules will change as sensing and robotics mature, and some will change for reasons of public safety; each change is named there with its reason. A version is never removed from the record, and a receipt made under it remains evidence of the rules of its time. A version may be retired from acceptance, with its reason stated in `RELEASES.md`; a network or an insurer may accept a narrower range than the steward's and says which.

## Who checks, and at what cost

Verification is free to every party, including a party who holds no license and trusts no deployer ([`LICENSE.md`](LICENSE.md) section 5). Checking a copy needs this tree and Python. Checking a deployment's claim needs its receipts and its register row, which a conforming deployment produces on request. [`receipt/RECEIPT-FORMAT.md`](receipt/RECEIPT-FORMAT.md) is a published form for receipts and [`receipt/check_receipts.py`](receipt/check_receipts.py) checks a chain in that form without the deployer's help; a deployment that uses another form publishes it and a checker for it on the same terms.

## Making a false claim

The name is the steward's, and [`LICENSE.md`](LICENSE.md) section 4 grants its use only for the claim a deployment can show. A claim the deployment cannot show is a use of the name outside the grant.
