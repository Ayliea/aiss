# Crosswalk — AISS × Healthcare Cyber-Insurance Underwriting

**Crosswalk type:** Industry profile (carrier-baseline)
**Last verified:** 2026-05-11
**Scope:** Cyber-insurance underwriting questions commonly required of healthcare organizations operating AI systems in 2025-2026.

## Why this crosswalk exists

Healthcare organizations adopting AI are facing two simultaneous pressures from the cyber-insurance market:

1. **Coverage tightening.** Carriers writing cyber for healthcare are adding AI-specific exclusions or sub-limits (model-output liability, training-data privacy, agentic-tool privilege exposure) and asking detailed underwriting questions before binding.
2. **Premium differentiation.** Carriers offer material premium reductions — typically 10-30% — for demonstrated control maturity. Healthcare orgs that can produce auditor-grade evidence against a recognized AI control framework price below peers in the same risk class.

AISS sub-controls map cleanly to most of what carriers ask. This crosswalk gives the firm one auditable artifact to submit when answering the AI section of a cyber-insurance application, and gives the carrier one auditable artifact to score against.

The crosswalk is **carrier-neutral**. Specific carrier ports (Coalition, At-Bay, Travelers, Beazley, Chubb, Hiscox) will follow in separate crosswalk files as their questionnaire structures stabilize through 2026.

## Sources

This crosswalk draws on the following public sources for typical healthcare cyber-underwriting questions:

- NAIC Cybersecurity (EX) Working Group bulletins
- Coalition Cyber Risk Bulletins (public broker resources)
- At-Bay public broker FAQs and underwriting guides
- Marsh and Aon healthcare cyber market overviews (annual)
- HIMSS Healthcare Cybersecurity Survey methodology
- AHIMA AI Governance guidance for HIPAA Covered Entities

> When a carrier's question framing differs from the baseline below, prefer the carrier's exact wording for the application response and use the AISS sub-control evidence as the underlying control attestation.

---

## Section 1 — AI System Inventory & Governance

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Do you maintain a documented inventory of AI tools used across your organization, including SaaS-embedded AI features? | AC-2.1, AC-2.2, AC-2.4 |
| Do you classify AI systems by risk level (e.g., low / moderate / high)? | AC-2.3, AC-2.5 |
| Do you have a designated AI governance owner or committee? | AC-1.1, AC-1.2 |
| Do you have written acceptable-use policies for AI tools? | AC-1.4, AC-9.2 |
| Are AI systems integrated with clinical workflows (CDS, diagnostic, prescription) inventoried separately and reviewed at higher cadence? | AC-2.5, AC-2.6 |

## Section 2 — PHI & Sensitive Data Handling in AI

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Do you have written controls preventing transmission of PHI to AI tools without an executed BAA? | AC-3.1, AC-3.4, AC-5.3 |
| Are AI prompts and outputs containing PHI logged, retained, and protected at the same level as the EHR? | AC-3.5, AC-3.6, AC-8.1 |
| Have you reviewed AI provider data-handling commitments (training-data retention, secondary use, geographic processing)? | AC-3.1, AC-5.2, AC-5.3 |
| Do AI systems that ingest PHI honor minimum-necessary at the model/prompt layer, not just at the surrounding application? | AC-3.4, AC-3.6 |
| Is differential privacy or other de-identification applied before AI training/fine-tuning on PHI? | AC-3.2, AC-3.3, AC-10.4 |

## Section 3 — Access Control & Authentication

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Is MFA enforced for all access to AI tools and AI administration interfaces? | AC-4.1, AC-4.5 |
| Are AI API keys and service-account tokens managed centrally with documented rotation policy? | AC-4.2, AC-4.3, AC-4.4 |
| Is least-privilege enforced for AI tool access by clinical and non-clinical roles? | AC-4.1, AC-4.2 |
| Are agentic AI tools restricted from invoking high-risk actions (prescription, billing, identity changes) without human approval? | AC-10.5, AC-10.6 |

## Section 4 — AI Supply-Chain & Vendor Risk

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Do you perform AI vendor risk assessment before procurement, separate from general SaaS vendor due diligence? | AC-5.1, AC-5.2 |
| Are AI model provenance (pre-training data, fine-tuning data, marketplace source) verified before deployment? | AC-5.2, AC-5.3, AC-10.4 |
| Do vendor contracts include AI-specific terms (training-data exclusion, output indemnity, model-change notification)? | AC-5.3, AC-5.4 |
| Do you monitor for material changes to AI vendor products (model updates, terms changes, breach notifications)? | AC-5.4 |

## Section 5 — Output Validation & Clinical-Decision Safety

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Are AI outputs used in clinical decisions subject to mandatory human review before action? | AC-6.1, AC-6.2 |
| Do you have controls preventing hallucinated citations or fabricated content from entering the clinical record? | AC-6.1, AC-6.2, AC-6.3 |
| Are AI-generated outputs that may be used by patients (chatbots, education content) marked as such? | AC-6.6 |
| Is RAG content (clinical guidelines, formularies, knowledge base entries) validated for source integrity? | AC-3.7, AC-6.1 |

## Section 6 — Incident Response & Breach Notification

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Do AI-specific incidents (prompt-injection successes, model-output errors causing harm, training-data leak) have a documented response procedure? | AC-7.1, AC-7.2, AC-7.3 |
| Does your HIPAA breach-notification workflow account for AI-mediated PHI disclosures? | AC-7.4 |
| Are AI vendors contractually required to notify within 24-72 hours of AI-related security events affecting your data? | AC-5.3, AC-7.4 |

## Section 7 — Monitoring, Logging & Audit

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Are AI tool usage logs retained at HIPAA-equivalent levels (typically 6 years) and protected from tampering? | AC-8.1, AC-8.2 |
| Are anomalous AI-tool patterns (off-hours access, geo-anomalies, abnormal data volumes) monitored and alerted? | AC-8.3 |
| Can you produce evidence of AI tool usage for a given workforce member during a specified time window? | AC-8.1, AC-8.2 |

## Section 8 — Workforce Awareness & Training

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Does your annual HIPAA training include AI-specific modules (acceptable use, PHI handling, recognized AI risks)? | AC-9.1, AC-9.2 |
| Are clinical staff trained on AI hallucination recognition and clinical-decision verification? | AC-9.1, AC-9.3 |
| Do you maintain attestations of completion for AI-specific training elements? | AC-9.2 |

## Section 9 — Model & Adversarial Robustness

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Do you have a documented model-update policy that includes rollback procedures? | AC-10.2, AC-10.3 |
| Are AI models that inform clinical decisions tested against adversarial inputs at a documented cadence (typically annual)? | AC-10.1, AC-10.2 |
| Are prompt-injection defenses (input sanitization, content filtering, sandboxing) in place for patient-facing or production AI systems? | AC-10.1, AC-10.5 |
| Are agentic AI tools' actions logged, rate-limited, and subject to circuit-breakers? | AC-10.5, AC-10.6 |

---

## Submitting AISS evidence in a cyber-insurance application

When responding to a healthcare cyber-insurance application:

1. **Run an AISS assessment.** Score the AC-1 through AC-10 sub-controls listed above.
2. **Attach the assessment summary.** The Ayliea platform produces a one-page summary suitable for carrier submission. Auditors can reproduce the scoring from the published AISS standard at github.com/Ayliea/aiss.
3. **Map your answers to the carrier's specific question wording.** Some carriers ask very precise questions ("Do you enforce MFA on all administrative interfaces?"). Use the carrier's wording in the application; cite the AISS sub-control evidence as supporting documentation.
4. **Flag any in-progress controls.** Carriers typically accept "in-flight remediation with documented completion plan" for controls scored at ML2-3 with an active improvement plan. Document the plan.

## Disclaimer

This crosswalk reflects typical carrier underwriting questions as observed in public broker materials and industry resources as of 2026-05-11. Carrier-specific underwriting is non-public and changes annually. **This document is not legal, insurance, or underwriting advice.** Consult your broker for carrier-specific application guidance.
