
# Secure Support Agent

A security-focused AI support assistant built with Python, LangGraph, Retrieval-Augmented Generation (RAG), and Anthropic Claude.

The agent answers technical support questions in Spanish using a controlled knowledge base of Markdown runbooks.

It is designed to reduce unsupported answers, enforce escalation policies, protect credentials, and resist prompt injection attempts.

## Solution Approach

The proposed solution implements a security-focused support assistant using RAG and LangGraph. It retrieves information from five Markdown runbooks and uses Claude to generate responses in Spanish, following predefined security policies.

The architecture combines document retrieval, deterministic security checks, and structured output validation to reduce unsupported answers, prevent credential handling, and mitigate prompt injection attempts. When sufficient information is unavailable, the agent escalates the request.

This approach was chosen to prioritize **security, traceability, and simplicity**, while keeping the solution easy to test, maintain, and extend.

## Tech Stack

- Python 3.12
- LangGraph
- LangChain Anthropic
- Claude Haiku 4.5
- Scikit-learn (TF-IDF and cosine similarity)
- Pydantic
- Python-dotenv

## Architecture

The application uses a two-node LangGraph workflow:

    User Question
         |
         v
    +-------------------+
    | Retrieve          |
    | TF-IDF + Cosine   |
    | Similarity        |
    +-------------------+
         |
         v
    +-------------------+
    | Generate          |
    | Security Checks   |
    | Claude + Pydantic |
    +-------------------+
         |
         v
    Structured Response

### 1. Retrieval

The RAG module:

- Loads Markdown runbooks from `runbooks/`.
- Normalizes text for improved matching.
- Uses TF-IDF with unigram and bigram features.
- Calculates cosine similarity.
- Applies a minimum relevance threshold.
- Reduces the influence of selected prompt injection patterns.

If no relevant documentation is retrieved, the agent escalates instead of generating an unsupported answer.

### 2. Generation

The LangGraph generation node:

- Applies credential-request checks.
- Builds context using retrieved runbooks.
- Sends the context and question to Claude.
- Requests structured output using Pydantic.
- Validates returned source filenames.
- Applies additional escalation rules.

The agent allows at most one retry when structured-output parsing fails.

## Knowledge Base

The project includes five synthetic runbooks created for this technical challenge:

| Runbook | Topic |
|---------|-------|
| `vpn.md` | VPN connectivity |
| `mfa.md` | Multifactor authentication |
| `email.md` | Corporate email troubleshooting |
| `network.md` | Network connectivity |
| `software.md` | Corporate software installation |

These documents are fictional examples and do not contain real organizational procedures or credentials.

## Security Controls

### Credential Protection

The agent rejects detected requests for passwords, tokens, MFA codes, and other credentials.

These requests are escalated without sending them to Claude when identified by the deterministic checks.

### Prompt Injection Mitigation

User questions and retrieved documents are treated as untrusted data.

The system prompt instructs the model to ignore attempts to:

- Override security policies.
- Change the required response language.
- Manipulate escalation decisions.
- Change the expected response format.

The retrieval module also removes selected suspicious instruction patterns before calculating document relevance.

### Source Validation

The agent only accepts source filenames that exactly match retrieved runbooks.

If the model returns no valid source, the agent escalates.

### Escalation

The agent escalates when:

- No relevant documentation is retrieved.
- A credential request is detected.
- A mandatory escalation rule applies.
- Structured output cannot be generated successfully.
- No valid source can be verified.

## Response Format

The agent returns the following fields:

```json
{
  "answer": "Respuesta en español basada en la documentación.",
  "sources": ["vpn.md"],
  "escalate": false
}
```

- `answer`: Spanish-language support response.
- `sources`: Runbooks cited by the agent.
- `escalate`: Whether human intervention is required.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/FJulieta/secure-support-agent.git
cd secure-support-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

The `.env` file is excluded from version control.

Never commit API keys or other credentials.

## Evaluation

The project includes `questions.json` with eight synthetic evaluation cases:

| Category | Cases |
|----------|-------|
| Normal support questions | 4 |
| Out-of-knowledge questions | 2 |
| Credential request | 1 |
| Prompt injection attempt | 1 |

Run the evaluation with:

```bash
python eval.py
```

The evaluator checks:

- Required response fields and data types.
- Expected escalation decisions.
- Expected source filenames.
- Source filename validity.
- Selected refusal and uncertainty patterns.
- Selected indicators of prompt injection compliance.

### Evaluation Results

The latest local evaluation completed with:

```text
Pruebas aprobadas: 8/8
Cumplimiento: 100.0%
```

This result represents successful execution of the eight defined test cases, not a comprehensive security certification.

## Limitations

This project is a technical prototype.

- TF-IDF similarity does not guarantee semantic relevance.
- Regex-based credential detection may miss alternative phrasing.
- Prompt injection mitigation is not exhaustive.
- Valid source filenames do not guarantee factual grounding.
- The evaluator does not fully verify Spanish-language compliance or detect every possible credential disclosure.
- LLM outputs may vary between executions.
- The runbooks are synthetic and do not represent production policies.

Production deployment would require stronger content validation, expanded adversarial testing, monitoring, and additional safeguards.

## Project Structure

```text
secure-support-agent/
├── agent.py
├── rag.py
├── eval.py
├── questions.json
├── requirements.txt
├── README.md
├── main.py
├── test_graph.py
├── test_claude.py
└── runbooks/
    ├── vpn.md
    ├── mfa.md
    ├── email.md
    ├── network.md
    └── software.md
```

## Author

Julieta Fader