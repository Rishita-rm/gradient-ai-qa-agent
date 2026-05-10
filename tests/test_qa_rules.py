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
