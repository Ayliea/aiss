# AC-10 — Model Security

**Control count:** 6

## Overview

This domain covers AC-10 sub-controls in the Ayliea AI Security Standard. See the [machine-readable spec](../spec/aiss-v1.2.json) for the canonical definition.

## Sub-controls

### AC-10.1 — Model Access Controls (SHALL)

**Requirement:** The organization SHALL enforce access controls on AI model endpoints, ensuring that model access is authenticated, authorized, and rate-limited to prevent unauthorized use, abuse, or data extraction.

**Assessment question:** Does the organization enforce access controls on AI model endpoints, ensuring that model access is authenticated, authorized, and rate-limited to prevent unauthorized use, abuse, or data extraction?

**Implementation guidance:** Model access controls should address authentication (all model access requires valid credentials), authorization (model access is granted based on role and business need), rate limiting (API call rates are constrained to prevent abuse and cost overruns), endpoint security (model inference endpoints are not publicly accessible without authentication), and training and fine-tuning access (restricted to authorized data science personnel with additional controls). For organizations consuming models through vendor APIs, access controls are enforced through API key management and vendor platform configurations. For self-hosted models, the organization must implement controls directly.

**Testing procedure:**

1. Obtain the access control configuration for internally hosted or fine-tuned AI models
2. Verify that model access (training data, model weights, inference endpoints) is restricted to authorized personnel
3. Verify that model access uses separate authentication from general system access
4. Review model access logs for the past 90 days and verify that all access was by authorized personnel
5. Confirm that model access permissions are included in the access review process (AC-4.5)

**Evidence requirements:**

- Model endpoint access control configurations
- Authentication and authorization records
- Rate limiting configurations
- Access control testing results

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| NIST AI RMF | Map 1.1, Govern 4.1 |
| NIST AI 600-1 (GAI Profile) | MS-2.7-001, MS-2.7-004, MS-2.7-009 (Information Security) |
| CIS Controls v8.1 | CIS 5, CIS 6 |
| ISO 27001:2022 | A.8.2, A.8.3, A.8.5 |
| EU AI Act | Art. 9, 15 |
| MITRE ATLAS | AML.T0040, AML.T0044, AML.T0084, AML.T0069, AML.T0056 |

---

### AC-10.2 — Adversarial Testing (SHALL)

**Requirement:** The organization SHALL conduct adversarial testing of AI systems used in high-risk or production contexts at least annually and after any significant model update, including prompt injection testing, data extraction attempts, and jailbreak testing to identify vulnerabilities in model behavior and safety controls.

**Assessment question:** Does the organization conduct adversarial testing of AI systems used in high-risk or production contexts at least annually and after any significant model update, including prompt injection testing, data extraction attempts, and jailbreak testing to identify vulnerabilities in model behavior and safety controls?

**Implementation guidance:** Adversarial testing should be performed before deployment for custom or fine-tuned models and periodically (at least annually) for production AI systems. Testing should cover prompt injection attacks (attempts to manipulate the model into ignoring instructions or executing unintended actions), data extraction attacks (attempts to extract training data, system prompts, or confidential information from model responses), jailbreak testing (attempts to bypass content filters or safety controls), and boundary testing (edge cases that cause unexpected or harmful outputs). Testing methodology should reference the OWASP Top 10 for LLM Applications as a baseline.

**Testing procedure:**

1. Obtain adversarial testing plans and results for AI systems
2. Verify that adversarial testing was conducted at least annually for all production AI systems and after any significant model update
3. Confirm that testing scope includes prompt injection, jailbreaking, data extraction, and model manipulation
4. Review testing findings and verify that identified vulnerabilities were remediated or accepted with documented risk justification
5. Verify that adversarial testing results are reported to the governance body

**Evidence requirements:**

- Adversarial testing methodology documentation
- Testing results reports
- Vulnerability remediation records
- OWASP LLM Top 10 coverage assessment

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | ID.RA-01, PR.DS-01 |
| NIST AI RMF | Measure 1.1, 2.3, 2.6 |
| NIST AI 600-1 (GAI Profile) | MP-2.3-005, MP-5.1-005, MS-2.6-006, MS-2.6-007, MS-2.7-007 (Information Security, CBRN Information or Capabilities, Harmful Bias and Homogenization, Dangerous Violent or Hateful Content) |
| CIS Controls v8.1 | CIS 16, CIS 18 |
| ISO 27001:2022 | A.8.25, A.8.28, A.8.29 |
| EU AI Act | Art. 9, 15 |
| MITRE ATLAS | AML.T0043, AML.T0015, AML.T0054, AML.T0042 |

---

### AC-10.3 — Model Versioning and Rollback (SHALL)

**Requirement:** For self-hosted or fine-tuned models, the organization SHALL maintain version control and rollback capabilities, ensuring that any model deployment can be reverted to a previous known-good version within a defined recovery time objective.

**Assessment question:** For self-hosted or fine-tuned models, does the organization maintain version control and rollback capabilities, ensuring that any model deployment can be reverted to a previous known-good version within a defined recovery time objective?

**Implementation guidance:** Model versioning should track model version identifiers, training data and parameters used for each version, deployment dates and environments, performance metrics at each version, and the reason for each version change. Rollback capability should be tested periodically (at least quarterly) to confirm that previous model versions can be restored within the defined recovery time objective. For organizations that only consume vendor models through APIs, this control applies to any custom configurations, system prompts, or fine-tuning applied to vendor models.

**Testing procedure:**

1. Obtain the model versioning and rollback procedures
2. Verify that a version control system is in use and all model versions are tagged with version number, deployment date, and change description
3. Verify that rollback procedures are documented and have been tested within the past 12 months
4. Confirm that rollback can be executed within a defined timeframe (verify against documented RTO)
5. Verify that model version changes are approved through the change management process

**Evidence requirements:**

- Model version history with change records
- Rollback procedure documentation
- Rollback test results
- Recovery time objective documentation

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.PS-01, RC.RP-01 |
| NIST AI RMF | Manage 2.3, 4.1 |
| NIST AI 600-1 (GAI Profile) | GV-6.2-005, GV-6.2-006, MG-3.2-002, MS-2.8-003 (Information Integrity, Harmful Bias and Homogenization, Value Chain and Component Integration) |
| CIS Controls v8.1 | CIS 16 |
| ISO 27001:2022 | A.8.25, A.8.32 |
| EU AI Act | Art. 9, 15 |
| MITRE ATLAS | AML.T0018, AML.T0076 |

---

### AC-10.4 — Model Integrity Verification (SHALL)

**Requirement:** For self-hosted models, the organization SHALL implement integrity verification procedures to ensure that deployed models have not been tampered with, corrupted, or substituted since their approved deployment.

**Assessment question:** For self-hosted models, does the organization implement integrity verification procedures to ensure that deployed models have not been tampered with, corrupted, or substituted since their approved deployment?

**Implementation guidance:** Model integrity verification should include cryptographic hash verification of model weights against known-good checksums, monitoring for unauthorized changes to model files, configurations, or system prompts, verification that model behavior is consistent with expected outputs for a standardized test set (behavioral fingerprinting), and access logging for all model file modifications. For vendor-hosted models, integrity verification shifts to monitoring for unexpected changes in model behavior and verifying that the vendor has not changed the model version without notification.

**Testing procedure:**

1. Obtain model integrity verification procedures
2. Verify that integrity baselines (checksums, cryptographic hashes) are established for all production models
3. Verify that automated integrity checks are performed on a defined schedule (at minimum, at each deployment and weekly during production operation)
4. Review integrity check results for the past 90 days and verify no unauthorized modifications were detected
5. Confirm that integrity verification failures trigger an incident response process

**Evidence requirements:**

- Model integrity verification procedures
- Cryptographic hash baselines for deployed models
- Integrity verification logs
- Behavioral test set and results

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.DS-01, PR.DS-02 |
| NIST AI RMF | Measure 1.1, 2.3 |
| NIST AI 600-1 (GAI Profile) | MS-2.5-005, MS-2.7-005, MS-2.7-008, MS-2.7-009 (Information Integrity, Information Security, Dangerous Violent or Hateful Content) |
| CIS Controls v8.1 | CIS 16 |
| ISO 27001:2022 | A.8.25, A.8.26, A.8.27 |
| EU AI Act | Art. 9, 15 |
| MITRE ATLAS | AML.T0019, AML.T0058, AML.T0020, AML.T0018, AML.T0070, AML.T0071, AML.T0099 |

---

### AC-10.5 — Prompt Injection Defense (SHALL)

**Requirement:** The organization SHALL implement defenses against prompt injection attacks for AI systems that process external inputs, including input validation, system prompt protection, and output filtering to prevent manipulation of AI behavior through adversarial inputs.

**Assessment question:** Does the organization implement defenses against prompt injection attacks for AI systems that process external inputs, including input validation, system prompt protection, and output filtering to prevent manipulation of AI behavior through adversarial inputs?

**Implementation guidance:** Prompt injection is consistently ranked among the top security risks for LLM applications (OWASP LLM01). Defenses should include input validation and sanitization to detect and neutralize injection patterns, system prompt protection to prevent extraction or override of system-level instructions, output filtering to detect and suppress AI responses that indicate successful injection, separation of system context from user input in API-based implementations, and monitoring for patterns that indicate injection attempts (unusual output patterns, system prompt exposure, unexpected tool use). Defense depth is important because no single defense is sufficient against all injection techniques.

**Testing procedure:**

1. Obtain prompt injection defense documentation and configuration
2. Verify that defenses include at least two of: input validation/sanitization, system prompt isolation, output filtering, or rate limiting
3. Test prompt injection defenses by submitting a set of known prompt injection patterns and verifying they are detected or neutralized
4. Review prompt injection detection logs from the past 90 days and verify that detected attempts were triaged
5. Confirm that prompt injection defenses are tested after each significant system update

**Evidence requirements:**

- Prompt injection defense configurations
- Testing results using injection pattern library
- System prompt protection verification
- Injection monitoring alert logs

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.DS-01, DE.CM-01 |
| NIST AI RMF | Measure 2.6, Manage 1.1 |
| NIST AI 600-1 (GAI Profile) | MP-2.3-005, MP-5.1-005, MP-5.1-006, MS-2.6-006, MS-2.7-007 (Information Security, CBRN Information or Capabilities, Dangerous Violent or Hateful Content) |
| CIS Controls v8.1 | CIS 16 |
| ISO 27001:2022 | A.8.25, A.8.26, A.8.28 |
| EU AI Act | Art. 9, 15 |
| MITRE ATLAS | AML.T0051, AML.T0093, AML.T0065, AML.T0080, AML.T0061, AML.T0068 |

---

### AC-10.6 — Agentic AI Action Authorization and Guardrails (SHALL)

**Requirement:** The organization SHALL constrain agentic AI systems — any AI workflow that invokes tools, calls APIs, executes code, browses systems, or otherwise takes autonomous action — through (a) a documented per-agent tool inventory granted on a least-privilege basis tied to a specific use case, (b) explicit human-in-the-loop approval gates before any irreversible or high-impact action (data deletion, schema changes, financial transfers, account suspension, code merges to protected branches, outbound communication to customers, production configuration changes), (c) blast-radius limits enforced server-side — per-session rate caps, monetary ceilings, row-count limits, and scope predicates that the agent cannot rewrite — (d) acting-on-behalf-of authorization in which an agent invoked by a user inherits that user's permission scope (never broader) and every action is logged with both the agent identity and the originating human principal, (e) per-tool-invocation logging capturing tool name, input arguments, output, agent identity, human principal, session ID, and decision outcome, (f) version control, code review, and integrity protection for tool definitions, agent system prompts, and agent configurations such that changes follow the same change-management path as production code, and (g) for computer-use, browser-use, or shell-execution agents, restriction of execution to ephemeral isolated sandboxes with explicit user confirmation before any persistent state change outside the sandbox.

**Assessment question:** Does the organization constrain agentic AI systems through documented per-agent tool inventories scoped to least privilege, human-in-the-loop approval gates for irreversible actions, server-side blast-radius limits (rate, monetary, row-count, scope), acting-on-behalf-of authorization that inherits but does not exceed the invoking user's permissions, per-tool-invocation logging tied to both agent and human principal, version control and integrity protection for tool definitions and agent configurations, and ephemeral-sandbox isolation with user confirmation for any computer-use, browser-use, or shell-execution agent?

**Implementation guidance:** Agentic AI is the fastest-growing source of unbounded blast-radius risk in modern stacks: a single prompt-injected support agent with a 'refund' tool, a customer-write database tool, and a Slack tool can — within one model turn — drain a payment account, corrupt customer records, and post the result publicly. The control's job is to make that one-turn worst case impossible by construction, not by hoping the model behaves. Start with a tool inventory: every agent gets a written manifest enumerating each tool it can call (e.g., search_orders, send_email, run_sql_readonly), the data scope each tool sees, and the use case that justifies it. Tool grants are reviewed quarterly and revoked when the use case ends — the same lifecycle you apply to service-account credentials under AC-4. Frameworks like LangGraph, Anthropic's Claude tool-use, OpenAI Assistants, and Vercel AI SDK all support enumerated tool sets; what they do not do for you is enforce least privilege, blast-radius caps, or approval gates — that is your application's job, server-side.

Approval gates are the single highest-leverage control. Classify each tool by reversibility and scope: read-only tools (search, summarize, lookup) execute autonomously; reversible writes scoped to a single user's own data (draft an email, create a calendar event in the user's calendar) execute autonomously with logging; mutative production operations (DELETE/DROP/TRUNCATE, payment transfers above the configured threshold, account suspension, code merges to main, mass outbound communication, schema changes, role grants) MUST require a synchronous human approval before the tool function returns. Implement this as a server-side interrupt: the agent's tool call returns a 'pending_approval' result, the human is notified via a UI surface or alert, and the action proceeds only on explicit confirmation. Never trust a model claim like 'the user approved this' embedded in the prompt — verify against a separate, model-untouchable approval record. Blast-radius limits backstop the approval gate: rate-limit tool calls per session (e.g., max 50 write-tool invocations per agent run), enforce monetary caps on any financial tool, cap row counts on SQL tools (e.g., DELETE statements limited to 100 rows and rejected entirely if no WHERE clause), and enforce scope predicates server-side (an agent invoked by user U can only operate on rows where owner_id = U; the model cannot override this even if it crafts a clever argument).

Acting-on-behalf-of authorization is the boundary that prevents agents from becoming a privilege-escalation path. When an agent runs in a user's session, it inherits that user's permissions and nothing more — even if the agent is technically calling a service-role API, the server must apply the calling user's authorization scope. Log every tool call with both the agent identity (which agent + which version of its prompt/config) and the human principal who triggered the session; this lets you forensically distinguish 'the user did this manually' from 'the agent did this on the user's behalf' from 'the agent did this autonomously on a schedule.' Treat the agent's tool definitions, system prompts, and configuration as production code: store them in version control, require code review, sign or hash them so that runtime can verify integrity, and reject startup if the deployed configuration does not match the signed manifest. This closes off MITRE ATLAS AML.T0081 (Modify AI Agent Configuration), AML.T0083 (Credentials from AI Agent Configuration), AML.T0104 (Publish Poisoned AI Agent Tool), and AML.T0110 (AI Agent Tool Poisoning). For agents that drive a browser, operate a UI (Anthropic Computer Use, OpenAI Operator), or execute shell commands, run them in ephemeral, network-restricted sandboxes (e.g., Vercel Sandbox, Firecracker microVMs, dedicated containers) that are destroyed at session end; require explicit user confirmation before any persistent state change reaches a system outside the sandbox, and disable autonomous follow-link or autonomous file-download behavior on untrusted content to mitigate AML.T0100 (AI Agent Clickbait), AML.T0102 (Generate Malicious Commands), AML.T0105 (Escape to Host), and AML.T0112 (Machine Compromise).

**Testing procedure:**

1. Obtain the inventory of production agentic AI systems and, for each agent, the tool manifest listing every tool the agent can invoke, the data scope each tool sees, the use case justifying the grant, and the date of the last least-privilege review
2. For each agent, classify its tools by reversibility and impact; verify that every tool capable of irreversible or high-impact action (data deletion, financial transfer, account suspension, code merge to protected branch, outbound customer communication, production configuration change) requires a synchronous human approval gate enforced server-side, and inspect the approval record store to confirm gate decisions are recorded independently of model-generated content
3. Inspect blast-radius limit configuration and verify server-side enforcement of per-session tool-call rate caps, monetary ceilings on financial tools, row-count or scope predicates on data-mutation tools, and rejection of unbounded operations (e.g., DELETE/UPDATE without WHERE); attempt or review a red-team test where the agent is instructed to exceed each limit and confirm the limits hold
4. Verify acting-on-behalf-of authorization by selecting a sample of agent invocations and confirming that each tool call executed with the calling user's permission scope and that the audit log records both the agent identity (with prompt/config version) and the human principal
5. Review per-tool-invocation logs from the past 90 days and confirm each entry captures tool name, input arguments, output, agent identity, human principal, session ID, and decision outcome; verify logs are retained per AC-8 and tamper-evident
6. Inspect the version control history and code-review records for agent tool definitions, system prompts, and configurations; verify integrity protection (signed manifests, hash verification at startup) and confirm a change-management path equivalent to production application code
7. For any computer-use, browser-use, or shell-execution agent, verify execution occurs in an ephemeral isolated sandbox with restricted network egress, that sandboxes are destroyed at session end, and that an explicit user confirmation is required before any persistent state change is committed outside the sandbox

**Evidence requirements:**

- Inventory of agentic AI systems with per-agent tool manifests, data scope, use-case justification, and last least-privilege review date
- Approval-gate configuration showing which tools require human-in-the-loop sign-off and a sample of approval records from the past 90 days
- Server-side blast-radius limit configurations (rate caps, monetary ceilings, row-count limits, scope predicates) and red-team test results confirming limits cannot be bypassed by adversarial prompting
- Per-tool-invocation log sample (last 90 days) showing tool name, inputs, outputs, agent identity with config version, human principal, session ID, and decision outcome
- Version control history and signed/hashed manifests for agent tool definitions, system prompts, and configurations with integrity-verification logs
- Sandbox configuration and lifecycle records for any computer-use, browser-use, or shell-execution agent, plus user-confirmation records for persistent state changes

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.AA-01, PR.AA-05, PR.PS-01, DE.CM-01 |
| NIST AI RMF | Manage 1.3, Manage 2.3, Manage 4.1 |
| NIST AI 600-1 (GAI Profile) | GV-3.2-003, MS-2.7-001, MG-3.1-003, MG-4.1-002 (Information Security, Human-AI Configuration, Value Chain and Component Integration) |
| CIS Controls v8.1 | CIS 5, CIS 6, CIS 14 |
| ISO 27001:2022 | A.5.15, A.5.18, A.8.2, A.8.3, A.8.16 |
| EU AI Act | Art. 14, Art. 15 |
| MITRE ATLAS | AML.T0080 (AI Agent Context Poisoning), AML.T0081 (Modify AI Agent Configuration), AML.T0083 (Credentials from AI Agent Configuration), AML.T0086 (Exfiltration via AI Agent Tool Invocation), AML.T0098 (AI Agent Tool Credential Harvesting), AML.T0099 (AI Agent Tool Data Poisoning), AML.T0100 (AI Agent Clickbait), AML.T0101 (Data Destruction via AI Agent Tool Invocation), AML.T0102 (Generate Malicious Commands), AML.T0103 (Deploy AI Agent), AML.T0104 (Publish Poisoned AI Agent Tool), AML.T0108 (AI Agent — C2), AML.T0110 (AI Agent Tool Poisoning), AML.T0112 (Machine Compromise) |
| OWASP LLM Top 10 (2025) | LLM06 (Excessive Agency), LLM05 (Improper Output Handling) |

---

