import sys
import os
from dotenv import load_dotenv
from typing import List, Optional

# Load environment variables
load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from smolagents.models import LiteLLMModel
from workspace.src.brainstorming import BrainstormingAgent

class SimpleOrchestrator:
    """A simple orchestrator that directly routes to agents without code execution"""
    
    def __init__(self, api_key: str):
        self.model = LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest", api_key=api_key)
        self.brainstorming_agent = BrainstormingAgent(api_key)
        
    def run(self, prompt: str, agents: Optional[List[str]] = None) -> str:
        """Route the prompt to appropriate agents based on content or selection"""
        
        # If no agents specified, analyze the prompt to determine which to use
        if not agents:
            agents = self._determine_agents(prompt)
        
        responses = []
        
        # Process with each selected agent
        for agent_id in agents:
            if agent_id == "brainstorming":
                # Extract mode if specified
                mode = "SCAMPER"  # Default
                modes = ["Starbursting", "Mind Mapping", "Reverse Brainstorming", 
                         "Role Storming", "SCAMPER", "Six Thinking Hats"]
                
                for m in modes:
                    if prompt.lower().startswith(m.lower() + ":"):
                        mode = m
                        prompt = prompt[len(m)+1:].strip()
                        break
                
                response = self.brainstorming_agent.generate_ideas(mode, prompt)
                responses.append(f"[Brainstorming Agent - {mode}]\n{response}")
                
            elif agent_id == "hello":
                response = f"Hello! I received your message: {prompt}"
                responses.append(f"[Hello Agent]\n{response}")
                
            elif agent_id == "analyst":
                # Placeholder for analyst agent
                response = f"Analyzing: {prompt}\n\nKey insights:\n- This requires further analysis\n- Multiple perspectives should be considered\n- Data-driven approach recommended"
                responses.append(f"[Analyst Agent]\n{response}")
                
            elif agent_id == "research":
                # Placeholder for research agent
                response = f"Researching: {prompt}\n\nInitial findings:\n- Topic requires investigation\n- Multiple sources should be consulted\n- Further research recommended"
                responses.append(f"[Research Agent]\n{response}")
                
            elif agent_id == "technical":
                # Placeholder for technical agent
                response = f"Technical analysis of: {prompt}\n\nTechnical considerations:\n- Implementation feasibility needs assessment\n- Architecture planning required\n- Technology stack to be determined"
                responses.append(f"[Technical Agent]\n{response}")
                
            elif agent_id == "legal_jurist":
                # Placeholder for legal agent
                response = f"Legal perspective on: {prompt}\n\nLegal considerations:\n- Compliance requirements to be reviewed\n- Regulatory framework analysis needed\n- Risk assessment recommended"
                responses.append(f"[Legal Jurist Agent]\n{response}")
        
        # Combine all responses
        if len(responses) == 1:
            return responses[0]
        else:
            return "\n\n---\n\n".join(responses)
    
    def _determine_agents(self, prompt: str) -> List[str]:
        """Simple heuristic to determine which agents to use based on prompt content"""
        prompt_lower = prompt.lower()
        agents = []
        
        # Check for keywords to determine agents
        if any(word in prompt_lower for word in ["idea", "brainstorm", "creative", "think"]):
            agents.append("brainstorming")
        if any(word in prompt_lower for word in ["hello", "hi", "greet"]):
            agents.append("hello")
        if any(word in prompt_lower for word in ["analyze", "analysis", "insight"]):
            agents.append("analyst")
        if any(word in prompt_lower for word in ["research", "investigate", "study"]):
            agents.append("research")
        if any(word in prompt_lower for word in ["technical", "code", "implement", "build"]):
            agents.append("technical")
        if any(word in prompt_lower for word in ["legal", "law", "compliance", "regulation"]):
            agents.append("legal_jurist")
        
        # Default to brainstorming if no specific agent detected
        if not agents:
            agents.append("brainstorming")
        
        return agents

def run_simple_orchestrator(prompt: str, agents: Optional[List[str]] = None) -> str:
    """Entry point for the simple orchestrator"""
    if not ANTHROPIC_API_KEY:
        return "Error: ANTHROPIC_API_KEY not set"
    
    try:
        orchestrator = SimpleOrchestrator(ANTHROPIC_API_KEY)
        return orchestrator.run(prompt, agents)
    except Exception as e:
        return f"Error: {str(e)}"