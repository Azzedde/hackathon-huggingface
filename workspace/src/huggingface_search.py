from smol_agents.tools import tool
import requests

HUGGINGFACE_API_URL = "https://huggingface.co/api"

@tool
def search_models(query: str, limit: int = 5) -> str:
    """
    Recherche les modèles sur Hugging Face à partir d'une description.
    """
    response = requests.get(
        f"{HUGGINGFACE_API_URL}/models",
        params={"search": query, "limit": limit}
    )
    if response.status_code != 200:
        return f"Erreur lors de la recherche de modèles : {response.text}"

    models = response.json()
    if not models:
        return "Aucun modèle trouvé."

    return "\n\n".join([f"{m['modelId']} - {m.get('description', 'Pas de description')}" for m in models])
