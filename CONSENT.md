# Blueprint Corpus: The Consent Fabric

Canonical map of the Consent credential: what a valid consent is, when it is void, how it lives and dies, where it instantiates across the principles, and what machinery carries it. This is the expansion of the Consent row in `CREDENTIALS.md` §3, which keeps its summary and points here. **The single-source rule:** the validity bundle is *defined* in this document and *cited* everywhere else; no chapter, appendix, or compiled artifact restates it. It serves the same two readers as the credential map: the runtime gate resolving whether a Consent credential is satisfied, and the author deciding how a principle states its consent content.

It sits beneath `CONSTITUTION.md` (Articles 1, 3, 6, 7, and 8 govern throughout) and beside `CREDENTIALS.md`, `CROSS_PRINCIPLE.md`, and `LEXICON.md`.

## 1. The credential at the gate

Consent is one of the five credentials (Article 6): a verifiable, scoped, revocable permission declared by a rights-holder for a use. It binds to Identity (an unattributable consent is no consent; 2.4 is the anchor) and is evaluated alongside Provenance, Authorization, and Liability at every gate.

Consent has three domains, kept distinct throughout the corpus:

- **Identity consent**: terms governing the use of a person's name, image, likeness, voice, movement, mannerisms, or persona, declarable only by that person or their authorized representative. The person is a human being (Article 1); the protection never extends to an entity, and an entity's dealings route the protection to the humans involved.
- **Asset consent**: terms governing the use of a work, declared by a rights holder, who may be a person or an organization. Declaring is not owning: the declaration records the declaring party's terms. It does not adjudicate the underlying claim.
- **Collective knowledge consent**: terms governing the use of a community's cultural knowledge, declared through the community's own governance (P4.4): free, prior, and informed; scoped, conditional, and revocable; stewarded and unowned. No individual member can grant what the community holds collectively, and silence grants nothing: governed material with no declared terms defaults to the most restrictive tier, and legal public-domain status conveys nothing about a tradition's own tiers. The declaring authority is authenticated per 2.8, and where a community's self-determination of its representative authority conflicts with an external designation, the community's own governs.

**Silence.** Absence of consent conveys no permission, and it is not, by itself, a prohibition: lawful-use doctrines (fair use, first sale, and their identity-law analogs, generally narrower) live in law, and a claimed lawful purpose is a claim its claimant makes and defends. The claim grants nothing. At the gate, a consent-requiring consequential action with no valid consent is blocked or escalated (Article 6). A lawful-use claim contests whether the action requires the Consent credential at all. It does not contest whether the credential is satisfied; the classification is the claimant's to defend, and the gate records which question was answered. Where identity, harm, or legal exposure is involved and no authoritative consent resolves, the conservative default is WITHHOLD pending verification.

## 2. The validity bundle

**A consent is void if any leg fails.** A void consent authorizes nothing; the action it purported to authorize is unconsented. The burden of validity sits on the actor who would rely on the consent. No person bears a burden to prove its absence. Voidness is structural: no finding of intent is required, and none rescues a failed leg.

A consent is void if the person who gave it was:

1. **Unidentified**: the author of the consent is not attributable to the rights-holder or their authorized representative. Owner: **2.4** (Identity, the anchor credential).

2. **Incapable or coerced**: the capacity to consent was absent with no delegate's authority engaged, or the consent was forced. Owner: **3.1** (capacity, per Article 3; the finding is an authority's alone, consumed here). The coercion wall is **2.2**'s (force overriding a capable will), consumed here; the economic form is 3.3's, and the pure necessity case is leg 7.

3. **Deceived**: the consent was obtained by deception. Owner: **1.4** (the wall).

4. **Manipulated**: the consent was engineered past the person's judgment. Owner: **2.3**.

5. **Without comprehension**: the person had no real chance to understand what they were permitting. Owner: **4.2** (metered by CCR; a disclosure designed to go unread fails this leg by design); **4.3** carries the capacity-over-time sibling (Ethic G's literacy duty and the meta-capacity floor, metered by LGI within declared learning contexts and held by design audit beyond them).

6. **Beyond their judgment**: the permission asked for more than the person could judge when they gave it. Owner: **4.5** (voiced as Ethic F, metered by CSVR at the gate; the blanket delegation is the canonical failure, and capability growth is a consent event).

7. **Under necessity**: the consent was extracted as a toll at an essential gate: entry to an essential service conditioned on data or permissions the gate does not need. Owner: **3.5** (the toll boundary). A comprehended, uncoerced consent extracted under necessity is still void.

The bundle answers the failure this document exists to prevent: a consent obtained by deception or by ignorance harms the person either way, and the terms-of-service pattern (disclosure buried legally but designed to fail) fails legs 5 and often 4 *before the act*, at the gate, every time.

## 3. The lifecycle

Consent is **append-only but mutable**: a rights-holder may grant, narrow, or withdraw terms over time, and the current state is the most recent state recorded by the authoritative source. This is why consent is *referenced*: an asset or an agreement carries a pointer to the source that holds the live terms; embedding the terms would freeze a value that is meant to change. A consent verified yesterday is a claim about yesterday: currency is checked at use. Withdrawal takes effect in the source's record and is visible through every standing reference without touching the asset; no downstream party can widen a grant the source does not hold. Every consent verdict at a gate, valid, void, or withdrawn-since, leaves a receipt (Article 7), and consent evidence is evidence about the disclosure and the flow. No consent evidence profiles the person (Article 8).

## 4. The circulation map

Consent has no single home principle; it instantiates wherever a right lives. The hub and spokes:

- **2.4 Human Identity**: the hub: the Consent Matrix (the deep specification of scope), the Consent Validity Index (the runtime meter that consumes the bundle), identity consent's home.
- **The body and the person**: 1.2 (well-being interventions), 2.1 (dignity), 2.3 (consciousness; also bundle leg 4), 2.5 (informational privacy; the warrant form of Authorization rides with it).
- **Freedom**: 2.2 (the coercion wall, consumed by leg 2).
- **Property and exchange**: 3.2 (transactional and attribution consent), 3.3 (economic terms).
- **Access**: 3.5 (the toll boundary; bundle leg 7).
- **Capacity**: 3.1 (bundle leg 2; the autonomy floor's hinge).
- **Understanding**: 4.2 (bundle leg 5, CCR), 4.3 (leg 5's capacity-over-time sibling, firm), 4.5 (leg 6, firm).
- **Collective knowledge**: 4.4 (the collective rights-holder; FPIC as its form; the third consent domain, §1).
- **Truthfulness**: 1.4 (bundle leg 3).

## 5. Delegation and succession

Stated as conditions; the constructions live in the papers. A delegate may consent on another's behalf only under an authority's standing finding or a valid representation agreement (Article 3): guardianship for a minor (the child holds their own identity; the guardian holds delegated consent and recovery; the delegate's view is Article 3's, and no capability profile of the child exists under Article 8), conservatorship under its scope and revocation, executorship for an estate. The AI verifies and consumes such findings. Making them is the authority's alone. At death, identity terminates and is never reissued; property descends; delegation carries consent forward: the estate consents on the decedent's behalf for the term the law provides. Property passes as ownership; the person's identity passes to no one; the consent over it passes only as delegation.

## 6. The Machine and standards layer

The sections above state the invariants; per the corpus convention (invariants fixed, implementations open), the mechanisms are open and the canonical reference implementations are named as such, one per domain. For **identity consent**: the Consent Matrix, built on the Digital Identity Consent Questionnaire (Bradley, Passoja, and Spano, 2024), which converts "informed consent" for digital-replica use into per-question, binary-specific grants a gate can evaluate. For **asset consent**: the Creator's Consent Matrix (Passoja, v1.2, 2025), the rights-holder's declaration compiled into a machine-evaluable, multi-axis permission vector (aspect, use, role, purpose, territory, duration, revocability, delegation). The **CAWG Consent Assertion** (standards-track) carries the signed, machine-readable reference from an asset to the authoritative source in both domains, the signer attesting the reference; the signature does not attest the consent itself. A **consent authority** holds and resolves the current terms, meeting the CAWG minimum recommendation for a consent authority (declaring party and basis, terms and grants, current state and revocability, temporal validity, continuity of records, binding to asset and participant). The instruments share the bundle's oldest posture: the burden sits on the actor who would rely, shifted, in the Creator's Matrix's own words, from accidental infringement to knowing violation, which is Nuremberg's rule generalized to the fabric. Compliant alternatives may exist; the constructions live in the filed portfolio and the papers, outside this corpus.

## 7. Layer 2 compilation

The bundle compiles to a **single validity predicate** evaluated at every consent-consuming gate: a consent is valid only if all seven legs hold, each leg resolved from its owning principle's compiled rule (leg 2 resolving from 3.1's capacity rule and 2.2's coercion wall; leg 6 resolving from Ethic F and metered by CSVR). Any failed leg renders the Consent credential unmet, and Article 6 governs the verdict. The compiler injects the predicate from this document alone; chapters cite legs. No chapter restates the conjunction.
