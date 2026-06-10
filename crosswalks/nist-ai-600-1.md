# AISS ↔ NIST AI 600-1 (GAI Profile) Crosswalk

This crosswalk maps AISS sub-controls to **NIST AI 600-1 (GAI Profile)** requirements. For the forward direction (NIST AI 600-1 (GAI Profile) → AISS), refer to the per-control `framework_mappings` field in [spec/aiss-v1.3.json](../spec/aiss-v1.3.json).

## Mappings

| AISS Control | Title | Normative | NIST AI 600-1 (GAI Profile) References |
|---|---|---|---|
| AC-1.1 | AI Acceptable Use Policy | SHALL | GV-1.1-001, GV-1.4-002, GV-6.1-010 (Data Privacy, Intellectual Property, Information Security) |
| AC-1.2 | AI Governance Oversight Structure | SHALL | GV-2.1-001, GV-2.1-003, GV-3.2-001, GV-4.1-003 (Human-AI Configuration, Value Chain and Component Integration, Information Security) |
| AC-1.3 | AI Risk Appetite Statement | SHALL | GV-1.3-001, GV-1.3-002, GV-1.3-006, GV-1.3-007 (Information Integrity, Information Security, CBRN Information or Capabilities, Dangerous Violent or Hateful Content) |
| AC-1.4 | AI Ethics and Responsible Use Guidelines | SHALL | GV-1.2-001, GV-1.4-001, GV-3.2-003, GV-5.1-001 (Information Integrity, Harmful Bias and Homogenization, Human-AI Configuration, Obscene Degrading and/or Abusive Content) |
| AC-1.5 | AI Policy Review and Maintenance Cadence | SHALL | GV-1.5-002, GV-1.5-003, GV-4.1-001 (Information Security, Information Integrity, Confabulation) |
| AC-1.6 | Regulatory Compliance Program | SHALL | GV-1.1-001, GV-1.4-002, MP-4.1-003 (Data Privacy, Intellectual Property, Information Security) |
| AC-2.1 | AI Asset Inventory | SHALL | GV-1.6-001, GV-1.6-003, GV-6.1-007 (Information Security, Data Privacy, Value Chain and Component Integration, Intellectual Property) |
| AC-2.2 | AI Asset Classification | SHALL | GV-1.3-001, GV-1.6-003, MP-1.1-001 (Data Privacy, Intellectual Property, Information Integrity, Value Chain and Component Integration) |
| AC-2.3 | AI Asset Ownership Assignment | SHALL | GV-1.6-003, GV-2.1-001, GV-4.1-003 (Human-AI Configuration, Value Chain and Component Integration, Information Security) |
| AC-2.4 | Shadow AI Discovery | SHALL | GV-1.6-001, GV-1.6-002, GV-6.1-007 (Information Security, Value Chain and Component Integration) |
| AC-2.5 | AI Asset Lifecycle Management | SHALL | GV-1.7-001, GV-1.7-002, GV-4.1-003, MG-2.4-004 (Information Security, Value Chain and Component Integration, Human-AI Configuration) |
| AC-2.6 | AI Development Tool Governance | SHALL | GV-6.1-001, GV-6.1-010, MP-4.1-006, MS-2.6-004 (Intellectual Property, Value Chain and Component Integration, Dangerous Violent or Hateful Content) |
| AC-3.1 | Data Classification for AI Inputs | SHALL | MP-4.1-001, MP-4.1-005, MP-4.1-009 (Data Privacy, Information Security, Intellectual Property) |
| AC-3.2 | Data Loss Prevention for AI Endpoints | SHALL | MP-4.1-001, MP-4.1-009, MS-2.7-001 (Data Privacy, Information Security) |
| AC-3.3 | Encryption for AI Data Flows | SHALL | MS-2.7-001, MS-2.7-004 (Information Security, Data Privacy) |
| AC-3.4 | Data Minimization for AI Interactions | SHALL | MP-4.1-005, MS-2.2-002, MS-2.2-004 (Data Privacy, Human-AI Configuration, Information Security) |
| AC-3.5 | AI Data Retention and Deletion | SHALL | GV-1.5-003, MP-4.1-005, MG-4.1-006, MS-2.2-003 (Data Privacy, Information Integrity, Intellectual Property) |
| AC-3.6 | Cross-Border Data Transfer Controls | SHALL | MG-3.1-002, MP-4.1-005, MP-4.1-010 (Data Privacy, Value Chain and Component Integration, Information Security) |
| AC-3.7 | RAG and Vector Store Security | SHALL | MP-1.1-001, MS-2.3-001, MS-2.5-005, MS-2.7-001, MG-3.1-003 (Information Security, Data Privacy, Confabulation, Information Integrity) |
| AC-4.1 | Role-Based Access Control for AI Tools | SHALL | GV-2.1-001, GV-3.2-003, GV-4.1-003 (Information Security, Human-AI Configuration) |
| AC-4.2 | Multi-Factor Authentication for AI Services | SHALL | MS-2.7-001, MS-2.7-004, MS-2.7-009 (Information Security) |
| AC-4.3 | Privileged Access Management for AI | SHALL | MS-2.7-001, MS-2.7-004, MS-2.7-009 (Information Security) |
| AC-4.4 | API Key and Secret Management | SHALL | MS-2.7-001, MS-2.7-004 (Information Security) |
| AC-4.5 | AI Access Review and Recertification | SHALL | GV-1.5-001, MS-2.7-009 (Information Security, Information Integrity) |
| AC-5.1 | AI Vendor Risk Assessment | SHALL | GV-6.1-005, GV-6.1-009, MG-3.1-001, MG-3.1-002 (Value Chain and Component Integration, Data Privacy, Information Security, Intellectual Property) |
| AC-5.2 | Contractual Data Protection Terms | SHALL | GV-6.1-004, GV-6.1-006, GV-6.2-007 (Information Integrity, Information Security, Intellectual Property, Value Chain and Component Integration) |
| AC-5.3 | Model Provenance Verification | SHALL | GV-1.6-003, MG-3.1-005, MS-2.5-005, MS-2.7-005 (Information Integrity, Value Chain and Component Integration, Intellectual Property) |
| AC-5.4 | Third-Party AI Security Monitoring | SHALL | GV-6.1-005, GV-6.1-009, GV-6.2-004, MG-3.1-001 (Value Chain and Component Integration, Information Security, Data Privacy) |
| AC-5.5 | Vendor Termination and Data Return | SHALL | GV-1.7-001, GV-1.7-002, GV-6.2-007, MG-2.3-001 (Information Security, Value Chain and Component Integration, Human-AI Configuration) |
| AC-6.1 | Human Review Processes for High-Risk AI Outputs | SHALL | GV-3.2-003, MG-2.2-001, MG-3.2-008, MS-2.5-003 (Human-AI Configuration, Confabulation, Harmful Bias and Homogenization, Dangerous Violent or Hateful Content) |
| AC-6.2 | Accuracy and Hallucination Monitoring | SHALL | MS-2.3-002, MS-2.5-003, MS-2.6-005, MP-2.3-003, MG-4.1-004 (Confabulation, Information Integrity, Information Security) |
| AC-6.3 | Bias Detection and Mitigation | SHALL | MS-2.11-001, MS-2.11-002, MS-2.11-004, MG-2.2-004, MG-3.2-001 (Harmful Bias and Homogenization, Dangerous Violent or Hateful Content) |
| AC-6.4 | AI Output Labeling and Disclosure | SHALL | GV-5.1-002, MP-5.1-003, MS-1.1-001, MS-2.7-005 (Human-AI Configuration, Information Integrity, Confabulation) |
| AC-6.5 | Automated Output Quality Controls | SHOULD | MG-3.2-005, MG-3.2-006, MS-2.6-005, MS-2.7-005 (Information Integrity, Harmful Bias and Homogenization, Dangerous Violent or Hateful Content, Obscene Degrading and/or Abusive Content) |
| AC-6.6 | Synthetic Content Provenance and Marking | SHALL | GV-5.1-002, MS-1.1-001, MS-2.7-005, MG-3.2-008 (Information Integrity, Human-AI Configuration, Confabulation) |
| AC-7.1 | AI-Specific Incident Response Playbooks | SHALL | GV-4.3-002, GV-6.2-003, MG-2.3-001, MG-4.2-002, MG-4.3-002 (Information Security, Value Chain and Component Integration, Human-AI Configuration, Dangerous Violent or Hateful Content) |
| AC-7.2 | AI Incident Escalation and Communication | SHALL | GV-2.1-001, MG-2.4-001, MG-2.4-002, MG-4.3-001 (Human-AI Configuration, Value Chain and Component Integration, Information Security) |
| AC-7.3 | AI Incident Classification and Severity | SHALL | GV-4.3-002, MG-2.4-002, MG-2.4-004 (Information Security) |
| AC-7.4 | Post-Incident Review and Lessons Learned | SHALL | GV-1.5-002, MG-4.2-002, MG-4.3-001, MG-4.3-002 (Information Security, Human-AI Configuration, Information Integrity, Confabulation) |
| AC-7.5 | Regulatory Notification Procedures | SHALL | GV-2.1-001, GV-6.2-003, MG-4.3-001, MG-4.3-003 (Information Security, Data Privacy, Value Chain and Component Integration) |
| AC-8.1 | AI Usage Logging | SHALL | GV-1.5-001, MG-3.2-006, MS-2.7-004 (Information Integrity, Information Security) |
| AC-8.2 | AI Anomaly Detection | SHALL | GV-6.1-005, MG-3.2-006, MS-2.6-005, MS-2.7-004 (Information Security, Information Integrity, Value Chain and Component Integration) |
| AC-8.3 | Prompt and Response Logging | SHOULD | MG-3.2-006, MG-4.1-007, MS-2.2-002, MS-2.7-004 (Data Privacy, Information Integrity, Information Security, Human-AI Configuration) |
| AC-8.4 | AI Performance and Availability Monitoring | SHALL | MG-3.2-006, MG-4.1-002, MG-4.2-001, MS-4.2-002 (Information Security, Confabulation, Harmful Bias and Homogenization) |
| AC-8.5 | Log Retention and Integrity | SHALL | GV-1.5-003, MG-4.1-006, MS-2.8-003 (Information Integrity, Intellectual Property) |
| AC-9.1 | AI Security Awareness Program | SHALL | MP-3.4-002, MP-3.4-003 (Information Integrity, Human-AI Configuration) |
| AC-9.2 | Role-Based AI Training | SHALL | GV-2.1-003, MP-3.4-003, MP-3.4-006 (Human-AI Configuration, Information Integrity, Harmful Bias and Homogenization, Dangerous Violent or Hateful Content) |
| AC-9.3 | AI Acceptable Use Policy Communication | SHALL | GV-1.1-001, GV-1.4-002, GV-6.1-010 (Data Privacy, Intellectual Property, Value Chain and Component Integration) |
| AC-9.4 | AI Threat Awareness | SHALL | GV-3.2-005, MP-1.1-003, MP-3.4-002, MS-2.7-007 (Information Security, Dangerous Violent or Hateful Content, Information Integrity) |
| AC-9.5 | Executive and Board AI Literacy | SHALL | GV-2.1-003, GV-4.1-003, MP-3.4-002 (Human-AI Configuration, Value Chain and Component Integration, Information Integrity) |
| AC-10.1 | Model Access Controls | SHALL | MS-2.7-001, MS-2.7-004, MS-2.7-009 (Information Security) |
| AC-10.2 | Adversarial Testing | SHALL | MP-2.3-005, MP-5.1-005, MS-2.6-006, MS-2.6-007, MS-2.7-007 (Information Security, CBRN Information or Capabilities, Harmful Bias and Homogenization, Dangerous Violent or Hateful Content) |
| AC-10.3 | Model Versioning and Rollback | SHALL | GV-6.2-005, GV-6.2-006, MG-3.2-002, MS-2.8-003 (Information Integrity, Harmful Bias and Homogenization, Value Chain and Component Integration) |
| AC-10.4 | Model Integrity Verification | SHALL | MS-2.5-005, MS-2.7-005, MS-2.7-008, MS-2.7-009 (Information Integrity, Information Security, Dangerous Violent or Hateful Content) |
| AC-10.5 | Prompt Injection Defense | SHALL | MP-2.3-005, MP-5.1-005, MP-5.1-006, MS-2.6-006, MS-2.7-007 (Information Security, CBRN Information or Capabilities, Dangerous Violent or Hateful Content) |
| AC-10.6 | Agentic AI Action Authorization and Guardrails | SHALL | GV-3.2-003, MS-2.7-001, MG-3.1-003, MG-4.1-002 (Information Security, Human-AI Configuration, Value Chain and Component Integration) |
