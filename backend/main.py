from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import resume, career, auth

app = FastAPI(title="VidyaMitra AI Career Agent")

# CORS configuration (allows React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router)
app.include_router(career.router)
app.include_router(auth.router)


@app.get("/")
def home():
    return {"message": "VidyaMitra backend running"}