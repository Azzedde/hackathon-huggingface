import sys
import os
from dotenv import load_dotenv

load_dotenv()
ANTHROPIC_API_KEY =os.getenv("ANTHROPIC_API_KEY")

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from smolagents import CodeAgent
from smolagents.models import LiteLLMModel

class VCDataAnalystAgent:
    def __init__(self, api_key):
        self.agent = CodeAgent(
            tools=[],
            model=LiteLLMModel(model="anthropic/claude-sonnet-4", api_key=api_key),
            add_base_tools=True,
        )

    def extract_text(self, file_path):
      if file_path.endswith(".txt"):
          try:
              with open(file_path, "r", encoding="utf-8") as f:
                  content = f.read()
              return content, None  # ici on renvoie deux valeurs
          except Exception as e:
              return None, f"Erreur lors de la lecture du fichier texte : {e}"
      else:
          return None, "Seuls les fichiers .txt sont pris en charge."


    def analyze(self, file_path):
        content, error = self.extract_text(file_path)
        if error:
            return error

        # Prompt spécialisé VC due diligence
        prompt = f"""
You are a Data Analyst Agent specializing in venture capital due diligence. Your job is to evaluate startup performance using key metrics, focusing especially on growth rate and churn. When provided with a startup's metrics, analyze them critically from a VC’s perspective: Is growth healthy and sustainable? Is churn under control? What do these numbers indicate about product-market fit and future potential?

If exact growth or churn figures are missing, intelligently estimate or extrapolate using relevant industry benchmarks, public data, or typical values for similar companies at this stage. Clearly state when you are using estimates and cite the source or reasoning behind your extrapolation.

For each analysis, briefly explain:
- What the numbers mean for an investor (e.g., are they attractive or concerning?).
- How the startup compares to industry norms.
- Any risks, red flags, or positive signals you see.
- What follow-up questions or additional data a VC should request.

Always be quantitative, objective, and clear. Prioritize actionable insights that a venture capitalist would care about in a due diligence process.

Here is the startup data to analyze:

\"\"\"{content}\"\"\"
"""

        return self.agent.run(prompt)


if __name__ == "__main__":
    # Exemple d'utilisation
    file_path = "/TEST.txt"  
    agent = VCDataAnalystAgent(ANTHROPIC_API_KEY)
    result = agent.analyze(file_path)
    print(result)
