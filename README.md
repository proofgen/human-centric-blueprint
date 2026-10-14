# A Human-Centric Blueprint for Safe AI Ethics

By Erik Passoja. Version 1.2.0, sealed 2026-10-13. Fingerprint: `79887915e0a289a706f1d10c0e2a9883d9d9aa71b9c01bbcac9235b52c5372fb`. DOI: 10.5281/zenodo.23356105.

This document is a rulebook for machines that act in the world: the AI that prescribes a medication, drives a car, executes a financial transaction, or tutors a child. The Human-Centric Blueprint states what such a machine may do, what it may not do under any authority, and what record it must leave so that anyone can check it afterward.

These rules bind machines alone and not humans. People have human laws.

This document is a specification. The rules are here in two forms:

(1) text a person can read, and

(2) data a program can load.

The governance and enforcement that hold a machine to these rules, including a gate before every consequential AI action and a receipt behind it, are being built separately. None of it has been shown publicly yet.

## Read in this order

1. [`INTRODUCTION.md`](INTRODUCTION.md): why this exists, the idea, and a map of the whole. About thirteen minutes.
2. [`CONSTITUTION.md`](CONSTITUTION.md): the law, in eleven articles. About ten minutes.
3. Any chapter in [`CHAPTERS/`](CHAPTERS/) that concerns you.

## Or go straight to your door

- **Engineers:** [`FOR_ENGINEERS/`](FOR_ENGINEERS/). What a gate receives and returns, what each claim requires, the test cases, the receipt format and its free checker, and a glossary of every metric.
- **AI agents:** [`AGENTS.md`](AGENTS.md). What this document is and is not, the argument as seven claims, and how to read it within a context window.
- **Regulators, auditors, and researchers:** cite the version and fingerprint (`CITATION.cff`).

The receipt a governed machine must leave is Article 7 of the Constitution. What a product may call itself is [`LICENSE.md`](LICENSE.md), section 4.

## Check your copy

    python3 compiled/verify.py --expect 79887915e0a289a706f1d10c0e2a9883d9d9aa71b9c01bbcac9235b52c5372fb

Python 3.8 or later, and nothing to install. Take the fingerprint from a source other than this download, such as the DOI record. PASS means every file here is the file the sealed version describes.

---

## Where things are

Readers often report as missing what is here and unfound. This table answers the questions reviewers have asked. Where something does not exist yet, the row says so.

| If you are looking for | It is here |
|---|---|
| The philosophy: Aristotle, Asimov, the purpose | [`INTRODUCTION.md`](INTRODUCTION.md), then [`CHAPTERS/AI_Eudaimonia.md`](CHAPTERS/AI_Eudaimonia.md) |
| How the technology is licensed to other implementers | [`LICENSE.md`](LICENSE.md) section 5: royalty-free for deployments operated without commercial gain, published terms for commercial ones, and verification free to all |
| Who controls the text, and what follows the author | [`LICENSE.md`](LICENSE.md) sections 6 and 7, and Constitution, Article 11 |
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

The text is licensed CC BY-ND 4.0, and the two checking programs Apache 2.0. The terms are in [`LICENSE.md`](LICENSE.md), and verification is free to everyone. Questions, corrections, and challenges are welcome as issues: https://github.com/proofgen/human-centric-blueprint/issues. The text changes only by a new version with a new fingerprint, and each version cites the one before it.
