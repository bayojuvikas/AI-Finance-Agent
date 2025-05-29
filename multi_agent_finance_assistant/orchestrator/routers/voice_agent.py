from fastapi import APIRouter
from multi_agent_finance_assistant.agents.voice_agent import speak_text

router = APIRouter(prefix="/speak", tags=["Voice Agent"])

@router.post("/")
def speak(payload: dict):
    text = payload.get("text", "")
    if not text:
        return {"error": "Missing text"}
    speak_text(text)
    return {"status": "spoken"}
