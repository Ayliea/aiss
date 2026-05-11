# Crosswalk — AISS × Financial-Services Cyber-Insurance Underwriting

**Crosswalk type:** Industry profile (carrier-baseline)
**Last verified:** 2026-05-11
**Scope:** Cyber-insurance underwriting questions commonly required of financial-services organizations operating AI systems in 2025-2026.

## Why this crosswalk exists

Financial-services organizations adopting AI face an unusually pointed insurance market:

1. **Concentrated regulatory pressure.** NYDFS Part 500 (cybersecurity), DORA (EU Digital Operational Resilience Act, fully effective 2025-01-17), and the SR 11-7-derived model-risk-management discipline at federally supervised institutions all impose AI-relevant control expectations. Carriers translate these into underwriting questions.
2. **AI-specific sub-limits and exclusions.** Cyber carriers writing for FinServ are adding sub-limits or carve-outs for AI-mediated fraud, trading-model exploitation, and model-extraction-driven IP loss. Demonstrated control maturity reduces premium and broadens coverage.
3. **Audit-grade evidence is rewarded.** FinServ orgs that can produce reproducible scoring against a recognized framework price below peers in the same risk class — particularly when scoring is auditor-verifiable, not vendor-attested.

AISS sub-controls map cleanly to most of what carriers ask. This crosswalk gives the firm one auditable artifact when answering the AI section of a cyber-insurance application, and gives carriers one auditable artifact to score against.

The crosswalk is **carrier-neutral**. Specific carrier ports (Coalition, At-Bay, Travelers, Beazley, Chubb, Hiscox, AIG, AXIS) will follow in separate crosswalk files as their FinServ-specific AI questions stabilize.

## Sources

This crosswalk draws on the following public sources for typical FinServ cyber-underwriting questions:

- NYDFS 23 NYCRR Part 500 (Cybersecurity Requirements for Financial Services Companies)
- EU Regulation 2022/2554 (DORA — Digital Operational Resilience Act)
- Federal Reserve SR 11-7 Guidance on Model Risk Management
- OCC Comptroller's Handbook — Model Risk Management
- FINRA Rule 2210 (Communications with the Public) and 3110 (Supervision)
- Coalition Cyber Risk Bulletins (public broker resources)
- At-Bay public broker FAQs and underwriting guides
- Marsh and Aon FinServ cyber market overviews (annual)

> When a carrier's question framing differs from the baseline below, prefer the carrier's exact wording in the application response and use the AISS sub-control evidence as the underlying control attestation.

---

## Section 1 — AI System Inventory & Model Risk Governance

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Do you maintain a documented inventory of AI models used in customer-facing, decisioning, or financial-reporting workflows? | AC-2.1, AC-2.2, AC-2.4 |
| Are AI models classified by materiality (e.g., SR 11-7 tiering) with high-tier models receiving enhanced governance? | AC-2.3, AC-2.5 |
| Is there a model risk management committee or designated MRM function with AI scope? | AC-1.1, AC-1.2 |
| Do you maintain documented AI/ML model risk policies aligned to SR 11-7, OCC handbook, or DORA expectations? | AC-1.4, AC-9.2 |
| Are models supporting trading, underwriting, fraud detection, or AML transaction monitoring inventoried separately with documented validation cadence? | AC-2.5, AC-10.2 |

## Section 2 — Sensitive Data Handling in AI

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Do you have controls preventing transmission of customer PII, MNPI, or trade-secret data to general-purpose AI tools? | AC-3.1, AC-3.4, AC-5.3 |
| Are AI prompts and outputs containing regulated financial data logged, retained, and protected at the same level as production data? | AC-3.5, AC-3.6, AC-8.1 |
| Have you reviewed AI provider data-handling commitments (training-data retention, secondary use, cross-border processing under GDPR / DORA)? | AC-3.1, AC-5.2, AC-5.3 |
| Is data minimization applied at the prompt/model layer, not just at surrounding applications? | AC-3.4, AC-3.6 |
| Is differential privacy or other de-identification applied before AI training/fine-tuning on customer or transaction data? | AC-3.2, AC-3.3, AC-10.4 |

## Section 3 — Access Control & Authentication

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Is MFA enforced for all access to AI tools and AI administration interfaces (NYDFS §500.12)? | AC-4.1, AC-4.5 |
| Are AI API keys and service-account tokens managed centrally with documented rotation policy? | AC-4.2, AC-4.3, AC-4.4 |
| Is least-privilege enforced for AI tool access by role (front office, ops, compliance, audit)? | AC-4.1, AC-4.2 |
| Are agentic AI tools restricted from invoking high-risk actions (trade execution, wire transfer, account changes) without human approval and step-up authentication? | AC-10.5, AC-10.6 |

## Section 4 — AI Supply-Chain & Vendor Risk

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Do you perform AI vendor risk assessment before procurement, separate from general SaaS vendor due diligence? | AC-5.1, AC-5.2 |
| Are AI model provenance (pre-training data, fine-tuning data, marketplace source) verified before deployment in production decisioning? | AC-5.2, AC-5.3, AC-10.4 |
| Do vendor contracts include AI-specific terms (training-data exclusion, output indemnity, model-change notification, audit rights)? | AC-5.3, AC-5.4 |
| Do you monitor for material changes to AI vendor products (model updates, terms changes, breach notifications)? Is this monitoring documented for examination? | AC-5.4, AC-8.3 |
| For DORA-scoped institutions: are AI providers classified as critical ICT third-party providers where applicable? | AC-5.1, AC-5.2 |

## Section 5 — Output Validation & Compliance Liability

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Are AI-generated customer communications reviewed against FINRA Rule 2210 / SEC Marketing Rule before publication? | AC-6.1, AC-6.2 |
| Do you have controls preventing hallucinated pricing, regulatory citations, or product features from being communicated to customers? | AC-6.1, AC-6.2, AC-6.3 |
| Are AI-generated outputs that may be used by customers (advisory chat, account summaries) marked as such? | AC-6.6 |
| Is RAG content (regulatory references, policy documents, product specifications) validated for source integrity? | AC-3.7, AC-6.1 |
| For trading-strategy outputs: are model predictions logged with the inputs that produced them for back-testing and supervision? | AC-6.1, AC-8.2 |

## Section 6 — Incident Response & Regulatory Notification

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Do AI-specific incidents (prompt-injection successes, model-output errors causing financial harm, training-data leak, model-extraction events) have a documented response procedure? | AC-7.1, AC-7.2, AC-7.3 |
| Does your NYDFS §500.17 / DORA / FINRA 4530 incident-reporting workflow account for AI-mediated incidents? | AC-7.4 |
| Are AI vendors contractually required to notify within 24-72 hours of AI-related security events affecting your data or models? | AC-5.3, AC-7.4 |
| For MNPI-adjacent incidents: is the incident-response procedure coordinated with insider-trading surveillance? | AC-7.3, AC-8.3 |

## Section 7 — Monitoring, Logging & Audit

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Are AI tool usage logs retained at minimum 6 years (FINRA 4511, SEC 17a-4) and protected from tampering? | AC-8.1, AC-8.2 |
| Are anomalous AI-tool patterns (off-hours access, geo-anomalies, abnormal volumes, suspicious extraction queries) monitored and alerted? | AC-8.3 |
| Can you produce evidence of AI tool usage for a given user during a specified time window for a regulatory inquiry or supervisory review? | AC-8.1, AC-8.2 |

## Section 8 — Workforce Awareness & Training

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Does your annual mandatory training include AI-specific modules (acceptable use, MNPI handling, recognized AI risks, regulatory communication standards)? | AC-9.1, AC-9.2 |
| Are front-office and trading staff trained on AI hallucination recognition and the dangers of acting on unverified AI output? | AC-9.1, AC-9.3 |
| Do you maintain attestations of completion for AI-specific training elements? | AC-9.2 |

## Section 9 — Model & Adversarial Robustness

| Carrier question (typical) | AISS sub-controls |
|---|---|
| Do you have a documented model-update policy that includes rollback procedures and pre-production validation (aligned to SR 11-7 ongoing monitoring)? | AC-10.2, AC-10.3 |
| Are AI models used in fraud detection, AML, or credit underwriting tested against adversarial inputs at a documented cadence (typically annual or per significant change)? | AC-10.1, AC-10.2 |
| Are prompt-injection defenses (input sanitization, content filtering, sandboxing) in place for customer-facing and trading-floor AI systems? | AC-10.1, AC-10.5 |
| Are agentic AI tools' actions logged, rate-limited, and subject to circuit-breakers? Is there a documented kill-switch procedure? | AC-10.5, AC-10.6 |
| For models used in financial-reporting workflows (SOX-relevant): is model integrity attested at a frequency aligned to internal-control testing? | AC-10.2, AC-10.4 |

---

## Submitting AISS evidence in a cyber-insurance application

When responding to a FinServ cyber-insurance application:

1. **Run an AISS assessment.** Score the AC-1 through AC-10 sub-controls listed above.
2. **Attach the assessment summary.** The Ayliea platform produces a one-page summary suitable for carrier submission. Auditors and supervisors can reproduce the scoring from the published AISS standard at github.com/Ayliea/aiss.
3. **Map your answers to the carrier's specific question wording.** Some carriers ask very precise questions ("Do you enforce MFA on all administrative interfaces?"). Use the carrier's wording in the application; cite the AISS sub-control evidence as supporting documentation.
4. **Flag in-progress controls + planned-remediation dates.** Carriers typically accept "in-flight remediation with documented completion plan" for controls scored at ML2-3 with an active improvement plan. This also aligns with SR 11-7 / DORA expectations on ongoing-monitoring.

## Disclaimer

This crosswalk reflects typical carrier underwriting questions as observed in public broker materials and industry resources as of 2026-05-11. Carrier-specific underwriting is non-public and changes annually. **This document is not legal, insurance, regulatory, or underwriting advice.** Consult your broker, compliance counsel, and primary regulators for institution-specific guidance.
