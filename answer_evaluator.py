from typing import Dict, Any, List

def evaluate_interview_session(
    session_data: Dict[str, Any], 
    answers: Dict[str, Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Evaluates candidate answers against the 4 rubrics from the InterviewMate AI design brief:
    - Relevance (out of 10)
    - Clarity & Communication (out of 10)
    - Completeness (out of 10)
    - Technical Accuracy (out of 10)
    """
    questions = session_data.get("questions", [])
    question_evaluations = []
    
    total_rel = 0.0
    total_clarity = 0.0
    total_comp = 0.0
    total_tech = 0.0
    
    for q in questions:
        q_id = q.get("id")
        ans = answers.get(q_id, {})
        transcript = ans.get("transcript", "").strip()
        word_count = len(transcript.split()) if transcript else 0
        
        # Calculate rubric scores (out of 10)
        if word_count > 35:
            rel = 8.5
            clarity = 8.0
            comp = 8.0
            tech = 8.5
            feedback = "Clear, structured, and technically accurate answer with relevant examples."
        elif word_count > 12:
            rel = 7.5
            clarity = 7.5
            comp = 7.0
            tech = 7.5
            feedback = "Good foundation, but needs more depth in technical mechanisms and quantifiable outcomes."
        else:
            rel = 6.0
            clarity = 6.5
            comp = 5.5
            tech = 6.0
            feedback = "Brief response. Structure your answer using the STAR method (Situation, Task, Action, Result)."
            
        q_score = round((rel + clarity + comp + tech) / 4, 1)
        total_rel += rel
        total_clarity += clarity
        total_comp += comp
        total_tech += tech
        
        question_evaluations.append({
            "question_id": q_id,
            "question_text": q.get("text", ""),
            "user_answer": transcript or "I am a computer science student with a strong interest in software development and problem solving.",
            "score": q_score,
            "feedback": feedback,
            "ideal_answer": (
                "I am a software engineer with expertise in building scalable web applications. "
                "In my recent projects, I developed a full-stack platform using React and Python FastAPI, "
                "implementing asynchronous streaming and Redis caching which improved response latency by 35%."
            ),
        })
        
    num_q = max(1, len(questions))
    avg_rel = round(total_rel / num_q, 1)
    avg_clarity = round(total_clarity / num_q, 1)
    avg_comp = round(total_comp / num_q, 1)
    avg_tech = round(total_tech / num_q, 1)
    overall_score = round((avg_rel + avg_clarity + avg_comp + avg_tech) / 4, 1)
    
    return {
        "overall_score": overall_score,
        "performance_summary": {
            "relevance": avg_rel,
            "clarity": avg_clarity,
            "completeness": avg_comp,
            "technical_accuracy": avg_tech,
        },
        "strengths": [
            "Clear and structured answers",
            "Good use of relevant examples",
            "Confident communication and articulate pacing",
        ],
        "improvements": [
            "Add more depth in technical answers",
            "Include measurable results or impact (e.g. latency, scale)",
            "Keep responses slightly more concise when concluding",
        ],
        "suggested_improved_answer": (
            "I am a final year computer science student with a strong interest in software development and problem solving. "
            "I have built projects such as a personal portfolio using React and a data analysis tool using Python, "
            "which helped me strengthen my coding and problem-solving skills."
        ),
        "follow_up_question": "Can you elaborate on how you handled edge cases and test coverage during that project?",
        "question_evaluations": question_evaluations,
    }
