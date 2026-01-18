from fastapi import FastAPI
from app.schemas import InputRequest, TextExtractionResponse
from app.ocr import extract_text

app = FastAPI(title="Medical Report Simplifier")

@app.post("/simplify", response_model=TextExtractionResponse)
def simplify_report(request: InputRequest):
    text, confidence = extract_text(request)
    return {
        "tests_raw": text,
        "confidence": confidence
    }
