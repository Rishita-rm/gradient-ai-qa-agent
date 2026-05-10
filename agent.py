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
