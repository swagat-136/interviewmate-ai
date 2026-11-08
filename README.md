# InterviewMate AI 🎙️🤖

> **Multilingual AI-Powered Interview Practice Assistant**  
> *Developed for the Gnani AI Great Indian AI Internship Challenge*

[![React](https://img.shields.io/badge/React-18.3.1-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-6.0.5-646CFF?logo=vite&logoColor=white)](https://vitejs.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4.17-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![Gnani Prisma](https://img.shields.io/badge/Gnani_Prisma_STT-v3.0-5B35D5)](https://gnani.ai/)

---

## 🌟 Executive Overview

**InterviewMate AI** is a full-stack interview preparation platform allowing candidates to practice realistic job interviews using voice or text. Powered by **Gnani Prisma Speech-to-Text (v3.0)**, it supports multiple Indian languages—featuring automatic speech recognition for **Hindi, English, Odia, Tamil, Telugu, Kannada, Bengali, Marathi, and Gujarati**.

The application delivers evidence-based 10-point rubric evaluations across **Relevance, Clarity & Communication, Completeness, and Technical Accuracy**, complete with actionable feedback, model answers, and a personalized AI learning roadmap.

---

## 🎨 UI/UX Design System

Built in strict compliance with the **InterviewMate AI Visual Design Guide**:
- **Color Identity**: Rich purple (`#5B35D5`) & deep indigo (`#24135C`) accents on white/lavender surfaces (`#FFFFFF` · `#F2EEFF`).
- **Dark Theme**: Purposefully designed dark navy theme (`#090D1A` · `#0D1424`) with instant toggle in the navbar.
- **Card Surfaces**: Rounded cards with fine borders, subtle shadows, and responsive layouts across mobile, tablet, and desktop.
- **Micro-Interactions**: Real-time microphone audio visualizer that **animates strictly while recording and stops when recording ends**.

---

## 📂 Project Architecture

```text
interviewmate-ai/
│
├── backend/                       # FastAPI Python Backend (Ready for Render)
│   ├── main.py                    # REST API routes, CORS, session & evaluation handlers
│   ├── requirements.txt           # Dependencies (FastAPI, uvicorn, requests, pydantic, etc.)
│   ├── Procfile                   # Process file for Render deployment
│   ├── .env.example               # Clean configuration template with placeholders
│   ├── .env                       # Local secrets (never committed to Git)
│   ├── .gitignore                 # Backend-specific ignore rules
│   │
│   └── services/
│       ├── __init__.py            # Package initializer
│       ├── gnani_stt.py           # Gnani Prisma v3.0 STT API integration
│       ├── interview_generator.py # Dynamic question generation by role & level
│       └── answer_evaluator.py    # 10-point rubric answer evaluation
│
├── frontend/                      # React + Vite + Tailwind CSS (Ready for Vercel)
│   ├── index.html                 # HTML entry point (Plus Jakarta Sans font)
│   ├── package.json               # Node.js dependencies & scripts
│   ├── package-lock.json          # Locked dependency tree
│   ├── vite.config.js             # Vite config with backend proxy
│   ├── tailwind.config.js         # Custom brand purple & dark theme colors
│   ├── postcss.config.js          # PostCSS configuration
│   ├── vercel.json                # SPA rewrite rules for Vercel
│   │
│   ├── public/
│   │   ├── favicon.svg            # Tab icon
│   │   └── logo.svg               # Vector brand logo
│   │
│   └── src/
│       ├── main.jsx               # React DOM render entry
│       ├── App.jsx                # Layout, routes & providers
│       ├── index.css              # Custom styling, scrollbars & glassmorphism
│       │
│       ├── components/
│       │   ├── Navbar.jsx         # Navigation bar with Dark Mode toggle
│       │   ├── AudioRecorder.jsx  # Mic permissions, recording timer & waveform
│       │   ├── QuestionCard.jsx   # Question prompt & answering strategy tips
│       │   ├── TranscriptionDisplay.jsx # Transcript review & edit panel
│       │   ├── ScoreCard.jsx      # Metric cards with 10-point scale
│       │   ├── PerformanceChart.jsx # Competency benchmark chart
│       │   ├── FeedbackCard.jsx   # AI synthesis, strengths & improvement tips
│       │   ├── LoadingSpinner.jsx # Orbital loading animation
│       │   └── Notification.jsx   # Floating toast alerts
│       │
│       ├── pages/
│       │   ├── LandingPage.jsx    # Hero, Indic glyphs, How it Works & FAQ
│       │   ├── DashboardPage.jsx  # Overview metrics, rubrics & recent sessions
│       │   ├── InterviewSetupPage.jsx # Role, level, language & question count
│       │   ├── LiveInterviewPage.jsx  # Dual voice/text live interview room
│       │   ├── EvaluationPage.jsx # Full 10-point rubric evaluation report
│       │   ├── HistoryPage.jsx    # Searchable session history table
│       │   ├── RoadmapPage.jsx    # AI coach skill gaps & milestones
│       │   └── ProfilePage.jsx    # Candidate career preferences & badges
│       │
│       ├── context/
│       │   ├── InterviewContext.jsx # Global interview session state
│       │   └── ThemeContext.jsx     # Light / Dark mode persistence
│       │
│       ├── hooks/
│       │   └── useAudioRecorder.js  # Web Audio API & MediaRecorder hook
│       │
│       ├── services/
│       │   └── api.js               # Axios client with VITE_API_BASE_URL support
│       │
│       └── utils/
│           ├── constants.js         # Supported roles, languages & levels
│           └── formatters.js        # Score out of 10 & date/time formatters
│
├── .gitignore                     # Root gitignore protecting .env, node_modules, etc.
└── README.md                      # Complete project documentation
```

---

## 🛠️ Local Development & Running

### 1. Backend (FastAPI)
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```
- API Docs: `http://127.0.0.1:8000/docs`
- Health Endpoint: `http://127.0.0.1:8000/health`

### 2. Frontend (React + Vite)
```bash
cd frontend
npm install
npm run dev
```
- App URL: `http://localhost:5173`

---

## 🚢 Deployment Guide

### A. Deploy Backend to Render

1. Go to [Render Dashboard](https://dashboard.render.com/) and click **New +** -> **Web Service**.
2. Connect your GitHub repository: `swagat-136/interviewmate-ai`.
3. Configure the service:
   - **Name**: `interviewmate-ai-backend` (or your choice)
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. In the **Environment Variables** section on Render, add:
   - `GNANI_API_KEY`: `your_gnani_api_key_here`
   - `GNANI_ENDPOINT`: `https://api.vachana.ai/stt/v3`
   - `GNANI_MODEL`: `prisma-v3.0`
5. Click **Create Web Service**. Note your public URL (e.g., `https://interviewmate-ai-backend.onrender.com`).

---

### B. Deploy Frontend to Vercel

1. Go to [Vercel Dashboard](https://vercel.com/) and click **Add New** -> **Project**.
2. Import the `swagat-136/interviewmate-ai` repository.
3. **CRITICAL STEP (Prevents `[vite:build-html] Failed to resolve /src/main.jsx` error)**:
   - Expand the **Root Directory** setting.
   - Click **Edit** and set it to: `frontend`
   - Framework Preset will automatically detect **Vite**.
4. In the **Environment Variables** section on Vercel, add:
   - `VITE_API_BASE_URL`: `https://interviewmate-ai-backend.onrender.com`
     *(Replace with your actual Render backend URL)*
5. Click **Deploy**. Vercel will run `npm run build` and launch your live application with complete SPA routing.
