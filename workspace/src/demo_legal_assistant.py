#!/usr/bin/env python3
"""
Demo script for the Legal Assistant
Showcases legal analysis capabilities for VC investment due diligence
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

from workspace.src.legal_assistant import LegalAssistant


def demo_startup_legal_analysis():
    """Demo comprehensive legal analysis for startup investment."""
    print("⚖️ ASSISTANT JURIDIQUE DEMO - ANALYSE D'INVESTISSEMENT STARTUP")
    print("=" * 80)
    
    assistant = LegalAssistant(ANTHROPIC_API_KEY)
    
    # Test Case 1: FinTech Startup
    print("\n📊 CAS D'ÉTUDE 1: Startup FinTech - Plateforme de paiement")
    print("-" * 60)
    
    fintech_startup = """
    Une startup française développe une plateforme de paiement mobile innovante 
    qui utilise l'intelligence artificielle pour détecter les fraudes en temps réel. 
    La solution cible les e-commerçants et les marketplaces. L'entreprise prévoit 
    de lever 5M€ en série A et souhaite s'étendre en Europe dans les 18 prochains mois.
    """
    
    try:
        result = assistant.analyze_startup_legal_framework(fintech_startup, "FinTech")
        print(result)
    except Exception as e:
        print(f"Erreur dans l'analyse: {e}")
    
    print("\n" + "="*80)
    
    # Test Case 2: HealthTech Startup
    print("\n🏥 CAS D'ÉTUDE 2: Startup HealthTech - Dispositif médical connecté")
    print("-" * 60)
    
    healthtech_startup = """
    Une startup développe un dispositif médical connecté pour le monitoring 
    cardiaque à domicile. Le dispositif collecte des données biométriques 
    et utilise des algorithmes d'IA pour alerter les professionnels de santé 
    en cas d'anomalie. L'entreprise vise le marché français puis européen.
    """
    
    try:
        result = assistant.analyze_startup_legal_framework(healthtech_startup, "HealthTech")
        print(result)
    except Exception as e:
        print(f"Erreur dans l'analyse: {e}")
    
    print("\n" + "="*80)


def demo_legal_risk_evaluation():
    """Demo legal risk evaluation for different business models."""
    print("\n⚠️ ÉVALUATION DES RISQUES JURIDIQUES")
    print("=" * 80)
    
    assistant = LegalAssistant(ANTHROPIC_API_KEY)
    
    # Test Case 1: AI-powered SaaS
    print("\n🤖 Évaluation: Plateforme SaaS d'IA pour RH")
    print("-" * 50)
    
    ai_saas_model = """
    Plateforme SaaS qui utilise l'intelligence artificielle pour automatiser 
    le processus de recrutement. L'IA analyse les CV, conduit des entretiens 
    vidéo automatisés et recommande les meilleurs candidats. La plateforme 
    traite des données personnelles sensibles et prend des décisions automatisées.
    """
    
    try:
        result = assistant.evaluate_legal_risks(ai_saas_model, "France et UE")
        print(result)
    except Exception as e:
        print(f"Erreur dans l'évaluation des risques: {e}")
    
    print("\n" + "="*80)


def demo_sector_regulations():
    """Demo sector-specific regulation research."""
    print("\n📚 RECHERCHE RÉGLEMENTAIRE SECTORIELLE")
    print("=" * 80)
    
    assistant = LegalAssistant(ANTHROPIC_API_KEY)
    
    # Research regulations for different sectors
    sectors = [
        "Intelligence Artificielle",
        "Technologies Financières (FinTech)",
        "Technologies de Santé (HealthTech)"
    ]
    
    for sector in sectors:
        print(f"\n🔍 Recherche réglementaire: {sector}")
        print("-" * 50)
        
        try:
            result = assistant.research_sector_regulations(sector)
            print(result)
        except Exception as e:
            print(f"Erreur dans la recherche pour {sector}: {e}")
        
        print("\n" + "="*80)


def demo_investment_legal_structure():
    """Demo investment legal structure analysis."""
    print("\n🏗️ ANALYSE DE STRUCTURE JURIDIQUE D'INVESTISSEMENT")
    print("=" * 80)
    
    assistant = LegalAssistant(ANTHROPIC_API_KEY)
    
    # Test different investment structures
    investment_types = [
        ("Série A - Capital Risque", "5M€"),
        ("Série B - Croissance", "15M€"),
        ("Investissement Stratégique", "25M€")
    ]
    
    for investment_type, amount in investment_types:
        print(f"\n💰 Analyse: {investment_type} - {amount}")
        print("-" * 50)
        
        try:
            result = assistant.analyze_investment_legal_structure(investment_type, amount)
            print(result)
        except Exception as e:
            print(f"Erreur dans l'analyse pour {investment_type}: {e}")
        
        print("\n" + "="*80)


def demo_individual_legal_tools():
    """Demo individual legal tool capabilities."""
    print("\n🛠️ DÉMONSTRATION DES OUTILS JURIDIQUES INDIVIDUELS")
    print("=" * 80)
    
    # Import tools directly for testing
    from workspace.src.legifrance_search import search_legal_texts, analyze_legal_compliance, search_jurisprudence
    
    # Test legal text search
    print("\n📜 RECHERCHE DE TEXTES LÉGAUX: 'société par actions simplifiée'")
    print("-" * 50)
    try:
        legal_texts_result = search_legal_texts("société par actions simplifiée", "code", 3)
        print(legal_texts_result)
    except Exception as e:
        print(f"Erreur dans la recherche de textes légaux: {e}")
    
    # Test compliance analysis
    print("\n📋 ANALYSE DE CONFORMITÉ: 'Plateforme e-commerce'")
    print("-" * 50)
    try:
        compliance_result = analyze_legal_compliance("Plateforme e-commerce avec marketplace", "SAS")
        print(compliance_result)
    except Exception as e:
        print(f"Erreur dans l'analyse de conformité: {e}")
    
    # Test jurisprudence search
    print("\n⚖️ RECHERCHE JURISPRUDENTIELLE: 'droit des sociétés'")
    print("-" * 50)
    try:
        jurisprudence_result = search_jurisprudence("droit des sociétés", "responsabilité dirigeant", 3)
        print(jurisprudence_result)
    except Exception as e:
        print(f"Erreur dans la recherche jurisprudentielle: {e}")
    
    print("\n" + "="*80)


def main():
    """Run all legal assistant demos."""
    if not ANTHROPIC_API_KEY:
        print("❌ Erreur: ANTHROPIC_API_KEY non trouvée dans les variables d'environnement.")
        print("Veuillez configurer votre clé API dans le fichier .env.")
        return
    
    print("⚖️ ASSISTANT JURIDIQUE POUR INVESTISSEURS VC")
    print("🏆 Démo Hackathon - Analyse Juridique Complète d'Investissement")
    print("=" * 80)
    
    try:
        # Run startup legal analysis demo
        demo_startup_legal_analysis()
        
        # Run legal risk evaluation demo
        demo_legal_risk_evaluation()
        
        # Run sector regulations demo
        demo_sector_regulations()
        
        # Run investment structure demo
        demo_investment_legal_structure()
        
        # Run individual tools demo
        demo_individual_legal_tools()
        
        print("\n✅ DÉMONSTRATION TERMINÉE AVEC SUCCÈS!")
        print("🎉 L'Assistant Juridique est prêt pour l'analyse d'investissements!")
        
    except KeyboardInterrupt:
        print("\n\n⏹️ Démonstration interrompue par l'utilisateur.")
    except Exception as e:
        print(f"\n❌ Démonstration échouée avec l'erreur: {e}")
        print("Veuillez vérifier votre clé API et la connexion internet.")


if __name__ == "__main__":
    main()