# AC-7 — AI Incident Response

**Control count:** 5

## Overview

This domain covers AC-7 sub-controls in the Ayliea AI Security Standard. See the [machine-readable spec](../spec/aiss-v1.2.json) for the canonical definition.

## Sub-controls

### AC-7.1 — AI-Specific Incident Response Playbooks (SHALL)

**Requirement:** The organization SHALL develop and maintain incident response playbooks that address AI-specific incident types, including data exposure through AI prompts, AI-generated output failures with business impact, unauthorized AI model access or manipulation, AI vendor security incidents, and algorithmic discrimination discovery.

**Assessment question:** Does the organization develop and maintain incident response playbooks that address AI-specific incident types, including data exposure through AI prompts, AI-generated output failures with business impact, unauthorized AI model access or manipulation, AI vendor security incidents, and algorithmic discrimination discovery?

**Implementation guidance:** AI incident playbooks should be integrated with the organization's broader incident response plan. Each playbook should define the incident trigger criteria, initial containment actions, investigation procedures, evidence preservation requirements, communication templates (internal and external), escalation paths, and recovery procedures. Playbooks should be tested through tabletop exercises at least annually.

**Testing procedure:**

1. Obtain AI-specific incident response playbooks
2. Verify playbooks address at least the following scenario types: data leakage through AI, adversarial manipulation, model failure, bias-related incidents, and unauthorized AI deployment
3. Verify each playbook defines: trigger criteria, initial response steps, containment actions, communication requirements, and escalation paths
4. Confirm that playbooks reference applicable regulatory notification requirements (EU AI Act Art. 73, Colorado AI Act)
5. Verify that playbooks were tested through tabletop exercise or simulation within the past 12 months

**Evidence requirements:**

- AI incident response playbooks
- Tabletop exercise records with findings and action items
- Integration documentation with the broader incident response plan

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | RS.MA-01, RS.MA-03 |
| NIST AI RMF | Manage 3.1, 3.2, 4.1 |
| NIST AI 600-1 (GAI Profile) | GV-4.3-002, GV-6.2-003, MG-2.3-001, MG-4.2-002, MG-4.3-002 (Information Security, Value Chain and Component Integration, Human-AI Configuration, Dangerous Violent or Hateful Content) |
| CIS Controls v8.1 | CIS 17 |
| ISO 27001:2022 | A.5.24, A.5.25, A.5.26 |
| EU AI Act | Art. 73 |
| Colorado AI Act | §6-1-1702(5), 1703(5) |
| MITRE ATLAS | AML.T0051, AML.T0010, AML.T0018 |

---

### AC-7.2 — AI Incident Escalation and Communication (SHALL)

**Requirement:** The organization SHALL define clear escalation paths for AI security incidents, including criteria for escalating to executive leadership, legal counsel, external regulators, and affected data subjects.

**Assessment question:** Does the organization define clear escalation paths for AI security incidents, including criteria for escalating to executive leadership, legal counsel, external regulators, and affected data subjects?

**Implementation guidance:** Escalation criteria should be specific and measurable. For example: any confirmed exposure of restricted data through an AI service escalates to the CISO within 1 hour and to legal counsel within 4 hours. Any discovery of algorithmic discrimination in a high-risk AI system triggers notification to the Colorado Attorney General within 90 days (per the Colorado AI Act). Communication templates should be prepared for each escalation tier to enable rapid response without requiring real-time drafting under pressure.

**Testing procedure:**

1. Obtain the AI incident escalation matrix
2. Verify it defines escalation paths for each incident severity level with named roles and contact information
3. Verify communication templates exist for internal stakeholders, affected customers, and regulators
4. Review at least one AI incident from the past 12 months (or simulate one) and trace the escalation path taken against the documented matrix
5. Confirm that escalation procedures are accessible to all personnel likely to detect AI incidents

**Evidence requirements:**

- Escalation path documentation with criteria
- Pre-drafted communication templates
- Escalation records for past incidents (if applicable)

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | RS.CO-02, RS.CO-03 |
| NIST AI RMF | Manage 3.2 |
| NIST AI 600-1 (GAI Profile) | GV-2.1-001, MG-2.4-001, MG-2.4-002, MG-4.3-001 (Human-AI Configuration, Value Chain and Component Integration, Information Security) |
| CIS Controls v8.1 | CIS 17 |
| ISO 27001:2022 | A.5.24, A.5.25, A.5.26 |
| EU AI Act | Art. 73 |
| Colorado AI Act | §6-1-1702(5), 1703(5) |

---

### AC-7.3 — AI Incident Classification and Severity (SHALL)

**Requirement:** The organization SHALL classify AI security incidents using a severity framework that accounts for data sensitivity, blast radius, regulatory impact, and whether the incident involves algorithmic discrimination or affects consumer rights.

**Assessment question:** Does the organization classify AI security incidents using a severity framework that accounts for data sensitivity, blast radius, regulatory impact, and whether the incident involves algorithmic discrimination or affects consumer rights?

**Implementation guidance:** AI incident severity classification should integrate with the organization's existing incident severity framework while accounting for AI-specific factors. Critical severity indicators include exposure of restricted data (PHI, credentials) through AI services, confirmed algorithmic discrimination in consequential decisions, and AI vendor breach affecting organizational data. High severity indicators include exposure of confidential data through AI prompts, AI output failures affecting client-facing communications, and unauthorized model access or manipulation.

**Testing procedure:**

1. Obtain the AI incident classification and severity framework
2. Verify the framework defines severity levels with specific criteria for each level
3. Verify classification criteria include data sensitivity, number of affected users, regulatory implications, and operational impact
4. Select three AI incidents (or simulated scenarios) and verify consistent classification against the framework
5. Confirm that classification drives response timelines and resource allocation per the incident response playbooks

**Evidence requirements:**

- AI incident classification framework
- Severity criteria documentation
- Classification records for past AI incidents (if applicable)

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | RS.AN-02, RS.AN-03 |
| NIST AI RMF | Manage 3.1 |
| NIST AI 600-1 (GAI Profile) | GV-4.3-002, MG-2.4-002, MG-2.4-004 (Information Security) |
| CIS Controls v8.1 | CIS 17 |
| ISO 27001:2022 | A.5.25 |
| EU AI Act | Art. 73 |
| Colorado AI Act | §6-1-1702(5), 1703(5) |

---

### AC-7.4 — Post-Incident Review and Lessons Learned (SHALL)

**Requirement:** The organization SHALL conduct a post-incident review for all AI security incidents rated high or critical severity, documenting root causes, contributing factors, remediation actions, and improvements to prevent recurrence.

**Assessment question:** Does the organization conduct a post-incident review for all AI security incidents rated high or critical severity, documenting root causes, contributing factors, remediation actions, and improvements to prevent recurrence?

**Implementation guidance:** Post-incident reviews should be conducted within 14 days of incident closure. The review should identify the root cause (technical, procedural, or human), evaluate the effectiveness of the incident response, identify control gaps that contributed to the incident, recommend specific improvements with assigned ownership and timelines, and update playbooks and procedures based on lessons learned.

**Testing procedure:**

1. Obtain post-incident review (PIR) procedures for AI incidents
2. Verify that PIRs are required for all AI incidents classified at severity level 2 or above
3. Review the most recent AI-related PIR and verify it was completed within 30 days of incident closure
4. Confirm the PIR includes root cause analysis, contributing factors, corrective actions, and action item owners with deadlines
5. Verify that PIR findings are reported to the governance body and tracked to completion

**Evidence requirements:**

- Post-incident review reports
- Recommendation tracking with implementation status
- Updated playbooks and procedures reflecting lessons learned

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | RS.AN-08, ID.IM-01, ID.IM-02 |
| NIST AI RMF | Manage 4.2 |
| NIST AI 600-1 (GAI Profile) | GV-1.5-002, MG-4.2-002, MG-4.3-001, MG-4.3-002 (Information Security, Human-AI Configuration, Information Integrity, Confabulation) |
| CIS Controls v8.1 | CIS 17 |
| ISO 27001:2022 | A.5.27, A.5.28 |
| EU AI Act | Art. 73 |
| Colorado AI Act | §6-1-1703(3) |

---

### AC-7.5 — Regulatory Notification Procedures (SHALL)

**Requirement:** The organization SHALL maintain documented procedures for notifying regulators and affected individuals of AI security incidents as required by applicable law, including specific notification timelines and content requirements for each applicable regulation.

**Assessment question:** Does the organization maintain documented procedures for notifying regulators and affected individuals of AI security incidents as required by applicable law, including specific notification timelines and content requirements for each applicable regulation?

**Implementation guidance:** Regulatory notification requirements vary by jurisdiction and regulation. Key requirements include the Colorado AI Act which requires deployers who discover algorithmic discrimination to notify the Attorney General within 90 days, the EU AI Act which requires providers of high-risk AI systems to report serious incidents to market surveillance authorities, GDPR which requires breach notification to supervisory authorities within 72 hours and to affected individuals without undue delay when the breach is likely to result in high risk, and HIPAA which requires notification to HHS and affected individuals within 60 days of discovery for breaches of unsecured PHI. Procedures should pre-identify the regulatory bodies to notify, the required content of each notification, and the individuals authorized to submit notifications.

**Testing procedure:**

1. Obtain regulatory notification procedures for AI incidents
2. Verify procedures include notification timelines for all applicable regulations (EU AI Act Art. 73: without undue delay, Colorado AI Act: AG notification within 90 days of discovery of algorithmic discrimination)
3. Verify notification templates exist and have been reviewed by legal counsel
4. Confirm that a regulatory notification decision tree exists to determine when notification is required
5. Review any regulatory notifications filed in the past 12 months and verify compliance with documented timelines

**Evidence requirements:**

- Regulatory notification procedures by jurisdiction
- Notification timeline matrix
- Authorized notifier designations
- Notification records for past incidents (if applicable)

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | RS.CO-02, RS.CO-03 |
| NIST AI RMF | Manage 3.2, Govern 1.1 |
| NIST AI 600-1 (GAI Profile) | GV-2.1-001, GV-6.2-003, MG-4.3-001, MG-4.3-003 (Information Security, Data Privacy, Value Chain and Component Integration) |
| CIS Controls v8.1 | CIS 17 |
| ISO 27001:2022 | A.5.24, A.5.26 |
| EU AI Act | Art. 73 |
| Colorado AI Act | §6-1-1702(5), 1703(5) |

---

