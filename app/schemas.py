from pydantic import BaseModel
from typing import List, Literal

class InputRequest(BaseModel):
    type: Literal["text", "image"]
    content: str

class TextExtractionResponse(BaseModel):
    tests_raw: List[str]
    confidence: float
