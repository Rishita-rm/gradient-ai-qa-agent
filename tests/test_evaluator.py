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
