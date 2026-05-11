# AISS ↔ OWASP LLM Top 10 (2025) Crosswalk

This crosswalk maps AISS sub-controls to **OWASP LLM Top 10 (2025)** requirements. For the forward direction (OWASP LLM Top 10 (2025) → AISS), refer to the per-control `framework_mappings` field in [spec/aiss-v1.2.json](../spec/aiss-v1.2.json).

## Mappings

| AISS Control | Title | Normative | OWASP LLM Top 10 (2025) References |
|---|---|---|---|
| AC-3.7 | RAG and Vector Store Security | SHALL | LLM01 (Prompt Injection — indirect via retrieved content), LLM02 (Sensitive Information Disclosure), LLM08 (Vector and Embedding Weaknesses) |
| AC-6.6 | Synthetic Content Provenance and Marking | SHALL | LLM09 (Misinformation) |
| AC-10.6 | Agentic AI Action Authorization and Guardrails | SHALL | LLM06 (Excessive Agency), LLM05 (Improper Output Handling) |
