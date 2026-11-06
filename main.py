import os
import uuid
from datetime import datetime
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

from services.gnani_stt import transcribe_audio_gnani
from services.interview_generator import generate_interview_questions
from services.answer_evaluator import evaluate_interview_session

app = FastAPI(
    title="InterviewMate AI API",
    description="Multilingual AI-powered interview practice assistant powered by Gnani Prisma",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GNANI_API_KEY = os.getenv("GNANI_API_KEY")

# In-memory storage seeded with sample history matching the visual reference gallery
SESSIONS_DB: Dict[str, Dict[str, Any]] = {
    "session_1": {
        "id": "session_1",
        "role": "Software Developer",
        "experience": "Fresher (0-1 year)",
        "interview_type": "Mixed",
        "language": "indic-auto (English)",
        "questions": [
            {"id": "q1", "text": "Tell me about yourself.", "category": "HR & Background"},
            {"id": "q2", "text": "Why do you want to work in this role?", "category": "Motivation"},
            {"id": "q3", "text": "Explain how React virtual DOM differs from real DOM.", "category": "Technical"},
            {"id": "q4", "text": "Describe a challenge you solved in a software project.", "category": "Behavioral"},
            {"id": "q5", "text": "Where do you see yourself in the next 2-3 years?", "category": "Career Goals"}
        ],
        "created_at": "2026-11-04T10:30:00Z",
        "status": "completed",
        "overall_score": 8.0,
    },
    "session_2": {
        "id": "session_2",
        "role": "Data Analyst",
        "experience": "Junior (1-3 years)",
        "interview_type": "Technical",
        "language": "Hindi (hi)",
        "questions": [
            {"id": "q1", "text": "Explain the difference between WHERE and HAVING in SQL.", "category": "Technical"},
            {"id": "q2", "text": "How do you handle missing values in a dataset?", "category": "Data Wrangling"},
            {"id": "q3", "text": "Describe a dashboard you built that drove business value.", "category": "Analytics"}
        ],
        "created_at": "2026-11-02T14:15:00Z",
        "status": "completed",
        "overall_score": 7.6,
    },
    "session_3": {
        "id": "session_3",
        "role": "Software Developer",
        "experience": "Junior (1-3 years)",
        "interview_type": "HR",
        "language": "English",
        "questions": [
            {"id": "q1", "text": "Tell me about yourself.", "category": "Introduction"},
            {"id": "q2", "text": "Tell me about a time you handled a difficult deadline.", "category": "Behavioral"},
            {"id": "q3", "text": "What are your greatest technical strengths?", "category": "Self-Assessment"}
        ],
        "created_at": "2026-10-30T09:00:00Z",
        "status": "completed",
        "overall_score": 8.4,
    }
}

ANSWERS_DB: Dict[str, Dict[str, Any]] = {}
EVALUATIONS_DB: Dict[str, Dict[str, Any]] = {}

class CreateInterviewRequest(BaseModel):
    role: str = "Software Developer"
    experience: str = "fresher"
    interview_type: str = "mixed"
    num_questions: int = 5
    language: str = "indic-auto"
    custom_focus: Optional[str] = None

class SubmitAnswerRequest(BaseModel):
    question_id: str
    transcript: str
    duration_seconds: Optional[int] = 0

@app.get("/")
def home():
    return {
        "status": "online",
        "service": "InterviewMate AI Backend",
        "stt_engine": "Gnani Prisma v3.0",
        "version": "1.0.0"
    }

@app.get("/health")
@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "gnani_api_key_configured": bool(GNANI_API_KEY),
        "engine": "Gnani Prisma v3.0",
        "supported_languages": ["indic-auto", "hi", "en", "or", "ta", "te", "kn", "bn", "mr", "gu"]
    }

@app.post("/upload-audio")
@app.post("/api/transcribe")
async def transcribe_audio(
    file: UploadFile = File(...),
    language: str = Form("indic-auto")
):
    audio_data = await file.read()
    if not audio_data or len(audio_data) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The uploaded audio file is empty."
        )

    result = await transcribe_audio_gnani(
        audio_bytes=audio_data,
        filename=file.filename or "recording.webm",
        language=language
    )
    return result

@app.post("/api/interviews")
def create_interview(request: CreateInterviewRequest):
    session_id = f"session_{uuid.uuid4().hex[:8]}"
    questions = generate_interview_questions(
        role=request.role,
        experience=request.experience,
        interview_type=request.interview_type,
        num_questions=request.num_questions,
        custom_focus=request.custom_focus
    )

    session_data = {
        "id": session_id,
        "role": request.role,
        "experience": request.experience,
        "interview_type": request.interview_type,
        "language": request.language,
        "questions": questions,
        "created_at": datetime.utcnow().isoformat(),
        "status": "in_progress",
        "overall_score": 8.0,
    }

    SESSIONS_DB[session_id] = session_data
    ANSWERS_DB[session_id] = {}

    return session_data

@app.get("/api/interviews/{session_id}")
def get_interview(session_id: str):
    if session_id not in SESSIONS_DB:
        raise HTTPException(status_code=404, detail="Interview session not found.")
    return SESSIONS_DB[session_id]

@app.post("/api/interviews/{session_id}/answer")
def submit_answer(session_id: str, payload: SubmitAnswerRequest):
    if session_id not in SESSIONS_DB:
        raise HTTPException(status_code=404, detail="Interview session not found.")

    if session_id not in ANSWERS_DB:
        ANSWERS_DB[session_id] = {}

    ANSWERS_DB[session_id][payload.question_id] = {
        "transcript": payload.transcript,
        "duration_seconds": payload.duration_seconds,
        "submitted_at": datetime.utcnow().isoformat()
    }

    return {
        "message": "Answer recorded successfully",
        "question_id": payload.question_id,
        "feedback_preview": "Answer saved and analyzed"
    }

@app.post("/api/interviews/{session_id}/evaluate")
def evaluate_interview(session_id: str):
    if session_id not in SESSIONS_DB:
        raise HTTPException(status_code=404, detail="Interview session not found.")

    session_data = SESSIONS_DB[session_id]
    answers = ANSWERS_DB.get(session_id, {})

    evaluation = evaluate_interview_session(session_data, answers)
    evaluation["session_id"] = session_id
    evaluation["role"] = session_data["role"]
    evaluation["evaluated_at"] = datetime.utcnow().isoformat()

    EVALUATIONS_DB[session_id] = evaluation
    session_data["status"] = "completed"
    session_data["overall_score"] = evaluation["overall_score"]

    return evaluation

@app.get("/api/interviews/history")
def get_interview_history():
    history_list = []
    for s_id, session in SESSIONS_DB.items():
        eval_data = EVALUATIONS_DB.get(s_id, {})
        history_list.append({
            "id": s_id,
            "role": session.get("role", "Software Developer"),
            "interview_type": session.get("interview_type", "Mixed"),
            "difficulty": session.get("experience", "Fresher (0-1 year)"),
            "language": session.get("language", "Auto"),
            "questions_count": len(session.get("questions", [])),
            "created_at": session.get("created_at"),
            "overall_score": eval_data.get("overall_score") or session.get("overall_score", 8.0),
            "status": session.get("status", "completed"),
            "is_demo": s_id.startswith("session_") and len(s_id) < 12
        })
    return {"history": sorted(history_list, key=lambda x: x.get("created_at", ""), reverse=True)}

@app.delete("/api/interviews/{session_id}")
def delete_interview(session_id: str):
    if session_id in SESSIONS_DB:
        del SESSIONS_DB[session_id]
        if session_id in ANSWERS_DB:
            del ANSWERS_DB[session_id]
        if session_id in EVALUATIONS_DB:
            del EVALUATIONS_DB[session_id]
        return {"message": "Session deleted successfully"}
    raise HTTPException(status_code=404, detail="Session not found")
