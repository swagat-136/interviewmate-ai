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

**InterviewMate AI** is a complete, production-grade interview preparation platform that allows candidates to practice realistic job interviews using voice or text. Engineered with **Gnani Prisma Speech-to-Text (v3.0)**, it empowers job seekers across India to practice comfortably in their native language—featuring automatic speech recognition for **Hindi, English, Odia, Tamil, Telugu, Kannada, Bengali, Marathi, and Gujarati**.

The application delivers evidence-based 10-point rubric evaluations across **Relevance, Clarity & Communication, Completeness, and Technical Accuracy**, complete with actionable feedback, model answers, and a personalized AI learning roadmap.

---

## 🎨 UI/UX Design System

Built in strict compliance with the **InterviewMate AI Visual Design Guide**:
- **Color Identity**: Rich purple (`#5B35D5`) & deep indigo (`#24135C`) accents on white/lavender surfaces (`#FFFFFF` · `#F2EEFF`).
- **Dark Theme**: Purposefully designed dark navy theme (`#090D1A` · `#0D1424`) with instant toggle in the navbar.
- **Card Surfaces**: Rounded cards with fine borders, subtle shadows, and responsive layouts across mobile, tablet, and desktop.
- **Micro-Interactions**: Real-time microphone audio visualizer that **animates strictly while recording and stops when recording ends**.

---

## 🚀 Key Features

### 1. 🌐 Multilingual Speech Recognition (Gnani Prisma v3.0)
- Record voice responses directly in the browser via `MediaRecorder`.
- Automatic language detection using `indic-auto` or specific language codes (`en`, `hi`, `or`, `ta`, `te`, `kn`, `bn`, `mr`, `gu`).
- Uploads audio through secure `multipart/form-data` to the backend STT engine.

### 2. 🎛️ Dual-Mode Live Voice Studio
- Seamless toggle between **Voice Answer** (microphone recording) and **Text Answer** modes.
- Visualizer waveform reflecting real-time microphone volume levels.
- Live recording timer (`Recording... 00:12`) with red circular stop control.

### 3. ✏️ Transcript Review & Edit
- Inspect the raw speech-to-text transcript returned by the backend.
- Full in-place editing allows candidates to correct technical jargon or noise artifacts before evaluation, ensuring fair scoring.

### 4. 📊 10-Point Multi-Rubric Evaluation
- Circular overall score indicator (`8.0 / 10` or `8.2 / 10`).
- Dedicated rubric scores:
  - **Relevance**: `8.5 / 10`
  - **Clarity & Communication**: `8.0 / 10`
  - **Completeness**: `7.5 / 10`
  - **Technical Accuracy**: `8.0 / 10`
- **Key Strengths** (green checkmarks) and **Areas to Improve** (amber warnings).
- **Suggested Improved Answer** (model response card) and intelligent follow-up questions.

### 5. 🗺️ AI Coach & Learning Roadmap (`/roadmap`)
- Skill gap analysis comparing current candidate metrics against 8.5+ industry standards.
- 4-milestone roadmap: Elevator pitch framing, quantitative impact metrics, STAR method behavioral delivery, and multilingual fluency.

### 6. 📜 Practice History & Management (`/history`)
- Searchable interview sessions with filter by interview type (`Mixed`, `Technical`, `HR`).
- Detailed report modal, score tracking, and delete session with confirmation.

---

## 📂 Project Architecture

```text
interviewmate-ai/
│
├── backend/                       # FastAPI Python Backend
│   ├── main.py                    # API routes, CORS, session & evaluation handlers
│   ├── requirements.txt           # Python dependencies
│   ├── .env.example               # Template for Gnani credentials
│   ├── .env                       # Local environment variables
│   │
│   └── services/
│       ├── gnani_stt.py           # Gnani Prisma v3.0 STT API integration
│       ├── interview_generator.py # Dynamic question generation by role & level
│       └── answer_evaluator.py    # 10-point rubric answer evaluation
│
├── frontend/                      # React + Vite + Tailwind CSS Frontend
│   ├── index.html                 # HTML entry point (Plus Jakarta Sans font)
│   ├── package.json               # Node.js dependencies & scripts
│   ├── vite.config.js             # Vite config with /api proxy to port 8000
│   ├── tailwind.config.js         # Custom brand purple & dark theme colors
│   ├── postcss.config.js          # PostCSS configuration
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
│       │   ├── ScoreCard.jsx      # Metric cards with gradient progress
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
│       │   └── api.js               # Axios client for backend API
│       │
│       └── utils/
│           ├── constants.js         # Supported roles, languages & levels
│           └── formatters.js        # Score out of 10 & date/time formatters
│
└── README.md                      # Complete project documentation
```

---

## 🛠️ Installation & Setup

### Prerequisites
- **Node.js**: v18.0.0 or higher
- **npm**: v9.0.0 or higher
- **Python**: v3.10 or higher

---

### Step 1: Backend Setup

1. Open a terminal and navigate to the backend folder:
   ```bash
   cd C:\Users\KIIT\Desktop\interviewmate-ai\backend
   ```

2. Activate the existing virtual environment:
   - **Windows PowerShell**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **Windows Command Prompt**:
     ```cmd
     .\venv\Scripts\activate.bat
     ```

3. Ensure dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your `.env` file (already created with template):
   ```ini
   GNANI_API_KEY=your_gnani_api_key_here
   GNANI_ENDPOINT=https://api.vachana.ai/stt/v3
   GNANI_MODEL=prisma-v3.0
   ```
   *(Note: If no API key is provided, the backend automatically provides high-fidelity fallback transcripts for offline development and demonstrations).*

5. Start the FastAPI server:
   ```bash
   python -m uvicorn main:app --reload --port 8000
   ```
   - **Server URL**: `http://127.0.0.1:8000`
   - **Interactive API Docs (Swagger)**: `http://127.0.0.1:8000/docs`

---

### Step 2: Frontend Setup

1. Open a second terminal and navigate to the frontend folder:
   ```bash
   cd C:\Users\KIIT\Desktop\interviewmate-ai\frontend
   ```

2. Install dependencies (if not already installed):
   ```bash
   npm install
   ```

3. Start the Vite development server:
   ```bash
   npm run dev
   ```
   - **Application URL**: `http://localhost:5173`

4. To generate a production build:
   ```bash
   npm run build
   ```

---

## 🔌 API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Check backend & Gnani STT service status |
| `POST` | `/api/transcribe` | Upload audio (`multipart/form-data`) & get transcription |
| `POST` | `/api/interviews` | Create new interview practice session |
| `GET` | `/api/interviews/{id}` | Retrieve session details and questions |
| `POST` | `/api/interviews/{id}/answer` | Record candidate transcript for a question |
| `POST` | `/api/interviews/{id}/evaluate` | Compute 10-point rubric scores and feedback |
| `GET` | `/api/interviews/history` | List all completed and in-progress sessions |
| `DELETE`| `/api/interviews/{id}` | Delete a practice session record |

---

## 🧪 Testing

### Frontend Build Test
```bash
cd frontend
npm run build
# Result: 1665 modules transformed cleanly in 3.46s
```

### Backend Endpoint Test
Run the inline diagnostic script inside the Python virtual environment:
```powershell
python -c "import main; print(main.health())"
# Output: {'status': 'healthy', 'gnani_api_key_configured': True, 'engine': 'Gnani Prisma v3.0', ...}
```

---

## 👥 Authors & Acknowledgments

- **Developer**: KIIT Student Developer
- **Challenge**: Gnani AI Great Indian AI Internship Challenge
- **Speech Engine**: Gnani Prisma v3.0 STT (`api.vachana.ai`)
