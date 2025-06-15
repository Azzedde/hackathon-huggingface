import sys
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from workspace.src.orchestrator_agent import run_orchestrator

# Define the request body model
class PromptRequest(BaseModel):
    prompt: str
    agents: Optional[List[str]] = None
    brainstorming_method: Optional[str] = None
    is_follow_up: Optional[bool] = False

app = FastAPI()

@app.post("/run")
async def run_orchestrator_endpoint(request: PromptRequest):
    """
    Endpoint to run the orchestrator with a given prompt.
    """
    try:
        response = run_orchestrator(
            request.prompt,
            agents=request.agents,
            brainstorming_method=request.brainstorming_method
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running orchestrator: {e}")

if __name__ == "__main__":
    # This is for local development/testing.
    # In a production environment, you would typically run this with `uvicorn orchestrator_api:app --reload`
    uvicorn.run(app, host="0.0.0.0", port=8000)