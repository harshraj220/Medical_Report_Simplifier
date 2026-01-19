## 🩺 AI-Powered Medical Report Simplifier (Backend)

This project implements **Problem Statement 3: AI-Powered Medical Report Simplifier** from the SDE Intern Backend assignment.

The service accepts **medical reports (text or scanned images)** and returns:

* Structured medical test results
* Normalized values with reference ranges
* Patient-friendly explanations
  while ensuring **no hallucinated data** is introduced.

---

## ✨ Key Features

* Supports **text and image inputs** (OCR ready)
* Robust **multi-step processing pipeline**
* Strict **guardrails** to prevent hallucinations
* Deterministic medical normalization
* Safe, non-diagnostic patient explanations
* Clean REST API with JSON responses

---

## 🧠 Processing Pipeline

```
Input (text / image)
   ↓
OCR / Text Extraction
   ↓
Candidate Test Detection
   ↓
Structured Parsing
   ↓
Normalization (Reference Ranges)
   ↓
Patient-Friendly Explanation
   ↓
Final JSON Output
```

Each step is isolated, validated, and tested independently.

---

## 🛡️ Guardrails & Safety

The system **intentionally stops processing** when unsafe or ambiguous input is detected.

### Guardrail Conditions

* No medical tests found
* Unable to parse test values
* Unknown tests without reference ranges
* Prevents hallucinated tests or explanations

Example guardrail response:

```json
{
  "status": "unprocessed",
  "reason": "unknown test normalization"
}
```

---

## 🚀 How to Run Locally

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start Server

```bash
uvicorn app.main:app
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Usage

### Endpoint

```
POST /simplify
```

### Request (Text Input)

```json
{
  "type": "text",
  "content": "Hemoglobin 10.2 g/dL (Low), WBC 9000 /uL"
}
```

---

## ✅ Example Responses

### Normal WBC

```json
{
  "tests": [
    {
      "name": "WBC",
      "value": 9000,
      "unit": "/uL",
      "status": "normal",
      "ref_range": {
        "low": 4000,
        "high": 11000
      }
    }
  ],
  "summary": "White blood cell count is within the normal range.",
  "explanations": [
    "A normal white blood cell count generally suggests no active infection."
  ],
  "status": "ok"
}
```

---

### Low Hemoglobin

```json
{
  "tests": [
    {
      "name": "Hemoglobin",
      "value": 10.2,
      "unit": "g/dL",
      "status": "low",
      "ref_range": {
        "low": 12.0,
        "high": 15.0
      }
    }
  ],
  "summary": "Hemoglobin level is lower than normal.",
  "explanations": [
    "Low hemoglobin levels may be associated with anemia."
  ],
  "status": "ok"
}
```

---

## 📂 Project Structure

```
app/
 ├── main.py          # API entry point
 ├── schemas.py       # Request schemas
 ├── ocr.py           # Text / OCR extraction
 ├── extractor.py     # Candidate test detection
 ├── parser.py        # Structured parsing
 ├── normalizer.py    # Reference range normalization
 ├── explainer.py     # Patient-friendly explanations
 └── __init__.py
```

---

## 🧪 Testing

All pipeline steps were tested using `curl` with:

* Normal values
* High / Low values
* Unknown tests (guardrails)

---

## 🎯 Notes

* Reference ranges are **hardcoded intentionally** for deterministic behavior.
* Explanations use **template-based logic** to avoid hallucinations.
* The system is **non-diagnostic** and for informational purposes only.

---

## 👤 Author

**Harsh**



