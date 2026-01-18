from fastapi import FastAPI
from app.schemas import InputRequest
from app.ocr import extract_text
from app.extractor import extract_candidate_tests
from app.parser import parse_test_line
from app.normalizer import normalize_test
from app.explainer import explain_tests



app = FastAPI(title="Medical Report Simplifier")


@app.post("/simplify")
def simplify_report(request: InputRequest):
    tests_raw, confidence = extract_text(request)
    candidate_tests = extract_candidate_tests(tests_raw)

    if not candidate_tests:
        return {
            "status": "unprocessed",
            "reason": "no valid medical tests found"
        }

    # STEP 3: Parsing
    parsed_tests = []
    for line in candidate_tests:
        parsed = parse_test_line(line)
        if not parsed:
            return {
                "status": "unprocessed",
                "reason": "unable to parse medical test values"
            }
        parsed_tests.append(parsed)

    # STEP 4: Normalization
    normalized_tests = []
    for test in parsed_tests:
        normalized = normalize_test(test)
        if not normalized:
            return {
                "status": "unprocessed",
                "reason": "unknown test normalization"
            }
        normalized_tests.append(normalized)

    explanation = explain_tests(normalized_tests)

    return {
        "tests": normalized_tests,
        "summary": explanation["summary"],
        "explanations": explanation["explanations"],
        "status": "ok"
    }

