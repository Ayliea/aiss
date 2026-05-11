# Appendix: AI Service Domains Reference

**Last reviewed:** 2026-05

Curated reference list of known AI service domains for use with AC-2.4 (Shadow AI Discovery) network traffic analysis and AC-3.2 (DLP for AI) endpoint rules. This list is not exhaustive — new AI services emerge continuously. Organizations should treat this as a starting point and supplement with their own observations. Not all listed services pose equal risk; classification depends on data flows and contractual terms, not the domain itself.

## Categories

### Major foundation-model APIs

- `api.openai.com`
- `api.anthropic.com`
- `generativelanguage.googleapis.com`
- `api.mistral.ai`
- `api.cohere.com`
- `api.together.xyz`
- `api.groq.com`
- `api.deepseek.com`
- `api.x.ai`

### Consumer/web chat surfaces

- `chat.openai.com`
- `chatgpt.com`
- `claude.ai`
- `gemini.google.com`
- `grok.com`
- `x.com/i/grok`
- `perplexity.ai`
- `you.com`
- `poe.com`
- `character.ai`

### Enterprise embedded copilots

- `copilot.microsoft.com`
- `copilot.cloud.microsoft`
- `copilot.office.com`
- `copilot-pw.cloud.microsoft`
- `duet.workspace.google.com`
- `gemini.google.com (workspace integration)`
- `einstein.salesforce.com`

### Developer / coding assistants

- `copilot.github.com`
- `api.githubcopilot.com`
- `cursor.sh`
- `cursor.com`
- `api.cursor.sh`
- `codeium.com`
- `tabnine.com`
- `supermaven.com`
- `windsurf.com`

### Aggregator gateways

- `openrouter.ai`
- `api.openrouter.ai`
- `huggingface.co`
- `api.huggingface.co`
- `replicate.com`
- `api.replicate.com`
- `fireworks.ai`
- `api.fireworks.ai`
- `anyscale.com`

### Image / video / audio generation

- `stability.ai`
- `api.stability.ai`
- `labs.openai.com`
- `midjourney.com`
- `runwayml.com`
- `leonardo.ai`
- `elevenlabs.io`
- `api.elevenlabs.io`
- `playht.com`
- `suno.com`
- `luma.ai`

### Agentic / workflow AI

- `lindy.ai`
- `make.com (AI modules)`
- `zapier.com (AI actions)`
- `n8n.io`
- `crew.ai`
- `langchain.com`
- `smith.langchain.com`
- `autogen.dev`

### Embedding / vector / RAG services

- `pinecone.io`
- `api.pinecone.io`
- `weaviate.io`
- `qdrant.tech`
- `chroma.com`
- `vectorize.io`

### AI security / governance / observability

- `lakera.ai`
- `rebuff.ai`
- `promptarmor.com`
- `credo.ai`
- `holistic.ai`
- `ayliea.com`

## Usage notes

- Domains marked '(workspace integration)' are surfaces of a primary domain that may need separate policy treatment.
- Subdomains of api.* are typically the highest-data-volume surfaces and should be the primary DLP target.
- Aggregator gateways (OpenRouter, Hugging Face Inference) route requests to underlying model providers; logging at the aggregator does not always indicate which provider ultimately processed the data.
- For region-specific endpoints (e.g., eu.api.openai.com, australia.api.cognitive.microsoft.com), apply DLP rules to the regional variant in addition to the primary domain.
- This list does not endorse any service. Inclusion reflects industry adoption, not security posture.
