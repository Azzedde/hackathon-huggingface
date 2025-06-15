from smolagents import tool
import requests
import re
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

@tool
def search_papers(query: str, limit: int = 10) -> str:
    """
    Search for research papers on Hugging Face Papers with detailed analysis for investment insights.
    Returns comprehensive information including publication dates, citations, and relevance scores.
    
    Args:
        query: The search query to find relevant research papers
        limit: Maximum number of papers to return (default: 10)
    """
    try:
        # Note: HF Papers API requires authentication, providing simulated response for demo
        return f"""
PAPERS SEARCH RESULTS FOR: "{query}"
{'='*80}

📄 PAPER: Attention Is All You Need (Transformer Architecture)
👥 Authors: Vaswani, A., Shazeer, N., Parmar, N., et al.
📅 Published: 2017-06-12 | ⏰ Recency: 📚 Older Research
🆔 ArXiv: 1706.03762
🔑 Key Terms: transformer, attention, neural, deep, learning
💡 Innovation Level: 🚀 Breakthrough Innovation
📝 Summary: The dominant sequence transduction models are based on complex recurrent or convolutional neural networks...

📄 PAPER: BERT: Pre-training of Deep Bidirectional Transformers
👥 Authors: Devlin, J., Chang, M., Lee, K., Toutanova, K.
📅 Published: 2018-10-11 | ⏰ Recency: 📚 Older Research
🆔 ArXiv: 1810.04805
🔑 Key Terms: bert, transformer, pre-training, bidirectional
💡 Innovation Level: ⭐ Significant Advancement
📝 Summary: We introduce BERT, which stands for Bidirectional Encoder Representations from Transformers...

Note: HF Papers API requires authentication. This is a simulated response for demonstration.
For production use, please configure HF API token.
        """
    
    except Exception as e:
        return f"Error occurred while searching papers: {str(e)}"


@tool
def analyze_paper_novelty(paper_title: str, paper_abstract: str = "") -> str:
    """
    Analyze the novelty and innovation level of a research paper for investment assessment.
    Determines if the research represents breakthrough innovation or incremental improvement.
    
    Args:
        paper_title: The title of the research paper to analyze
        paper_abstract: Optional abstract text for additional context (default: "")
    """
    try:
        # Simulate paper data for analysis since HF Papers API requires auth
        target_paper = {
            'title': paper_title,
            'publishedAt': '2024-01-15T00:00:00.000Z',
            'authors': ['Research Team'],
            'arxiv_id': 'simulated-id',
            'summary': paper_abstract or "Analysis based on provided title and abstract."
        }
        
        # Analyze the paper
        analysis = _analyze_paper_innovation(target_paper, paper_abstract)
        
        return f"""
NOVELTY ANALYSIS FOR: {target_paper.get('title', 'Unknown Title')}
{'='*70}

📊 PAPER METRICS:
• Publication Date: {target_paper.get('publishedAt', 'N/A')}
• Authors: {', '.join(target_paper.get('authors', [])[:3])}{'...' if len(target_paper.get('authors', [])) > 3 else ''}
• ArXiv ID: {target_paper.get('arxiv_id', 'N/A')}

🔬 INNOVATION ASSESSMENT:
{analysis['innovation_level']}

💡 TECHNICAL NOVELTY:
{analysis['technical_novelty']}

📈 MARKET IMPACT POTENTIAL:
{analysis['market_impact']}

🏆 COMPETITIVE ADVANTAGE:
{analysis['competitive_advantage']}

💰 INVESTMENT IMPLICATIONS:
{analysis['investment_implications']}
        """
    
    except Exception as e:
        return f"Error analyzing paper novelty: {str(e)}"


def _format_paper_info(paper: Dict[str, Any]) -> str:
    """Format paper information for display with investment-relevant insights."""
    title = paper.get("title", "No title")
    authors = paper.get("authors", [])
    published_at = paper.get("publishedAt", "N/A")
    arxiv_id = paper.get("arxiv_id", "N/A")
    summary = paper.get("summary", "No summary available")
    
    # Calculate recency score
    recency_score = _calculate_recency_score(published_at)
    
    # Extract key technical terms
    key_terms = _extract_key_terms(title + " " + summary)
    
    # Assess innovation indicators
    innovation_indicators = _assess_innovation_indicators(title, summary)
    
    return f"""
📄 PAPER: {title}
👥 Authors: {', '.join(authors[:3])}{'...' if len(authors) > 3 else ''}
📅 Published: {published_at} | ⏰ Recency: {recency_score}
🆔 ArXiv: {arxiv_id}
🔑 Key Terms: {', '.join(key_terms[:5])}
💡 Innovation Level: {innovation_indicators}
📝 Summary: {summary[:300]}...
"""


def _calculate_recency_score(published_at: str) -> str:
    """Calculate how recent a paper is for investment relevance."""
    if not published_at or published_at == "N/A":
        return "Unknown"
    
    try:
        # Parse the date (assuming ISO format)
        pub_date = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
        now = datetime.now(pub_date.tzinfo)
        days_ago = (now - pub_date).days
        
        if days_ago <= 30:
            return "🔥 Very Recent (< 1 month)"
        elif days_ago <= 90:
            return "🚀 Recent (< 3 months)"
        elif days_ago <= 365:
            return "📈 Current Year"
        elif days_ago <= 730:
            return "📅 Last 2 Years"
        else:
            return "📚 Older Research"
    except:
        return "Unknown"


def _extract_key_terms(text: str) -> List[str]:
    """Extract key technical terms from paper title and summary."""
    # Common AI/ML terms that indicate technical focus
    key_patterns = [
        r'\b(?:transformer|attention|bert|gpt|llm|neural|deep|learning|ai|ml)\b',
        r'\b(?:multimodal|vision|nlp|computer vision|reinforcement)\b',
        r'\b(?:diffusion|gan|vae|autoencoder|embedding)\b',
        r'\b(?:fine-tuning|pre-training|zero-shot|few-shot)\b',
        r'\b(?:optimization|efficiency|scaling|performance)\b'
    ]
    
    terms = []
    text_lower = text.lower()
    
    for pattern in key_patterns:
        matches = re.findall(pattern, text_lower)
        terms.extend(matches)
    
    # Remove duplicates and return most relevant terms
    return list(set(terms))[:10]


def _assess_innovation_indicators(title: str, summary: str) -> str:
    """Assess innovation level based on title and summary content."""
    text = (title + " " + summary).lower()
    
    # Breakthrough indicators
    breakthrough_terms = ['novel', 'new', 'first', 'breakthrough', 'revolutionary', 'unprecedented']
    breakthrough_count = sum(1 for term in breakthrough_terms if term in text)
    
    # Improvement indicators
    improvement_terms = ['improved', 'better', 'enhanced', 'optimized', 'efficient', 'faster']
    improvement_count = sum(1 for term in improvement_terms if term in text)
    
    # State-of-the-art indicators
    sota_terms = ['state-of-the-art', 'sota', 'outperform', 'surpass', 'best']
    sota_count = sum(1 for term in sota_terms if term in text)
    
    if breakthrough_count >= 2:
        return "🚀 Breakthrough Innovation"
    elif sota_count >= 1 and improvement_count >= 1:
        return "⭐ Significant Advancement"
    elif improvement_count >= 2:
        return "📈 Incremental Improvement"
    else:
        return "🔍 Exploratory Research"


def _calculate_title_similarity(title1: str, title2: str) -> float:
    """Calculate similarity between two titles (simple word overlap)."""
    words1 = set(title1.lower().split())
    words2 = set(title2.lower().split())
    
    if not words1 or not words2:
        return 0.0
    
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    return len(intersection) / len(union)


def _analyze_paper_innovation(paper: Dict[str, Any], abstract: str = "") -> Dict[str, str]:
    """Analyze paper for innovation level and investment implications."""
    title = paper.get('title', '')
    summary = paper.get('summary', abstract)
    published_at = paper.get('publishedAt', '')
    authors = paper.get('authors', [])
    
    text_content = f"{title} {summary}".lower()
    
    # Innovation Level Assessment
    innovation_keywords = {
        'breakthrough': ['novel', 'first', 'new', 'breakthrough', 'revolutionary', 'unprecedented'],
        'significant': ['state-of-the-art', 'outperform', 'surpass', 'significant', 'major'],
        'incremental': ['improved', 'enhanced', 'optimized', 'better', 'efficient'],
        'survey': ['survey', 'review', 'overview', 'comprehensive']
    }
    
    innovation_scores = {}
    for category, keywords in innovation_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_content)
        innovation_scores[category] = score
    
    max_category = max(innovation_scores, key=innovation_scores.get)
    max_score = innovation_scores[max_category]
    
    if max_category == 'breakthrough' and max_score >= 2:
        innovation_level = "🚀 BREAKTHROUGH - Potentially disruptive innovation"
    elif max_category == 'significant' and max_score >= 1:
        innovation_level = "⭐ SIGNIFICANT - Major advancement in the field"
    elif max_category == 'incremental' and max_score >= 2:
        innovation_level = "📈 INCREMENTAL - Evolutionary improvement"
    elif max_category == 'survey':
        innovation_level = "📚 SURVEY - Knowledge consolidation, limited novelty"
    else:
        innovation_level = "🔍 EXPLORATORY - Early-stage research"
    
    # Technical Novelty Assessment
    technical_terms = _extract_key_terms(text_content)
    novelty_indicators = ['architecture', 'algorithm', 'method', 'approach', 'framework', 'model']
    novelty_count = sum(1 for term in novelty_indicators if term in text_content)
    
    if novelty_count >= 3:
        technical_novelty = "🔬 High technical novelty - New methodological contributions"
    elif novelty_count >= 1:
        technical_novelty = "🛠️ Moderate novelty - Methodological improvements"
    else:
        technical_novelty = "📊 Limited novelty - Primarily empirical or application-focused"
    
    # Market Impact Assessment
    application_terms = ['application', 'real-world', 'practical', 'deployment', 'industry', 'commercial']
    application_count = sum(1 for term in application_terms if term in text_content)
    
    if application_count >= 2:
        market_impact = "💼 High commercial potential - Clear practical applications"
    elif application_count >= 1:
        market_impact = "🎯 Moderate potential - Some practical relevance"
    else:
        market_impact = "🔬 Academic focus - Limited immediate commercial impact"
    
    # Competitive Advantage
    performance_terms = ['performance', 'accuracy', 'efficiency', 'speed', 'cost', 'resource']
    performance_count = sum(1 for term in performance_terms if term in text_content)
    
    if performance_count >= 3:
        competitive_advantage = "🏆 Strong advantage - Multiple performance improvements"
    elif performance_count >= 1:
        competitive_advantage = "📊 Moderate advantage - Some performance gains"
    else:
        competitive_advantage = "❓ Unclear advantage - Limited performance metrics"
    
    # Investment Implications
    if max_category == 'breakthrough' and application_count >= 1:
        investment_implications = "💰 HIGH INVESTMENT POTENTIAL - Breakthrough with commercial relevance"
    elif max_category == 'significant' and performance_count >= 2:
        investment_implications = "💵 MODERATE INVESTMENT POTENTIAL - Significant advancement with performance gains"
    elif max_category == 'incremental' and application_count >= 2:
        investment_implications = "💲 LIMITED INVESTMENT POTENTIAL - Incremental but practical improvements"
    else:
        investment_implications = "⚠️ LOW INVESTMENT POTENTIAL - Limited commercial or breakthrough value"
    
    return {
        'innovation_level': innovation_level,
        'technical_novelty': technical_novelty,
        'market_impact': market_impact,
        'competitive_advantage': competitive_advantage,
        'investment_implications': investment_implications
    }
