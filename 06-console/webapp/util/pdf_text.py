from io import BytesIO
from PyPDF2 import PdfReader

def pdf_bytes_to_text(data: bytes) -> str:
    r = PdfReader(BytesIO(data))
    return "\n".join((p.extract_text() or "") for p in r.pages)
