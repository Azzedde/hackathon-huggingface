#!/usr/bin/env python3
"""
Clean version of technical_assistant.py that suppresses Pydantic warnings
"""

import warnings
import sys
import os
from dotenv import load_dotenv

# Suppress specific Pydantic warnings
warnings.filterwarnings("ignore", message=".*PydanticSerializationUnexpectedValue.*")
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic.main")

load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from workspace.src.huggingface_search import search_models, analyze_model_feasibility
from workspace.src.hf_papers_search import search_papers, analyze_paper_novelty
from smolagents import CodeAgent
from smolagents.models import LiteLLMModel


class TechnicalAssistant:
    def __init__(self, api_key):
        # Initialize the tools explicitly
        self.tools = [search_models, search_papers, analyze_model_feasibility, analyze_paper_novelty]
        
        self.agent = CodeAgent(
            tools=self.tools,
            model=LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest", api_key=api_key),
            add_base_tools=True,  # Changed to True to include base tools
            additional_authorized_imports=["requests", "json", "datetime", "re"],  # Add necessary imports
        )

    def analyze_ai_project(self, project_description: str) -> str:
        """
        Comprehensive analysis of an AI project for investment purposes.
        Evaluates feasibility, novelty, and provides literature insights.
        """
        analysis_prompt = f"""
        As an AI investment analyst, provide a comprehensive technical analysis of this AI project:
        
        Project Description: {project_description}
        
        Your analysis should include:
        1. Technical feasibility assessment
        2. Innovation level (novel vs existing techniques)
        3. Implementation complexity
        4. Market readiness of underlying technologies
        5. Competitive landscape insights
        6. Risk assessment
        7. Investment recommendation (High/Medium/Low potential)
        
        Use the available tools to search for relevant models and papers to support your analysis.
        Provide specific evidence and citations from your research.
        """
        
        return self.agent.run(analysis_prompt)

    def evaluate_technique_novelty(self, technique_description: str) -> str:
        """
        Evaluates if a described AI technique is novel or just a wrapper around existing methods.
        """
        novelty_prompt = f"""
        Analyze this AI technique for novelty and originality:
        
        Technique: {technique_description}
        
        Determine:
        1. Is this a genuinely novel approach or a wrapper/combination of existing methods?
        2. What are the core underlying technologies?
        3. How does it compare to state-of-the-art approaches?
        4. What is the innovation level (Breakthrough/Incremental/Derivative)?
        5. Patent landscape considerations
        
        Search for relevant papers and models to support your assessment.
        """
        
        return self.agent.run(novelty_prompt)

    def research_latest_developments(self, research_area: str) -> str:
        """
        Researches the latest developments in a specific AI research area.
        """
        research_prompt = f"""
        Research the latest developments in: {research_area}
        
        Provide:
        1. Recent breakthrough papers (last 12 months)
        2. Trending models and architectures
        3. Key research groups and companies leading this area
        4. Emerging applications and use cases
        5. Future research directions
        6. Investment opportunities and market potential
        
        Use tools to gather current information from Hugging Face.
        """
        
        return self.agent.run(research_prompt)


if __name__ == "__main__":
    # Example usage
    assistant = TechnicalAssistant(ANTHROPIC_API_KEY)
    
    # Test comprehensive project analysis
    project_desc = """
    A startup claims to have developed a revolutionary multimodal AI system that can understand
    and generate content across text, images, and audio simultaneously. They use a novel
    'Unified Transformer Architecture' that they say outperforms existing models like GPT-4V
    and DALL-E 3. The system allegedly requires 90% less training data and compute resources.
    """
    
    print("=== AI PROJECT ANALYSIS ===")
    result = assistant.analyze_ai_project(project_desc)
    print(result)
    
    print("\n=== TECHNIQUE NOVELTY EVALUATION ===")
    technique = "Unified Transformer Architecture for multimodal AI"
    novelty_result = assistant.evaluate_technique_novelty(technique)
    print(novelty_result)