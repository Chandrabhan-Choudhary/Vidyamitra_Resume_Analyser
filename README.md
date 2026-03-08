## VidyaMitra – Intelligent Career Agent

VidyaMitra is an AI-powered career assistant that helps students and professionals with **resume evaluation**, **mock interviews**, and **personalized career roadmaps** using a modern full‑stack architecture (React.js + FastAPI).

### Features

- **Personalized Resume Evaluation**: Upload a resume (PDF/TXT) and get structured feedback and skill gap hints.
- **AI-Driven Mock Interviews**: Simulated interview Q&A with feedback on answers (initially rule-based / stubbed, ready to plug into LLMs).
- **Career Path & Upskilling Planner**: High‑level recommendations for skills, courses, and next steps based on your current profile.

### Tech Stack

- **Frontend**: React.js single-page application (SPA) in `frontend/`
- **Backend**: FastAPI application in `backend/`
- **API Style**: JSON REST over HTTPS

### Local Development

#### 1. Backend (FastAPI)

From the `backend` folder:

```bash
python -m venv .venv
# On Windows PowerShell
.venv\\Scripts\\Activate.ps1

pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000` and the interactive docs at `http://localhost:8000/docs`.

#### 2. Frontend (React)

From the `frontend` folder:

```bash
npm install
npm run dev
```

The frontend dev server will run at `http://localhost:5173` (or similar). By default it expects the backend at `http://localhost:8000`; this can be configured via environment variable `VITE_API_BASE_URL`.

### High-Level Architecture

- Users access the **React** frontend, which provides dashboards for:
  - Resume upload & insights
  - Mock interview interface
  - Career path and upskilling roadmap
- The frontend calls the **FastAPI** backend for:
  - Resume analysis (`/api/resume/evaluate`)
  - Mock interview generation (`/api/interview/start`, `/api/interview/answer`)
  - Career recommendation (`/api/career/recommend`)
- AI/ML logic can be implemented behind these endpoints or delegated to external LLM APIs.

### Production / Demo Setup (Overview)

- Deploy **backend** (FastAPI) to a PaaS such as Render/Railway with:
  - `requirements.txt`
  - Start command: `uvicorn main:app --host 0.0.0.0 --port 8000`
- Deploy **frontend** (React) to Vercel/Netlify:
  - Build: `npm run build`
  - Output: `dist/`
  - Environment variable `VITE_API_BASE_URL` pointing to the deployed FastAPI base URL.

