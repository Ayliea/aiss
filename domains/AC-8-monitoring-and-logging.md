# AC-8 — AI Monitoring and Logging

**Control count:** 5

## Overview

This domain covers AC-8 sub-controls in the Ayliea AI Security Standard. See the [machine-readable spec](../spec/aiss-v1.2.json) for the canonical definition.

## Sub-controls

### AC-8.1 — AI Usage Logging (SHALL)

**Requirement:** The organization SHALL log AI system usage at a sufficient level of detail to support security monitoring, policy compliance verification, and incident investigation, including user identity, timestamp, AI service accessed, and general interaction type.

**Assessment question:** Does the organization log AI system usage at a sufficient level of detail to support security monitoring, policy compliance verification, and incident investigation, including user identity, timestamp, AI service accessed, and general interaction type?

**Implementation guidance:** The scope and granularity of AI usage logging should be proportional to the data sensitivity and regulatory requirements of each AI system. At minimum, logs should capture who used the AI service (user identity), when the interaction occurred, which AI service was accessed, the general nature of the interaction (chat, API call, file upload, etc.), and the volume of data transmitted. For AI systems processing regulated data, more detailed logging may be required. Privacy considerations should be balanced against security needs, with clear policies on what is logged and how logs are protected.

**Testing procedure:**

1. Obtain the AI usage logging configuration documentation
2. Verify that logs capture: user identity, AI service accessed, timestamp, data classification of inputs, and action type (query, upload, configuration change)
3. Select three AI services and verify that logging is active and producing records
4. Review a sample of 20 log entries for completeness against the defined schema
5. Confirm that logging cannot be disabled by standard users

**Evidence requirements:**

- AI usage logging configurations for each service
- Sample log entries demonstrating required fields
- Log centralization and access documentation
- Privacy impact assessment for AI logging (if applicable)

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | DE.CM-01, DE.CM-09 |
| NIST AI RMF | Measure 1.1, 2.2 |
| NIST AI 600-1 (GAI Profile) | GV-1.5-001, MG-3.2-006, MS-2.7-004 (Information Integrity, Information Security) |
| CIS Controls v8.1 | CIS 8 |
| ISO 27001:2022 | A.8.15, A.8.16 |
| EU AI Act | Art. 12, 19, 26(5) |
| MITRE ATLAS | AML.T0053, AML.T0040, AML.T0108, AML.T0096 |

---

### AC-8.2 — AI Anomaly Detection (SHALL)

**Requirement:** The organization SHALL implement detection capabilities for anomalous AI usage patterns, including unusual data volumes, access from unexpected locations, off-hours usage patterns, and rapid escalation in AI consumption that may indicate data exfiltration or compromised accounts.

**Assessment question:** Does the organization implement detection capabilities for anomalous AI usage patterns, including unusual data volumes, access from unexpected locations, off-hours usage patterns, and rapid escalation in AI consumption that may indicate data exfiltration or compromised accounts?

**Implementation guidance:** Anomaly detection should be tuned to the organization's normal AI usage baselines. Detection rules should cover volume anomalies (sudden increase in data submitted to AI services), temporal anomalies (AI usage outside normal business hours), geographic anomalies (AI access from unexpected locations), behavioral anomalies (access to AI tools not aligned with the user's role), and pattern anomalies (repeated attempts to submit data that is blocked by DLP rules). Alerts should be integrated with the organization's SIEM or security monitoring platform.

**Testing procedure:**

1. Obtain the AI anomaly detection configuration and rules
2. Verify that detection rules address: unusual usage volume, off-hours access, bulk data exfiltration patterns, and access from unauthorized locations
3. Review anomaly detection alerts from the past 90 days and verify that alerts were triaged within the defined SLA
4. Test detection capabilities by simulating at least one anomalous pattern and verifying an alert is generated
5. Confirm that anomaly detection rules are reviewed and updated at least quarterly

**Evidence requirements:**

- Anomaly detection rule configurations
- SIEM integration documentation
- Alert logs and investigation records
- Detection rule tuning history

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | DE.AE-02, DE.AE-03, DE.CM-01 |
| NIST AI RMF | Measure 2.2, Manage 1.1 |
| NIST AI 600-1 (GAI Profile) | GV-6.1-005, MG-3.2-006, MS-2.6-005, MS-2.7-004 (Information Security, Information Integrity, Value Chain and Component Integration) |
| CIS Controls v8.1 | CIS 8 |
| ISO 27001:2022 | A.8.15, A.8.16 |
| EU AI Act | Art. 12, 26(5) |
| MITRE ATLAS | AML.T0006, AML.T0061, AML.T0094, AML.T0105 |

---

### AC-8.3 — Prompt and Response Logging (SHOULD)

**Requirement:** For AI systems processing confidential or restricted data, the organization SHOULD implement prompt and response logging sufficient to support incident investigation, data exposure analysis, and compliance auditing, subject to applicable privacy and data retention requirements.

**Assessment question:** For AI systems processing confidential or restricted data, does the organization implement prompt and response logging sufficient to support incident investigation, data exposure analysis, and compliance auditing, subject to applicable privacy and data retention requirements?

**Implementation guidance:** Prompt and response logging captures the content of AI interactions and is the most sensitive form of AI monitoring. Implementation must balance security needs against privacy considerations and storage costs. Organizations should evaluate whether prompt logging is necessary based on the data sensitivity of the AI use case, applicable regulatory requirements (some regulations may require or prohibit logging of specific data types), storage and security requirements for log data (prompt logs may contain the same sensitive data they are designed to monitor), and user notification requirements (employees should be informed that prompt logging is active). This control uses SHOULD rather than SHALL because implementation feasibility and appropriateness vary significantly by context.

**Testing procedure:**

1. Verify that prompt and response logging is enabled for AI systems processing Confidential or Restricted data
2. Confirm that logged prompts and responses are stored separately from production AI data with access restricted to authorized security and compliance personnel
3. Verify that prompt logs are protected from unauthorized modification with integrity controls (e.g., write-once storage, hash verification)
4. Review prompt log access records and verify that all access was by authorized personnel
5. Confirm that prompt logging practices comply with applicable privacy requirements

**Evidence requirements:**

- Prompt logging configuration and scope documentation
- Log data protection measures
- User notification records
- Data retention policy for prompt logs

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | DE.CM-01 |
| NIST AI RMF | Measure 2.2, 2.5 |
| NIST AI 600-1 (GAI Profile) | MG-3.2-006, MG-4.1-007, MS-2.2-002, MS-2.7-004 (Data Privacy, Information Integrity, Information Security, Human-AI Configuration) |
| CIS Controls v8.1 | CIS 8 |
| ISO 27001:2022 | A.8.15 |
| EU AI Act | Art. 12, 19 |
| MITRE ATLAS | AML.T0068, AML.T0063 |

---

### AC-8.4 — AI Performance and Availability Monitoring (SHALL)

**Requirement:** For mission-critical AI systems, the organization SHALL monitor system performance, availability, and response quality to detect degradation that could affect business operations or output reliability.

**Assessment question:** For mission-critical AI systems, does the organization monitor system performance, availability, and response quality to detect degradation that could affect business operations or output reliability?

**Implementation guidance:** Performance monitoring should track response time and latency, availability and uptime, error rates and failure patterns, output quality metrics relevant to the use case, and model version changes or updates by the vendor. This control is primarily applicable to AI systems classified as operational or mission-critical in the AI asset classification. Experimental AI tools may not require performance monitoring.

**Testing procedure:**

1. Obtain AI performance and availability monitoring configuration
2. Verify monitoring covers response time, error rates, throughput, and availability for each production AI service
3. Verify that performance thresholds and SLAs are defined and that threshold breaches trigger alerts
4. Review performance data for the past 90 days and verify that SLA breaches were investigated
5. Confirm that monitoring dashboards are accessible to AI asset owners and operations personnel

**Evidence requirements:**

- Performance monitoring dashboards or reports
- Availability and uptime metrics
- Performance incident records
- Alert configurations for performance degradation

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | DE.CM-01, ID.RA-01 |
| NIST AI RMF | Measure 1.1, 1.3, Manage 4.1 |
| NIST AI 600-1 (GAI Profile) | MG-3.2-006, MG-4.1-002, MG-4.2-001, MS-4.2-002 (Information Security, Confabulation, Harmful Bias and Homogenization) |
| CIS Controls v8.1 | CIS 8 |
| ISO 27001:2022 | A.8.6, A.8.16 |
| EU AI Act | Art. 9(3), 72 |

---

### AC-8.5 — Log Retention and Integrity (SHALL)

**Requirement:** The organization SHALL retain AI-related logs for a minimum of 12 months in a manner that preserves log integrity and prevents unauthorized modification or deletion.

**Assessment question:** Does the organization retain AI-related logs for a minimum of 12 months in a manner that preserves log integrity and prevents unauthorized modification or deletion?

**Implementation guidance:** Log retention requirements should align with the longest applicable regulatory retention period and the organization's incident investigation needs. At minimum, 12 months of retention is required to support annual assessment cycles. Logs should be stored in a centralized, tamper-evident repository (SIEM, log management platform, or immutable cloud storage). Access to log data should be restricted to authorized security and compliance personnel.

**Testing procedure:**

1. Obtain the AI log retention policy
2. Verify that retention periods meet the minimum of 12 months for all AI-related logs
3. Verify that log integrity controls are in place (e.g., tamper-evident storage, cryptographic hashing, write-once media)
4. Attempt to retrieve log entries from 6 months ago and 11 months ago to verify accessibility and integrity
5. Confirm that log disposal procedures exist and are followed when retention periods expire

**Evidence requirements:**

- Log retention configuration documentation
- Log storage architecture showing integrity controls
- Access control records for log repositories
- Sample retrieval of historical log data

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | DE.CM-09, PR.DS-01 |
| NIST AI RMF | Measure 2.2 |
| NIST AI 600-1 (GAI Profile) | GV-1.5-003, MG-4.1-006, MS-2.8-003 (Information Integrity, Intellectual Property) |
| CIS Controls v8.1 | CIS 8 |
| ISO 27001:2022 | A.8.15, A.5.33 |
| EU AI Act | Art. 12, 19 |
| MITRE ATLAS | AML.T0092 |

---

