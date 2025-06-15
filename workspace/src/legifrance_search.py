from smolagents import tool
import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

# Note: Légifrance API requires authentication and has specific endpoints
# For demonstration purposes, we'll simulate responses with realistic legal data
LEGIFRANCE_API_URL = "https://api.legifrance.gouv.fr"

@tool
def search_legal_texts(query: str, text_type: str = "all", limit: int = 10) -> str:
    """
    Search for legal texts in Légifrance database with detailed analysis for investment due diligence.
    Returns comprehensive information including codes, laws, decrees, and regulations.
    
    Args:
        query: The search query to find relevant legal texts
        text_type: Type of legal text (all, code, loi, decret, arrete, ordonnance) (default: "all")
        limit: Maximum number of results to return (default: 10)
    """
    try:
        # Note: Real Légifrance API requires authentication and specific formatting
        # Providing simulated response with realistic legal data for demonstration
        return f"""
RECHERCHE LÉGIFRANCE POUR: "{query}"
{'='*80}

📜 TEXTE LÉGAL: Code de commerce - Article L225-1 et suivants (Sociétés anonymes)
📅 Dernière modification: 2023-12-15 | 🔄 Statut: En vigueur
🏛️ Source: Code de commerce
📍 Référence: Articles L225-1 à L225-270
💼 Domaine: Droit des sociétés - Constitution et fonctionnement des SA
📝 Résumé: Dispositions relatives à la constitution, au fonctionnement et à la gouvernance des sociétés anonymes...

📜 TEXTE LÉGAL: Loi n° 2019-486 du 22 mai 2019 (PACTE)
📅 Publication: 2019-05-23 | 🔄 Statut: En vigueur
🏛️ Source: Loi PACTE
📍 Référence: Articles 1 à 229
💼 Domaine: Droit des affaires - Croissance et transformation des entreprises
📝 Résumé: Plan d'action pour la croissance et la transformation des entreprises, incluant les dispositions sur les startups...

📜 TEXTE LÉGAL: Règlement (UE) 2016/679 (RGPD)
📅 Application: 2018-05-25 | 🔄 Statut: En vigueur
🏛️ Source: Droit européen
📍 Référence: Articles 1 à 99
💼 Domaine: Protection des données personnelles
📝 Résumé: Règlement général sur la protection des données, applicable à toutes les entreprises traitant des données...

📜 TEXTE LÉGAL: Code du travail - Livre II (Relations individuelles de travail)
📅 Dernière modification: 2024-01-01 | 🔄 Statut: En vigueur
🏛️ Source: Code du travail
📍 Référence: Articles L1221-1 et suivants
💼 Domaine: Droit du travail - Contrats et relations de travail
📝 Résumé: Dispositions relatives aux contrats de travail, durée du travail, et relations employeur-salarié...

Note: API Légifrance nécessite une authentification. Réponse simulée pour démonstration.
Pour un usage en production, veuillez configurer les clés d'API Légifrance.
        """
    
    except Exception as e:
        return f"Erreur lors de la recherche de textes légaux: {str(e)}"


@tool
def analyze_legal_compliance(business_activity: str, company_type: str = "SAS") -> str:
    """
    Analyze legal compliance requirements for a specific business activity and company type.
    Provides detailed compliance roadmap and regulatory obligations.
    
    Args:
        business_activity: Description of the business activity to analyze
        company_type: Type of company structure (SAS, SARL, SA, etc.) (default: "SAS")
    """
    try:
        # Simulate compliance analysis based on business activity
        compliance_analysis = _analyze_compliance_requirements(business_activity, company_type)
        
        return f"""
ANALYSE DE CONFORMITÉ LÉGALE
{'='*70}

🏢 ACTIVITÉ: {business_activity}
🏛️ FORME JURIDIQUE: {company_type}

📋 OBLIGATIONS RÉGLEMENTAIRES:
{compliance_analysis['regulatory_obligations']}

📄 LICENCES ET AUTORISATIONS:
{compliance_analysis['licenses_required']}

🔒 PROTECTION DES DONNÉES (RGPD):
{compliance_analysis['data_protection']}

👥 DROIT DU TRAVAIL:
{compliance_analysis['employment_law']}

💰 OBLIGATIONS FISCALES:
{compliance_analysis['tax_obligations']}

⚖️ PROPRIÉTÉ INTELLECTUELLE:
{compliance_analysis['intellectual_property']}

⚠️ RISQUES JURIDIQUES IDENTIFIÉS:
{compliance_analysis['legal_risks']}

✅ RECOMMANDATIONS DE CONFORMITÉ:
{compliance_analysis['compliance_recommendations']}
        """
    
    except Exception as e:
        return f"Erreur lors de l'analyse de conformité: {str(e)}"


@tool
def search_jurisprudence(legal_domain: str, keywords: str = "", limit: int = 5) -> str:
    """
    Search for relevant jurisprudence and case law in a specific legal domain.
    Provides insights from court decisions and legal precedents.
    
    Args:
        legal_domain: Legal domain to search (droit des sociétés, droit du travail, etc.)
        keywords: Additional keywords for refined search (default: "")
        limit: Maximum number of cases to return (default: 5)
    """
    try:
        # Simulate jurisprudence search with realistic case data
        return f"""
JURISPRUDENCE - DOMAINE: {legal_domain}
{'='*80}

⚖️ ARRÊT: Cour de cassation, Chambre commerciale, 15 mars 2023, n° 21-20.456
📅 Date: 2023-03-15 | 🏛️ Juridiction: Cour de cassation (Com.)
🎯 Domaine: Droit des sociétés - Responsabilité des dirigeants
📝 Principe: La responsabilité civile du dirigeant de société peut être engagée en cas de faute de gestion...
💡 Impact: Renforce les obligations de diligence des dirigeants de startups

⚖️ ARRÊT: Conseil d'État, 6e chambre, 12 janvier 2024, n° 468234
📅 Date: 2024-01-12 | 🏛️ Juridiction: Conseil d'État
🎯 Domaine: Droit administratif - Autorisation d'exploitation
📝 Principe: Les entreprises de technologie financière doivent obtenir un agrément préalable...
💡 Impact: Clarification des obligations réglementaires pour les FinTech

⚖️ ARRÊT: Cour d'appel de Paris, Pôle 5, 28 septembre 2023, n° 22/15678
📅 Date: 2023-09-28 | 🏛️ Juridiction: CA Paris
🎯 Domaine: Propriété intellectuelle - Protection des algorithmes
📝 Principe: Les algorithmes d'intelligence artificielle peuvent bénéficier d'une protection...
💡 Impact: Protection renforcée des innovations technologiques

⚖️ DÉCISION: CNIL, Délibération n° 2023-045, 5 juin 2023
📅 Date: 2023-06-05 | 🏛️ Autorité: CNIL
🎯 Domaine: Protection des données - IA et RGPD
📝 Principe: Les traitements de données par IA doivent respecter les principes de transparence...
💡 Impact: Obligations spécifiques pour les startups utilisant l'IA

Note: Recherche jurisprudentielle simulée. Pour un accès complet aux bases de données 
jurisprudentielles, veuillez utiliser les services officiels (Légifrance, Dalloz, etc.).
        """
    
    except Exception as e:
        return f"Erreur lors de la recherche jurisprudentielle: {str(e)}"


def _analyze_compliance_requirements(business_activity: str, company_type: str) -> Dict[str, str]:
    """Analyze compliance requirements based on business activity and company type."""
    
    activity_lower = business_activity.lower()
    
    # Determine regulatory obligations based on activity
    if any(term in activity_lower for term in ['fintech', 'finance', 'paiement', 'banque']):
        regulatory_obligations = """
• Agrément ACPR (Autorité de Contrôle Prudentiel et de Résolution)
• Respect des directives DSP2 et MiFID II
• Déclaration auprès de TRACFIN (lutte anti-blanchiment)
• Obligations de reporting prudentiel
• Respect des ratios de solvabilité"""
        
        licenses_required = """
• Licence d'établissement de paiement ou de monnaie électronique
• Agrément bancaire (si applicable)
• Passeport européen pour services financiers
• Enregistrement ORIAS (si intermédiation)"""
        
    elif any(term in activity_lower for term in ['ia', 'intelligence artificielle', 'algorithme', 'données']):
        regulatory_obligations = """
• Conformité au Règlement IA européen (AI Act)
• Respect du RGPD pour le traitement des données
• Déclaration des systèmes d'IA à haut risque
• Obligations de transparence algorithmique
• Respect des principes éthiques de l'IA"""
        
        licenses_required = """
• Pas de licence spécifique requise actuellement
• Certification CE pour systèmes IA à haut risque (à venir)
• Enregistrement auprès des autorités compétentes
• Conformité aux standards techniques européens"""
        
    elif any(term in activity_lower for term in ['santé', 'médical', 'dispositif médical']):
        regulatory_obligations = """
• Conformité au Règlement MDR (Medical Device Regulation)
• Respect du Code de la santé publique
• Obligations de pharmacovigilance
• Respect des bonnes pratiques cliniques
• Déclaration auprès de l'ANSM"""
        
        licenses_required = """
• Marquage CE pour dispositifs médicaux
• Autorisation de mise sur le marché (si applicable)
• Licence d'exploitation pharmaceutique (si applicable)
• Agrément établissement pharmaceutique"""
        
    else:
        regulatory_obligations = """
• Respect du Code de commerce
• Conformité aux réglementations sectorielles
• Obligations déclaratives standard
• Respect des règles de concurrence
• Conformité environnementale (si applicable)"""
        
        licenses_required = """
• Immatriculation au RCS (Registre du Commerce et des Sociétés)
• Déclaration d'activité auprès des autorités compétentes
• Licences sectorielles spécifiques (selon activité)
• Autorisations d'exploitation (si nécessaire)"""
    
    # Common compliance areas
    data_protection = """
• Mise en conformité RGPD complète
• Nomination d'un DPO (si seuils atteints)
• Registre des traitements de données
• Politique de confidentialité et mentions légales
• Procédures de gestion des violations de données
• Contrats de sous-traitance conformes"""
    
    employment_law = f"""
• Respect du Code du travail français
• Convention collective applicable
• Contrats de travail conformes
• Règlement intérieur (si > 50 salariés)
• Obligations de formation et sécurité
• Représentation du personnel (selon effectifs)"""
    
    if company_type.upper() == "SAS":
        tax_obligations = """
• Impôt sur les sociétés (IS) - Taux standard ou réduit
• TVA (si chiffre d'affaires > seuils)
• Contribution économique territoriale (CET)
• Taxe sur les salaires (si applicable)
• Crédit d'impôt recherche (CIR) - Opportunité
• Statut JEI (Jeune Entreprise Innovante) - Avantages fiscaux"""
    else:
        tax_obligations = """
• Obligations fiscales selon la forme juridique
• Impôt sur les sociétés ou IR (selon option)
• TVA et taxes parafiscales
• Contributions sociales
• Optimisations fiscales disponibles"""
    
    intellectual_property = """
• Protection des marques et noms de domaine
• Dépôt de brevets (innovations techniques)
• Protection des droits d'auteur (logiciels)
• Contrats de cession/licence de PI
• Clauses de confidentialité et non-concurrence
• Veille concurrentielle et contrefaçon"""
    
    legal_risks = """
• Risque de non-conformité réglementaire
• Responsabilité civile et pénale des dirigeants
• Litiges commerciaux et contractuels
• Violations de propriété intellectuelle
• Non-respect des obligations sociales
• Sanctions administratives et pénales"""
    
    compliance_recommendations = """
• Audit juridique complet avant levée de fonds
• Mise en place d'un système de veille réglementaire
• Formation des équipes aux obligations légales
• Documentation et traçabilité des processus
• Assurance responsabilité civile professionnelle
• Accompagnement juridique spécialisé
• Plan de mise en conformité progressive"""
    
    return {
        'regulatory_obligations': regulatory_obligations,
        'licenses_required': licenses_required,
        'data_protection': data_protection,
        'employment_law': employment_law,
        'tax_obligations': tax_obligations,
        'intellectual_property': intellectual_property,
        'legal_risks': legal_risks,
        'compliance_recommendations': compliance_recommendations
    }


def _format_legal_text_info(text: Dict[str, Any]) -> str:
    """Format legal text information for display."""
    title = text.get("title", "Texte sans titre")
    reference = text.get("reference", "N/A")
    status = text.get("status", "N/A")
    last_modified = text.get("lastModified", "N/A")
    domain = text.get("domain", "N/A")
    summary = text.get("summary", "Résumé non disponible")
    
    return f"""
📜 TEXTE LÉGAL: {title}
📍 Référence: {reference}
🔄 Statut: {status}
📅 Dernière modification: {last_modified}
💼 Domaine: {domain}
📝 Résumé: {summary[:300]}...
"""


def _calculate_legal_relevance_score(text_content: str, query: str) -> str:
    """Calculate relevance score for legal texts."""
    query_terms = query.lower().split()
    content_lower = text_content.lower()
    
    matches = sum(1 for term in query_terms if term in content_lower)
    relevance_ratio = matches / len(query_terms) if query_terms else 0
    
    if relevance_ratio > 0.8:
        return "🔥 Très pertinent"
    elif relevance_ratio > 0.6:
        return "🚀 Pertinent"
    elif relevance_ratio > 0.4:
        return "📈 Moyennement pertinent"
    else:
        return "🔍 Faiblement pertinent"