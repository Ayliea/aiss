# AISS ↔ NIST AI RMF Crosswalk

This crosswalk maps AISS sub-controls to **NIST AI RMF** requirements. For the forward direction (NIST AI RMF → AISS), refer to the per-control `framework_mappings` field in [spec/aiss-v1.2.json](../spec/aiss-v1.2.json).

## Mappings

| AISS Control | Title | Normative | NIST AI RMF References |
|---|---|---|---|
| AC-1.1 | AI Acceptable Use Policy | SHALL | Govern 1.1, 1.2, 1.7 |
| AC-1.2 | AI Governance Oversight Structure | SHALL | Govern 1.3, 2.1, 2.3 |
| AC-1.3 | AI Risk Appetite Statement | SHALL | Govern 1.1, 1.4, 1.5 |
| AC-1.4 | AI Ethics and Responsible Use Guidelines | SHALL | Govern 1.6, 1.7, Map 1.5 |
| AC-1.5 | AI Policy Review and Maintenance Cadence | SHALL | Govern 1.2, 5.1, 5.2 |
| AC-1.6 | Regulatory Compliance Program | SHALL | Govern 1.1, 1.2 |
| AC-2.1 | AI Asset Inventory | SHALL | Map 1.1, 1.5, 1.6 |
| AC-2.2 | AI Asset Classification | SHALL | Map 1.1, 1.5, 2.1 |
| AC-2.3 | AI Asset Ownership Assignment | SHALL | Govern 2.1, 2.3 |
| AC-2.4 | Shadow AI Discovery | SHALL | Map 1.5, 1.6, 5.1 |
| AC-2.5 | AI Asset Lifecycle Management | SHALL | Map 1.1, Govern 1.5 |
| AC-2.6 | AI Development Tool Governance | SHALL | Govern 1.6, Map 2.1 |
| AC-3.1 | Data Classification for AI Inputs | SHALL | Map 3.4, Measure 2.5 |
| AC-3.2 | Data Loss Prevention for AI Endpoints | SHALL | Measure 2.5, Manage 2.2 |
| AC-3.3 | Encryption for AI Data Flows | SHALL | Manage 2.2 |
| AC-3.4 | Data Minimization for AI Interactions | SHALL | Map 3.4, Govern 1.7 |
| AC-3.5 | AI Data Retention and Deletion | SHALL | Map 3.4, Manage 2.4 |
| AC-3.6 | Cross-Border Data Transfer Controls | SHALL | Govern 1.1, Map 3.4 |
| AC-3.7 | RAG and Vector Store Security | SHALL | Map 3.4, Measure 2.5, Manage 1.3 |
| AC-4.1 | Role-Based Access Control for AI Tools | SHALL | Govern 4.1 |
| AC-4.2 | Multi-Factor Authentication for AI Services | SHALL | Govern 4.1 |
| AC-4.3 | Privileged Access Management for AI | SHALL | Govern 4.1, Manage 1.3 |
| AC-4.4 | API Key and Secret Management | SHALL | Govern 4.1 |
| AC-4.5 | AI Access Review and Recertification | SHALL | Govern 4.1 |
| AC-5.1 | AI Vendor Risk Assessment | SHALL | Govern 6.1, 6.2, Map 3.4 |
| AC-5.2 | Contractual Data Protection Terms | SHALL | Govern 6.1, 6.2 |
| AC-5.3 | Model Provenance Verification | SHALL | Map 1.1, 1.5, 2.1 |
| AC-5.4 | Third-Party AI Security Monitoring | SHALL | Govern 6.2, Manage 4.1 |
| AC-5.5 | Vendor Termination and Data Return | SHALL | Govern 6.2, Manage 2.4 |
| AC-6.1 | Human Review Processes for High-Risk AI Outputs | SHALL | Measure 2.6, 2.7, 2.11 |
| AC-6.2 | Accuracy and Hallucination Monitoring | SHALL | Measure 1.1, 2.3, 2.6 |
| AC-6.3 | Bias Detection and Mitigation | SHALL | Measure 2.6, 2.10, 2.11 |
| AC-6.4 | AI Output Labeling and Disclosure | SHALL | Govern 1.7, Measure 2.7 |
| AC-6.5 | Automated Output Quality Controls | SHOULD | Measure 1.3, 2.3 |
| AC-6.6 | Synthetic Content Provenance and Marking | SHALL | Govern 1.7, Measure 1.3, Measure 2.6 |
| AC-7.1 | AI-Specific Incident Response Playbooks | SHALL | Manage 3.1, 3.2, 4.1 |
| AC-7.2 | AI Incident Escalation and Communication | SHALL | Manage 3.2 |
| AC-7.3 | AI Incident Classification and Severity | SHALL | Manage 3.1 |
| AC-7.4 | Post-Incident Review and Lessons Learned | SHALL | Manage 4.2 |
| AC-7.5 | Regulatory Notification Procedures | SHALL | Manage 3.2, Govern 1.1 |
| AC-8.1 | AI Usage Logging | SHALL | Measure 1.1, 2.2 |
| AC-8.2 | AI Anomaly Detection | SHALL | Measure 2.2, Manage 1.1 |
| AC-8.3 | Prompt and Response Logging | SHOULD | Measure 2.2, 2.5 |
| AC-8.4 | AI Performance and Availability Monitoring | SHALL | Measure 1.1, 1.3, Manage 4.1 |
| AC-8.5 | Log Retention and Integrity | SHALL | Measure 2.2 |
| AC-9.1 | AI Security Awareness Program | SHALL | Govern 2.2, 3.1 |
| AC-9.2 | Role-Based AI Training | SHALL | Govern 2.2, 3.1 |
| AC-9.3 | AI Acceptable Use Policy Communication | SHALL | Govern 1.7, 2.2 |
| AC-9.4 | AI Threat Awareness | SHALL | Govern 3.1, Map 5.1 |
| AC-9.5 | Executive and Board AI Literacy | SHALL | Govern 2.3, 1.4 |
| AC-10.1 | Model Access Controls | SHALL | Map 1.1, Govern 4.1 |
| AC-10.2 | Adversarial Testing | SHALL | Measure 1.1, 2.3, 2.6 |
| AC-10.3 | Model Versioning and Rollback | SHALL | Manage 2.3, 4.1 |
| AC-10.4 | Model Integrity Verification | SHALL | Measure 1.1, 2.3 |
| AC-10.5 | Prompt Injection Defense | SHALL | Measure 2.6, Manage 1.1 |
| AC-10.6 | Agentic AI Action Authorization and Guardrails | SHALL | Manage 1.3, Manage 2.3, Manage 4.1 |
