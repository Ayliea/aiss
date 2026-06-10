# AC-9 — AI Training and Awareness

**Control count:** 5

## Overview

This domain covers AC-9 sub-controls in the Ayliea AI Security Standard. See the [machine-readable spec](../spec/aiss-v1.3.json) for the canonical definition.

## Sub-controls

### AC-9.1 — AI Security Awareness Program (SHALL)

**Requirement:** The organization SHALL include AI-specific security topics in its security awareness program, delivered to all employees within 30 days of hire and refreshed at least annually, covering AI-related risks, organizational policies, and individual responsibilities.

**Assessment question:** Does the organization include AI-specific security topics in its security awareness program, delivered to all employees within 30 days of hire and refreshed at least annually, covering AI-related risks, organizational policies, and individual responsibilities?

**Implementation guidance:** AI security awareness content should cover common AI security risks (data exposure through prompts, hallucination risks, shadow AI dangers, social engineering using AI), organizational AI policies (acceptable use, approved tools, data classification requirements), individual responsibilities (what to do and what not to do with AI tools), how to report suspected AI security incidents, and examples of both proper and improper AI use relevant to the employee's role. Training should be engaging and practical, not just a compliance checkbox.

**Testing procedure:**

1. Obtain the AI security awareness training program materials
2. Verify that training covers: AI-specific risks, data handling for AI interactions, the AI AUP, social engineering involving AI, and incident reporting procedures
3. Verify that all employees with access to AI systems completed the training within the past 12 months
4. Review training completion records and calculate the completion rate
5. Verify that new employees receive AI security training within 30 days of onboarding

**Evidence requirements:**

- AI security awareness training materials
- Training delivery and completion records
- Assessment or quiz results
- New hire training timeline compliance records

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.AT-01, PR.AT-02 |
| NIST AI RMF | Govern 2.2, 3.1 |
| NIST AI 600-1 (GAI Profile) | MP-3.4-002, MP-3.4-003 (Information Integrity, Human-AI Configuration) |
| CIS Controls v8.1 | CIS 14 |
| ISO 27001:2022 | A.6.3 |
| EU AI Act | Art. 4 |
| MITRE ATLAS | AML.T0011, AML.T0052 |

---

### AC-9.2 — Role-Based AI Training (SHALL)

**Requirement:** The organization SHALL provide additional role-specific AI security training to personnel in high-risk roles, including IT administrators managing AI platforms, developers integrating AI APIs, data scientists working with models, and personnel using AI in regulated decision-making.

**Assessment question:** Does the organization provide additional role-specific AI security training to personnel in high-risk roles, including IT administrators managing AI platforms, developers integrating AI APIs, data scientists working with models, and personnel using AI in regulated decision-making?

**Implementation guidance:** Role-based training should provide deeper technical content relevant to each role. IT administrators should receive training on AI platform security configuration, access control, and monitoring. Developers should receive training on secure AI API integration, secrets management, and prompt injection defense. Data scientists should receive training on model security, adversarial testing, and bias detection. Regulated decision-makers should receive training on human review requirements, output validation, and applicable regulatory obligations.

**Testing procedure:**

1. Obtain role-based AI training curricula for each designated role (e.g., AI developers, administrators, power users, executives)
2. Verify that training content addresses role-specific risks and responsibilities
3. Select three individuals from different roles and verify they completed the training appropriate to their role within the past 12 months
4. Verify that training is updated when roles change or when new AI systems are deployed
5. Confirm that training effectiveness is assessed (e.g., quiz scores, simulation results)

**Evidence requirements:**

- Role-specific AI training curricula
- Training completion records by role
- Training update logs following platform or regulatory changes

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.AT-01, PR.AT-02 |
| NIST AI RMF | Govern 2.2, 3.1 |
| NIST AI 600-1 (GAI Profile) | GV-2.1-003, MP-3.4-003, MP-3.4-006 (Human-AI Configuration, Information Integrity, Harmful Bias and Homogenization, Dangerous Violent or Hateful Content) |
| CIS Controls v8.1 | CIS 14 |
| ISO 27001:2022 | A.6.3 |
| EU AI Act | Art. 4, 14, 26 |

---

### AC-9.3 — AI Acceptable Use Policy Communication (SHALL)

**Requirement:** The organization SHALL ensure that the AI Acceptable Use Policy is communicated to all employees with documented acknowledgment, and that policy updates are communicated within 30 days of approval with re-acknowledgment required.

**Assessment question:** Does the organization ensure that the AI Acceptable Use Policy is communicated to all employees with documented acknowledgment, and that policy updates are communicated within 30 days of approval with re-acknowledgment required?

**Implementation guidance:** Policy communication should go beyond making the document available on an intranet. Active communication methods include dedicated email notifications with summary of key requirements, team meeting discussions led by managers, new hire orientation coverage, and acknowledgment mechanisms that confirm the employee has read and understood the policy (not just clicked a button).

**Testing procedure:**

1. Obtain evidence of the most recent AUP communication to all employees
2. Verify that the communication occurred within the past 12 months and within 30 days of any AUP revision
3. Review acknowledgment records and calculate the acknowledgment rate (target: 100% of active employees)
4. Verify that new employees acknowledge the AUP during onboarding
5. Confirm that acknowledgment records are retained for the duration of employment plus one year

**Evidence requirements:**

- AUP communication records and distribution logs
- Employee acknowledgment records with dates
- Re-acknowledgment records following policy updates
- Communication templates and distribution methods

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.AT-01, GV.PO-01 |
| NIST AI RMF | Govern 1.7, 2.2 |
| NIST AI 600-1 (GAI Profile) | GV-1.1-001, GV-1.4-002, GV-6.1-010 (Data Privacy, Intellectual Property, Value Chain and Component Integration) |
| CIS Controls v8.1 | CIS 14 |
| ISO 27001:2022 | A.5.1, A.6.2, A.6.3 |
| EU AI Act | Art. 4, 14 |

---

### AC-9.4 — AI Threat Awareness (SHALL)

**Requirement:** The organization SHALL include AI-specific threat vectors in its security awareness program, covering social engineering using AI-generated content (deepfakes, voice cloning, AI-generated phishing), AI-enabled attack techniques, and the risks of adversarial manipulation of organizational AI systems.

**Assessment question:** Does the organization include AI-specific threat vectors in its security awareness program, covering social engineering using AI-generated content (deepfakes, voice cloning, AI-generated phishing), AI-enabled attack techniques, and the risks of adversarial manipulation of organizational AI systems?

**Implementation guidance:** The AI threat landscape is evolving rapidly. Training should cover deepfake audio and video used for social engineering (e.g., AI-generated voice calls impersonating executives for wire fraud), AI-generated phishing content that is more convincing and personalized than traditional phishing, prompt injection attacks targeting organizational AI systems, data poisoning risks for organizations training or fine-tuning models, and AI-assisted credential stuffing and brute force attacks. Training content should be updated at least semi-annually to reflect emerging threats.

**Testing procedure:**

1. Obtain AI threat awareness training or communication materials
2. Verify that content addresses current AI-specific threats: prompt injection, data poisoning, model manipulation, deepfakes, and AI-powered social engineering
3. Verify that threat awareness communications were issued at least twice in the past 12 months
4. Confirm that threat awareness content is updated based on emerging threat intelligence
5. Verify that employees can identify the reporting channel for suspected AI-related threats

**Evidence requirements:**

- AI threat awareness training materials
- Content update logs showing currency
- Employee assessment results
- Phishing simulation results incorporating AI-generated content (if applicable)

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.AT-01, PR.AT-02 |
| NIST AI RMF | Govern 3.1, Map 5.1 |
| NIST AI 600-1 (GAI Profile) | GV-3.2-005, MP-1.1-003, MP-3.4-002, MS-2.7-007 (Information Security, Dangerous Violent or Hateful Content, Information Integrity) |
| CIS Controls v8.1 | CIS 14 |
| ISO 27001:2022 | A.6.3, A.5.7 |
| EU AI Act | Art. 4, 15 |
| Colorado AI Act | §6-1-1703(3) |
| MITRE ATLAS | AML.T0052, AML.T0100, AML.T0073 |

---

### AC-9.5 — Executive and Board AI Literacy (SHALL)

**Requirement:** The organization SHALL ensure that executive leadership and board members (or equivalent governing body) receive AI literacy training at least annually, covering AI capabilities and limitations, organizational AI risk exposure, regulatory obligations, and the governance body's oversight responsibilities for AI systems.

**Assessment question:** Does the organization ensure that executive leadership and board members (or equivalent governing body) receive AI literacy training at least annually, covering AI capabilities and limitations, organizational AI risk exposure, regulatory obligations, and the governance body's oversight responsibilities for AI systems?

**Implementation guidance:** EU AI Act Article 4 explicitly requires providers and deployers to ensure that their staff and other persons dealing with AI systems on their behalf have a sufficient level of AI literacy. For mid-market organizations, this obligation extends to the executive team and board members who make strategic decisions about AI adoption and bear governance responsibilities. Training should be tailored to the audience: executives and board members do not need technical depth on model architectures but must understand the organizational risk implications of AI adoption, the regulatory landscape (EU AI Act timelines, Colorado AI Act obligations), the financial exposure from AI incidents, and their specific oversight responsibilities under the organization's AI governance framework. Training should be delivered annually, with ad-hoc updates when significant regulatory changes occur or when the organization adopts AI in a new high-risk use case.

**Testing procedure:**

1. Obtain executive and board AI literacy training materials and delivery records
2. Verify that training content covers AI capabilities and limitations, organizational AI risk exposure, applicable regulatory obligations, and governance oversight responsibilities
3. Confirm that all members of the executive team and governing body completed the training within the past 12 months
4. Verify that training is tailored to a non-technical executive audience rather than repurposed from general employee training
5. Review whether ad-hoc training updates were delivered in response to significant regulatory changes or new high-risk AI deployments within the past 12 months

**Evidence requirements:**

- Executive AI literacy training materials
- Training delivery and completion records for all executive and board members
- Training update logs tied to regulatory or organizational changes

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.OV-01, GV.RR-01 |
| NIST AI RMF | Govern 2.3, 1.4 |
| NIST AI 600-1 (GAI Profile) | GV-2.1-003, GV-4.1-003, MP-3.4-002 (Human-AI Configuration, Value Chain and Component Integration, Information Integrity) |
| CIS Controls v8.1 | CIS 14 |
| ISO 27001:2022 | A.5.4, A.6.3 |
| EU AI Act | Art. 4 |
| Colorado AI Act | §6-1-1703(2) |

---

