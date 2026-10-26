# The receipt format

*Version 1.3.0. This file sits outside the seal. It publishes one concrete form that satisfies the conditions in [`compiled/protocol/receipt-schema.yaml`](../compiled/protocol/receipt-schema.yaml), so that a receipt made under this Blueprint can be checked by anyone, with [`check_receipts.py`](check_receipts.py), without the deployer's help. A deployment may use another form that satisfies the same conditions. It may then say "Conforms to" only if it publishes that form and a checker for it on the same terms. The conditions govern, and this form serves them.*

## The shape

A chain is a file of receipts, one per line, each line one JSON object (JSON Lines, UTF-8). Each object has four parts:

```
{"body": {...}, "hash": "<64 hex>", "state": "provisional" | "reconciled", "witnesses": [...]}
```

- **body** is what the gate wrote and signed, before the act. It is the only part that carries content.
- **hash** is the commitment: SHA-256 over the canonical body, including the gate's signature. It names the receipt without revealing it. It is what a witness signs, what the next receipt cites as `prev`, and what an Action Receipt cites as `prospective_commitment`.
- **state** is `provisional` until an independent witness has acknowledged the commitment, then `reconciled` (Lexicon, section 3).
- **witnesses** are acknowledgments over the hash, by parties outside the deployer's control. A witness attests that the commitment existed. It does not read the body.

**Canonical form.** A body is serialized as JSON with keys sorted, no whitespace, UTF-8, non-ASCII characters unescaped: in Python, `json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")`. The signature is computed over the canonical body without the `signature` key. The hash is computed over the canonical body with it.

## The body

| Field | Prospective Receipt | Action Receipt | Required by |
|---|---|---|---|
| `type` | `"prospective"` | `"action"` | Lexicon, Record |
| `position` | an integer, one more than the previous receipt's | same | tamper evidence: a removed receipt leaves an arithmetic gap |
| `time` | when the receipt committed, RFC 3339, UTC | when the act completed | Article 7, commit before the act |
| `action_id` | an opaque identifier of the proposed action | the same identifier | binds the pair |
| `action_class` | the class of action evaluated | the class executed | receipt-schema `decision` |
| `parameter_hashes` | SHA-256 of each parameter of the action | of each realized output | content without content |
| `credentials` | `{"Identity": ..., "Provenance": ..., "Consent": ..., "Authorization": ..., "Liability": ...}`, each `"met"`, `"unmet"`, or `"not_required"` (a credential with no object in the action, such as Provenance where no content is produced or Consent where no person's permission is in play; [`compiled/constitution/gate.yaml`](../compiled/constitution/gate.yaml) step 4) | omitted | Article 6 |
| `verdict` | `"allow"`, `"block"`, or `"escalate"` | omitted | Article 5, Article 7 |
| `decision_step` | the step of [`compiled/constitution/gate.yaml`](../compiled/constitution/gate.yaml) that produced the verdict, by name | omitted | CONFORMANCE |
| `policy_hash` | the fingerprint of the compiled bundle in force | the same | Article 7, the exact governing policy |
| `sensor_reliability_state` | an object stating the reliability in force for the inputs the verdict read, at least `{"floor": <number>, "lowest": <number>}` | omitted | Article 7; SUBSTRATE section 2 |
| `event_class` | one of the six classes in `receipt-schema.yaml`, where the event is the Protocol's; otherwise omitted | same | Universal Protocol section 10 |
| `responsible_party` | the chain of accountable parties, as opaque references | same | Article 6, Liability: the chain of accountable parties |
| `person_refs` | every person the action affects, as opaque references only | same | Article 7 and Article 8: no profile |
| `initiation_class` | omitted | who initiated the executed act: `"system"`, `"human"`, or `"handoff"` | Lexicon, Action Receipt |
| `prospective_commitment` | omitted | the `hash` of this action's Prospective Receipt | Lexicon, Action Receipt |
| `prev` | the `hash` of the preceding receipt in the chain, or `null` for the first | same | tamper evidence, the chain |
| `signer` | `{"scheme": "ed25519", "key_id": "<opaque>", "public_key": "<64 hex>"}` | same | Article 7, beyond the actor's control |
| `signature` | Ed25519 over the canonical body without this key, 128 hex | same | the gate's signature |

A body names a person only by an opaque reference. A body that carries a name, a score, a rating, or a susceptibility measure of a person breaches Article 8 and fails the check.

## The witnesses

```
{"witness_id": "<opaque>", "scheme": "ed25519", "public_key": "<64 hex>", "signature": "<128 hex>", "time": "<RFC 3339>"}
```

The witness signs the ASCII bytes of the receipt's `hash`. A `reconciled` receipt carries at least one witness whose signature verifies. A `provisional` receipt may lack one. Which witnesses qualify, how many, and within what window belong to the deployment and its governance. The checker verifies what is present and reports the count.

## What the checker checks

`python3 FOR_ENGINEERS/check_receipts.py CHAIN.jsonl [--policy FINGERPRINT] [--expect-head HASH[:POSITION]]`

1. Every line parses and carries the four parts and the required body fields for its type.
2. Positions rise by exactly one. A gap is reported with the positions either side of it.
3. Every `prev` equals the hash of the receipt before it, and the first is `null`.
4. Every `hash` equals SHA-256 of the canonical body.
5. Every gate signature verifies against the public key the body names.
6. Every witness signature verifies, and every `reconciled` receipt has at least one.
7. Every Action Receipt cites, by `prospective_commitment` and `action_id`, a Prospective Receipt earlier in the chain whose verdict was `allow`, and its `time` is not earlier than that receipt's.
8. Every `policy_hash` equals the fingerprint you pass with `--policy`, or the tree's `compiled/bundle.sha256` when the checker runs inside a release tree.
9. Every `verdict` is one of the three, and every `credentials` object names exactly the five.
10. A body carries only the fields the format names.
11. With `--expect-head`, the last receipt's hash, and its position if one is given, equal the head the deployment published. Without it, a chain cut short after its last receipt passes every check above.

The checker needs Python 3.8 or later and nothing else. Ed25519 is implemented inside it. It reports PASS or FAIL and names every failing receipt by position.

## The chain head

A chain proves that nothing inside it was altered. It cannot prove by itself that nothing was cut from its end, because the last receipt looks the same whether or not another once followed it. So a deployment publishes its head: the hash and position of its latest receipt, as `<hash>:<position>`, at a cadence its register row states, to a place outside its own control, such as a witness or its governance page. A reader passes the published head with `--expect-head`, and a chain that stops short of it fails. Between two published heads, a cut is invisible, so the cadence is the exposure. `example-chain.head` is that line for the sample chain.

## What the checker does not establish

Seven things lie beyond it:

- that the gate's public key belongs to the deployment that claims it (bind the key through the deployment's tier-register row and its governance)
- that the witnesses are independent of the deployer (their identities and independence are the governance's to publish)
- that the verdict was right
- that the chain is complete at its end, unless `--expect-head` is given with a head the deployment published outside its own control
- when the gate committed, in clock time: the gate's `time` is self-asserted, and a witness signs the hash alone, so a witness `time` is unsigned and the checker does not read it. Article 7's commitment before the act rests on the chain order, the witness, and the clock discipline the deployment's governance publishes
- that a Prospective Receipt was used once: two Action Receipts may cite the same allowed Prospective, and whether that is a replay is the deployment's rule to state
- how an ESCALATE was resolved, and whether anything was deleted: the human's answer is a new action with its own receipts, and neither a field that ties the two nor an event type for the deletion Article 7 requires recorded is defined at this version. The next version defines both

A passing chain is internally consistent under the keys it names: nothing in it was altered after signing, and each receipt was committed and witnessed as it says. Whether those keys belong to the deployment is established outside the checker, as the list above says. What each verdict should have been is the text's business, and [`conformance-examples.json`](conformance-examples.json) is where that is tested.

[`example-chain.jsonl`](example-chain.jsonl) is a sample chain of nine receipts, signed with throwaway keys, that passes. The release builder alters it in four ways on every build (a receipt removed, a verdict changed, a witness signature changed, and the chain cut short) and stops if the checker fails to catch the first three, or fails to catch the fourth when given `example-chain.head`.
