import uuid
from typing import List, Dict, Any

ROLE_QUESTIONS = {
    "Full-Stack Engineer": [
        {
            "id": "q1",
            "category": "Architecture & Concurrency",
            "text": "How do you handle asynchronous background processing and prevent connection pool exhaustion in a FastAPI web service?",
            "tip": "Discuss async/await vs def, database pool sizing, background tasks vs Celery/Redis queues.",
        },
        {
            "id": "q2",
            "category": "Frontend State & Rendering",
            "text": "What strategies do you use in React 18 to optimize re-renders and handle real-time streaming audio or WebSocket data?",
            "tip": "Mention React 18 concurrent features, useMemo/useCallback, and isolating state updates to child components.",
        },
        {
            "id": "q3",
            "category": "System Design",
            "text": "Design a resilient rate limiter for an AI audio transcription API handling 10,000 requests per minute.",
            "tip": "Explain Token Bucket or Leaky Bucket algorithms, Redis sliding window counters, and 429 status responses.",
        },
        {
            "id": "q4",
            "category": "Database & Data Modeling",
            "text": "How would you model and index interview session transcripts and evaluation scores for high-throughput analytics?",
            "tip": "Discuss composite indexes, foreign key cascades, partitioning by date or tenant, and JSON vs relational columns.",
        },
        {
            "id": "q5",
            "category": "Behavioral / Leadership",
            "text": "Tell me about a time you had a technical disagreement with a team member about system architecture. How was it resolved?",
            "tip": "Use the STAR method: explain the trade-offs evaluated, proof-of-concept benchmarked, and team alignment achieved.",
        },
    ],
    "Frontend Developer (React/Vite)": [
        {
            "id": "q1",
            "category": "Core React & Hooks",
            "text": "Explain the mechanics of the browser event loop vs React 18 concurrent rendering transitions.",
            "tip": "Compare microtasks/macrotasks with React fiber reconciliation and startTransition.",
        },
        {
            "id": "q2",
            "category": "Web Audio API",
            "text": "How does MediaRecorder work in modern browsers, and how do you handle varying audio codec support across Safari and Chrome?",
            "tip": "Mention MediaRecorder.isTypeSupported, audio/webm vs audio/mp4, and audio chunk aggregation.",
        },
        {
            "id": "q3",
            "category": "Performance Optimization",
            "text": "How do you audit and reduce First Contentful Paint (FCP) and Cumulative Layout Shift (CLS) in a Vite application?",
            "tip": "Discuss code-splitting with dynamic import, font optimization, and Tailwind CSS tree-shaking.",
        },
    ],
    "Backend Developer (Python/FastAPI)": [
        {
            "id": "q1",
            "category": "API Architecture",
            "text": "Explain the difference between ASGI and WSGI servers, and how Uvicorn coordinates with Starlette.",
            "tip": "Cover asynchronous protocol handling, async def endpoints, and worker thread management.",
        },
        {
            "id": "q2",
            "category": "Security & Auth",
            "text": "How do you design a secure OAuth2 with JWT authentication flow with refresh tokens and rate-limiting?",
            "tip": "Cover cryptographic signing algorithms, expiry validation, and httpOnly cookie storage.",
        },
        {
            "id": "q3",
            "category": "Reliability & Testing",
            "text": "How do you write deterministic unit and integration tests for external AI APIs like Gnani STT using pytest and httpx mock?",
            "tip": "Discuss dependency injection in FastAPI, pytest fixtures, and mock transport layers.",
        },
    ],
}

def generate_interview_questions(
    role: str = "Full-Stack Engineer",
    experience: str = "mid",
    interview_type: str = "technical",
    num_questions: int = 5,
    custom_focus: str = None
) -> List[Dict[str, Any]]:
    # Pick matching pool or default
    pool = ROLE_QUESTIONS.get(role, ROLE_QUESTIONS["Full-Stack Engineer"])
    
    questions = []
    for i in range(min(num_questions, len(pool))):
        q = pool[i].copy()
        q["id"] = f"q_{uuid.uuid4().hex[:6]}"
        questions.append(q)
        
    # If more requested, generate additional targeted questions
    while len(questions) < num_questions:
        idx = len(questions) + 1
        questions.append({
            "id": f"q_{uuid.uuid4().hex[:6]}",
            "category": "Core Competency",
            "text": f"Discuss an advanced engineering challenge you solved in {role} related to {custom_focus or 'production reliability'}.",
            "tip": "Focus on root cause analysis, architecture design, and measurable positive outcomes.",
        })
        
    return questions
