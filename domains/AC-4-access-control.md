# AC-4 — Access Control for AI

**Control count:** 6

## Overview

This domain covers AC-4 sub-controls in the Ayliea AI Security Standard. See the [machine-readable spec](../spec/aiss-v1.3.json) for the canonical definition.

## Sub-controls

### AC-4.1 — Role-Based Access Control for AI Tools (SHALL)

**Requirement:** The organization SHALL enforce role-based or attribute-based access control for all AI systems, ensuring that access is granted based on job function and business need, with different permission levels for standard users, power users, and administrators.

**Assessment question:** Does the organization enforce role-based or attribute-based access control for all AI systems, ensuring that access is granted based on job function and business need, with different permission levels for standard users, power users, and administrators?

**Implementation guidance:** AI tools often have multiple permission tiers (e.g., basic chat access vs. fine-tuning capabilities vs. admin console access). Each tier should map to a defined role with documented permissions. Standard users should have access to approved AI tools for their job function with standard data classification limits. Power users may have access to advanced features (custom GPTs, API access, integration capabilities) with additional training requirements. Administrators should be limited to IT and security personnel who manage the AI platform configuration.

**Testing procedure:**

1. Obtain the RBAC matrix or access control policy for AI tools and platforms
2. Verify that roles are defined with minimum necessary permissions (least privilege principle)
3. Select three AI tools and verify that user access aligns with assigned roles
4. Verify that role assignments are approved by the AI asset owner or designated authority
5. Confirm that role definitions distinguish between standard users, power users, and administrators

**Evidence requirements:**

- RBAC configuration documentation for AI platforms
- Role-to-permission mapping
- User access lists by role
- Access provisioning and deprovisioning procedures

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| NIST AI RMF | Govern 4.1 |
| NIST AI 600-1 (GAI Profile) | GV-2.1-001, GV-3.2-003, GV-4.1-003 (Information Security, Human-AI Configuration) |
| CIS Controls v8.1 | CIS 5, CIS 6 |
| ISO 27001:2022 | A.5.15, A.5.18, A.8.2, A.8.3 |
| EU AI Act | Art. 14, 26 |
| MITRE ATLAS | AML.T0012 |

---

### AC-4.2 — Multi-Factor Authentication for AI Services (SHALL)

**Requirement:** The organization SHALL require multi-factor authentication (MFA) for all AI services that process internal, confidential, or restricted data, including web-based AI platforms, API management consoles, and AI administration interfaces.

**Assessment question:** Does the organization require multi-factor authentication (MFA) for all AI services that process internal, confidential, or restricted data, including web-based AI platforms, API management consoles, and AI administration interfaces?

**Implementation guidance:** MFA should be enforced through the organization's identity provider (Entra ID, Google Workspace, Okta, etc.) via SSO integration where available. For AI services that do not support SSO, MFA should be enabled natively within the platform. API-based access should use token-based authentication with short-lived credentials rather than static API keys where possible.

**Testing procedure:**

1. Obtain the list of all AI services accessible by organizational users
2. For each AI service, verify that MFA is enabled and enforced
3. Test MFA enforcement by attempting access without a second factor (or reviewing configuration settings)
4. Verify that MFA requirements apply to all access methods (web, API, mobile)
5. Confirm that MFA exceptions, if any, are documented and approved by the governance body

**Evidence requirements:**

- IdP conditional access policies showing MFA requirements for AI services
- Platform authentication configuration screenshots
- MFA enrollment and adoption metrics

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.AA-01, PR.AA-02 |
| NIST AI RMF | Govern 4.1 |
| NIST AI 600-1 (GAI Profile) | MS-2.7-001, MS-2.7-004, MS-2.7-009 (Information Security) |
| CIS Controls v8.1 | CIS 6 |
| ISO 27001:2022 | A.5.17, A.8.5 |
| EU AI Act | Art. 15 |
| MITRE ATLAS | AML.T0012, AML.T0091 |

---

### AC-4.3 — Privileged Access Management for AI (SHALL)

**Requirement:** The organization SHALL implement privileged access controls for AI administration functions, including model management, training pipeline access, data export capabilities, and platform configuration changes.

**Assessment question:** Does the organization implement privileged access controls for AI administration functions, including model management, training pipeline access, data export capabilities, and platform configuration changes?

**Implementation guidance:** Privileged AI access includes the ability to modify AI system configurations, access training data, export conversation logs or usage data, manage API keys and integrations, approve or deploy models, and modify content filters or safety settings. These privileges should be restricted to named individuals, require additional authentication (step-up MFA or separate admin accounts), and be logged for audit purposes.

**Testing procedure:**

1. Obtain the list of users with privileged access to AI systems (administrative accounts, model training access, configuration access)
2. Verify that privileged access is limited to personnel whose roles require it
3. Confirm that privileged AI sessions are logged with user identity, timestamp, and actions performed
4. Verify that privileged access requires separate authentication from standard user access
5. Review the most recent privileged access review and confirm it was completed within the past 90 days

**Evidence requirements:**

- Privileged role definitions for each AI platform
- Named list of personnel with privileged AI access
- Privileged access logs
- Evidence of periodic privileged access review

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.AA-05 |
| NIST AI RMF | Govern 4.1, Manage 1.3 |
| NIST AI 600-1 (GAI Profile) | MS-2.7-001, MS-2.7-004, MS-2.7-009 (Information Security) |
| CIS Controls v8.1 | CIS 5, CIS 6 |
| ISO 27001:2022 | A.8.2, A.8.18 |
| EU AI Act | Art. 14, 26 |
| MITRE ATLAS | AML.T0044, AML.T0081, AML.T0083 |

---

### AC-4.4 — API Key and Secret Management (SHALL)

**Requirement:** The organization SHALL manage all AI API keys and secrets through a centralized secrets management system, with automated rotation at least every 90 days, access logging, and immediate revocation procedures for compromised credentials.

**Assessment question:** Does the organization manage all AI API keys and secrets through a centralized secrets management system, with automated rotation at least every 90 days, access logging, and immediate revocation procedures for compromised credentials?

**Implementation guidance:** API keys for AI services should never be hardcoded in application source code, stored in plain text configuration files, shared via email or messaging platforms, or embedded in prompts or AI interactions. Keys should be stored in a secrets vault (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, or equivalent), rotated on a defined schedule (no less than every 90 days), scoped to minimum necessary permissions, and immediately revokable through documented procedures.

**Testing procedure:**

1. Obtain the inventory of all API keys, secrets, and tokens used to access AI services
2. Verify that keys are stored in a secrets management vault (not in source code, configuration files, or documentation)
3. Confirm that API keys are scoped to minimum required permissions
4. Verify that key rotation has occurred within the past 90 days for all active keys
5. Confirm that a process exists for immediate key revocation when compromise is suspected
6. Review access logs for API key usage and verify that usage patterns are consistent with approved use cases

**Evidence requirements:**

- Secrets management system configuration
- API key inventory with rotation dates
- Code repository scan results for secrets detection
- Documented key revocation procedures

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.AA-02, PR.DS-01 |
| NIST AI RMF | Govern 4.1 |
| NIST AI 600-1 (GAI Profile) | MS-2.7-001, MS-2.7-004 (Information Security) |
| CIS Controls v8.1 | CIS 5, CIS 6 |
| ISO 27001:2022 | A.5.17, A.8.4, A.8.9 |
| EU AI Act | Art. 15 |
| MITRE ATLAS | AML.T0040, AML.T0055, AML.T0098, AML.T0096 |

---

### AC-4.5 — AI Access Review and Recertification (SHALL)

**Requirement:** The organization SHALL conduct access reviews for all AI systems at least every 90 days, verifying that access remains appropriate for each user's current role and removing access for users who have changed roles or left the organization.

**Assessment question:** Does the organization conduct access reviews for all AI systems at least every 90 days, verifying that access remains appropriate for each user's current role and removing access for users who have changed roles or left the organization?

**Implementation guidance:** Access reviews should be conducted by or with input from the business owner of each AI tool. Reviews should verify that all users with access have a current business need, users who have changed roles still require their assigned access level, terminated employees and contractors have been deprovisioned, and service accounts and API keys are still in active use and appropriately scoped.

**Testing procedure:**

1. Obtain the most recent AI access review records
2. Verify that access reviews for AI systems with privileged accounts are completed at least quarterly
3. Verify that access reviews for AI systems with standard user accounts are completed at least annually
4. Confirm that access reviews result in documented decisions (retain, modify, or revoke) for each account reviewed
5. Verify that accounts flagged for revocation during the review were disabled within 7 business days of the review completion
6. Confirm that access review results are reported to the governance body

**Evidence requirements:**

- Access recertification records with dates and reviewer names
- Remediation records for identified access issues
- Cross-reference results showing deprovisioning compliance

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.AA-05 |
| NIST AI RMF | Govern 4.1 |
| NIST AI 600-1 (GAI Profile) | GV-1.5-001, MS-2.7-009 (Information Security, Information Integrity) |
| CIS Controls v8.1 | CIS 5, CIS 6 |
| ISO 27001:2022 | A.5.18, A.8.2 |
| EU AI Act | Art. 26 |
| Colorado AI Act | §6-1-1703(3) |
| MITRE ATLAS | AML.T0012, AML.T0021 |

---

### AC-4.6 — AI Integration Controls (SHOULD)

**Requirement:** The organization SHOULD maintain an approved-integration list governing which AI tools and agents may connect to internal systems, databases, and APIs, and SHOULD require a security review scoping each integration to least privilege before access is granted.

**Assessment question:** Does the organization restrict which AI tools and agents can connect to internal systems, databases, and APIs through an approved-integration list and a pre-connection security review?

**Implementation guidance:** AI tools and agents that integrate directly with internal data sources (via plugins, connectors, MCP servers, or service accounts) can expose large volumes of organizational data through a single over-permissioned integration. This control governs the AI tool's access to systems and data; user-level access to AI tools is covered by AC-4.1. Maintain an allowlist of approved AI integrations, scope each to least privilege, and require security review of data scope, authentication method, and data-processing location before connection. Re-review integrations periodically and on scope change.

**Testing procedure:**

1. Obtain the approved AI-integration list
2. Verify that a security review is required before any AI tool or agent is connected to internal systems
3. Select three AI integrations and confirm each was reviewed and scoped to least privilege
4. Verify that declined integration requests are documented
5. Confirm that approved integrations are periodically re-reviewed

**Evidence requirements:**

- Approved AI-integration allowlist
- Security review records for each integration with data-scope and authentication detail
- Least-privilege scoping configuration per integration
- Records of declined integration requests

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.AA-05, ID.AM-03 |
| NIST AI RMF | Manage 2.1 |
| CIS Controls v8.1 | CIS 3, CIS 6 |
| ISO 27001:2022 | A.5.15, A.8.3 |

---

