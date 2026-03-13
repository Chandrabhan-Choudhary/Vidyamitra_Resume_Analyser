# 🚀 VidyaMitra – AI Resume Analyzer & Career Assistant

VidyaMitra is an **AI-powered career assistant** that helps students and professionals improve their resumes, identify skill gaps, and explore career opportunities.

The platform allows users to **upload their resume as a PDF**, analyze it using AI models, and receive structured feedback such as strengths, weaknesses, missing skills, and career suggestions.

---

# ✨ Features

### 📄 AI Resume Analyzer

Upload a **PDF resume** and receive:

* Resume strengths
* Weaknesses
* Missing skills
* Career recommendations

### 🎯 Career Guidance

Users can input their skills to get **AI-powered career suggestions** and learning paths.

### 🤖 Multi-LLM Support

The backend supports multiple AI providers:

* **Google Gemini**
* **OpenAI**

### ☁️ Cloud Database

Uses **Supabase** for secure cloud storage and real-time synchronization.

### 📚 Learning Resource Integration

External APIs provide:

* YouTube learning resources
* Visual learning content (Pexels API)

---

# 🏗 System Architecture

```
User
  ↓
React Frontend
  ↓
FastAPI Backend
  ↓
PDF Resume Parsing (PyMuPDF)
  ↓
AI Processing (Gemini / OpenAI)
  ↓
Career Insights & Recommendations
```

---

# 🧠 Tech Stack

## Frontend

* React.js
* Axios
* CSS

## Backend

* FastAPI
* Python

## AI Services

* Google Gemini API
* OpenAI API

## Database

* Supabase

## Additional Libraries

* PyMuPDF (PDF parsing)
* python-multipart (file upload handling)
* python-dotenv

---

# 📂 Project Structure

```
vidyamitra/
│
├── backend/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── database/
│   ├── models/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── .gitignore
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```
git clone https://github.com/Chandrabhan-Choudhary/Vidyamitra_Resume_Analyser
cd Vidyamitra_Resume_Analyser
```

---

# 2️⃣ Backend Setup (FastAPI)

```
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

Start backend server:

```
uvicorn main:app --reload
```

Backend will run at:

```
http://localhost:8000
```

API documentation:

```
http://localhost:8000/docs
```

---

# 3️⃣ Frontend Setup (React)

```
cd frontend

npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

# 🔑 Environment Variables

Create a `.env` file inside `backend/`:

```
AI_PROVIDER=gemini

OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key

SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

YOUTUBE_API_KEY=your_youtube_key
PEXELS_API_KEY=your_pexels_key
```

---

# 🧪 API Endpoints

| Endpoint           | Description                   |
| ------------------ | ----------------------------- |
| `/auth/register`   | Register new user             |
| `/auth/login`      | Login user                    |
| `/resume-analysis` | Upload and analyze resume PDF |
| `/career-advice`   | Get career recommendations    |

---

# 🔮 Future Improvements

* Resume **ATS scoring system**
* AI **mock interview trainer**
* Skill gap detection dashboard
* Multi-agent career planning system

---

# 👨‍💻 Contributors

* Chandrabhan Choudhary – Team Lead
* Vinayak Sen
* Amber Gupta
* Anupam Agrawal

---

# 📜 License

This project is developed for **educational and research purposes**.
