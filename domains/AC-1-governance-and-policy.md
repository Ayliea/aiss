# AC-1 — AI Governance and Policy

**Control count:** 6

## Overview

This domain covers AC-1 sub-controls in the Ayliea AI Security Standard. See the [machine-readable spec](../spec/aiss-v1.2.json) for the canonical definition.

## Sub-controls

### AC-1.1 — AI Acceptable Use Policy (SHALL)

**Requirement:** The organization SHALL maintain a formal, board- or executive-approved AI Acceptable Use Policy (AUP) that defines permitted and prohibited uses of AI tools, specifies data handling requirements for AI interactions, and establishes consequences for policy violations.

**Assessment question:** Does the organization maintain a formal, board- or executive-approved AI Acceptable Use Policy (AUP) that defines permitted and prohibited uses of AI tools, specifies data handling requirements for AI interactions, and establishes consequences for policy violations?

**Implementation guidance:** The AI AUP should address all categories of AI use: sanctioned enterprise tools, embedded AI features in existing SaaS platforms, personal AI tool usage for business purposes, and explicitly prohibited uses. The policy must be specific enough to be actionable. Stating that employees should use AI responsibly is insufficient. The policy should enumerate what data classifications may and may not be submitted to AI systems, which tools are approved, and what review processes apply to AI-generated outputs used in business decisions.

**Testing procedure:**

1. Obtain the current AI Acceptable Use Policy (AUP) document
2. Verify executive or board approval and confirm the publication date is within the past 12 months
3. Confirm the AUP addresses all required topics: approved AI tools, prohibited uses, data handling requirements, and consequences for violation
4. Select a random sample of five employees across different departments and verify they can locate and describe the key provisions of the AUP
5. Review policy exception or waiver requests from the past 12 months and confirm each was formally documented and approved
6. Verify the AUP is accessible to all employees through the organization's policy management system or intranet

**Evidence requirements:**

- Current AI AUP document with approval signatures and effective date
- Policy distribution records or acknowledgment logs
- Policy exception requests and approvals
- Documented policy violations and remediation actions

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.PO-01, GV.PO-02 |
| NIST AI RMF | Govern 1.1, 1.2, 1.7 |
| NIST AI 600-1 (GAI Profile) | GV-1.1-001, GV-1.4-002, GV-6.1-010 (Data Privacy, Intellectual Property, Information Security) |
| CIS Controls v8.1 | CIS 1, CIS 2 |
| ISO 27001:2022 | A.5.1 |
| EU AI Act | Art. 9, 26 |
| Colorado AI Act | §6-1-1702(2) |

---

### AC-1.2 — AI Governance Oversight Structure (SHALL)

**Requirement:** The organization SHALL designate a governance body or individual with explicit authority and accountability for AI security oversight, including approval of new AI system deployments, review of AI-related risk assessments, and escalation of AI security incidents.

**Assessment question:** Does the organization designate a governance body or individual with explicit authority and accountability for AI security oversight, including approval of new AI system deployments, review of AI-related risk assessments, and escalation of AI security incidents?

**Implementation guidance:** For organizations with fewer than 200 employees, this may be an individual (such as the CISO, CTO, or a designated AI security lead) rather than a committee. The critical requirement is that someone has named accountability. The governance function must have authority to approve or reject AI tool requests, require risk assessments before deployment, and mandate remediation of identified control gaps. Meeting cadence should be no less than quarterly, with ad hoc sessions triggered by material AI security events.

**Testing procedure:**

1. Obtain the charter, terms of reference, or role description defining AI governance authority
2. Verify the governance body includes representation from security, legal, IT, and business stakeholders
3. Review meeting minutes or decision logs for the past 12 months to confirm the governance body convened at least quarterly
4. Select three AI-related decisions made in the past 12 months and trace each to a documented governance approval
5. Verify that governance responsibilities are reflected in position descriptions or performance objectives for designated individuals
6. Confirm escalation paths exist for AI governance decisions that exceed the authority of the designated body

**Evidence requirements:**

- Governance charter or terms of reference
- Meeting minutes or decision logs
- AI tool approval and rejection records
- Organizational chart showing reporting lines for AI governance

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.RR-01, GV.RR-02, GV.OV-01 |
| NIST AI RMF | Govern 1.3, 2.1, 2.3 |
| NIST AI 600-1 (GAI Profile) | GV-2.1-001, GV-2.1-003, GV-3.2-001, GV-4.1-003 (Human-AI Configuration, Value Chain and Component Integration, Information Security) |
| CIS Controls v8.1 | CIS 1 |
| ISO 27001:2022 | A.5.2, A.5.4 |
| EU AI Act | Art. 9, 17, 26 |

---

### AC-1.3 — AI Risk Appetite Statement (SHALL)

**Requirement:** The organization SHALL document its risk appetite for AI adoption, specifying acceptable risk thresholds for data exposure, AI-driven decision-making, and regulatory compliance, aligned to the broader enterprise risk management framework.

**Assessment question:** Does the organization document its risk appetite for AI adoption, specifying acceptable risk thresholds for data exposure, AI-driven decision-making, and regulatory compliance, aligned to the broader enterprise risk management framework?

**Implementation guidance:** The risk appetite statement should be concrete, not aspirational. It should specify which data classifications are permissible in AI interactions (e.g., public and internal only, or up to confidential with specific controls), whether AI outputs may be used in regulated decision-making without human review, and what level of vendor risk is acceptable for AI service providers. This statement directly informs control implementation priorities and maturity targets across all other domains.

**Testing procedure:**

1. Obtain the AI risk appetite statement
2. Verify it specifies acceptable and unacceptable AI use cases by risk category (e.g., data sensitivity, decision impact)
3. Confirm the statement is referenced in at least two AI tool approval decisions made in the past 12 months
4. Verify alignment between the AI risk appetite statement and the organization's enterprise risk management framework
5. Confirm the statement was approved by senior leadership and review the approval date

**Evidence requirements:**

- Documented AI risk appetite statement
- Evidence of risk appetite being applied in AI governance decisions
- Enterprise risk register entries for AI-related risks

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.RM-01, GV.RM-02, GV.RM-03 |
| NIST AI RMF | Govern 1.1, 1.4, 1.5 |
| NIST AI 600-1 (GAI Profile) | GV-1.3-001, GV-1.3-002, GV-1.3-006, GV-1.3-007 (Information Integrity, Information Security, CBRN Information or Capabilities, Dangerous Violent or Hateful Content) |
| CIS Controls v8.1 | CIS 1 |
| ISO 27001:2022 | A.5.1, A.5.2 |
| EU AI Act | Art. 9(1) |
| Colorado AI Act | §6-1-1703(3)(a) |

---

### AC-1.4 — AI Ethics and Responsible Use Guidelines (SHALL)

**Requirement:** The organization SHALL establish guidelines for the ethical and responsible use of AI, addressing fairness, transparency, accountability, and the potential for algorithmic discrimination in AI-driven processes.

**Assessment question:** Does the organization establish guidelines for the ethical and responsible use of AI, addressing fairness, transparency, accountability, and the potential for algorithmic discrimination in AI-driven processes?

**Implementation guidance:** Ethics guidelines should be practical and enforceable, not purely aspirational. They should address specific scenarios relevant to the organization: whether AI may be used to screen job applicants, evaluate customer creditworthiness, generate client-facing communications without disclosure, or make decisions that materially affect individuals. The guidelines must account for the algorithmic discrimination provisions of the Colorado AI Act and the EU AI Act's transparency and human oversight requirements for high-risk systems.

**Testing procedure:**

1. Obtain the AI ethics and responsible use guidelines
2. Verify coverage of all high-risk AI use cases identified during the assessment
3. Confirm guidelines address applicable regulatory requirements (EU AI Act transparency, Colorado AI Act algorithmic discrimination)
4. Review at least two instances where the guidelines were applied to an AI adoption or deployment decision
5. Verify that a process exists for employees to raise ethical concerns about AI usage

**Evidence requirements:**

- AI ethics and responsible use guidelines document
- Records of ethics review for high-risk AI use cases
- Consumer disclosure templates or notices related to AI use
- Bias audit or impact assessment records

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.OC-04, GV.PO-01 |
| NIST AI RMF | Govern 1.6, 1.7, Map 1.5 |
| NIST AI 600-1 (GAI Profile) | GV-1.2-001, GV-1.4-001, GV-3.2-003, GV-5.1-001 (Information Integrity, Harmful Bias and Homogenization, Human-AI Configuration, Obscene Degrading and/or Abusive Content) |
| CIS Controls v8.1 | CIS 1 |
| ISO 27001:2022 | A.5.1 |
| EU AI Act | Art. 4, 13, 14, 15, 27 |
| Colorado AI Act | §6-1-1703(2), (4) |

---

### AC-1.5 — AI Policy Review and Maintenance Cadence (SHALL)

**Requirement:** The organization SHALL review and update all AI-related policies at least annually, or within 30 days of a material change in AI regulatory requirements, significant AI security incident, or substantial change to the organization's AI technology landscape.

**Assessment question:** Does the organization review and update all AI-related policies at least annually, or within 30 days of a material change in AI regulatory requirements, significant AI security incident, or substantial change to the organization's AI technology landscape?

**Implementation guidance:** The annual review cycle must be documented and tracked. Policy updates triggered by regulatory changes (such as the Colorado AI Act effective date of June 30, 2026, or EU AI Act high-risk obligations effective August 2, 2026) should be proactively scheduled rather than reactive. Each review should assess whether current policies adequately address new AI tools adopted since the last review, changes in the threat landscape, lessons learned from incidents or near-misses, and evolving regulatory requirements.

**Testing procedure:**

1. Obtain the documented AI policy review schedule
2. Verify that all AI-related policies have been reviewed within the past 12 months
3. Review change logs for each AI policy and confirm that substantive changes were tracked with date, author, and approval
4. Identify any regulatory changes affecting AI (e.g., EU AI Act enforcement milestones, Colorado AI Act provisions) and verify that corresponding policy updates were initiated within 90 days of the regulatory change
5. Confirm that policy review outcomes are reported to the AI governance body

**Evidence requirements:**

- Policy review schedule with documented completion dates
- Policy change logs with rationale for changes
- Evidence of regulatory monitoring for AI-related requirements

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.PO-02, ID.IM-02 |
| NIST AI RMF | Govern 1.2, 5.1, 5.2 |
| NIST AI 600-1 (GAI Profile) | GV-1.5-002, GV-1.5-003, GV-4.1-001 (Information Security, Information Integrity, Confabulation) |
| CIS Controls v8.1 | CIS 1 |
| ISO 27001:2022 | A.5.1, A.5.36 |
| EU AI Act | Art. 9(3), 72 |
| Colorado AI Act | §6-1-1703(3) |

---

### AC-1.6 — Regulatory Compliance Program (SHALL)

**Requirement:** The organization SHALL maintain an inventory of applicable AI regulations and map organizational AI activities to specific regulatory requirements, identifying compliance gaps and tracking remediation progress.

**Assessment question:** Does the organization maintain an inventory of applicable AI regulations and map organizational AI activities to specific regulatory requirements, identifying compliance gaps and tracking remediation progress?

**Implementation guidance:** The compliance program must go beyond awareness to active tracking. For each applicable regulation, the organization should document which AI systems fall under its scope, which requirements apply, the current compliance status of each requirement, and planned remediation actions with timelines for any gaps. Priority attention should be given to regulations with near-term effective dates, particularly the Colorado AI Act (effective June 30, 2026) and EU AI Act high-risk system obligations (effective August 2, 2026).

**Testing procedure:**

1. Obtain the compliance program documentation addressing AI-specific regulatory obligations
2. Verify the program identifies all applicable AI regulations by jurisdiction (EU AI Act, Colorado AI Act, sector-specific requirements)
3. Confirm a compliance monitoring calendar exists with key regulatory dates and milestones
4. Review evidence that compliance obligations are tracked and assigned to specific owners
5. Verify that the compliance program includes a process for monitoring new or amended AI regulations
6. Confirm that compliance status is reported to the governance body at least quarterly

**Evidence requirements:**

- Regulatory applicability inventory
- AI system to regulation mapping
- Compliance gap register with remediation timelines
- Evidence of regulatory monitoring activities

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.OC-03, GV.OC-05 |
| NIST AI RMF | Govern 1.1, 1.2 |
| NIST AI 600-1 (GAI Profile) | GV-1.1-001, GV-1.4-002, MP-4.1-003 (Data Privacy, Intellectual Property, Information Security) |
| CIS Controls v8.1 | CIS 1 |
| ISO 27001:2022 | A.5.31, A.5.36 |
| EU AI Act | Art. 8, 9, 16, 17 |
| Colorado AI Act | §6-1-1702, 1703 |

---

