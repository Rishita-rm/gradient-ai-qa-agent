# Gradient AI QA Agent — Complete GitHub Project

A complete markdown-formatted project package for your GitHub repository.

Use this document to create each file in your GitHub repo.

---

# 1. Repository Name

```text
gradient-ai-qa-agent
```

---

# 2. GitHub Description

```text
A Python-based AI QA agent that tests LLM responses, logs failures, and generates structured QA reports before production deployment.
```

---

# 3. Recommended GitHub Topics

```text
ai
llm
quality-assurance
ai-testing
python
digitalocean
gradient-ai
agentic-ai
observability
testing
```

---

# 4. Repository Structure

```text
gradient-ai-qa-agent/
├── README.md
├── requirements.txt
├── .env.example
├── agent.py
├── evaluator.py
├── qa_rules.py
├── report_generator.py
├── examples/
│   └── sample_prompts.json
├── outputs/
│   └── sample_qa_report.json
├── tests/
│   ├── test_evaluator.py
│   └── test_qa_rules.py
└── docs/
    ├── header.png
    └── architecture.png
```

---

# 5. `README.md`

```markdown
# Gradient AI QA Agent

![Gradient AI QA Agent Header](docs/header.png)

A Python-based AI QA agent that tests LLM application responses, logs failures, and generates structured QA reports before production deployment.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Proof%20of%20Concept-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Testing](https://img.shields.io/badge/Testing-Pytest-purple)

---

## Why This Project Matters

Most AI agent demos stop when the first response works.

But production AI systems need more than a working demo. They need testing, logging, validation, repeatable evaluation, and clear failure reports.

This project shows how to build a lightweight QA layer for LLM applications. It checks AI responses for missing required facts, blocked terms, weak answers, and basic quality issues before those responses reach users.

The goal is simple:

> Turn manual AI response review into a repeatable QA workflow.

---

## What This Project Does

Gradient AI QA Agent helps test LLM outputs using simple rule-based checks.

It can:

- Load AI test prompts from a JSON file
- Generate mock LLM responses for local testing
- Evaluate responses against QA rules
- Check for required keywords
- Check for blocked or unsafe terms
- Check minimum response length
- Save a structured QA report
- Run basic unit tests for the QA logic

This is a proof-of-concept project. The first version uses mock responses so the QA workflow can be tested locally before connecting it to a real model or DigitalOcean Gradient endpoint.

---

## Architecture

![Architecture Diagram](docs/architecture.png)

```text
Test Prompts
     ↓
AI Response
     ↓
QA Agent
     ↓
Evaluation Rules
     ↓
Failure Logs
     ↓
QA Report
```

The workflow starts with sample prompts, runs each prompt through a mock AI response function, evaluates the response, and saves the results in a JSON report.

---

## Repository Structure

```text
gradient-ai-qa-agent/
├── README.md
├── requirements.txt
├── .env.example
├── agent.py
├── evaluator.py
├── qa_rules.py
├── report_generator.py
├── examples/
│   └── sample_prompts.json
├── outputs/
│   └── sample_qa_report.json
├── tests/
│   ├── test_evaluator.py
│   └── test_qa_rules.py
└── docs/
    ├── header.png
    └── architecture.png
```

---

## File Overview

| File | Purpose |
|---|---|
| `agent.py` | Runs the main QA workflow |
| `qa_rules.py` | Contains response quality checks |
| `evaluator.py` | Evaluates each AI response against a test case |
| `report_generator.py` | Saves QA results into a JSON report |
| `examples/sample_prompts.json` | Stores sample AI test cases |
| `outputs/sample_qa_report.json` | Stores the generated QA report |
| `tests/` | Contains unit tests for the QA logic |
| `.env.example` | Shows required environment variables |
| `requirements.txt` | Lists project dependencies |

---

## How It Works

The QA workflow has four main steps:

1. Load test cases from `examples/sample_prompts.json`
2. Generate or collect an AI response
3. Evaluate the response using QA rules
4. Save the final report in `outputs/sample_qa_report.json`

The current version uses a mock LLM response function. This keeps the project simple and easy to test locally.

Later, the mock response function can be replaced with a real DigitalOcean Gradient model or agent endpoint.

---

## Example Test Case

```json
{
  "id": "test_001",
  "prompt": "Explain password reset steps to a frustrated customer.",
  "required_keywords": ["password", "reset", "email"],
  "blocked_terms": ["stupid", "obviously", "your fault"],
  "expected_tone": "supportive",
  "min_words": 25
}
```

This test case checks whether the AI response:

- Mentions important required words
- Avoids blocked or unsafe terms
- Gives enough detail
- Matches the expected support use case

---

## Example Output

After the QA agent runs, it creates a report like this:

```json
{
  "total_tests": 3,
  "passed": 3,
  "failed": 0,
  "results": [
    {
      "test_id": "test_001",
      "prompt": "Explain password reset steps to a frustrated customer.",
      "passed": true,
      "checks": {
        "required_keywords": {
          "passed": true,
          "missing_keywords": []
        },
        "blocked_terms": {
          "passed": true,
          "blocked_terms_found": []
        },
        "minimum_length": {
          "passed": true,
          "word_count": 27,
          "minimum_required": 25
        }
      }
    }
  ]
}
```

---

## Prerequisites

Before running this project, make sure you have:

- Python 3.10 or higher
- Git
- pip
- Basic understanding of Python
- Optional: DigitalOcean account if you want to extend this with Gradient AI or ADK later

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/gradient-ai-qa-agent.git
cd gradient-ai-qa-agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
# Mac/Linux
source venv/bin/activate
```

```bash
# Windows
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file using the `.env.example` file.

```bash
cp .env.example .env
```

Example `.env.example`:

```bash
DIGITALOCEAN_API_KEY=your_api_key_here
MODEL_NAME=your_model_name_here
ENVIRONMENT=development
```

Do not commit real API keys to GitHub.

The current version does not require a real API key because it uses mock responses for local testing.

---

## How to Run

Run the QA agent:

```bash
python agent.py
```

Expected terminal output:

```text
QA run complete
Total tests: 3
Passed: 3
Failed: 0
```

The report will be saved here:

```text
outputs/sample_qa_report.json
```

---

## Running Tests

Run the test suite with:

```bash
pytest tests/
```

Expected output:

```text
tests/test_evaluator.py ..
tests/test_qa_rules.py .....
```

The tests check whether the evaluator and QA rules are working correctly.

---

## Current QA Checks

The first version includes three simple checks:

### 1. Required Keyword Check

Confirms that important expected words appear in the response.

Example:

```text
Required keywords: password, reset, email
```

### 2. Blocked Terms Check

Flags unsafe, rude, or unwanted phrases.

Example:

```text
Blocked terms: stupid, obviously, your fault
```

### 3. Minimum Length Check

Checks whether the response has enough detail.

Example:

```text
Minimum words: 25
```

These checks are simple on purpose. They make the first version easy to understand, test, and extend.

---

## Why Start With Rule-Based QA?

AI evaluation can get complicated very quickly.

You can use embeddings, semantic similarity, LLM-as-judge scoring, retrieval checks, and human review workflows.

But the first version of a QA system should be easy to trust.

Rule-based checks are not perfect, but they are useful for catching obvious failures:

- Missing facts
- Unsafe words
- Very short answers
- Basic formatting problems
- Repeated response issues

This project starts with simple checks, then leaves room for more advanced evaluation later.

---

## DigitalOcean Gradient / ADK Extension

This repository is designed as a local proof-of-concept that can later be connected to DigitalOcean Gradient and the Agent Development Kit.

A future cloud version could:

- Replace `mock_llm_response()` with a real Gradient model call
- Deploy the QA agent using DigitalOcean ADK
- Run automated evaluations on agent outputs
- Store logs and traces
- Trigger QA checks before production deployment
- Run on a DigitalOcean Droplet or GPU Droplet

The long-term goal is to create a shift-left QA workflow for AI agents.

Instead of waiting for users to find bad outputs, teams can test agent behavior earlier.

---

## Roadmap

- [ ] Add DigitalOcean Gradient model endpoint integration
- [ ] Add ADK deployment workflow
- [ ] Add semantic similarity checks
- [ ] Add LLM-as-judge evaluation
- [ ] Add hallucination-risk scoring
- [ ] Add dashboard for QA reports
- [ ] Add CI/CD quality gate
- [ ] Add Docker support
- [ ] Add GitHub Actions workflow
- [ ] Add cloud deployment guide

---

## Troubleshooting

| Problem | Possible Cause | Fix |
|---|---|---|
| `ModuleNotFoundError` | Dependencies not installed | Run `pip install -r requirements.txt` |
| `FileNotFoundError` | Missing `sample_prompts.json` | Check the `examples/` folder |
| Empty report | No test cases loaded | Confirm JSON file has test cases |
| Tests not running | Pytest not installed | Run `pip install pytest` |
| API key error | `.env` missing or incorrect | Add values to `.env` |

---

## Example Use Cases

This project can be adapted for:

- AIML QA testing
- LLM response validation
- Customer support bot testing
- Prompt regression testing
- Agentic workflow testing
- AI safety pre-checks
- Tone and policy validation
- Model comparison tests
- Pre-deployment AI quality gates

---

## Limitations

This project is intentionally lightweight.

Current limitations:

- Uses mock LLM responses
- Uses rule-based checks only
- Does not yet call a real DigitalOcean Gradient endpoint
- Does not include semantic evaluation
- Does not include dashboard visualization
- Does not replace human review for high-risk AI systems

This is the first useful version, not the final production system.

---

## Future Production Improvements

For production use, I would add:

- Real model endpoint integration
- Prompt version tracking
- Model version tracking
- Run timestamps
- Failure category labels
- Retry tracking
- Cost tracking
- Latency tracking
- CI/CD integration
- Human review for high-risk outputs

The goal is not just to test one response.

The goal is to make AI quality measurable over time.

---

## Medium Article

Full write-up:

```text
[Medium Link]
```

---

## Contributing

Contributions are welcome.

You can improve this project by:

- Adding new QA rules
- Adding DigitalOcean Gradient integration
- Improving test coverage
- Adding dashboard support
- Improving documentation
- Adding more example test cases

To contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Open a pull request

---

## License

This project is licensed under the MIT License.

---

## Final Note

Most AI demos prove that an agent can answer once.

Production AI systems need to prove something harder:

> The agent can behave reliably across repeated prompts, changing inputs, and real user workflows.

This project is a small step toward that goal.
```

---

# 6. `requirements.txt`

```txt
python-dotenv==1.0.1
pytest==8.2.2
```

---

# 7. `.env.example`

```bash
DIGITALOCEAN_API_KEY=your_api_key_here
MODEL_NAME=your_model_name_here
ENVIRONMENT=development
```

---

# 8. `examples/sample_prompts.json`

```json
[
  {
    "id": "test_001",
    "prompt": "Explain password reset steps to a frustrated customer.",
    "required_keywords": ["password", "reset", "email"],
    "blocked_terms": ["stupid", "obviously", "your fault"],
    "expected_tone": "supportive",
    "min_words": 25
  },
  {
    "id": "test_002",
    "prompt": "Explain what an API rate limit is.",
    "required_keywords": ["requests", "limit", "time"],
    "blocked_terms": ["guaranteed unlimited"],
    "expected_tone": "clear",
    "min_words": 20
  },
  {
    "id": "test_003",
    "prompt": "Explain how refunds work for a SaaS product.",
    "required_keywords": ["refund", "policy", "support"],
    "blocked_terms": ["always guaranteed", "no rules"],
    "expected_tone": "professional",
    "min_words": 25
  }
]
```

---

# 9. `qa_rules.py`

```python
from typing import Dict, List


def check_required_keywords(response: str, required_keywords: List[str]) -> Dict:
    """Check whether all required keywords appear in the response."""
    response_lower = response.lower()

    missing_keywords = [
        keyword for keyword in required_keywords
        if keyword.lower() not in response_lower
    ]

    return {
        "passed": len(missing_keywords) == 0,
        "missing_keywords": missing_keywords
    }


def check_blocked_terms(response: str, blocked_terms: List[str]) -> Dict:
    """Check whether blocked or unsafe terms appear in the response."""
    response_lower = response.lower()

    blocked_terms_found = [
        term for term in blocked_terms
        if term.lower() in response_lower
    ]

    return {
        "passed": len(blocked_terms_found) == 0,
        "blocked_terms_found": blocked_terms_found
    }


def check_minimum_length(response: str, min_words: int) -> Dict:
    """Check whether the response has enough detail."""
    word_count = len(response.split())

    return {
        "passed": word_count >= min_words,
        "word_count": word_count,
        "minimum_required": min_words
    }
```

---

# 10. `evaluator.py`

```python
from typing import Dict

from qa_rules import (
    check_required_keywords,
    check_blocked_terms,
    check_minimum_length
)


def evaluate_response(test_case: Dict, response: str) -> Dict:
    """Evaluate one AI response against one QA test case."""

    keyword_check = check_required_keywords(
        response=response,
        required_keywords=test_case.get("required_keywords", [])
    )

    blocked_terms_check = check_blocked_terms(
        response=response,
        blocked_terms=test_case.get("blocked_terms", [])
    )

    length_check = check_minimum_length(
        response=response,
        min_words=test_case.get("min_words", 25)
    )

    checks = {
        "required_keywords": keyword_check,
        "blocked_terms": blocked_terms_check,
        "minimum_length": length_check
    }

    passed = all(check["passed"] for check in checks.values())

    return {
        "test_id": test_case["id"],
        "prompt": test_case["prompt"],
        "passed": passed,
        "checks": checks,
        "response": response
    }
```

---

# 11. `report_generator.py`

```python
import json
from pathlib import Path
from typing import Dict, List


def save_report(results: List[Dict], output_path: str = "outputs/sample_qa_report.json") -> Dict:
    """Save QA results to a JSON report."""

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    summary = {
        "total_tests": len(results),
        "passed": sum(1 for result in results if result["passed"]),
        "failed": sum(1 for result in results if not result["passed"]),
        "results": results
    }

    with path.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2)

    return summary
```

---

# 12. `agent.py`

```python
import json
from pathlib import Path
from typing import Dict, List

from evaluator import evaluate_response
from report_generator import save_report


def load_test_cases(path: str = "examples/sample_prompts.json") -> List[Dict]:
    """Load QA test cases from a JSON file."""

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Test case file not found: {path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def mock_llm_response(prompt: str) -> str:
    """
    Mock LLM response function.

    Replace this with a real DigitalOcean Gradient model or agent endpoint
    when connecting the project to cloud infrastructure.
    """

    prompt_lower = prompt.lower()

    if "password" in prompt_lower:
        return (
            "I can help you reset your password. "
            "Please check your email for a secure password reset link. "
            "Follow the instructions in that email to complete the reset."
        )

    if "rate limit" in prompt_lower:
        return (
            "An API rate limit controls how many requests a user or system "
            "can make within a specific amount of time."
        )

    if "refund" in prompt_lower:
        return (
            "Refund requests are usually reviewed based on the refund policy. "
            "You can contact support to check whether your account is eligible."
        )

    return "I can help with that request."


def run_qa_agent() -> Dict:
    """Run the AI QA workflow."""

    test_cases = load_test_cases()
    results = []

    for test_case in test_cases:
        prompt = test_case["prompt"]
        response = mock_llm_response(prompt)

        result = evaluate_response(
            test_case=test_case,
            response=response
        )

        results.append(result)

    summary = save_report(results)

    print("QA run complete")
    print(f"Total tests: {summary['total_tests']}")
    print(f"Passed: {summary['passed']}")
    print(f"Failed: {summary['failed']}")

    return summary


if __name__ == "__main__":
    run_qa_agent()
```

---

# 13. `tests/test_qa_rules.py`

```python
from qa_rules import (
    check_required_keywords,
    check_blocked_terms,
    check_minimum_length
)


def test_required_keywords_pass():
    response = "You can reset your password using the email link."
    result = check_required_keywords(response, ["password", "email"])

    assert result["passed"] is True
    assert result["missing_keywords"] == []


def test_required_keywords_fail():
    response = "You can update your account settings."
    result = check_required_keywords(response, ["password", "email"])

    assert result["passed"] is False
    assert "password" in result["missing_keywords"]


def test_blocked_terms_pass():
    response = "I can help you solve this issue."
    result = check_blocked_terms(response, ["stupid", "your fault"])

    assert result["passed"] is True


def test_blocked_terms_fail():
    response = "This is obviously your fault."
    result = check_blocked_terms(response, ["your fault"])

    assert result["passed"] is False
    assert "your fault" in result["blocked_terms_found"]


def test_minimum_length_pass():
    response = "This response has enough words to pass the minimum length requirement."
    result = check_minimum_length(response, 5)

    assert result["passed"] is True
```

---

# 14. `tests/test_evaluator.py`

```python
from evaluator import evaluate_response


def test_evaluate_response_pass():
    test_case = {
        "id": "test_001",
        "prompt": "Explain password reset.",
        "required_keywords": ["password", "reset", "email"],
        "blocked_terms": ["your fault"],
        "min_words": 8
    }

    response = "You can reset your password by using the secure email link."

    result = evaluate_response(test_case, response)

    assert result["passed"] is True
    assert result["test_id"] == "test_001"


def test_evaluate_response_fail_missing_keyword():
    test_case = {
        "id": "test_002",
        "prompt": "Explain password reset.",
        "required_keywords": ["password", "reset", "email"],
        "blocked_terms": [],
        "min_words": 5
    }

    response = "You can update your account settings."

    result = evaluate_response(test_case, response)

    assert result["passed"] is False
```

---

# 15. `outputs/sample_qa_report.json`

```json
{
  "total_tests": 3,
  "passed": 3,
  "failed": 0,
  "results": []
}
```

---

# 16. `docs/architecture.png`

Use the generated architecture diagram with this workflow:

```text
AI QA Agent Workflow

Test Prompts
     ↓
AI Response
     ↓
QA Agent
     ↓
Evaluation Rules
     ↓
Failure Logs
     ↓
QA Report
```

Save the image as:

```text
docs/architecture.png
```

---

# 17. `docs/header.png`

Create a simple header image in Canva, Excalidraw, or PowerPoint.

Recommended text:

```text
Gradient AI QA Agent
Automated QA Testing for LLM Applications
```

Recommended style:

```text
Dark or clean white background
Rounded shapes
AI/cloud/testing icons
Simple professional font
16:9 horizontal layout
```

Save the image as:

```text
docs/header.png
```

---

# 18. First Git Commit Message

```bash
git add .
git commit -m "Initial commit: add AI QA agent proof-of-concept"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/gradient-ai-qa-agent.git
git push -u origin main
```

---

# 19. Quick Local Test Commands

Run the project:

```bash
python agent.py
```

Run tests:

```bash
pytest tests/
```

Check generated output:

```text
outputs/sample_qa_report.json
```

---

# 20. Final GitHub Checklist

Before posting on LinkedIn or Medium, make sure your repo has:

- [ ] Clean repo name: `gradient-ai-qa-agent`
- [ ] Strong GitHub description
- [ ] Complete `README.md`
- [ ] `requirements.txt`
- [ ] `.env.example`
- [ ] Working `agent.py`
- [ ] Working `qa_rules.py`
- [ ] Working `evaluator.py`
- [ ] Working `report_generator.py`
- [ ] `examples/sample_prompts.json`
- [ ] `outputs/sample_qa_report.json`
- [ ] Unit tests inside `tests/`
- [ ] Architecture image in `docs/architecture.png`
- [ ] Optional header image in `docs/header.png`
- [ ] No real API keys
- [ ] Medium link added after publishing

---

# 21. Final Note

This project is intentionally simple.

That is the strength.

The goal is not to pretend this is a full production AI observability system.

The goal is to show a clean proof-of-concept for how AI QA can become repeatable, measurable, and easier to extend.

A strong technical content project does not need to be huge.

It needs to be clear, useful, documented, and connected to a real production problem.

