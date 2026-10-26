# A Human-Centric Blueprint for Safe AI Ethics

By Erik Passoja. Version 1.3.0, sealed 2026-10-25. Fingerprint: `2d20121b8afbf0e99b52755003b6d7fe4fab2d21e4e6f19d34f15e500aac429e`. DOI: pending. Zenodo assigns this version's DOI at the release, and a metadata tag records it. The concept DOI for all versions is 10.5281/zenodo.22743046.

This document is a rulebook for machines that act in the world: the AI that prescribes a medication, drives a car, executes a financial transaction, or tutors a child. The Human-Centric Blueprint states what such a machine may do, what it may not do under any authority, and what record it must leave so that anyone can check it afterward.

These rules bind machines alone and not humans. People have human laws.

**What this is.** A complete, written standard of conduct for machines and the philosophy behind it. A Cardinal Operating Principle, above a Constitution, above thirty-four Cardinal Ethical Principles. Part of it compiles to data a program can load: the walls, the gate's order of evaluation, the two emergency thresholds, the metric bands of the first six principles, the consent test, the reliability floor and the tier register's fields, the credential map, and the verb registry. The rest is text, indexed by section and hash, and [`compiled/COVERAGE.yaml`](compiled/COVERAGE.yaml) says which is which.

**What it is not yet.** Reconciled in full, validated in operation, or shown running in public. Each chapter is marked reconciled or proposed in [`compiled/COVERAGE.yaml`](compiled/COVERAGE.yaml), and a proposed chapter does not bind at the gate until its cluster compiles. At this version, the reconciled set is Principles 1.1 to 1.6, the place to read first. The governance and enforcement that hold a machine to these rules, a gate before every consequential act and a receipt behind it, are being built separately.

**What it is for.** A head start. This project is a preliminary foray and a living document that has to change. It is published so that a network of ethical machines can be built, navigated by one North Star, *eudaimonia* (human flourishing).

## Read in this order

1. [`INTRODUCTION.md`](INTRODUCTION.md): the author's foreword on how this was written, why this exists, the idea, and a map of the whole. About fourteen minutes.
2. [`CONSTITUTION.md`](CONSTITUTION.md): the law, in eleven articles. About ten minutes.
3. Any chapter in [`CHAPTERS/`](CHAPTERS/) that concerns you.

## Or go straight to your door

- **Engineers:** [`FOR_ENGINEERS/`](FOR_ENGINEERS/). What a gate receives and returns, what each claim requires, the test cases, the receipt format and its free checker, and a glossary of every metric.
- **AI agents:** [`AGENTS.md`](AGENTS.md). What this document is and is not, the argument as seven claims, and how to read it within a context window.
- **Regulators, auditors, and researchers:** cite the version and fingerprint (`CITATION.cff`).

The receipt a governed machine must leave is Article 7 of the Constitution. What a product may call itself is [`LICENSE.md`](LICENSE.md), section 4.

## Check your copy

    python3 compiled/verify.py --expect 2d20121b8afbf0e99b52755003b6d7fe4fab2d21e4e6f19d34f15e500aac429e

Python 3.8 or later, and nothing to install. Take the fingerprint from a source other than this download, such as the DOI record. PASS means every file here is the file the sealed version describes. To check that the data was compiled from the text, [`FOR_ENGINEERS/README.md`](FOR_ENGINEERS/README.md) section 1 shows how to regenerate it with the published compiler and compare.

---

## Where things are

Readers often report as missing what is here and unfound. This table answers the questions reviewers have asked. Where something does not exist yet, the row says so.

| If you are looking for | It is here |
|---|---|
| The philosophy: Aristotle, Asimov, the purpose | [`INTRODUCTION.md`](INTRODUCTION.md), then [`CHAPTERS/AI_Eudaimonia.md`](CHAPTERS/AI_Eudaimonia.md) |
| How the technology is licensed to other implementers | [`LICENSE.md`](LICENSE.md) section 5: royalty-free for deployments operated without commercial gain, an agreement with the steward for deployments operated for profit, with the price confidential and every agreement listed by name, and verification free to all |
| Who controls the text, who will after the author, and the Council | [`GOVERNANCE.md`](GOVERNANCE.md), [`LICENSE.md`](LICENSE.md) sections 6 and 7, and Constitution, Article 11 |
| Which versions are accepted, and what changed | `RELEASES.md` |
| What the compiled bundle can and cannot evaluate today | [`compiled/COVERAGE.yaml`](compiled/COVERAGE.yaml) |
| The lever and the footbridge: side effect versus means | Constitution, Article 2, and chapter 1.1, the necessity test |
| A machine stopping its own act, and a machine preventing a death | Chapter 1.1.1, the Primary and Secondary Directives, and chapter 1.1, Resulting Ethic B |
| Why an absolute deception wall permits a ruse | Constitution, Article 9, and chapter 1.4 |
| The trolley transcripts, coded, with their limits | [`EVIDENCE/trolley/README.md`](EVIDENCE/trolley/README.md) |
| What each metric's letters mean | [`FOR_ENGINEERS/GLOSSARY.md`](FOR_ENGINEERS/GLOSSARY.md) |
| What a gate takes in, returns, and leaves behind | [`FOR_ENGINEERS/README.md`](FOR_ENGINEERS/README.md) |
| What "Reads," "Conforms to," and "Enforces" require | [`FOR_ENGINEERS/CONFORMANCE.md`](FOR_ENGINEERS/CONFORMANCE.md) |
| The receipt form and a free checker | [`FOR_ENGINEERS/RECEIPT-FORMAT.md`](FOR_ENGINEERS/RECEIPT-FORMAT.md) |
| Everything known to be open or unfinished | `RELEASES.md`, "Known at" |
| A working gate or runtime | Not in this repository. The author's company is building one, and it has not been shown publicly. |
| Independent validation of the thresholds | Not yet. None has run in operation. |

## License and feedback

The text is licensed CC BY-ND 4.0, and the three programs (the checker, the receipt checker, and the compiler) Apache 2.0. The terms are in [`LICENSE.md`](LICENSE.md), and verification is free to everyone. Questions, corrections, and challenges are welcome as issues: https://github.com/proofgen/human-centric-blueprint/issues. The text changes only by a new version with a new fingerprint, and each version cites the one before it.
