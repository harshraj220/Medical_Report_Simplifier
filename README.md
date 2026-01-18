# Medical Report Simplifier

A FastAPI-based web service for simplifying medical reports by extracting structured text from input data (text or images).

## Features

- **Text Processing**: Extract and clean text from raw medical report strings
- **Image OCR**: Placeholder for future OCR functionality to extract text from medical report images
- **RESTful API**: Simple HTTP endpoint for text extraction
- **Confidence Scoring**: Provides confidence levels for extracted text

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd plum_Assessment
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

Start the FastAPI server with:
```bash
uvicorn app.main:app --reload
```

The server will start at `http://127.0.0.1:8000`

### API Documentation

Once running, visit `http://127.0.0.1:8000/docs` for interactive API documentation.

### API Endpoint

**POST /simplify**

Extract text from medical reports.

#### Request Body
```json
{
  "type": "text",
  "content": "Hemoglobin: 14.5 g/dL, WBC: 8.2 x10^9/L, Platelet Count: 250 x10^9/L"
}
```

#### Response
```json
{
  "tests_raw": [
    "Hemoglobin: 14.5 g/dL",
    "WBC: 8.2 x10^9/L",
    "Platelet Count: 250 x10^9/L"
  ],
  "confidence": 0.95
}
```

#### Parameters

- `type`: Input type (`"text"` or `"image"`)
- `content`: The raw text content or base64-encoded image data

## Project Structure

```
plum_Assessment/
├── requirements.txt          # Python dependencies
├── app/
│   ├── main.py              # FastAPI application and routes
│   ├── ocr.py               # Text extraction logic
│   └── schemas.py           # Pydantic data models
└── README.md                # This file
```

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI
- **Pydantic**: Data validation and serialization
- **Pillow**: Image processing library
- **Pytesseract**: OCR engine (for future image processing)

## Development

The image OCR functionality is currently a placeholder and returns empty results. Future development will implement proper OCR using Tesseract.

## License

[Add license information here]