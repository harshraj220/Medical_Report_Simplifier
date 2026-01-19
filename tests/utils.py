from PIL import Image, ImageDraw, ImageFont
import io
import os

def create_image_from_text(text, filename="test_image.png"):
    # Create white image
    img = Image.new('RGB', (800, 600), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    
    # Use default font or try to load one. Default is usually fine for Tesseract if large enough.
    # On Mac/Linux, we can't reliably predict font paths, so we use default bitmap font
    # but scale it or just write default. Tesseract handles default font poorly if too small.
    # Let's try to load a basic font, or just use default and hope.
    # Better: Use a large invalid font size which ImageFont.load_default() doesn't support well.
    # We'll just rely on default.
    
    # To improve OCR chances with default font, we can just write it. 
    # But usually default font is very small. 
    # Let's try to find a ttf
    try:
        font = ImageFont.truetype("Arial.ttf", 20)
    except IOError:
        try:
            # Try a generic linux/mac font
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 30) # Mac
        except:
             font = None # Fallback to default

    # Write text
    d.multiline_text((50, 50), text, fill=(0, 0, 0), font=font)
    
    path = os.path.join(os.path.dirname(__file__), filename)
    img.save(path)
    return path
