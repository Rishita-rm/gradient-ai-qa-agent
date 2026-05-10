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
