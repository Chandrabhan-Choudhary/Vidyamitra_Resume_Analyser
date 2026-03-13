from fastapi import APIRouter, UploadFile, File
import fitz
from services.ai_service import generate_response

router = APIRouter()

@router.post("/resume-analysis")

async def resume_analysis(file: UploadFile = File(...)):

    pdf_bytes = await file.read()

    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    text = ""

    for page in doc:
        text += page.get_text()

    prompt = f"""
    Analyze this resume and provide:

    1. Strengths
    2. Weaknesses
    3. Missing Skills
    4. Career Suggestions

    Resume:
    {text}
    """

    result = generate_response(prompt)

    return {"analysis": result}