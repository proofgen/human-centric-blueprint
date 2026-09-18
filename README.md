# A Human-Centric Blueprint for Safe AI Ethics

By Erik Passoja. Version 1.1.0, sealed 2026-09-17. Fingerprint (Layer 3 policy hash): `c24f2438861e821f21a455ddf3b47d269361ab397a50dcb93ed769c53f65cb84`. DOI: 10.5281/zenodo.22822375. License: CC BY-ND 4.0 for the text; Apache 2.0 for verify.py; see LICENSE.md.

## What this is, in plain words

This is a rulebook for machines that act in the world: the AI that prescribes a medication, drives a car, decides an insurance claim, moderates what people say, or answers a child. It states, in ordinary language, what such a machine may do, what it may not do under any authority, and what it must leave behind so that a person can check it afterward.

It has two halves, and this repository is the first half. **The rules** are here, as text a person can read and as data a machine can load. **The machinery** that holds a machine to the rules, a gate in front of every consequential action and a receipt behind it, is the second half. Anyone may build that machinery to this text; the author's company builds one. The rules mean nothing without the machinery, and the machinery is only as good as the rules it enforces.

The rules bind machines and only machines. They ask nothing of any person and give no machine authority over anyone. A person who has not read them is protected by them all the same, in any system that runs them.

Why it exists: nobody cares what a machine thinks about ethics; we care how a machine behaves. Every approach in use today teaches a machine to want the good and hopes the wanting holds, and at the edge it does not. In 2014 the author's likeness was taken into a video game without consent, and no infrastructure existed that could have stopped it; the same missing infrastructure now sits under AI systems that decide far larger things. The Foreword tells that story and the reasoning that follows from it.

Written by Erik Passoja, a performer and systems architect, and stewarded by him under the terms in `LICENSE.md`. It is offered freely to everyone and imposed on no one. Once a system chooses to run it, the text is fixed, because a rule that can be quietly edited cannot be checked: that is the whole reason the text carries a fingerprint.

## Six terms you will meet

- **Gate.** The check a machine's action passes through before it happens. It returns one of three answers: allow, block, or escalate to a human.
- **Receipt.** The record the gate leaves for every decision, written before the act, that an outsider can check.
- **Walls.** The few things no verdict, instruction, or authority can open: a machine may not deceive, may not make a person's death the means to anything, may not apply force to a person, and more. Constitution, Article 9.
- **Profile bar.** The rule that no machine may keep a score or profile of a person that could be used to target, price, or rank them. Article 8.
- **Fingerprint.** A number computed from the compiled rules. Anyone can recompute it. If it matches, you have the exact text; if a receipt cites it, that receipt was made under this exact text. Also called the Layer 3 policy hash.
- **Tier-register row.** The one thing a deployment declares about itself: which risk tier it runs in and how fast a human must be reachable. `SUBSTRATE.md`, section 5.

## What this is, in structure

A Constitution of eleven articles sits above thirty-four principles, each principle a chapter of prose with a technical appendix, and one Cardinal chapter names what the whole thing is for: human flourishing. It is released so that it is set in time. One exact text, one fingerprint anyone can check, one citation number that will outlive any website.

## Three doors

**If you are a person.** Read the Foreword, then the Constitution, then any one chapter that concerns you. `PLAIN-WORDS.md` gives one paragraph on each of the documents the chapters depend on, and a glossary of every measurement name. Nothing here asks anything of you. It asks things of machines, on your behalf.

**If you are building a system.** Start with `START-HERE.md`: what a gate takes in, what it returns, and what it leaves behind. Load `compiled/` and run `python3 compiled/verify.py` (Python 3, no dependencies). It checks every file in this tree against the hashes the sealed bundle and the release manifest list, and prints the fingerprint and PASS or FAIL. The bundle gives you, as machine-readable rules: the Constitution's walls and the profile bar, the gate's rules and their order (Articles 3 to 7), the Universal Protocol's life and severe-harm trigger with its two thresholds and its emergency handler, the seven-leg consent test, the dependency graph between principles, and every principle's declared verbs and fail-safe. Everything else is prose your engineers read. `conformance/examples.json` holds worked cases to run your gate against; the verifier checks each one against the text and the compiled data. There is no deviation at this version: run it as published, declare your tier-register row, and do not edit the text (LICENSE.md, section 2). What the bundle does not give you yet is in the next section.

**If you are a regulator, an auditor, or a researcher.** Cite the version and fingerprint (`CITATION.cff`). The receipt a governed machine must leave is Article 7 of the Constitution; the rules for amending the text are Article 11; what a product may call itself is LICENSE.md, section 4. Any receipt that cites this fingerprint can be checked against this exact text.

## What is carried, and what is not

At 1.1.0 the bundle carries, as machine-readable rules, the constitutional walls and the profile bar, the Universal Protocol's trigger, the consent test, and the co-requisite graph, and every principle's declaration and fail-safe. A bundle is a file; a gate enforces. It does not yet carry any principle's metric bands; those ship cluster by cluster in the versions that follow. `compiled/COVERAGE.yaml` is the bundle's own statement of what it does not carry, so a gap is read from the build rather than inferred from silence. On any disagreement between the prose and the bundle, the prose wins and the bundle is recompiled.

## How to check this download

`python3 compiled/verify.py` confirms that every file here is the file the sealed bundle and the release manifest describe. That proves the tree is intact. It does not prove who published it. For that, take the fingerprint from a source independent of this download and pass it in:

    python3 compiled/verify.py --expect c24f2438861e821f21a455ddf3b47d269361ab397a50dcb93ed769c53f65cb84

The fingerprint for 1.1.0 is published at the Zenodo record (10.5281/zenodo.22822375), in the GitHub release notes and tag message, and in the author's public notices. A FAIL names the file that differs.

## What you may say

"Reads Human-Centric Blueprint 1.1.0 [fingerprint]" is a statement of fact any deployment may make. "Conforms to" requires a gate that checks every consequential action against this bundle and a copy whose fingerprint matches. "Enforces" requires the metric layer, which 1.1.0 does not carry, so no deployment may claim it against this version. LICENSE.md, section 4; `CONFORMANCE.md` lists what each claim requires and how anyone checks it.

## Feedback

Questions, corrections and challenges are welcome as issues on this repository. The text changes only by a new version with a new fingerprint (Constitution, Article 11); no version is withdrawn, and each cites the one before it (RELEASES.md).

## What follows

Each version compiles more of the prose into data, one cluster of principles at a time, until every principle's bands are data and the "Enforces" claim can open. A profile mechanism, if one is ever admitted, comes under its own rules. Each version is a new fingerprint with a receipt that cites the old one.
