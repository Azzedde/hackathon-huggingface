from smol_agents.tools import tool
import requests

@tool
def search_papers(query: str, limit: int = 5) -> str:
    """
    Recherche des articles scientifiques sur Hugging Face Papers à partir d'une description.
    """
    url = "https://huggingface.co/api/papers"
    params = {"query": query, "limit": limit}

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return f"Erreur lors de la recherche de papiers : {response.text}"

    results = response.json()
    if not results:
        return "Aucun papier trouvé."

    formatted = []
    for paper in results[:limit]:
        title = paper.get("title", "Sans titre")
        authors = ", ".join(paper.get("authors", []))
        link = paper.get("pdf_url") or paper.get("arxiv_url", "Lien non disponible")
        formatted.append(f"📄 {title}\n👤 {authors}\n🔗 {link}")

    return "\n\n".join(formatted)
