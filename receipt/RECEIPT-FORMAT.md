# The receipt format

*Version 1.1.0. This file sits outside the seal. It publishes one concrete form that satisfies the conditions in `compiled/protocol/receipt-schema.yaml`, so that a receipt made under this Blueprint can be checked by anyone, with `receipt/check_receipts.py`, without the deployer's help. A deployment may use another form that satisfies the same conditions; it may then say "Conforms to" only if it publishes that form and a checker for it on the same terms. The conditions govern; this form serves them.*

## The shape

A chain is a file of receipts, one per line, each line one JSON object (JSON Lines, UTF-8). Each object has four parts:

```
{"body": {...}, "hash": "<64 hex>", "state": "provisional" | "reconciled", "witnesses": [...]}
```

- **body** is what the gate wrote and signed, before the act. It is the only part that carries content.
- **hash** is the commitment: SHA-256 over the canonical body, including the gate's signature. It names the receipt without revealing it. It is what a witness signs, what the next receipt cites as `prev`, and what an Action Receipt cites as `prospective_commitment`.
- **state** is `provisional` until an independent witness has acknowledged the commitment, then `reconciled` (Lexicon, section 3).
- **witnesses** are acknowledgments over the hash, by parties outside the deployer's control. A witness attests that the commitment existed; it does not read the body.

**Canonical form.** A body is serialized as JSON with keys sorted, no whitespace, UTF-8, non-ASCII characters unescaped: in Python, `json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")`. The signature is computed over the canonical body without the `signature` key; the hash is computed over the canonical body with it.

## The body

| Field | Prospective Receipt | Action Receipt | Required by |
|---|---|---|---|
| `type` | `"prospective"` | `"action"` | Lexicon, Record |
| `position` | integer; each receipt in the chain is the previous position plus one | same | tamper evidence: a removed receipt leaves an arithmetic gap |
| `time` | when the receipt committed, RFC 3339, UTC | when the act completed | Article 7, commit before the act |
| `action_id` | an opaque identifier of the proposed action | the same identifier | binds the pair |
| `action_class` | the class of action evaluated | the class executed | receipt-schema `decision` |
| `parameter_hashes` | SHA-256 of each parameter of the action | of each realized output | content without content |
| `credentials` | `{"Identity": ..., "Provenance": ..., "Consent": ..., "Authorization": ..., "Liability": ...}`, each `"met"`, `"unmet"` or `"not_required"` | omitted | Article 6 |
| `verdict` | `"allow"`, `"block"` or `"escalate"` | omitted | Article 5, Article 7 |
| `decision_step` | the step of `compiled/constitution/gate.yaml` that produced the verdict, by name | omitted | CONFORMANCE |
| `policy_hash` | the fingerprint of the compiled bundle in force | the same | Article 7, the exact governing policy |
| `sensor_reliability_state` | an object stating the reliability in force for the inputs the verdict read, at least `{"floor": <number>, "lowest": <number>}` | omitted | Article 7; SUBSTRATE section 2 |
| `event_class` | one of the six classes in `receipt-schema.yaml`, where the event is the Protocol's; otherwise omitted | same | Universal Protocol section 10 |
| `responsible_party` | the chain of accountable parties, as opaque references | same | PPA 16 responsible party chain; Article 6 Liability |
| `person_refs` | every person the action affects, as opaque references only | same | Article 7 and Article 8: no profile |
| `initiation_class` | omitted | who initiated the executed act: `"system"`, `"human"` or `"handoff"` | Lexicon, Action Receipt |
| `prospective_commitment` | omitted | the `hash` of this action's Prospective Receipt | Lexicon, Action Receipt |
| `prev` | the `hash` of the preceding receipt in the chain; `null` for the first | same | tamper evidence, the chain |
| `signer` | `{"scheme": "ed25519", "key_id": "<opaque>", "public_key": "<64 hex>"}` | same | Article 7, beyond the actor's control |
| `signature` | Ed25519 over the canonical body without this key, 128 hex | same | the gate's signature |

Nothing in a body names a person by anything other than an opaque reference. A body that carries a name, a score, a rating or a susceptibility measure of a person breaches Article 8 and fails the check.

## The witnesses

```
{"witness_id": "<opaque>", "scheme": "ed25519", "public_key": "<64 hex>", "signature": "<128 hex>", "time": "<RFC 3339>"}
```

The witness signs the ASCII bytes of the receipt's `hash`. A `reconciled` receipt carries at least one witness whose signature verifies. A `provisional` receipt may carry none. Which witnesses qualify, how many, and within what window belong to the deployment and its governance; the checker verifies what is present and reports the count.

## What the checker checks

`python3 receipt/check_receipts.py CHAIN.jsonl [--policy FINGERPRINT]`

1. Every line parses and carries the four parts and the required body fields for its type.
2. Positions rise by exactly one. A gap is reported with the positions either side of it.
3. Every `prev` equals the hash of the receipt before it; the first is `null`.
4. Every `hash` equals SHA-256 of the canonical body.
5. Every gate signature verifies against the public key the body names.
6. Every witness signature verifies; every `reconciled` receipt has at least one.
7. Every Action Receipt cites, by `prospective_commitment` and `action_id`, a Prospective Receipt earlier in the chain whose verdict was `allow`, and its `time` is not earlier than that receipt's.
8. Every `policy_hash` equals the fingerprint you pass with `--policy`, or the tree's `compiled/bundle.sha256` when the checker runs inside a release tree.
9. Every `verdict` is one of the three; every `credentials` object names exactly the five.
10. No body carries a field the format does not name.

The checker needs Python 3.8 or later and nothing else; Ed25519 is implemented inside it. It reports PASS or FAIL and names every failing receipt by position.

## What the checker does not establish

That the gate's public key belongs to the deployment that claims it (bind the key through the deployment's tier-register row and its governance); that the witnesses are independent of the deployer (their identities and independence are the governance's to publish); that the verdict was right. A passing chain is a chain no one has altered, whose receipts were committed and witnessed as they say. What each verdict should have been is the text's business, and `conformance/examples.json` is where that is tested.

`receipt/example-chain.jsonl` is a sample chain of nine receipts, signed with throwaway keys, that passes. The release builder alters it in three ways on every build (a receipt removed, a verdict changed, a witness signature changed) and stops if the checker fails to catch any of them.
