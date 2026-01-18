# Medical Report Simplifier

A FastAPI-based web service for simplifying medical reports by extracting and structuring test information from raw text input.

## Features

- **Text Extraction**: Parse and clean medical test data from raw text strings
- **Structured Output**: Convert comma-separated or line-based test results into structured lists
- **Confidence Scoring**: Provides extraction confidence levels
- **RESTful API**: Simple HTTP endpoint for processing medical reports
- **Extensible Design**: Ready for future image OCR integration

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd plum_Assessment
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
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

Once running, visit `http://127.0.0.1:8000/docs` for interactive Swagger UI documentation.

### API Endpoint

**POST /simplify**

Process medical report text to extract test information.

#### Request Body
```json
{
  "type": "text",
  "content": "Hemoglobin 10.2 g/dL (Low)"
}
```

#### Response
```json
{
  "tests_raw": [
    "Hemoglobin 10.2 g/dL (Low)"
  ],
  "confidence": 0.95
}
```

### Testing the API

You can test the endpoint using curl:

```bash
curl -X POST "http://127.0.0.1:8000/simplify" \
     -H "Content-Type: application/json" \
     -d '{
       "type": "text",
       "content": "Hemoglobin: 14.5 g/dL, WBC: 8.2 x10^9/L"
     }'
```

## Project Structure

```
plum_Assessment/
├── requirements.txt          # Python dependencies
├── app/
│   ├── main.py              # FastAPI application and routes
│   ├── ocr.py               # Text extraction and processing logic
│   └── schemas.py           # Pydantic data models
├── venv/                    # Virtual environment (created during setup)
└── README.md                # This file
```

## Dependencies

- **FastAPI**: Web framework for building APIs with automatic OpenAPI docs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pydantic**: Data validation and serialization using Python type hints
- **Pillow**: Image processing library (prepared for future OCR features)
- **Pytesseract**: Python wrapper for Tesseract OCR (prepared for future use)

## Development Notes

- **Current Implementation**: Only text input processing is implemented. Image OCR functionality is a placeholder.
- **Future Enhancements**: 
  - Implement image upload and OCR processing
  - Add more sophisticated text parsing for medical reports
  - Include validation for medical test formats
  - Add authentication and rate limiting

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

[Add license information here]