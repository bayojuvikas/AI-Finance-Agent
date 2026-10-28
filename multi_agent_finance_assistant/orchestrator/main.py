import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from multi_agent_finance_assistant.orchestrator.routers import api_agent, analysis_agent, language_agent, qa_agent
from fastapi import FastAPI

app = FastAPI(title="Finance Assistant API")

# Include agent routers
app.include_router(api_agent.router)
app.include_router(analysis_agent.router)
app.include_router(language_agent.router)
app.include_router(qa_agent.router)

try:
    from multi_agent_finance_assistant.orchestrator.routers import voice_agent
    app.include_router(voice_agent.router)
except Exception:
    pass
