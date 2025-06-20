# mypy: ignore-errors
import sys
import os
from dotenv import load_dotenv
from typing import List, Optional, Any

# Load environment variables
load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

# Import necessary components from smolagents
from smolagents import CodeAgent, ToolCallingAgent  # type: ignore
from smolagents.models import LiteLLMModel  # type: ignore
from workspace.src.brainstorming import BrainstormingAgent  # type: ignore
from workspace.src.data_analyst_agent import VCDataAnalystAgent  # type: ignore
from workspace.src.technical_assistant import TechnicalAssistant  # type: ignore
from workspace.src.legal_assistant import LegalAssistant  # type: ignore

# Create a wrapper for BrainstormingAgent to make it work as a managed agent
class BrainstormingAgentWrapper(ToolCallingAgent):
    def __init__(self, brainstorming_agent: BrainstormingAgent, model: LiteLLMModel, default_mode: str = "SCAMPER"):
        super().__init__(
            tools=[],  # No tools needed, we'll use the internal agent
            model=model,
            name="brainstorming",
            description=f"Generates ideas using the {default_mode} brainstorming technique. This agent helps with creative ideation and problem-solving."
        )
        self.brainstorming_agent = brainstorming_agent
        self.default_mode = default_mode
    
    def run(self, query: str) -> str:
        # Use the default mode set during initialization
        mode = self.default_mode
        
        # Don't parse mode from query anymore - use the one set by the user
        # This ensures the user's selected brainstorming method is always used
        
        return self.brainstorming_agent.generate_ideas(mode, query)

# Create a simple Hello agent
class HelloAgent(ToolCallingAgent):
    def __init__(self, model: LiteLLMModel):
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

# Create a wrapper for VCDataAnalystAgent to make it work as a managed agent
class VCDataAnalystAgentWrapper(ToolCallingAgent):
    def __init__(self, data_analyst_agent: VCDataAnalystAgent, model: LiteLLMModel):
        super().__init__(
            tools=[], # No tools needed, we'll use the internal agent
            model=model,
            name="data_analyst",
            description="Analyzes startup data from a VC perspective, focusing on growth and churn."
        )
        self.data_analyst_agent = data_analyst_agent

    def run(self, query: str) -> str:
        # The query for the data analyst agent is expected to be a file path
        file_path = query.strip()
        if not file_path:
            return "Please provide a file path to analyze."
        
        # Call the analyze method of the internal VCDataAnalystAgent
        result = self.data_analyst_agent.analyze(file_path) # type: ignore
        return result # type: ignore

# Create a wrapper for TechnicalAssistant to make it work as a managed agent
class TechnicalAssistantWrapper(ToolCallingAgent):
    def __init__(self, technical_assistant: TechnicalAssistant, model: LiteLLMModel):
        # Import the tools to make them available
        from workspace.src.huggingface_search import search_models, analyze_model_feasibility
        from workspace.src.hf_papers_search import search_papers, analyze_paper_novelty
        
        super().__init__(
            tools=[search_models, search_papers, analyze_model_feasibility, analyze_paper_novelty],  # Include the tools
            model=model,
            name="technical_assistant",
            description="Analyzes AI projects for technical feasibility, novelty, and investment potential. Provides comprehensive analysis using HuggingFace models and papers."
        )
        self.technical_assistant = technical_assistant
    
    def run(self, query: str) -> str:
        # Determine what type of analysis to perform based on the query
        query_lower = query.lower()
        
        # For research queries, directly use the agent to leverage tools
        if "research" in query_lower or "latest" in query_lower or "developments" in query_lower:
            # Research latest developments - this needs the tools
            return self.technical_assistant.research_latest_developments(query)
        elif "novelty" in query_lower or "novel" in query_lower or "technique" in query_lower:
            # Technique novelty evaluation
            return self.technical_assistant.evaluate_technique_novelty(query)
        elif "project" in query_lower or "analyze" in query_lower or "investment" in query_lower:
            # Full project analysis
            return self.technical_assistant.analyze_ai_project(query)
        else:
            # Default to research if no clear indicator
            return self.technical_assistant.research_latest_developments(query)

# Create a wrapper for LegalAssistant to make it work as a managed agent
class LegalAssistantWrapper(ToolCallingAgent):
    def __init__(self, legal_assistant: LegalAssistant, model: LiteLLMModel):
        # Import the tools to make them available
        from workspace.src.legifrance_search import search_legal_texts, analyze_legal_compliance, search_jurisprudence
        
        super().__init__(
            tools=[search_legal_texts, analyze_legal_compliance, search_jurisprudence],  # Include the tools
            model=model,
            name="legal_assistant",
            description="Provides comprehensive legal analysis, risk evaluation, and regulatory research using French legal databases."
        )
        self.legal_assistant = legal_assistant
    
    def run(self, query: str) -> str:
        # Determine what type of analysis to perform based on the query
        query_lower = query.lower()
        
        if "startup" in query_lower or "investment" in query_lower or "framework" in query_lower:
            # Analyze startup legal framework
            # This is a simplified call; in a real scenario, you'd parse startup_description and business_sector from query
            return self.legal_assistant.analyze_startup_legal_framework(query)
        elif "risk" in query_lower or "risks" in query_lower or "evaluate" in query_lower:
            # Evaluate legal risks
            # Simplified call; parse business_model and target_market from query
            return self.legal_assistant.evaluate_legal_risks(query)
        elif "regulation" in query_lower or "regulations" in query_lower or "sector" in query_lower:
            # Research sector regulations
            # Simplified call; parse sector from query
            return self.legal_assistant.research_sector_regulations(query)
        elif "structure" in query_lower or "legal structure" in query_lower:
            # Analyze investment legal structure
            # Simplified call; parse investment_type and amount from query
            return self.legal_assistant.analyze_investment_legal_structure(query)
        else:
            # Default to general legal analysis if no clear indicator
            return self.legal_assistant.analyze_startup_legal_framework(query)


# Initialize the orchestrator
def create_orchestrator(agents: Optional[List[str]] = None, brainstorming_method: Optional[str] = None) -> CodeAgent:
    # Check if API key is available
    if ANTHROPIC_API_KEY is None:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        return None
    
    # Create the model
    model = LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest", api_key=ANTHROPIC_API_KEY)
    
    # Initialize managed agents
    managed_agents = []
    
    # If no agents specified, use all available agents
    if agents is None:
        agents = ["brainstorming", "hello", "data_analyst", "technical_assistant", "legal_assistant"]
    
    # Create and add BrainstormingAgent if requested
    if "brainstorming" in agents:
        try:
            brainstorming_agent_instance = BrainstormingAgent(ANTHROPIC_API_KEY)
            # Use the provided brainstorming method or default to SCAMPER
            default_mode = brainstorming_method if brainstorming_method else "SCAMPER"
            brainstorming_wrapper = BrainstormingAgentWrapper(brainstorming_agent_instance, model, default_mode)
            managed_agents.append(brainstorming_wrapper)
            print(f"BrainstormingAgent initialized successfully with method: {default_mode}")
        except Exception as e:
            print(f"Error initializing BrainstormingAgent: {e}")
    
    # Create and add HelloAgent if requested
    if "hello" in agents:
        hello_agent = HelloAgent(model)
        managed_agents.append(hello_agent)
        print("HelloAgent initialized successfully.")

    # Create and add VCDataAnalystAgent if requested
    if "data_analyst" in agents:
        try:
            data_analyst_agent_instance = VCDataAnalystAgent(ANTHROPIC_API_KEY)
            data_analyst_wrapper = VCDataAnalystAgentWrapper(data_analyst_agent_instance, model)
            managed_agents.append(data_analyst_wrapper)
            print("VCDataAnalystAgent initialized successfully.")
        except Exception as e:
            print(f"Error initializing VCDataAnalystAgent: {e}")
    
    # Create and add TechnicalAssistant if requested
    if "technical_assistant" in agents:
        try:
            technical_assistant_instance = TechnicalAssistant(ANTHROPIC_API_KEY)
            technical_assistant_wrapper = TechnicalAssistantWrapper(technical_assistant_instance, model)
            managed_agents.append(technical_assistant_wrapper)
            print("TechnicalAssistant initialized successfully.")
        except Exception as e:
            print(f"Error initializing TechnicalAssistant: {e}")

    # Create and add LegalAssistant if requested
    if "legal_assistant" in agents:
        try:
            legal_assistant_instance = LegalAssistant(ANTHROPIC_API_KEY)
            legal_assistant_wrapper = LegalAssistantWrapper(legal_assistant_instance, model)
            managed_agents.append(legal_assistant_wrapper)
            print("LegalAssistant initialized successfully.")
        except Exception as e:
            print(f"Error initializing LegalAssistant: {e}")
    
    # Create the manager agent
    manager_agent = CodeAgent(
        tools=[],
        model=model,
        managed_agents=managed_agents,
        additional_authorized_imports=["time", "numpy", "pandas"],  # Add if needed
        max_steps=5,  # Increased max_steps to allow for more complex interactions
    )
    
    return manager_agent

# Entry point to run the manager agent
def run_orchestrator(user_input: str, agents: Optional[List[str]] = None, brainstorming_method: Optional[str] = None) -> str:
    print("Creating orchestrator...")
    manager_agent = create_orchestrator(agents, brainstorming_method)
    
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