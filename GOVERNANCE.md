# Governance

*Version 1.3.0. This page sits outside the seal. It says who may change the text, by what act, and who will hold that authority after the author. It names the Council at the level of principle. The Council is not yet seated, and this page says what changes when it is.*

## 1. What exists now

One person is currently author and steward: Erik Passoja, acting through Seventh Planet, Inc. The text is hashed (`compiled/bundle.sha256`), it may not be altered (`LICENSE.md` section 1), and it changes only by an amendment under the Constitution's Article 11: receipted, citing the outgoing and incoming fingerprints, stating the incident or reasoning that prompted it, and published as a new version that a deployment adopts only by its own choice. The steward is the sole signer of amendments and releases. The succession instruments of `LICENSE.md` section 6 are not yet signed.

This is a temporary situation.

The first deployment under this text, a gate running in one narrow setting with its receipts published for anyone to check, is under way and needs sponsors.

## 2. The Council

An excellent way to oversee the Blueprint in the future would be to elect a standing body whose work is *eudaimonia*, or "human flourishing," the stewardship of the Cardinal Ethical Principles, and the release of future iterations of the Blueprint. The Council has six obligations:

1. **It accepts versions.** A version is accepted when it meets the tests in section 3, and the Council's acceptance is the act `RELEASES.md` records.
2. **It carries amendments.** Article 11 requires every change to the text to be receipted, with the old and new fingerprints and the reason. Once the Council exists, more than one member signs each change, so that one person can no longer change the text alone. It cannot open a wall of Article 9, because no one can.
3. **It reviews proposed variations** at the front door of `LICENSE.md` section 1 and gives an accepted variation its own fingerprint and its own line in `RELEASES.md`.
4. **It keeps the rules away from the money.** The fee of `LICENSE.md` section 5 is collected by the operating company. The rules that produce an allow, and the power to change them, belong to the Council, so that nobody can buy a looser rule by paying more.
5. **It publishes the list of incidents that led to amendments** and reviews it on a schedule. Article 11 requires every change to name the event that prompted it, and this is that list. The incidents of individual deployments stay in those deployments' own receipts.
6. **It issues the written grant** a military or law-enforcement body needs before it may run a Blueprint-governed system at all (`LICENSE.md` section 2). The grant certifies that the deployment sits outside the kill chain. Until the Council is seated, nobody issues one, the steward included. The Blueprint was not written for military use, and the answer to a request may be no.

The Council does not run a gate, render or revise a verdict on any action, or hold profiles of humans (Article 8). A deployment's receipts are the deployment's to publish and anyone's to check (`FOR_ENGINEERS/RECEIPT-FORMAT.md`).

## 3. What a version must meet

A version is accepted when every item holds, and the acceptance names the fingerprint it accepts.

- Every wall of Article 9 is unchanged in wording, or changed only by an Article 11 amendment with its record, and the lethal-force wall is never reopened.
- The validators pass with no failure, and every remaining flag is published in `RELEASES.md` under "Known at."
- Every compiled artifact agrees with the prose it compiles from: the chapter-against-appendix checks of the metric layer, the Article 7 and Article 9 sentence checks, the Lexicon's registry check, and the rest the compiler runs, each of which stops the build on a disagreement.
- Two compiles of the same tree are byte-identical, and `compiled/verify.py` passes on the tree.
- A reader outside the project has reviewed the version cold, and the review is published with the release. This item takes effect when the Council is seated. Until then, `RELEASES.md` names the cold reads a version received.
- Every change since the last accepted version is receipted, and the receipt chain verifies end to end. The amendment receipts are published in `EVIDENCE/amendments/`, and the chain itself stays private until the Council's instruments are signed.
- The release notes say in plain words what changed and what did not.

## 4. What a variation must meet

A variation is a published alternative to a stated part of the text, carrying its own fingerprint. The Council accepts one only when it states its reason, touches no wall of Article 9, leaves the Universal Protocol and the Constitution as they are, passes the checks of section 3 as a version does, and is listed in `RELEASES.md` so that a receipt citing it points to one exact text. A variation that removes a protection a principle grants is a different text under a different name, and it is not a variation of this one.

## 5. Seating

At this version there is no Council. There is a steward, one person, who does not seek the authority and will not have the hours to steward the Blueprint at scale. What follows is a recommendation for the Council's composition, and it takes effect only when the Council is seated. It will have more than one member. Its members will not be paid from the fee. Its roster will be public. The steward intends to place the patents in a nonprofit holding entity and license them back to the operating company, so that the patents cannot be sold with the company. When the Council is seated, `RELEASES.md` records the date and the roster, Article 11 is amended under its own mechanics to name the Council, the grant-back of `LICENSE.md` section 6 passes to it, and the steward's signature becomes one of several.

## 6. How to propose a change

Open an issue on the repository that names the file, the sentence, and the reason. A proposal that would change the sealed text is read as an Article 11 question. A proposal about the entry pages, the engineers' pages, or this page can be taken at any time, because those sit outside the seal.
