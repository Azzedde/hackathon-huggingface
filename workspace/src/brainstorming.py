import sys
import os
from dotenv import load_dotenv

load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from workspace.src.brainstorming_methods import sb
from smolagents import CodeAgent
from smolagents import Tool
from smolagents.models import LiteLLMModel


class BrainstormingAgent:
    def __init__(self, api_key):
        self.agent = CodeAgent(
            tools=[],
            model = LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest", api_key=api_key),
            add_base_tools=False,
        )

    def generate_ideas(self, mode, query) -> str:
        modes = {
            "Starbursting": {
                "function": lambda query: sb(query, self.agent),
                "description": "Focuses on generating questions rather than answers using the 5 W's and 1 H (Who, What, Where, When, Why, How). "
                               "Ideal for comprehensive topic exploration."
            }
        }
        if mode in modes:
            return modes[mode]["function"](query)
        else:
            return "Invalid mode selected."


if __name__ == "__main__":
    # Example usage
    brainstorming_agent = BrainstormingAgent(ANTHROPIC_API_KEY)
    user_query = "I want idea projects using smolagents that involves AI Agents and that solves social problems."
    mode = "Starbursting"
    result = brainstorming_agent.generate_ideas(mode, user_query)
    print(result)
