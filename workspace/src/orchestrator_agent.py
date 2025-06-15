import sys
import os
from dotenv import load_dotenv
from typing import List, Optional

# Load environment variables
load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

# Import necessary components from smolagents
from smolagents import CodeAgent, ToolCallingAgent
from smolagents.models import LiteLLMModel
from workspace.src.brainstorming import BrainstormingAgent

# Create a wrapper for BrainstormingAgent to make it work as a managed agent
class BrainstormingAgentWrapper(ToolCallingAgent):
    def __init__(self, brainstorming_agent: BrainstormingAgent, model):
        super().__init__(
            tools=[],  # No tools needed, we'll use the internal agent
            model=model,
            name="brainstorming",
            description="Generates ideas using various brainstorming techniques. Specify mode by prefixing with 'MODE:' (e.g., 'SCAMPER: your query'). Available modes: Starbursting, Mind Mapping, Reverse Brainstorming, Role Storming, SCAMPER, Six Thinking Hats."
        )
        self.brainstorming_agent = brainstorming_agent
    
    def run(self, query: str) -> str:
        # Parse the query to extract mode if specified, otherwise use default
        mode = "SCAMPER"  # Default mode
        
        # Check if query starts with a mode specification
        modes = ["Starbursting", "Mind Mapping", "Reverse Brainstorming", 
                 "Role Storming", "SCAMPER", "Six Thinking Hats"]
        for m in modes:
            if query.lower().startswith(m.lower() + ":"):
                mode = m
                query = query[len(m)+1:].strip()
                break
        
        return self.brainstorming_agent.generate_ideas(mode, query)

# Create a simple Hello agent
class HelloAgent(ToolCallingAgent):
    def __init__(self, model):
        super().__init__(
            tools=[],
            model=model,
            name="hello",
            description="A simple agent that says hello and acknowledges your message."
        )
    
    def run(self, query: str) -> str:
        result = f"[HelloAgent] says: Hello! You said: {query}"
        print(result)
        return result

# Initialize the orchestrator
def create_orchestrator():
    # Check if API key is available
    if ANTHROPIC_API_KEY is None:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        return None
    
    # Create the model
    model = LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest", api_key=ANTHROPIC_API_KEY)
    
    # Initialize managed agents
    managed_agents = []
    
    # Create and add BrainstormingAgent
    try:
        brainstorming_agent_instance = BrainstormingAgent(ANTHROPIC_API_KEY)
        brainstorming_wrapper = BrainstormingAgentWrapper(brainstorming_agent_instance, model)
        managed_agents.append(brainstorming_wrapper)
        print("BrainstormingAgent initialized successfully.")
    except Exception as e:
        print(f"Error initializing BrainstormingAgent: {e}")
    
    # Create and add HelloAgent
    hello_agent = HelloAgent(model)
    managed_agents.append(hello_agent)
    print("HelloAgent initialized successfully.")
    
    # Create the manager agent
    manager_agent = CodeAgent(
        tools=[],
        model=model,
        managed_agents=managed_agents,
        additional_authorized_imports=["time", "numpy", "pandas"],  # Add if needed
    )
    
    return manager_agent

# Entry point to run the manager agent
def run_orchestrator(user_input: str) -> str:
    print("Creating orchestrator...")
    manager_agent = create_orchestrator()
    
    if manager_agent is None:
        return "Orchestrator could not be initialized due to missing API key or other error."
    
    print("Running manager agent...")
    try:
        response = manager_agent.run(user_input)
        return response
    except Exception as e:
        return f"Error running manager agent: {e}"

# Example usage
if __name__ == "__main__":
    print("Orchestrator test mode using Manager Agent.")
    
    # Test 1: Both agents
    print("\n" + "="*60)
    query_both = "First say hello to me, then use SCAMPER: brainstorm ideas for a new app using smolagents that solves social problems."
    print(f"User query: {query_both}")
    response_both = run_orchestrator(query_both)
    print("\n--- Final Orchestrator Response ---")
    print(response_both)
    
    # Test 2: Hello only
    print("\n" + "="*60)
    query_hello_only = "Just say hello please."
    print(f"User query: {query_hello_only}")
    response_hello_only = run_orchestrator(query_hello_only)
    print("\n--- Final Orchestrator Response ---")
    print(response_hello_only)
    
    # Test 3: Brainstorming only
    print("\n" + "="*60)
    query_brainstorm_only = "Use the brainstorming agent to generate ideas for a new app using smolagents."
    print(f"User query: {query_brainstorm_only}")
    response_brainstorm_only = run_orchestrator(query_brainstorm_only)
    print("\n--- Final Orchestrator Response ---")
    print(response_brainstorm_only)