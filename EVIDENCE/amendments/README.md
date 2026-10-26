# Amendments under Article 11: the receipts

*Outside the seal. Evidence offered by the steward, Erik Passoja. Each file here is one record from his receipt chain, copied verbatim.*

## What this folder holds

The Constitution changes only by an amendment under Article 11, and an amendment is receipted: the record names the outgoing and incoming fingerprints and states the reasoning. This folder publishes those receipts. The rest of the chain, which records every edit to the hub, stays private until the Council's instruments are signed (`GOVERNANCE.md` section 1).

## receipt-165.json

The first amendment made under the procedure: Article 8, the profile bar, amended on the steward's ruling of 2026-10-14 and approved in text on 2026-10-15. The record is the receipt as written that night, with every field as it stands in the chain.

What a reader can check from the public releases: the Article 8 text of 1.2.0 (fingerprint 79887915…) against the Article 8 text of 1.3.0, and the reasoning the record states for the change.

What a reader cannot check without the hub: the file hashes, which are hashes of the hub's own build files at the two commits the record names, and the `prev` and `self` fields, which link this record to the one before it in a chain whose other records are private. The `policy` field is the hub's build fingerprint after the amendment, and it is not a published release fingerprint, since the hub built on from there.

The fields: `seq` is the record's position in the chain. `actor` names who made the change. `reason` states the amendment, the two fingerprints, and the reasoning. `files` lists the files the change touched, each with its hash after the change. `git_head_before` is the hub commit the change was made against. `prev` is the hash of the record before this one, and `self` is this record's own hash. `ts` and `ts_local` are the time of writing. `witness.remote` is the repository the chain is kept in.
