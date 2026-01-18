from fastapi import FastAPI
from app.schemas import InputRequest
from app.ocr import extract_text
from app.extractor import extract_candidate_tests
from app.parser import parse_test_line

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

    parsed_tests = []

    for line in candidate_tests:
        parsed = parse_test_line(line)
        if not parsed:
            return {
                "status": "unprocessed",
                "reason": "unable to parse medical test values"
            }
        parsed_tests.append(parsed)

    return {
        "tests": parsed_tests,
        "confidence": confidence
    }
