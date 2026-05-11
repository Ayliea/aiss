# AISS ↔ NIST CSF 2.0 Crosswalk

This crosswalk maps AISS sub-controls to **NIST CSF 2.0** requirements. For the forward direction (NIST CSF 2.0 → AISS), refer to the per-control `framework_mappings` field in [spec/aiss-v1.2.json](../spec/aiss-v1.2.json).

## Mappings

| AISS Control | Title | Normative | NIST CSF 2.0 References |
|---|---|---|---|
| AC-1.1 | AI Acceptable Use Policy | SHALL | GV.PO-01, GV.PO-02 |
| AC-1.2 | AI Governance Oversight Structure | SHALL | GV.RR-01, GV.RR-02, GV.OV-01 |
| AC-1.3 | AI Risk Appetite Statement | SHALL | GV.RM-01, GV.RM-02, GV.RM-03 |
| AC-1.4 | AI Ethics and Responsible Use Guidelines | SHALL | GV.OC-04, GV.PO-01 |
| AC-1.5 | AI Policy Review and Maintenance Cadence | SHALL | GV.PO-02, ID.IM-02 |
| AC-1.6 | Regulatory Compliance Program | SHALL | GV.OC-03, GV.OC-05 |
| AC-2.1 | AI Asset Inventory | SHALL | ID.AM-01, ID.AM-02 |
| AC-2.2 | AI Asset Classification | SHALL | ID.AM-01, ID.AM-05 |
| AC-2.3 | AI Asset Ownership Assignment | SHALL | ID.AM-01, GV.RR-02 |
| AC-2.4 | Shadow AI Discovery | SHALL | ID.AM-01, ID.AM-02, DE.CM-09 |
| AC-2.5 | AI Asset Lifecycle Management | SHALL | ID.AM-01, PR.PS-01 |
| AC-2.6 | AI Development Tool Governance | SHALL | ID.AM-01, PR.DS-01 |
| AC-3.1 | Data Classification for AI Inputs | SHALL | PR.DS-01, PR.DS-02 |
| AC-3.2 | Data Loss Prevention for AI Endpoints | SHALL | PR.DS-01, PR.DS-02, PR.DS-10 |
| AC-3.3 | Encryption for AI Data Flows | SHALL | PR.DS-01, PR.DS-02 |
| AC-3.4 | Data Minimization for AI Interactions | SHALL | PR.DS-01, PR.DS-10 |
| AC-3.5 | AI Data Retention and Deletion | SHALL | PR.DS-01 |
| AC-3.6 | Cross-Border Data Transfer Controls | SHALL | GV.OC-03, PR.DS-01 |
| AC-3.7 | RAG and Vector Store Security | SHALL | PR.DS-01, PR.DS-02, PR.AA-05, DE.CM-01 |
| AC-4.1 | Role-Based Access Control for AI Tools | SHALL | PR.AA-01, PR.AA-03, PR.AA-05 |
| AC-4.2 | Multi-Factor Authentication for AI Services | SHALL | PR.AA-01, PR.AA-02 |
| AC-4.3 | Privileged Access Management for AI | SHALL | PR.AA-05 |
| AC-4.4 | API Key and Secret Management | SHALL | PR.AA-02, PR.DS-01 |
| AC-4.5 | AI Access Review and Recertification | SHALL | PR.AA-05 |
| AC-5.1 | AI Vendor Risk Assessment | SHALL | GV.SC-03, GV.SC-04, GV.SC-07 |
| AC-5.2 | Contractual Data Protection Terms | SHALL | GV.SC-05, GV.SC-06 |
| AC-5.3 | Model Provenance Verification | SHALL | GV.SC-07, ID.AM-01 |
| AC-5.4 | Third-Party AI Security Monitoring | SHALL | GV.SC-09, GV.SC-10 |
| AC-5.5 | Vendor Termination and Data Return | SHALL | GV.SC-08 |
| AC-6.1 | Human Review Processes for High-Risk AI Outputs | SHALL | GV.OC-04 |
| AC-6.2 | Accuracy and Hallucination Monitoring | SHALL | GV.OC-04 |
| AC-6.3 | Bias Detection and Mitigation | SHALL | GV.OC-04 |
| AC-6.4 | AI Output Labeling and Disclosure | SHALL | GV.OC-04 |
| AC-6.5 | Automated Output Quality Controls | SHOULD | PR.DS-01 |
| AC-6.6 | Synthetic Content Provenance and Marking | SHALL | GV.OC-04, PR.DS-01 |
| AC-7.1 | AI-Specific Incident Response Playbooks | SHALL | RS.MA-01, RS.MA-03 |
| AC-7.2 | AI Incident Escalation and Communication | SHALL | RS.CO-02, RS.CO-03 |
| AC-7.3 | AI Incident Classification and Severity | SHALL | RS.AN-02, RS.AN-03 |
| AC-7.4 | Post-Incident Review and Lessons Learned | SHALL | RS.AN-08, ID.IM-01, ID.IM-02 |
| AC-7.5 | Regulatory Notification Procedures | SHALL | RS.CO-02, RS.CO-03 |
| AC-8.1 | AI Usage Logging | SHALL | DE.CM-01, DE.CM-09 |
| AC-8.2 | AI Anomaly Detection | SHALL | DE.AE-02, DE.AE-03, DE.CM-01 |
| AC-8.3 | Prompt and Response Logging | SHOULD | DE.CM-01 |
| AC-8.4 | AI Performance and Availability Monitoring | SHALL | DE.CM-01, ID.RA-01 |
| AC-8.5 | Log Retention and Integrity | SHALL | DE.CM-09, PR.DS-01 |
| AC-9.1 | AI Security Awareness Program | SHALL | PR.AT-01, PR.AT-02 |
| AC-9.2 | Role-Based AI Training | SHALL | PR.AT-01, PR.AT-02 |
| AC-9.3 | AI Acceptable Use Policy Communication | SHALL | PR.AT-01, GV.PO-01 |
| AC-9.4 | AI Threat Awareness | SHALL | PR.AT-01, PR.AT-02 |
| AC-9.5 | Executive and Board AI Literacy | SHALL | GV.OV-01, GV.RR-01 |
| AC-10.1 | Model Access Controls | SHALL | PR.AA-01, PR.AA-03, PR.AA-05 |
| AC-10.2 | Adversarial Testing | SHALL | ID.RA-01, PR.DS-01 |
| AC-10.3 | Model Versioning and Rollback | SHALL | PR.PS-01, RC.RP-01 |
| AC-10.4 | Model Integrity Verification | SHALL | PR.DS-01, PR.DS-02 |
| AC-10.5 | Prompt Injection Defense | SHALL | PR.DS-01, DE.CM-01 |
| AC-10.6 | Agentic AI Action Authorization and Guardrails | SHALL | PR.AA-01, PR.AA-05, PR.PS-01, DE.CM-01 |
