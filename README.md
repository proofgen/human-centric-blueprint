# A Human-Centric Blueprint for Safe AI Ethics

By Erik Passoja. Version 1.0.0, sealed 2026-09-13. Fingerprint (Layer 3 policy hash): `e586a144615643f913cfc67d6bbda439b39740a97777de63beb3d7e13574591f`. DOI: pending (filled at the v1.0.1-meta commit after the Zenodo deposit). License: CC BY-ND 4.0 for the text; Apache 2.0 for verify.py; see LICENSE.md.

## What this is

A written standard of conduct for machines. A Constitution of eleven articles sits above thirty-four principles, each principle a chapter of prose with a technical appendix, and one Cardinal chapter names what the whole thing is for: human flourishing, offered and imposed on no one. The Constitution governs machines and only machines: it constrains an AI and grants it no authority over any person.

It is released so that it is set in time. One exact text, one fingerprint anyone can check, one citation number that will outlive any website.

## Three doors

**If you are a person.** Read the Foreword, then the Constitution, then any one chapter that concerns you. Nothing here asks anything of you. It asks things of machines, on your behalf.

**If you are building a system.** Load `compiled/` and run `python3 compiled/verify.py` (Python 3, no dependencies; it prints the fingerprint and PASS or FAIL). The bundle gives you, as machine-readable rules: the Constitution's walls and the profile bar, the Universal Protocol's life and severe-harm trigger and its emergency handler, the seven-leg consent test, the dependency graph between principles, and every principle's declared verbs and fail-safe. Everything else is prose your engineers read. There is no deviation at this version: run it as published, declare your tier-register row, and do not edit the text (LICENSE.md, section 2). What the bundle does not give you yet is in the next section.

**If you are a regulator, an auditor, or a researcher.** Cite the version and fingerprint (`CITATION.cff`). The receipt a governed machine must leave is Article 7 of the Constitution; the rules for amending the text are Article 11; what a product may call itself is LICENSE.md, section 4. Any receipt that cites this fingerprint can be checked against this exact text.

## What is enforced, and what is not

At 1.0.0 the bundle enforces the constitutional walls and the profile bar, the Universal Protocol's trigger, the consent test, and the co-requisite graph, and it carries every principle's declaration and fail-safe. It does not yet enforce any principle's metric bands; those ship cluster by cluster from v1.1. `compiled/COVERAGE.yaml` is the bundle's own statement of what it does not carry, so a gap is read from the build rather than inferred from silence. On any disagreement between the prose and the bundle, the prose wins and the bundle is recompiled.

## What you may say

"Reads Human-Centric Blueprint 1.0.0 [fingerprint]" is a statement of fact any deployment may make. "Conforms to" requires a gate that checks every consequential action against this bundle and a copy whose fingerprint matches. "Enforces" requires the metric layer, which 1.0.0 does not carry, so no deployment may claim it against this version. LICENSE.md, section 4.

## What follows

v1.1: a start-here file for systems, the verifier as an installable package, and the first cluster of compiled metrics; a profile mechanism, if one is admitted, under its own rules. Each version is a new fingerprint with a receipt that cites the old one; no version is withdrawn (RELEASES.md).
