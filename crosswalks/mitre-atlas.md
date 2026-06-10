# AISS ↔ MITRE ATLAS Crosswalk

This crosswalk maps AISS sub-controls to **MITRE ATLAS** requirements. For the forward direction (MITRE ATLAS → AISS), refer to the per-control `framework_mappings` field in [spec/aiss-v1.3.json](../spec/aiss-v1.3.json).

## Mappings

| AISS Control | Title | Normative | MITRE ATLAS References |
|---|---|---|---|
| AC-2.1 | AI Asset Inventory | SHALL | AML.T0007, AML.T0047 |
| AC-2.4 | Shadow AI Discovery | SHALL | AML.T0095 |
| AC-2.5 | AI Asset Lifecycle Management | SHALL | AML.T0103 |
| AC-2.6 | AI Development Tool Governance | SHALL | AML.T0000 |
| AC-3.1 | Data Classification for AI Inputs | SHALL | AML.T0070, AML.T0082, AML.T0085 |
| AC-3.2 | Data Loss Prevention for AI Endpoints | SHALL | AML.T0057, AML.T0086, AML.T0024, AML.T0025 |
| AC-3.4 | Data Minimization for AI Interactions | SHALL | AML.T0057 |
| AC-3.7 | RAG and Vector Store Security | SHALL | AML.T0070 (RAG Poisoning), AML.T0071 (False RAG Entry Injection), AML.T0051 (LLM Prompt Injection), AML.T0082 (RAG Credential Harvesting), AML.T0085.000 (Data from AI Services: RAG Databases) |
| AC-4.1 | Role-Based Access Control for AI Tools | SHALL | AML.T0012 |
| AC-4.2 | Multi-Factor Authentication for AI Services | SHALL | AML.T0012, AML.T0091 |
| AC-4.3 | Privileged Access Management for AI | SHALL | AML.T0044, AML.T0081, AML.T0083 |
| AC-4.4 | API Key and Secret Management | SHALL | AML.T0040, AML.T0055, AML.T0098, AML.T0096 |
| AC-4.5 | AI Access Review and Recertification | SHALL | AML.T0012, AML.T0021 |
| AC-5.1 | AI Vendor Risk Assessment | SHALL | AML.T0010, AML.T0111 |
| AC-5.3 | Model Provenance Verification | SHALL | AML.T0002, AML.T0019, AML.T0058, AML.T0020, AML.T0110 |
| AC-5.4 | Third-Party AI Security Monitoring | SHALL | AML.T0010, AML.T0109 |
| AC-5.5 | Vendor Termination and Data Return | SHALL | AML.T0109 |
| AC-6.1 | Human Review Processes for High-Risk AI Outputs | SHALL | AML.T0015, AML.T0067, AML.T0088 |
| AC-6.2 | Accuracy and Hallucination Monitoring | SHALL | AML.T0060, AML.T0062 |
| AC-6.4 | AI Output Labeling and Disclosure | SHALL | AML.T0088, AML.T0073 |
| AC-6.5 | Automated Output Quality Controls | SHOULD | AML.T0077, AML.T0102 |
| AC-6.6 | Synthetic Content Provenance and Marking | SHALL | AML.T0088 (Generate Deepfakes), AML.T0067 (LLM Trusted Output Components Manipulation), AML.T0060 (Publish Hallucinated Entities) |
| AC-7.1 | AI-Specific Incident Response Playbooks | SHALL | AML.T0051, AML.T0010, AML.T0018 |
| AC-8.1 | AI Usage Logging | SHALL | AML.T0053, AML.T0040, AML.T0108, AML.T0096 |
| AC-8.2 | AI Anomaly Detection | SHALL | AML.T0006, AML.T0061, AML.T0094, AML.T0105 |
| AC-8.3 | Prompt and Response Logging | SHOULD | AML.T0068, AML.T0063 |
| AC-8.5 | Log Retention and Integrity | SHALL | AML.T0092 |
| AC-9.1 | AI Security Awareness Program | SHALL | AML.T0011, AML.T0052 |
| AC-9.4 | AI Threat Awareness | SHALL | AML.T0052, AML.T0100, AML.T0073 |
| AC-10.1 | Model Access Controls | SHALL | AML.T0040, AML.T0044, AML.T0084, AML.T0069, AML.T0056 |
| AC-10.2 | Adversarial Testing | SHALL | AML.T0043, AML.T0015, AML.T0054, AML.T0042 |
| AC-10.3 | Model Versioning and Rollback | SHALL | AML.T0018, AML.T0076 |
| AC-10.4 | Model Integrity Verification | SHALL | AML.T0019, AML.T0058, AML.T0020, AML.T0018, AML.T0070, AML.T0071, AML.T0099 |
| AC-10.5 | Prompt Injection Defense | SHALL | AML.T0051, AML.T0093, AML.T0065, AML.T0080, AML.T0061, AML.T0068 |
| AC-10.6 | Agentic AI Action Authorization and Guardrails | SHALL | AML.T0080 (AI Agent Context Poisoning), AML.T0081 (Modify AI Agent Configuration), AML.T0083 (Credentials from AI Agent Configuration), AML.T0086 (Exfiltration via AI Agent Tool Invocation), AML.T0098 (AI Agent Tool Credential Harvesting), AML.T0099 (AI Agent Tool Data Poisoning), AML.T0100 (AI Agent Clickbait), AML.T0101 (Data Destruction via AI Agent Tool Invocation), AML.T0102 (Generate Malicious Commands), AML.T0103 (Deploy AI Agent), AML.T0104 (Publish Poisoned AI Agent Tool), AML.T0108 (AI Agent — C2), AML.T0110 (AI Agent Tool Poisoning), AML.T0112 (Machine Compromise) |
