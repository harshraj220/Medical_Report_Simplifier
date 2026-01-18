from fastapi import FastAPI
from app.schemas import InputRequest
from app.ocr import extract_text
from app.extractor import extract_candidate_tests

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

    return {
        "candidate_tests": candidate_tests,
        "confidence": confidence
    }
