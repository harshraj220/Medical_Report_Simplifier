def extract_text(request):
    if request.type == "text":
        # Split lines safely
        lines = request.content.replace(",", "\n").split("\n")
        cleaned = [line.strip() for line in lines if line.strip()]
        return cleaned, 0.95

    # Image OCR placeholder
    # (we’ll implement this properly later)
    return [], 0.0
