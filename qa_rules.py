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
