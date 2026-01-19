import base64
import pytesseract
from PIL import Image
import io


def extract_text(request):
    # Case 1: Typed text
    if request.type == "text":
        lines = request.content.replace(",", "\n").split("\n")
        cleaned = [line.strip() for line in lines if line.strip()]
        return cleaned, 0.95

    # Case 2: Image input (OCR)
    if request.type == "image":
        try:
            image_bytes = base64.b64decode(request.content)
            image = Image.open(io.BytesIO(image_bytes))

            raw_text = pytesseract.image_to_string(image)

            lines = raw_text.replace(",", "\n").split("\n")
            cleaned = [line.strip() for line in lines if line.strip()]

            confidence = 0.70 if cleaned else 0.0
            return cleaned, confidence

        except Exception:
            return [], 0.0
