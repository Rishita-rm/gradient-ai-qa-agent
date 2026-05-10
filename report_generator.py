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
