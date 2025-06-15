from smol_agents.agent import Agent
from huggingface_search import search_models
from hf_papers_search import search_papers

agent = Agent(
    name="HuggingFaceRetriever",
    role="Un agent qui trouve des modèles et articles scientifiques pertinents sur Hugging Face à partir d'une description de projet IA.",
    tools=[search_models, search_papers],
)

if __name__ == "__main__":
    description = """Je cherche des ressources pour entraîner un modèle de classification de texte basé sur des transformers pour détecter les sentiments."""
    result = agent.run(f"À partir de cette description : {description}, trouve les modèles disponibles sur Hugging Face ainsi que les articles scientifiques pertinents.")
    print(result)
