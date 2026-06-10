# AC-2 — AI Asset Management

**Control count:** 6

## Overview

This domain covers AC-2 sub-controls in the Ayliea AI Security Standard. See the [machine-readable spec](../spec/aiss-v1.3.json) for the canonical definition.

## Sub-controls

### AC-2.1 — AI Asset Inventory (SHALL)

**Requirement:** The organization SHALL maintain a current, comprehensive inventory of all AI systems, services, platforms, and integrations in use, including SaaS AI features embedded in existing business applications, standalone AI tools, API-based integrations, and internally developed models.

**Assessment question:** Does the organization maintain a current, comprehensive inventory of all AI systems, services, platforms, and integrations in use, including SaaS AI features embedded in existing business applications, standalone AI tools, API-based integrations, and internally developed models?

**Implementation guidance:** The inventory must capture sanctioned and unsanctioned AI tools. Minimum required fields per asset: tool name and vendor, deployment type (SaaS, API, self-hosted, embedded), business owner, data classification of inputs, integration points with other systems, license and cost information, and date added to inventory. Discovery methods should include financial record review (procurement, expense reports, credit card statements), identity provider and SSO audit (Entra ID or Google Workspace OAuth consent grants), and stakeholder interviews. The inventory should be updated no less than quarterly.

**Testing procedure:**

1. Obtain the AI asset inventory
2. Verify the inventory includes all categories: generative AI tools, AI-powered SaaS features, API integrations, internal models, and automated decision systems
3. For each entry, confirm it includes: system name, vendor, data classification, business owner, approval status, and deployment date
4. Select five AI tools known to be in use and verify all appear in the inventory
5. Select three entries from the inventory and verify accuracy against the live environment
6. Confirm the inventory was updated within the past 90 days

**Evidence requirements:**

- AI asset inventory with all required fields populated
- Discovery method records (financial, IdP, interview)
- Quarterly update logs with dates and changes
- Evidence of shadow AI discovery efforts

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | ID.AM-01, ID.AM-02 |
| NIST AI RMF | Map 1.1, 1.5, 1.6 |
| NIST AI 600-1 (GAI Profile) | GV-1.6-001, GV-1.6-003, GV-6.1-007 (Information Security, Data Privacy, Value Chain and Component Integration, Intellectual Property) |
| CIS Controls v8.1 | CIS 1, CIS 2 |
| ISO 27001:2022 | A.5.9, A.5.10 |
| EU AI Act | Art. 11, 12 |
| MITRE ATLAS | AML.T0007, AML.T0047 |

---

### AC-2.2 — AI Asset Classification (SHALL)

**Requirement:** The organization SHALL classify each AI asset across four dimensions: deployment type (SaaS, API, self-hosted, embedded), data sensitivity (public, internal, confidential, restricted), integration depth (standalone, integrated, automated), and business criticality (experimental, operational, mission-critical).

**Assessment question:** Does the organization classify each AI asset across four dimensions: deployment type (SaaS, API, self-hosted, embedded), data sensitivity (public, internal, confidential, restricted), integration depth (standalone, integrated, automated), and business criticality (experimental, operational, mission-critical)?

**Implementation guidance:** Classification drives control prioritization. An automated AI pipeline processing restricted data (e.g., AI auto-generating responses using customer PHI) requires fundamentally different controls than an experimental standalone tool used with public data. Each dimension should map to specific control requirements: higher data sensitivity requires stricter DLP and encryption, deeper integration requires broader monitoring, and higher business criticality requires availability and accuracy controls.

**Testing procedure:**

1. Obtain the AI asset classification methodology
2. Verify the classification scheme addresses risk dimensions including data sensitivity, decision impact, regulatory applicability, and user population
3. Select 10 AI assets from the inventory and verify each has a current classification rating
4. For assets classified as high-risk, verify that enhanced controls are documented and implemented
5. Confirm classification criteria are consistent with applicable regulatory definitions (EU AI Act high-risk, Colorado AI Act consequential decision)

**Evidence requirements:**

- Classification methodology document
- Completed classification for each inventoried AI asset
- Evidence that classification informed control implementation decisions

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | ID.AM-01, ID.AM-05 |
| NIST AI RMF | Map 1.1, 1.5, 2.1 |
| NIST AI 600-1 (GAI Profile) | GV-1.3-001, GV-1.6-003, MP-1.1-001 (Data Privacy, Intellectual Property, Information Integrity, Value Chain and Component Integration) |
| CIS Controls v8.1 | CIS 1, CIS 2 |
| ISO 27001:2022 | A.5.9, A.5.12, A.5.13 |
| EU AI Act | Art. 6, 9 |
| Colorado AI Act | §6-1-1701(7) |

---

### AC-2.3 — AI Asset Ownership Assignment (SHALL)

**Requirement:** The organization SHALL assign a named business owner and a named technical owner to each AI asset, with documented accountability for security compliance, risk acceptance, and lifecycle decisions.

**Assessment question:** Does the organization assign a named business owner and a named technical owner to each AI asset, with documented accountability for security compliance, risk acceptance, and lifecycle decisions?

**Implementation guidance:** Ownership must be individual, not team-based. Each asset should have a business owner (accountable for the business justification, data handling compliance, and risk acceptance) and a technical owner (accountable for configuration, integration, and security control implementation). Ownership assignments should be reviewed when personnel change roles or leave the organization.

**Testing procedure:**

1. Obtain the list of designated AI asset owners
2. Verify each AI asset in the inventory has a named individual (not a team or role) assigned as owner
3. Interview three asset owners to confirm they understand their responsibilities for the AI systems they own
4. Verify that ownership assignments are documented in the AI asset inventory and in position descriptions
5. Confirm a process exists to reassign ownership when personnel changes occur

**Evidence requirements:**

- Ownership assignment records for each AI asset
- Acknowledgment records from designated owners
- Evidence of ownership updates following organizational changes

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | ID.AM-01, GV.RR-02 |
| NIST AI RMF | Govern 2.1, 2.3 |
| NIST AI 600-1 (GAI Profile) | GV-1.6-003, GV-2.1-001, GV-4.1-003 (Human-AI Configuration, Value Chain and Component Integration, Information Security) |
| CIS Controls v8.1 | CIS 1 |
| ISO 27001:2022 | A.5.9, A.5.2 |
| EU AI Act | Art. 9(4) |

---

### AC-2.4 — Shadow AI Discovery (SHALL)

**Requirement:** The organization SHALL conduct discovery activities at least quarterly to identify AI tools in use that were not procured through approved channels, including personal accounts used for business purposes, unauthorized browser extensions, and AI features enabled by default in existing software.

**Assessment question:** Does the organization conduct discovery activities at least quarterly to identify AI tools in use that were not procured through approved channels, including personal accounts used for business purposes, unauthorized browser extensions, and AI features enabled by default in existing software?

**Implementation guidance:** Shadow AI discovery should employ multiple methods: financial discovery (searching expense reports and credit card statements for AI vendor charges), identity provider audit (reviewing OAuth consent grants in Entra ID or Google Workspace for AI service authorizations), endpoint analysis (scanning for AI-related applications and browser extensions via EDR or MDM platforms, when available), network traffic analysis (filtering outbound connections to known AI service domains, when firewall or proxy logging is available), and direct employee interviews. Where a discovery method cannot be applied because the required infrastructure does not exist, this gap should itself be documented as a finding.

**Testing procedure:**

1. Obtain documentation of shadow AI discovery activities performed in the past 12 months
2. Verify that discovery methods include at least two of the following: network traffic analysis, DNS monitoring, endpoint detection, expense/procurement review, or employee surveys
3. Review the results of the most recent discovery effort and confirm all identified shadow AI tools were either added to the approved inventory or blocked
4. Verify that discovery is performed at least quarterly
5. Confirm that newly discovered shadow AI tools are processed through the governance approval workflow

**Evidence requirements:**

- Shadow AI discovery reports with findings
- Records of remediation actions for discovered shadow AI
- Documentation of unavailable discovery methods as security gaps
- Employee acknowledgment of shadow AI policies

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | ID.AM-01, ID.AM-02, DE.CM-09 |
| NIST AI RMF | Map 1.5, 1.6, 5.1 |
| NIST AI 600-1 (GAI Profile) | GV-1.6-001, GV-1.6-002, GV-6.1-007 (Information Security, Value Chain and Component Integration) |
| CIS Controls v8.1 | CIS 1, CIS 2 |
| ISO 27001:2022 | A.5.9, A.8.9 |
| EU AI Act | Art. 26(5) |
| MITRE ATLAS | AML.T0095 |

---

### AC-2.5 — AI Asset Lifecycle Management (SHALL)

**Requirement:** The organization SHALL establish and enforce procedures for the complete lifecycle of AI assets: approval and onboarding, configuration review, periodic recertification, and secure decommissioning including data retrieval and account termination.

**Assessment question:** Does the organization establish and enforce procedures for the complete lifecycle of AI assets: approval and onboarding, configuration review, periodic recertification, and secure decommissioning including data retrieval and account termination?

**Implementation guidance:** The lifecycle should include a formal approval gate before any new AI tool is deployed, requiring at minimum a security risk assessment, data flow review, and vendor terms evaluation. Recertification should occur annually or when a material change occurs (vendor acquisition, pricing model change, terms of service update). Decommissioning must address data retrieval, account deletion, API key revocation, and removal from integration points.

**Testing procedure:**

1. Obtain AI asset lifecycle management procedures
2. Verify the procedures address all lifecycle stages: evaluation, approval, provisioning, operation, review, and decommissioning
3. Select two AI assets that were decommissioned in the past 12 months and verify that decommissioning procedures were followed, including data deletion confirmation
4. Verify that a periodic review of active AI assets is scheduled and performed at least annually
5. Confirm lifecycle status is tracked in the AI asset inventory

**Evidence requirements:**

- AI asset lifecycle management procedures
- New AI tool approval records with completed risk assessments
- Recertification records
- Decommissioning checklists and completion records

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | ID.AM-01, PR.PS-01 |
| NIST AI RMF | Map 1.1, Govern 1.5 |
| NIST AI 600-1 (GAI Profile) | GV-1.7-001, GV-1.7-002, GV-4.1-003, MG-2.4-004 (Information Security, Value Chain and Component Integration, Human-AI Configuration) |
| CIS Controls v8.1 | CIS 1, CIS 2 |
| ISO 27001:2022 | A.5.9, A.5.11, A.8.9 |
| EU AI Act | Art. 9, 72 |
| Colorado AI Act | §6-1-1703(3) |
| MITRE ATLAS | AML.T0103 |

---

### AC-2.6 — AI Development Tool Governance (SHALL)

**Requirement:** The organization SHALL establish governance requirements for AI-powered development tools (code assistants, code generation platforms, and AI-integrated development environments) that address code review obligations, intellectual property protections, and restrictions on submitting proprietary source code to external AI services.

**Assessment question:** Does the organization establish governance requirements for AI-powered development tools (code assistants, code generation platforms, and AI-integrated development environments) that address code review obligations, intellectual property protections, and restrictions on submitting proprietary source code to external AI services?

**Implementation guidance:** AI coding assistants such as GitHub Copilot, Cursor, Amazon CodeWhisperer, and similar tools present unique risks because they operate directly in the development environment with access to proprietary source code, internal APIs, and infrastructure configurations. Governance should address which AI coding tools are approved and how they are provisioned, whether proprietary or client code may be submitted to AI services (and under what conditions), code review requirements for AI-generated code before it enters production, licensing and intellectual property implications of AI-generated code, and configuration requirements such as disabling telemetry, restricting context sharing, and enforcing enterprise-tier data handling agreements with the tool vendor.

**Testing procedure:**

1. Obtain the list of approved AI development tools and their configuration requirements
2. Verify that governance policies address code submission restrictions, specifying which repositories and code classifications may be exposed to AI coding assistants
3. Confirm that AI-generated code is subject to the same code review standards as human-written code before merging to production branches
4. Review the configuration of at least two AI coding tools to verify compliance with organizational requirements (telemetry settings, context boundaries, enterprise data handling tier)
5. Verify that developers have been trained on the approved use conditions for AI coding assistants
6. Confirm that intellectual property and licensing implications of AI-generated code have been reviewed by legal counsel

**Evidence requirements:**

- AI development tool governance policy
- Approved tool list with configuration baselines
- Code review records showing AI-generated code review
- Developer training completion records for AI tool usage
- Legal review of IP implications

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | ID.AM-01, PR.DS-01 |
| NIST AI RMF | Govern 1.6, Map 2.1 |
| NIST AI 600-1 (GAI Profile) | GV-6.1-001, GV-6.1-010, MP-4.1-006, MS-2.6-004 (Intellectual Property, Value Chain and Component Integration, Dangerous Violent or Hateful Content) |
| CIS Controls v8.1 | CIS 2, CIS 16 |
| ISO 27001:2022 | A.8.4, A.8.25, A.8.28 |
| EU AI Act | Art. 10, 15 |
| Colorado AI Act | §6-1-1703(2) |
| MITRE ATLAS | AML.T0000 |

---

