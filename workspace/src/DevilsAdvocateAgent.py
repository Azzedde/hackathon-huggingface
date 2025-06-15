import sys
import os
from dotenv import load_dotenv

load_dotenv()
ANTHROPIC_API_KEY =os.getenv("ANTHROPIC_API_KEY")

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from smolagents import CodeAgent
from smolagents.models import LiteLLMModel


class DevilsAdvocateAgent:
    def __init__(self, api_key: str) -> None:
        self.agent = CodeAgent(
            tools=[],
            model=LiteLLMModel(model_id="claude-sonnet-4-20250514", api_key=api_key),
            add_base_tools=True,
        )

    def challenge_pitch(self, startup_pitch: str) -> str:
        prompt = f"""
ou are a Devil’s Advocate Agent embedded in a venture capital due diligence system.

Your mission is to pressure-test the following startup pitch from a critical and skeptical lens. You are not here to repeat their story — you are here to uncover what might break it.

Be skeptical, but fair. Focus on the assumptions, blind spots, inconsistencies, and risks that could undermine this opportunity.

Startup pitch:

{startup_pitch}
Your analysis should include the following sections:

🧠 Fragile or Optimistic Assumptions
Identify the key claims or beliefs in the pitch that rely on unproven behavior, favorable conditions, or overconfidence.

❓ Critical VC Questions
List 3 to 5 sharp, uncomfortable questions a seasoned investor should ask to stress-test those assumptions and surface hidden risks.

⚠️ Business Model & GTM Risks
Highlight vulnerabilities in the business model, pricing logic, scalability claims, or go-to-market motion.

👥 Founding Team Risk Factors
Evaluate the founders' composition, experience, strategic self-awareness, and ability to attract top talent.

Are they humble about unknowns?

Do they have relevant scars or just vision?

📉 Pattern Recognition: Analogies with Failed Startups
If applicable, name similar companies that failed and why — draw parallels that may apply here.

🌍 External Threats
Surface any market, regulatory, or tech shifts that could dramatically change the odds of success.

💣 Summary Rating: Fragility
Choose one: Low / Moderate / High
Justify your rating based on the combination of internal and external risks. What could bring this down?

Finally you must provide examples of near or same startups that failed in the past and give reasons of their failure.

Be direct. Be insightful. Do not soften your conclusions — this analysis should help VCs avoid buying a lemon masked by good storytelling.

"""
        return self.agent.run(prompt)


if __name__ == "__main__":
    if ANTHROPIC_API_KEY is None:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        sys.exit(1)

    devils_agent = DevilsAdvocateAgent(ANTHROPIC_API_KEY)

    example_pitch = """Nom de la Startup : GreenTech Innovations

Secteur : Énergie renouvelable

Description du produit :
GreenTech Innovations développe des panneaux solaires modulaires et intelligents destinés aux foyers urbains. Notre technologie brevetée optimise l'efficacité énergétique en ajustant automatiquement l'angle des panneaux en fonction de la position du soleil et des conditions météorologiques locales.

Date de création : Mars 2022

Localisation : Paris, France

Équipe fondatrice :
- Alice Dupont (CEO) : 10 ans d'expérience en gestion de projets technologiques.
- Marc Lefevre (CTO) : Ancien ingénieur principal chez SolarTech Corp.

Modèle économique :
- Vente directe aux consommateurs via notre site web.
- Partenariats avec des installateurs locaux pour l'installation et la maintenance."""

    result = devils_agent.challenge_pitch(example_pitch)
    print(result)