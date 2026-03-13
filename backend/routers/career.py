from fastapi import APIRouter
from services.ai_service import generate_response

router = APIRouter()

@router.post("/career-advice")
def career_advice(data: dict):

    skills = data["skills"]

    prompt = f"""
    Suggest career paths for someone with these skills:

    {skills}

    Provide:
    - Career options
    - Skills to learn
    - Learning roadmap
    """

    result = generate_response(prompt)

    return {"career_plan": result}

    from services.youtube_service import search_youtube

@router.get("/learning-videos")

def learning_videos(skill: str):

    videos = search_youtube(skill)

    return {"videos": videos}