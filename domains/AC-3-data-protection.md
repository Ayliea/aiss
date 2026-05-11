# AC-3 — Data Protection in AI

**Control count:** 7

## Overview

This domain covers AC-3 sub-controls in the Ayliea AI Security Standard. See the [machine-readable spec](../spec/aiss-v1.2.json) for the canonical definition.

## Sub-controls

### AC-3.1 — Data Classification for AI Inputs (SHALL)

**Requirement:** The organization SHALL enforce data classification requirements for all data submitted to AI systems, ensuring that employees understand which data classifications are permitted for each approved AI service and that technical controls prevent submission of data exceeding the approved classification level.

**Assessment question:** Does the organization enforce data classification requirements for all data submitted to AI systems, ensuring that employees understand which data classifications are permitted for each approved AI service and that technical controls prevent submission of data exceeding the approved classification level?

**Implementation guidance:** Data classification for AI must map to the organization's existing data classification scheme. At minimum, the organization should define which AI tools are approved for each classification level (e.g., public data may be used with any approved tool; internal data only with enterprise-tier tools that have contractual data protection terms; confidential data prohibited from AI submission without explicit approval and DLP controls; restricted data never permitted in AI interactions). Classification requirements should be communicated in the AI Acceptable Use Policy and enforced through DLP controls where technically feasible.

**Testing procedure:**

1. Obtain the data classification policy as it applies to AI inputs and outputs
2. Verify classification categories (e.g., Public, Internal, Confidential, Restricted) are defined with specific handling requirements for each
3. Select five AI use cases and verify that data flowing to/from AI systems has been classified
4. Verify that classification labels are applied before data is transmitted to external AI services
5. Confirm that data classification requirements are included in AI acceptable use policy training

**Evidence requirements:**

- AI data classification matrix mapping tools to permitted data levels
- DLP rule configurations for AI endpoints
- Test results demonstrating DLP enforcement
- Employee training records covering AI data classification

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.DS-01, PR.DS-02 |
| NIST AI RMF | Map 3.4, Measure 2.5 |
| NIST AI 600-1 (GAI Profile) | MP-4.1-001, MP-4.1-005, MP-4.1-009 (Data Privacy, Information Security, Intellectual Property) |
| CIS Controls v8.1 | CIS 3 |
| ISO 27001:2022 | A.5.12, A.5.13, A.8.11 |
| EU AI Act | Art. 10 |
| MITRE ATLAS | AML.T0070, AML.T0082, AML.T0085 |

---

### AC-3.2 — Data Loss Prevention for AI Endpoints (SHALL)

**Requirement:** The organization SHALL implement data loss prevention controls that monitor, detect, and prevent unauthorized transmission of sensitive data to AI services, including both sanctioned tools exceeding their approved data classification and unsanctioned AI endpoints.

**Assessment question:** Does the organization implement data loss prevention controls that monitor, detect, and prevent unauthorized transmission of sensitive data to AI services, including both sanctioned tools exceeding their approved data classification and unsanctioned AI endpoints?

**Implementation guidance:** DLP for AI endpoints requires rules that specifically target AI service domains and API endpoints. Controls should monitor web traffic to known AI service domains (see appendices.ai_service_domains for a curated starting list), inspect API calls to AI services for sensitive data patterns (PII, PHI, financial data, credentials), alert on or block data submissions that violate classification policies, and log all DLP events for audit and investigation. Where full DLP is not feasible (e.g., the organization lacks a web proxy or NGFW with SSL inspection), compensating controls such as endpoint-based DLP agents or CASB solutions should be evaluated.

**Testing procedure:**

1. Obtain DLP rule configurations applicable to AI services
2. Verify rules cover all known AI service domains (e.g., api.openai.com, claude.ai, copilot.microsoft.com, gemini.google.com)
3. Test DLP rules by submitting sanitized test data containing patterns that should trigger detection (e.g., simulated PII, credential patterns)
4. Review DLP alert logs from the past 90 days and verify that alerts were triaged and resolved
5. Confirm DLP rules are updated when new AI services are added to the approved inventory

**Evidence requirements:**

- DLP policy configurations for AI endpoints
- DLP alert and block logs
- Test results demonstrating DLP effectiveness
- If applicable, documentation of DLP gap as a finding with remediation plan

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.DS-01, PR.DS-02, PR.DS-10 |
| NIST AI RMF | Measure 2.5, Manage 2.2 |
| NIST AI 600-1 (GAI Profile) | MP-4.1-001, MP-4.1-009, MS-2.7-001 (Data Privacy, Information Security) |
| CIS Controls v8.1 | CIS 3 |
| ISO 27001:2022 | A.8.11, A.8.12 |
| EU AI Act | Art. 10, 25 |
| MITRE ATLAS | AML.T0057, AML.T0086, AML.T0024, AML.T0025 |

---

### AC-3.3 — Encryption for AI Data Flows (SHALL)

**Requirement:** The organization SHALL ensure that all data transmitted to and from AI services is encrypted in transit using TLS 1.2 or higher, and that data at rest within AI service environments is encrypted using AES-256 or equivalent, as verified through vendor documentation or contractual commitments.

**Assessment question:** Does the organization ensure that all data transmitted to and from AI services is encrypted in transit using TLS 1.2 or higher, and that data at rest within AI service environments is encrypted using AES-256 or equivalent, as verified through vendor documentation or contractual commitments?

**Implementation guidance:** Encryption in transit is typically enforced by AI service providers at the API level, but the organization must verify this for each service. Encryption at rest depends on vendor implementation and contractual terms. For self-hosted models, the organization must implement encryption directly. Verify that API connections to AI services use HTTPS with TLS 1.2 or higher, vendor documentation or SOC 2 reports confirm encryption at rest, and any local AI model data stores (model weights, training data, inference logs) are encrypted.

**Testing procedure:**

1. Identify all data transmission paths between organizational systems and AI services
2. Verify that each path uses TLS 1.2 or higher for data in transit
3. Verify that data at rest in AI-related datastores uses AES-256 or equivalent encryption
4. Obtain and review the encryption key management procedures
5. Verify encryption certificates are current and not expired
6. Confirm that encryption requirements are documented in AI vendor contracts

**Evidence requirements:**

- Network traffic analysis showing TLS versions for AI service connections
- Vendor security documentation or SOC 2 reports confirming encryption practices
- For self-hosted models, encryption configuration documentation

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.DS-01, PR.DS-02 |
| NIST AI RMF | Manage 2.2 |
| NIST AI 600-1 (GAI Profile) | MS-2.7-001, MS-2.7-004 (Information Security, Data Privacy) |
| CIS Controls v8.1 | CIS 3 |
| ISO 27001:2022 | A.8.24 |
| EU AI Act | Art. 15 |

---

### AC-3.4 — Data Minimization for AI Interactions (SHALL)

**Requirement:** The organization SHALL implement procedures and, where feasible, technical controls to ensure that data submitted to AI systems is limited to what is necessary for the intended purpose, preventing over-sharing of organizational information in AI prompts and inputs.

**Assessment question:** Does the organization implement procedures and, where feasible, technical controls to ensure that data submitted to AI systems is limited to what is necessary for the intended purpose, preventing over-sharing of organizational information in AI prompts and inputs?

**Implementation guidance:** Data minimization for AI is both a procedural and technical challenge. Procedurally, employees need clear guidance on what information is necessary for a given AI interaction versus what constitutes unnecessary exposure (e.g., including a customer's full name and account number when only the account type is needed for the query). Technically, pre-processing or sanitization tools can strip sensitive fields before data reaches AI endpoints. Prompt templates that structure AI interactions can help enforce minimization by design.

**Testing procedure:**

1. Obtain data minimization guidelines for AI interactions
2. Select five AI use cases and review the data sent to AI services for each
3. For each use case, verify that only data necessary for the intended purpose is transmitted (no unnecessary PII, credentials, or confidential data)
4. Verify that prompt templates or pre-processing scripts strip sensitive data before submission
5. Confirm that data minimization requirements are covered in the AI AUP and user training

**Evidence requirements:**

- Data minimization procedures or guidance
- Prompt templates enforcing minimization
- Sanitization tool configurations (if applicable)
- Training records covering data minimization for AI

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.DS-01, PR.DS-10 |
| NIST AI RMF | Map 3.4, Govern 1.7 |
| NIST AI 600-1 (GAI Profile) | MP-4.1-005, MS-2.2-002, MS-2.2-004 (Data Privacy, Human-AI Configuration, Information Security) |
| CIS Controls v8.1 | CIS 3 |
| ISO 27001:2022 | A.5.13, A.8.11 |
| EU AI Act | Art. 10(3) |
| MITRE ATLAS | AML.T0057 |

---

### AC-3.5 — AI Data Retention and Deletion (SHALL)

**Requirement:** The organization SHALL document and enforce data retention requirements for AI interactions, including vendor retention policies, and SHALL verify that deletion mechanisms function as documented.

**Assessment question:** Does the organization document and enforce data retention requirements for AI interactions, including vendor retention policies, and verify that deletion mechanisms function as documented?

**Implementation guidance:** For each AI service, the organization must understand and document how long the vendor retains input data and output data, whether retained data is used for model training (and whether this can be opted out), what deletion mechanisms exist and their verified effectiveness, and whether retention policies meet applicable regulatory requirements (GDPR right to erasure, HIPAA minimum necessary, etc.). For enterprise AI agreements, data retention terms should be explicitly negotiated. For consumer-tier tools used for business purposes, default retention settings should be reviewed and configured to minimize exposure.

**Testing procedure:**

1. Obtain the AI data retention and deletion policy
2. Verify retention periods are defined for each data classification level and that they do not exceed organizational or regulatory requirements
3. For AI vendor relationships, confirm vendor data retention terms are documented in contracts and align with organizational policy
4. Verify that a process exists to request deletion of organizational data from AI vendor systems
5. Review evidence that deletion requests have been executed and confirmed within the past 12 months

**Evidence requirements:**

- Vendor retention policy documentation for each AI service
- Contractual data retention and deletion terms
- Retention configuration screenshots or settings documentation
- Deletion verification records (if tested)

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.DS-01 |
| NIST AI RMF | Map 3.4, Manage 2.4 |
| NIST AI 600-1 (GAI Profile) | GV-1.5-003, MP-4.1-005, MG-4.1-006, MS-2.2-003 (Data Privacy, Information Integrity, Intellectual Property) |
| CIS Controls v8.1 | CIS 3 |
| ISO 27001:2022 | A.5.33, A.8.10 |
| EU AI Act | Art. 10(2), 25 |

---

### AC-3.6 — Cross-Border Data Transfer Controls (SHALL)

**Requirement:** The organization SHALL identify AI services that process data outside the organization's home jurisdiction and SHALL ensure that cross-border data transfers comply with applicable data protection regulations, including contractual safeguards and transfer impact assessments.

**Assessment question:** Does the organization identify AI services that process data outside the organization's home jurisdiction and ensure that cross-border data transfers comply with applicable data protection regulations, including contractual safeguards and transfer impact assessments?

**Implementation guidance:** Cross-border data transfer requirements apply when AI services process data in jurisdictions with different data protection regimes. This is particularly relevant for organizations subject to GDPR (which restricts transfers outside the EU/EEA without adequacy decisions or appropriate safeguards), HIPAA (which requires BAAs regardless of geography but has implications for data sovereignty), and state privacy laws. For each AI service, document the geographic location(s) where data is processed and stored, and verify that appropriate transfer mechanisms are in place.

**Testing procedure:**

1. Identify all AI services that process organizational data outside the organization's home jurisdiction
2. For each cross-border transfer, verify that a legal basis exists (e.g., Standard Contractual Clauses, adequacy decision, binding corporate rules)
3. Verify that data transfer impact assessments have been conducted where required by GDPR or other applicable law
4. Confirm that cross-border data flow documentation is current and has been reviewed within the past 12 months
5. Verify that AI vendor contracts specify data processing locations

**Evidence requirements:**

- Data residency documentation for each AI service
- Cross-border transfer register
- Transfer mechanism documentation (SCCs, adequacy decisions, etc
- Transfer impact assessments (where applicable)

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.OC-03, PR.DS-01 |
| NIST AI RMF | Govern 1.1, Map 3.4 |
| NIST AI 600-1 (GAI Profile) | MG-3.1-002, MP-4.1-005, MP-4.1-010 (Data Privacy, Value Chain and Component Integration, Information Security) |
| CIS Controls v8.1 | CIS 3 |
| ISO 27001:2022 | A.5.31, A.5.34 |
| EU AI Act | Art. 10, Ch. V GDPR |

---

### AC-3.7 — RAG and Vector Store Security (SHALL)

**Requirement:** The organization SHALL secure retrieval-augmented generation (RAG) pipelines and vector stores end-to-end, including (a) classifying and filtering source documents before embedding so that data above the consuming agent's authorization level is not indexed, (b) enforcing access control, encryption at rest, and network isolation on each vector store, (c) treating retrieved content as untrusted input subject to AC-10.5 prompt injection defenses, (d) producing source citations or provenance metadata with every RAG response so users can verify what was retrieved, (e) maintaining an inventory of vector stores with their embedding model, source corpus, refresh cadence, and tenant scope, and (f) enforcing tenant isolation in multi-tenant RAG deployments such that one tenant's queries cannot retrieve another tenant's embeddings.

**Assessment question:** Does the organization secure retrieval-augmented generation (RAG) pipelines and vector stores end-to-end, including classifying source documents before embedding, enforcing access control and encryption on vector stores, treating retrieved content as untrusted input, producing source citations with RAG responses, maintaining a vector store inventory, and enforcing tenant isolation in multi-tenant deployments?

**Implementation guidance:** RAG systems concentrate sensitive data into a single high-value index that is queryable in natural language, making the vector store one of the most attractive targets in an AI application. Before embedding any corpus, run it through the same data classification process used for AC-3.1: documents tagged Restricted or above (board materials, customer PII, secrets, M&A) should not be indexed into a store consumable by a lower-trust agent. Managed vector stores such as Pinecone, Weaviate Cloud, and Qdrant Cloud expose namespace- or collection-level access control, role-based API keys, and customer-managed encryption — turn these on; defaults are usually shared-tenant and not adequate for Restricted data. Self-hosted options (pgvector on Postgres, Chroma, Qdrant OSS, Weaviate OSS) inherit the host platform's controls and should be deployed in a private network with row-level security (pgvector) or per-collection API keys.

Embeddings are model-specific: vectors produced by OpenAI text-embedding-3-large are not comparable to vectors from Cohere embed-v3 or BGE-large, so the chosen embedding model becomes a long-lived dependency. Record the embedding model and version alongside each vector store and plan a full re-embedding when the model is replaced. When the source corpus changes (policy update, new SKU, document deletion), refresh the affected vectors on a documented cadence — daily for high-churn corpora, weekly for policy/knowledge bases, on-event for security-sensitive sources. Retrieved chunks must be treated as untrusted input: a poisoned document in the corpus is an indirect prompt injection vector (OWASP LLM01) and must pass the same input-handling and output-filtering controls described in AC-10.5. Every RAG response shown to a user SHOULD surface the source document, section, and retrieval score so the user can verify the citation; this is also the most practical detection mechanism for embedding poisoning, where an attacker-planted document begins appearing in unrelated queries.

For a 50-500 employee organization, the realistic minimum is one production vector store per trust boundary (e.g., one for internal knowledge, one per customer in multi-tenant SaaS), per-namespace API keys stored in a secrets manager, source documents tagged with classification before ingestion, and a weekly or on-change reindex job. Multi-tenant SaaS RAG deployments MUST enforce tenant isolation at the query layer — most commonly via a per-tenant namespace, collection, or metadata-filter predicate that is set server-side and cannot be overridden by the calling user. Test this isolation explicitly with an automated cross-tenant retrieval test that asserts tenant A's queries return zero results from tenant B's namespace.

**Testing procedure:**

1. Obtain the vector store inventory and verify it lists every production vector store with its embedding model, embedding model version, source corpus, refresh cadence, tenant scope, and data classification ceiling
2. For each vector store, verify access control configuration (namespace or collection-scoped API keys, RBAC roles, or row-level security), encryption at rest (managed-service customer keys or storage-layer encryption), and network isolation (private network, VPC peering, or IP allowlist)
3. Verify that source documents are classified before embedding and that documents above the consuming agent's authorization level are excluded; sample at least 10 indexed documents and confirm classification metadata is present
4. Inspect a sample of recent RAG responses and confirm each response surfaces source citations (document, section, and retrieval score) to the end user
5. Confirm retrieved content is passed through the AC-10.5 prompt injection defenses before being concatenated into the model prompt, and verify a reindex or refresh job ran within the documented cadence (e.g., last 7 days for a weekly cadence)
6. For multi-tenant RAG deployments, execute or review an automated cross-tenant retrieval test that confirms a query authenticated as tenant A returns zero documents belonging to tenant B

**Evidence requirements:**

- Vector store inventory listing embedding model, version, source corpus, refresh cadence, tenant scope, and classification ceiling per store
- Access control, encryption, and network isolation configuration for each vector store (API key scoping, KMS settings, VPC or allowlist)
- Source-document classification rules and a sample of ingested documents with classification metadata attached
- Sample RAG outputs showing source citation, section reference, and retrieval score visible to end users
- Reindex or refresh job logs covering the most recent cadence interval
- Cross-tenant isolation test results for multi-tenant RAG deployments

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.DS-01, PR.DS-02, PR.AA-05, DE.CM-01 |
| NIST AI RMF | Map 3.4, Measure 2.5, Manage 1.3 |
| NIST AI 600-1 (GAI Profile) | MP-1.1-001, MS-2.3-001, MS-2.5-005, MS-2.7-001, MG-3.1-003 (Information Security, Data Privacy, Confabulation, Information Integrity) |
| CIS Controls v8.1 | CIS 3, CIS 5, CIS 13 |
| ISO 27001:2022 | A.5.12, A.8.10, A.8.24, A.8.28 |
| EU AI Act | Art. 10, Art. 15 |
| MITRE ATLAS | AML.T0070 (RAG Poisoning), AML.T0071 (False RAG Entry Injection), AML.T0051 (LLM Prompt Injection), AML.T0082 (RAG Credential Harvesting), AML.T0085.000 (Data from AI Services: RAG Databases) |
| OWASP LLM Top 10 (2025) | LLM01 (Prompt Injection — indirect via retrieved content), LLM02 (Sensitive Information Disclosure), LLM08 (Vector and Embedding Weaknesses) |

---

