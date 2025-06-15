from smolagents import tool
import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any

HUGGINGFACE_API_URL = "https://huggingface.co/api"

@tool
def search_models(query: str, limit: int = 10) -> str:
    """
    Search for AI models on Hugging Face with detailed metadata for investment analysis.
    Returns comprehensive information including downloads, likes, and recent activity.
    
    Args:
        query: The search query to find relevant AI models
        limit: Maximum number of models to return (default: 10)
    """
    try:
        response = requests.get(
            f"{HUGGINGFACE_API_URL}/models",
            params={"search": query, "limit": limit, "sort": "downloads", "direction": -1}
        )
        if response.status_code != 200:
            return f"Error searching models: {response.text}"

        models = response.json()
        if not models:
            return "No models found for the given query."

        formatted_results = []
        for model in models[:limit]:
            model_info = _format_model_info(model)
            formatted_results.append(model_info)

        return "\n" + "="*80 + "\n".join(formatted_results)
    
    except Exception as e:
        return f"Error occurred while searching models: {str(e)}"


@tool
def analyze_model_feasibility(model_id: str) -> str:
    """
    Analyze the technical feasibility and implementation complexity of a specific Hugging Face model.
    Provides investment-relevant insights about model maturity, adoption, and technical requirements.
    
    Args:
        model_id: The Hugging Face model identifier to analyze
    """
    try:
        # Get detailed model information
        response = requests.get(f"{HUGGINGFACE_API_URL}/models/{model_id}")
        if response.status_code != 200:
            return f"Error fetching model details: {response.text}"
        
        model_data = response.json()
        
        # Analyze model characteristics
        analysis = _analyze_model_characteristics(model_data)
        
        return f"""
FEASIBILITY ANALYSIS FOR: {model_id}
{'='*60}

📊 ADOPTION METRICS:
• Downloads: {model_data.get('downloads', 'N/A'):,}
• Likes: {model_data.get('likes', 'N/A'):,}
• Created: {model_data.get('createdAt', 'N/A')}
• Last Modified: {model_data.get('lastModified', 'N/A')}

🏗️ TECHNICAL ASSESSMENT:
{analysis['technical_assessment']}

💼 INVESTMENT INSIGHTS:
{analysis['investment_insights']}

⚠️ RISK FACTORS:
{analysis['risk_factors']}

🎯 RECOMMENDATION:
{analysis['recommendation']}
        """
    
    except Exception as e:
        return f"Error analyzing model feasibility: {str(e)}"


def _format_model_info(model: Dict[str, Any]) -> str:
    """Format model information for display."""
    model_id = model.get('id', model.get('modelId', 'Unknown'))
    downloads = model.get('downloads', 0)
    likes = model.get('likes', 0)
    pipeline_tag = model.get('pipeline_tag', 'N/A')
    library = model.get('library_name', 'N/A')
    created_at = model.get('createdAt', 'N/A')
    
    # Calculate popularity score
    popularity_score = _calculate_popularity_score(downloads, likes)
    
    return f"""
🤖 MODEL: {model_id}
📈 Downloads: {downloads:,} | 👍 Likes: {likes:,} | ⭐ Popularity: {popularity_score}
🔧 Pipeline: {pipeline_tag} | 📚 Library: {library}
📅 Created: {created_at}
📝 Description: {model.get('description', 'No description available')[:200]}...
"""


def _calculate_popularity_score(downloads: int, likes: int) -> str:
    """Calculate a popularity score based on downloads and likes."""
    score = (downloads * 0.7) + (likes * 0.3)
    
    if score > 100000:
        return "🔥 Very High"
    elif score > 10000:
        return "🚀 High"
    elif score > 1000:
        return "📈 Medium"
    elif score > 100:
        return "🌱 Growing"
    else:
        return "🆕 New/Niche"


def _analyze_model_characteristics(model_data: Dict[str, Any]) -> Dict[str, str]:
    """Analyze model characteristics for investment insights."""
    downloads = model_data.get('downloads', 0)
    likes = model_data.get('likes', 0)
    pipeline_tag = model_data.get('pipeline_tag', '')
    library = model_data.get('library_name', '')
    tags = model_data.get('tags', [])
    
    # Technical Assessment
    tech_complexity = "Low"
    if any(tag in str(tags).lower() for tag in ['large', 'xl', 'xxl', 'billion', 'multimodal']):
        tech_complexity = "High"
    elif any(tag in str(tags).lower() for tag in ['medium', 'base', 'transformer']):
        tech_complexity = "Medium"
    
    technical_assessment = f"""
• Complexity Level: {tech_complexity}
• Pipeline Type: {pipeline_tag}
• Framework: {library}
• Model Tags: {', '.join(tags[:5]) if tags else 'None specified'}
• Implementation Difficulty: {'High' if tech_complexity == 'High' else 'Medium' if downloads < 1000 else 'Low'}
"""
    
    # Investment Insights
    market_validation = "Strong" if downloads > 10000 else "Moderate" if downloads > 1000 else "Limited"
    community_interest = "High" if likes > 100 else "Medium" if likes > 10 else "Low"
    
    investment_insights = f"""
• Market Validation: {market_validation} ({downloads:,} downloads)
• Community Interest: {community_interest} ({likes:,} likes)
• Commercial Viability: {'High' if downloads > 50000 else 'Medium' if downloads > 5000 else 'Uncertain'}
• Adoption Trend: {'Established' if downloads > 100000 else 'Growing' if downloads > 10000 else 'Early Stage'}
"""
    
    # Risk Factors
    risk_level = "Low"
    risk_factors_list = []
    
    if downloads < 100:
        risk_factors_list.append("• Very low adoption - unproven market demand")
        risk_level = "High"
    elif downloads < 1000:
        risk_factors_list.append("• Limited adoption - market validation needed")
        risk_level = "Medium"
    
    if likes < 10:
        risk_factors_list.append("• Low community engagement")
    
    if not library or library.lower() == 'unknown':
        risk_factors_list.append("• Unclear technical framework")
    
    if tech_complexity == "High":
        risk_factors_list.append("• High implementation complexity - requires significant resources")
    
    risk_factors = '\n'.join(risk_factors_list) if risk_factors_list else "• Minimal technical and market risks identified"
    
    # Recommendation
    if downloads > 50000 and likes > 100:
        recommendation = "🟢 STRONG BUY - Proven market demand and community support"
    elif downloads > 10000 and likes > 50:
        recommendation = "🟡 MODERATE BUY - Good traction, monitor growth"
    elif downloads > 1000:
        recommendation = "🟠 CAUTIOUS - Early stage, requires deeper analysis"
    else:
        recommendation = "🔴 HIGH RISK - Unproven technology, significant market risk"
    
    return {
        'technical_assessment': technical_assessment,
        'investment_insights': investment_insights,
        'risk_factors': risk_factors,
        'recommendation': recommendation
    }
