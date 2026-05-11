# AC-5 — AI Supply Chain Security

**Control count:** 5

## Overview

This domain covers AC-5 sub-controls in the Ayliea AI Security Standard. See the [machine-readable spec](../spec/aiss-v1.2.json) for the canonical definition.

## Sub-controls

### AC-5.1 — AI Vendor Risk Assessment (SHALL)

**Requirement:** The organization SHALL conduct a security risk assessment for each AI vendor before deployment and annually thereafter, evaluating the vendor's data handling practices, security posture, compliance certifications, and contractual data protection commitments.

**Assessment question:** Does the organization conduct a security risk assessment for each AI vendor before deployment and annually thereafter, evaluating the vendor's data handling practices, security posture, compliance certifications, and contractual data protection commitments?

**Implementation guidance:** The vendor risk assessment should cover security certifications (SOC 2 Type II, ISO 27001, etc.), data handling and retention policies, model training practices (whether customer data is used for training and opt-out mechanisms), sub-processor relationships and data sharing, incident response capabilities and notification commitments, business continuity and disaster recovery provisions, and geographic data processing locations. Assessment depth should be proportional to the data sensitivity and business criticality of the AI service.

**Testing procedure:**

1. Obtain the AI vendor risk assessment methodology
2. Verify that the methodology addresses data handling practices, security certifications, breach history, subprocessor usage, and AI model training practices
3. Select three AI vendors and verify that a risk assessment was completed prior to contract execution
4. Verify that risk assessments are refreshed at least annually for active vendors
5. Confirm that risk assessment results are documented and inform vendor tier classification

**Evidence requirements:**

- Completed vendor risk assessments for each AI service provider
- Vendor security documentation (SOC 2 reports, certifications, security whitepapers)
- Assessment approval records with noted risk acceptances
- Annual reassessment records

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.SC-03, GV.SC-04, GV.SC-07 |
| NIST AI RMF | Govern 6.1, 6.2, Map 3.4 |
| NIST AI 600-1 (GAI Profile) | GV-6.1-005, GV-6.1-009, MG-3.1-001, MG-3.1-002 (Value Chain and Component Integration, Data Privacy, Information Security, Intellectual Property) |
| CIS Controls v8.1 | CIS 15 |
| ISO 27001:2022 | A.5.19, A.5.20, A.5.21 |
| EU AI Act | Art. 16, 25 |
| MITRE ATLAS | AML.T0010, AML.T0111 |

---

### AC-5.2 — Contractual Data Protection Terms (SHALL)

**Requirement:** The organization SHALL ensure that contracts with AI service providers include explicit data protection terms covering data ownership, processing limitations, retention and deletion obligations, breach notification requirements, and prohibitions on using customer data for model training without consent.

**Assessment question:** Does the organization ensure that contracts with AI service providers include explicit data protection terms covering data ownership, processing limitations, retention and deletion obligations, breach notification requirements, and prohibitions on using customer data for model training without consent?

**Implementation guidance:** Key contractual provisions to verify include explicit statement that the organization retains ownership of all input and output data, prohibition on using input data for model training (or clear opt-out mechanism), defined data retention periods and deletion procedures, breach notification timeframes (ideally 72 hours or less to align with GDPR requirements), sub-processor disclosure and approval requirements, data processing addendum or equivalent for regulated data, and audit rights or third-party attestation commitments.

**Testing procedure:**

1. Obtain AI vendor contracts for the three highest-risk AI vendors
2. Verify each contract includes data protection clauses addressing: data ownership, processing limitations, breach notification timelines, audit rights, and subprocessor restrictions
3. Confirm that contracts specify data handling obligations upon termination
4. Verify that contract terms align with the organization's data classification and retention requirements
5. Confirm that contracts are reviewed by legal counsel prior to execution

**Evidence requirements:**

- AI vendor contracts with data protection terms highlighted
- Data processing addendums or agreements
- Vendor terms of service review records
- Documented gaps or conflicts with organizational requirements

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.SC-05, GV.SC-06 |
| NIST AI RMF | Govern 6.1, 6.2 |
| NIST AI 600-1 (GAI Profile) | GV-6.1-004, GV-6.1-006, GV-6.2-007 (Information Integrity, Information Security, Intellectual Property, Value Chain and Component Integration) |
| CIS Controls v8.1 | CIS 15 |
| ISO 27001:2022 | A.5.20, A.5.23 |
| EU AI Act | Art. 16, 25 |
| Colorado AI Act | §6-1-1702(2) |

---

### AC-5.3 — Model Provenance Verification (SHALL)

**Requirement:** The organization SHALL verify the provenance of AI models used in business operations, including the model source, training data lineage, version history, and any modifications made after deployment.

**Assessment question:** Does the organization verify the provenance of AI models used in business operations, including the model source, training data lineage, version history, and any modifications made after deployment?

**Implementation guidance:** Model provenance is critical for organizations that deploy open-source models, fine-tune vendor models, or use AI outputs in regulated decision-making. Provenance documentation should include the model developer and release version, known training data sources and any documented biases, fine-tuning data sources and procedures (if applicable), modification history since deployment, and known limitations and failure modes. For vendor-provided models, provenance information should be obtained from vendor documentation, model cards, or direct inquiry.

**Testing procedure:**

1. Obtain documentation of model provenance for all AI models in the inventory
2. For each model, verify that the following is documented: model origin, training data sources, version history, and any modifications made post-deployment
3. For third-party models, verify that the vendor provides transparency into model architecture and training practices
4. Confirm that provenance documentation is updated when model versions change
5. Verify that provenance requirements are included in AI vendor contracts

**Evidence requirements:**

- Model provenance documentation (model cards, datasheets)
- Fine-tuning records and training data lineage (if applicable)
- Version history and modification logs
- Vendor-provided model documentation

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.SC-07, ID.AM-01 |
| NIST AI RMF | Map 1.1, 1.5, 2.1 |
| NIST AI 600-1 (GAI Profile) | GV-1.6-003, MG-3.1-005, MS-2.5-005, MS-2.7-005 (Information Integrity, Value Chain and Component Integration, Intellectual Property) |
| CIS Controls v8.1 | CIS 15, CIS 16 |
| ISO 27001:2022 | A.5.21, A.8.25 |
| EU AI Act | Art. 11, 53, 55 |
| Colorado AI Act | §6-1-1702(2) |
| MITRE ATLAS | AML.T0002, AML.T0019, AML.T0058, AML.T0020, AML.T0110 |

---

### AC-5.4 — Third-Party AI Security Monitoring (SHALL)

**Requirement:** The organization SHALL monitor the security posture of critical AI vendors on an ongoing basis, including tracking vendor security incidents, service disruptions, terms of service changes, and regulatory enforcement actions.

**Assessment question:** Does the organization monitor the security posture of critical AI vendors on an ongoing basis, including tracking vendor security incidents, service disruptions, terms of service changes, and regulatory enforcement actions?

**Implementation guidance:** Ongoing monitoring should include subscribing to vendor security advisories and status pages, reviewing vendor SOC 2 or ISO 27001 recertification annually, monitoring for public disclosure of vendor security incidents, tracking terms of service changes that may affect data protection commitments, and monitoring regulatory enforcement actions against AI vendors. For critical AI vendors, consider requesting evidence of penetration testing results and vulnerability management metrics.

**Testing procedure:**

1. Obtain the third-party AI monitoring program documentation
2. Verify that monitoring activities include tracking vendor security advisories, breach notifications, and service changes
3. Confirm that vendor SLA compliance is monitored and documented
4. Review evidence that vendor security posture was reassessed at least annually
5. Verify that a process exists to escalate vendor security concerns to the governance body

**Evidence requirements:**

- Vendor monitoring procedures
- Vendor security advisory subscriptions
- Records of vendor security events identified and assessed
- Annual SOC 2 or equivalent report review records

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.SC-09, GV.SC-10 |
| NIST AI RMF | Govern 6.2, Manage 4.1 |
| NIST AI 600-1 (GAI Profile) | GV-6.1-005, GV-6.1-009, GV-6.2-004, MG-3.1-001 (Value Chain and Component Integration, Information Security, Data Privacy) |
| CIS Controls v8.1 | CIS 15 |
| ISO 27001:2022 | A.5.22 |
| EU AI Act | Art. 16, 25, 72 |
| MITRE ATLAS | AML.T0010, AML.T0109 |

---

### AC-5.5 — Vendor Termination and Data Return (SHALL)

**Requirement:** The organization SHALL maintain documented procedures for terminating AI vendor relationships, including data retrieval, confirmation of data deletion, credential revocation, and transition planning for dependent business processes.

**Assessment question:** Does the organization maintain documented procedures for terminating AI vendor relationships, including data retrieval, confirmation of data deletion, credential revocation, and transition planning for dependent business processes?

**Implementation guidance:** Vendor termination procedures should address exporting or retrieving all organizational data from the vendor platform, obtaining written confirmation of data deletion (including backups and training data), revoking all API keys, OAuth grants, and SSO integrations, identifying and transitioning dependent business processes to alternative solutions, updating the AI asset inventory and removing terminated vendor entries, and communicating changes to affected users.

**Testing procedure:**

1. Obtain vendor termination procedures specific to AI services
2. Verify procedures address data return or destruction, access revocation, API key deactivation, and transition planning
3. If any AI vendor relationships were terminated in the past 12 months, review evidence that termination procedures were followed
4. Verify that data destruction certificates or confirmation were obtained from terminated vendors
5. Confirm that terminated vendor access was revoked within the contractually defined timeframe

**Evidence requirements:**

- Vendor termination procedures
- Data deletion confirmation records from terminated vendors (if applicable)
- Credential revocation records
- Transition planning documentation

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.SC-08 |
| NIST AI RMF | Govern 6.2, Manage 2.4 |
| NIST AI 600-1 (GAI Profile) | GV-1.7-001, GV-1.7-002, GV-6.2-007, MG-2.3-001 (Information Security, Value Chain and Component Integration, Human-AI Configuration) |
| CIS Controls v8.1 | CIS 15 |
| ISO 27001:2022 | A.5.20, A.8.10 |
| EU AI Act | Art. 16, 25 |
| MITRE ATLAS | AML.T0109 |

---

