# AC-6 — AI Output Validation

**Control count:** 6

## Overview

This domain covers AC-6 sub-controls in the Ayliea AI Security Standard. See the [machine-readable spec](../spec/aiss-v1.2.json) for the canonical definition.

## Sub-controls

### AC-6.1 — Human Review Processes for High-Risk AI Outputs (SHALL)

**Requirement:** The organization SHALL require documented human review and approval for AI-generated outputs used in regulated decision-making, client-facing communications, financial reporting, legal analysis, medical recommendations, and any context where errors carry material business or compliance risk.

**Assessment question:** Does the organization require documented human review and approval for AI-generated outputs used in regulated decision-making, client-facing communications, financial reporting, legal analysis, medical recommendations, and any context where errors carry material business or compliance risk?

**Implementation guidance:** Human review requirements should be proportional to the risk of the output context. For high-risk use cases (e.g., AI-generated responses to regulatory inquiries, AI-informed hiring decisions, AI-generated medical or legal content), review should be performed by a qualified individual before the output is disseminated. Review should assess factual accuracy, compliance with organizational policies, appropriateness for the intended audience, and absence of harmful bias or discrimination.

**Testing procedure:**

1. Identify all AI use cases classified as high-risk (consequential decisions, regulated outputs, customer-facing AI content)
2. For each high-risk use case, verify that a human review process is documented with designated reviewer roles
3. Review a sample of at least five human-reviewed AI outputs to confirm the review was substantive (not rubber-stamped)
4. Interview at least two designated reviewers to assess their understanding of review criteria and escalation procedures
5. Verify that review completion is logged with reviewer identity, timestamp, and approval decision

**Evidence requirements:**

- Human review procedure documentation for each high-risk use case
- Review logs with reviewer identity and approval records
- Sample reviewed outputs with reviewer annotations or approval stamps

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.OC-04 |
| NIST AI RMF | Measure 2.6, 2.7, 2.11 |
| NIST AI 600-1 (GAI Profile) | GV-3.2-003, MG-2.2-001, MG-3.2-008, MS-2.5-003 (Human-AI Configuration, Confabulation, Harmful Bias and Homogenization, Dangerous Violent or Hateful Content) |
| ISO 27001:2022 | A.5.1 |
| EU AI Act | Art. 14, 26(1) |
| Colorado AI Act | §6-1-1703(4) |
| MITRE ATLAS | AML.T0015, AML.T0067, AML.T0088 |

---

### AC-6.2 — Accuracy and Hallucination Monitoring (SHALL)

**Requirement:** The organization SHALL implement procedures to monitor the accuracy of AI-generated outputs, particularly for domain-specific queries where the AI system may generate plausible but incorrect information (hallucinations).

**Assessment question:** Does the organization implement procedures to monitor the accuracy of AI-generated outputs, particularly for domain-specific queries where the AI system may generate plausible but incorrect information (hallucinations)?

**Implementation guidance:** Hallucination risk varies by use case and model. Organizations should identify use cases where hallucination carries the highest risk (legal citations, medical information, financial calculations, regulatory interpretations) and implement appropriate monitoring. This may include periodic sampling and manual verification of AI outputs, automated fact-checking against authoritative sources where feasible, tracking error rates over time to identify degradation, and user feedback mechanisms for reporting inaccurate AI outputs.

**Testing procedure:**

1. Obtain accuracy monitoring procedures for AI systems
2. Verify that high-risk AI use cases have been identified and prioritized for accuracy monitoring
3. Review accuracy measurement results for the past six months, including sample sizes and error rates
4. Verify that accuracy thresholds are defined for each high-risk use case and that threshold breaches trigger investigation
5. Confirm that identified accuracy issues were investigated and remediated with documented resolution

**Evidence requirements:**

- Accuracy monitoring procedures and results
- Hallucination risk assessment by use case
- Error rate tracking data
- Incident records for accuracy failures

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.OC-04 |
| NIST AI RMF | Measure 1.1, 2.3, 2.6 |
| NIST AI 600-1 (GAI Profile) | MS-2.3-002, MS-2.5-003, MS-2.6-005, MP-2.3-003, MG-4.1-004 (Confabulation, Information Integrity, Information Security) |
| ISO 27001:2022 | A.5.1 |
| EU AI Act | Art. 9(7), 15(1) |
| MITRE ATLAS | AML.T0060, AML.T0062 |

---

### AC-6.3 — Bias Detection and Mitigation (SHALL)

**Requirement:** The organization SHALL implement procedures to detect and mitigate bias in AI outputs, particularly for AI systems that influence decisions affecting individuals, including hiring, lending, insurance, and service delivery.

**Assessment question:** Does the organization implement procedures to detect and mitigate bias in AI outputs, particularly for AI systems that influence decisions affecting individuals, including hiring, lending, insurance, and service delivery?

**Implementation guidance:** Bias detection should focus on AI systems used in consequential decision-making as defined by applicable AI regulations. The Colorado AI Act specifically requires deployers of high-risk AI systems to use reasonable care to prevent algorithmic discrimination. Bias detection methods may include testing AI outputs across protected characteristic groups to identify differential treatment, reviewing AI-generated recommendations for patterns that correlate with demographic attributes, conducting periodic impact assessments for high-risk AI use cases, and establishing a process for consumers or employees to report suspected bias.

**Testing procedure:**

1. Identify all AI systems used in consequential decision-making as defined by applicable regulations
2. Review the bias detection methodology and confirm it tests for differential treatment across protected characteristic groups
3. Obtain bias testing results for the past 12 months and verify testing covered all high-risk AI systems
4. Verify that impact assessments have been conducted for high-risk AI systems as required by applicable regulations
5. Confirm that a mechanism exists for consumers or employees to report suspected bias
6. Review any bias incidents from the past 12 months and verify remediation was completed

**Evidence requirements:**

- Bias detection methodology documentation
- Bias testing results by AI system
- Impact assessment records for high-risk AI systems
- Bias incident and remediation records

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.OC-04 |
| NIST AI RMF | Measure 2.6, 2.10, 2.11 |
| NIST AI 600-1 (GAI Profile) | MS-2.11-001, MS-2.11-002, MS-2.11-004, MG-2.2-004, MG-3.2-001 (Harmful Bias and Homogenization, Dangerous Violent or Hateful Content) |
| ISO 27001:2022 | A.5.1 |
| EU AI Act | Art. 9, 10, 15, 27 |
| Colorado AI Act | §6-1-1702(1), 1703(1), 1703(4) |

---

### AC-6.4 — AI Output Labeling and Disclosure (SHALL)

**Requirement:** The organization SHALL implement disclosure practices that inform recipients when content or decisions have been generated or substantially influenced by AI systems, in compliance with applicable transparency requirements.

**Assessment question:** Does the organization implement disclosure practices that inform recipients when content or decisions have been generated or substantially influenced by AI systems, in compliance with applicable transparency requirements?

**Implementation guidance:** Disclosure requirements vary by regulation and context. The EU AI Act requires that AI systems intended to interact with natural persons be designed and developed in such a way that the persons concerned are informed they are interacting with an AI system. The Colorado AI Act requires deployers of high-risk AI systems to notify consumers before a consequential decision is made. Internally, AI-generated content should be identified as such in metadata, document properties, or visible labeling to support quality assurance and accountability.

**Testing procedure:**

1. Review AI output labeling practices across all business functions that use AI-generated content
2. Verify compliance with applicable transparency and disclosure requirements (EU AI Act Art. 50, Colorado AI Act consumer notification)
3. Test at least three consumer-facing AI interactions to confirm proper disclosure is provided before or at the point of interaction
4. Review internal content labeling practices and confirm AI-generated content is identified as such in metadata, document properties, or visible labeling
5. Verify that disclosure templates or notices have been reviewed by legal counsel

**Evidence requirements:**

- AI output labeling policy and procedures
- Consumer disclosure templates or notices
- Sample labeled AI outputs
- Compliance review records for applicable disclosure requirements

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.OC-04 |
| NIST AI RMF | Govern 1.7, Measure 2.7 |
| NIST AI 600-1 (GAI Profile) | GV-5.1-002, MP-5.1-003, MS-1.1-001, MS-2.7-005 (Human-AI Configuration, Information Integrity, Confabulation) |
| ISO 27001:2022 | A.5.1 |
| EU AI Act | Art. 13, 50 |
| Colorado AI Act | §6-1-1703(4) |
| MITRE ATLAS | AML.T0088, AML.T0073 |

---

### AC-6.5 — Automated Output Quality Controls (SHOULD)

**Requirement:** The organization SHOULD implement automated quality controls for AI outputs used in production workflows, including content filters, formatting validators, and consistency checks appropriate to the output context.

**Assessment question:** Does the organization implement automated quality controls for AI outputs used in production workflows, including content filters, formatting validators, and consistency checks appropriate to the output context?

**Implementation guidance:** Automated quality controls supplement human review and are particularly valuable for high-volume AI output workflows. Controls may include content safety filters that screen AI outputs for harmful, offensive, or inappropriate content; format validators that verify AI outputs meet structural requirements before use in downstream systems; consistency checks that compare AI outputs against known-good baselines or organizational standards; and automated flagging of outputs that exceed confidence thresholds or contain patterns indicating potential errors. Note that this control uses SHOULD rather than SHALL, as implementation feasibility depends on the organization's AI usage patterns and technical maturity.

**Testing procedure:**

1. Obtain documentation of automated output quality controls for AI systems in production
2. Verify that quality controls include at least two of: content filters, formatting validators, consistency checks, or toxicity detection
3. Test automated controls by submitting inputs designed to trigger quality control responses
4. Review quality control alert logs from the past 90 days and verify that flagged outputs were reviewed
5. Confirm that quality control thresholds are defined and documented for each production AI workflow

**Evidence requirements:**

- Automated quality control configurations
- Quality control alert and action logs
- Coverage assessment relative to AI output workflows

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | PR.DS-01 |
| NIST AI RMF | Measure 1.3, 2.3 |
| NIST AI 600-1 (GAI Profile) | MG-3.2-005, MG-3.2-006, MS-2.6-005, MS-2.7-005 (Information Integrity, Harmful Bias and Homogenization, Dangerous Violent or Hateful Content, Obscene Degrading and/or Abusive Content) |
| ISO 27001:2022 | A.8.9, A.8.29 |
| EU AI Act | Art. 9, 15 |
| MITRE ATLAS | AML.T0077, AML.T0102 |

---

### AC-6.6 — Synthetic Content Provenance and Marking (SHALL)

**Requirement:** The organization SHALL embed machine-readable provenance metadata (such as C2PA Content Credentials, SynthID, or equivalent watermarking) in AI-generated image, video, audio, and text content that it publishes externally; SHALL preserve that metadata through editing, transcoding, and storage workflows; SHALL evaluate externally received content used in decisions or downstream publication for synthetic-content markers; and SHALL provide clear human-readable disclosure on any deepfake or AI-generated depiction of real persons or events that it publishes, consistent with EU AI Act Article 50(2) and 50(4) where applicable.

**Assessment question:** Does the organization embed machine-readable provenance metadata in AI-generated content it publishes, preserve that metadata through content workflows, evaluate received content for synthetic-content markers, and disclose deepfakes depicting real persons or events?

**Implementation guidance:** Synthetic content provenance is distinct from human-readable disclosure (AC-6.4). It requires that machine-readable signals — cryptographically signed metadata, watermarks, or fingerprints — accompany AI-generated outputs so downstream systems can detect AI origin without relying on a human reading a label. The leading interoperable standard is C2PA Content Credentials (https://c2pa.org), already emitted by OpenAI DALL-E 3, Adobe Firefly, Microsoft Designer, and supported by Google's SynthID hybrid approach for images and audio. Producer-side, the organization should inventory which of its generative AI tools emit C2PA or equivalent provenance natively (link this to the AI tool inventory in AC-2.1), configure those tools to emit provenance by default, and document compensating manual disclosure for tools that do not.

Consumer-side, content workflows that ingest user-uploaded media, vendor submissions, or employee-supplied documents for use in decisions or downstream publication should run a C2PA verifier (the open-source c2patool, Adobe Content Authenticity Initiative SDK, or Truepic Lens) and route detected synthetic content per policy — for example, flagging for review rather than auto-trusting. Provenance metadata is fragile: image resizing, video transcoding, social-platform re-encoding, and some CMS pipelines strip C2PA manifests unless explicitly preserved. Asset pipelines should be tested end-to-end to confirm metadata survives, and stripped or tampered manifests should escalate rather than be silently accepted.

The EU AI Act Article 50(2) imposes a provider obligation: providers of generative AI systems must ensure outputs are marked in a machine-readable format and detectable as artificially generated, effective 2 August 2026. Article 50(4) is a separate deployer obligation: deployers publishing deepfakes that depict real persons or events must clearly disclose the content is AI-generated or manipulated. Organizations that both build and publish with generative AI fall under both. The European Commission's Code of Practice on AI-Generated Content (first draft published 17 December 2025; finalization anticipated June 2026) is expected to set the operational benchmark for compliance; until it is final, organizations should implement C2PA + SynthID-class watermarking as the reasonable-best-effort baseline.

**Testing procedure:**

1. Obtain the inventory of generative AI tools the organization uses to produce externally published content (cross-reference AC-2.1) and verify each is annotated with its native provenance capability (C2PA, SynthID, none)
2. Select at least three samples of recently published AI-generated content (image, video or audio, and text) and verify machine-readable provenance is present using a C2PA verifier (e.g., c2patool, Content Authenticity Initiative verify tool) or the tool's published watermark detector
3. Walk a representative content production pipeline end-to-end (generation → editing/resize/transcode → CMS → published asset) and confirm provenance metadata survives each step; document any stripping points and the compensating control
4. Review the procedure for handling externally received content used in decisions or downstream publication and confirm it includes provenance verification, handling rules for detected synthetic content, and escalation for stripped or tampered manifests
5. Test at least one published deepfake or AI-generated depiction of a real person or event and confirm clear, conspicuous human-readable disclosure is present in addition to machine-readable marking (EU AI Act Article 50(4))
6. Review the organization's tracking of the EU AI Act Article 50 effective date (2 August 2026) and the EU Code of Practice on AI-Generated Content for in-scope content and jurisdictions

**Evidence requirements:**

- Synthetic content provenance and marking policy
- Generative AI tool inventory annotated with provenance capability (C2PA, SynthID, watermarking, none)
- Sample published AI-generated assets with verified provenance metadata (C2PA verifier output)
- Content pipeline preservation test results showing metadata survives editing, transcoding, and CMS handoff
- Procedure for verifying provenance on externally received content and handling stripped or tampered manifests
- Deepfake disclosure templates and at least one sample deepfake publication with human-readable disclosure

**Framework mappings:**

| Framework | References |
|---|---|
| NIST CSF 2.0 | GV.OC-04, PR.DS-01 |
| NIST AI RMF | Govern 1.7, Measure 1.3, Measure 2.6 |
| NIST AI 600-1 (GAI Profile) | GV-5.1-002, MS-1.1-001, MS-2.7-005, MG-3.2-008 (Information Integrity, Human-AI Configuration, Confabulation) |
| CIS Controls v8.1 | CIS 3 |
| ISO 27001:2022 | A.5.34, A.8.9 |
| EU AI Act | Art. 50(1), Art. 50(2), Art. 50(4) |
| MITRE ATLAS | AML.T0088 (Generate Deepfakes), AML.T0067 (LLM Trusted Output Components Manipulation), AML.T0060 (Publish Hallucinated Entities) |
| OWASP LLM Top 10 (2025) | LLM09 (Misinformation) |

---

