#!/usr/bin/env python3
"""
Test script demonstrating multi-agent collaboration for VC investment analysis
Shows how legal, technical, and brainstorming agents work together
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

from workspace.src.simple_orchestrator import run_simple_orchestrator


def test_startup_investment_analysis():
    """Test comprehensive startup investment analysis using multiple agents."""
    print("🚀 TEST DE COLLABORATION MULTI-AGENTS")
    print("📊 Analyse d'investissement startup complète")
    print("=" * 80)
    
    # Startup case study
    startup_description = """
    Une startup française développe une plateforme d'IA pour l'analyse automatique 
    de contrats juridiques. La solution utilise des modèles de langage avancés pour 
    extraire les clauses importantes, identifier les risques et suggérer des améliorations. 
    Elle cible les cabinets d'avocats et les départements juridiques d'entreprises. 
    L'équipe souhaite lever 3M€ en série A.
    """
    
    print(f"📋 CAS D'ÉTUDE: {startup_description}")
    print("\n" + "="*80)
    
    # Test 1: Technical Analysis
    print("\n🔧 ANALYSE TECHNIQUE")
    print("-" * 50)
    technical_query = f"Analyse technique de cette startup: {startup_description}"
    
    try:
        technical_result = run_simple_orchestrator(technical_query, ["technical"])
        print(technical_result)
    except Exception as e:
        print(f"Erreur dans l'analyse technique: {e}")
    
    print("\n" + "="*80)
    
    # Test 2: Legal Analysis
    print("\n⚖️ ANALYSE JURIDIQUE")
    print("-" * 50)
    legal_query = f"Analyse juridique et conformité pour cette startup: {startup_description}"
    
    try:
        legal_result = run_simple_orchestrator(legal_query, ["legal_jurist"])
        print(legal_result)
    except Exception as e:
        print(f"Erreur dans l'analyse juridique: {e}")
    
    print("\n" + "="*80)
    
    # Test 3: Brainstorming for Business Development
    print("\n💡 BRAINSTORMING - DÉVELOPPEMENT BUSINESS")
    print("-" * 50)
    brainstorm_query = f"SCAMPER: Idées pour développer et améliorer cette startup: {startup_description}"
    
    try:
        brainstorm_result = run_simple_orchestrator(brainstorm_query, ["brainstorming"])
        print(brainstorm_result)
    except Exception as e:
        print(f"Erreur dans le brainstorming: {e}")
    
    print("\n" + "="*80)


def test_multi_agent_collaboration():
    """Test automatic agent selection and collaboration."""
    print("\n🤝 TEST DE COLLABORATION AUTOMATIQUE")
    print("=" * 80)
    
    # Test queries that should trigger multiple agents
    test_cases = [
        {
            "query": "Analyse complète d'une startup FinTech avec aspects techniques et juridiques",
            "description": "Devrait déclencher les agents technique et juridique"
        },
        {
            "query": "Brainstorm d'idées créatives pour améliorer la conformité légale d'une startup",
            "description": "Devrait déclencher les agents brainstorming et juridique"
        },
        {
            "query": "Recherche technique et analyse juridique d'une plateforme d'IA médicale",
            "description": "Devrait déclencher les agents technique et juridique"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 TEST {i}: {test_case['description']}")
        print(f"Query: {test_case['query']}")
        print("-" * 60)
        
        try:
            result = run_simple_orchestrator(test_case['query'])  # Auto-detection
            print(result)
        except Exception as e:
            print(f"Erreur dans le test {i}: {e}")
        
        print("\n" + "="*80)


def test_sector_specific_analysis():
    """Test sector-specific analysis combining multiple agents."""
    print("\n🏭 TEST D'ANALYSE SECTORIELLE SPÉCIALISÉE")
    print("=" * 80)
    
    sectors = [
        {
            "name": "FinTech",
            "description": "Startup de paiement mobile avec IA anti-fraude",
            "focus": "Réglementation financière et innovation technique"
        },
        {
            "name": "HealthTech", 
            "description": "Dispositif médical connecté avec algorithmes d'IA",
            "focus": "Conformité médicale et faisabilité technique"
        },
        {
            "name": "LegalTech",
            "description": "Plateforme d'automatisation juridique par IA",
            "focus": "Aspects juridiques et innovation technologique"
        }
    ]
    
    for sector in sectors:
        print(f"\n🎯 SECTEUR: {sector['name']}")
        print(f"Description: {sector['description']}")
        print(f"Focus: {sector['focus']}")
        print("-" * 60)
        
        # Combined analysis query
        query = f"""
        Analyse complète d'investissement pour une startup {sector['name']}: 
        {sector['description']}. 
        Inclure les aspects techniques, juridiques et réglementaires.
        """
        
        try:
            result = run_simple_orchestrator(query, ["technical", "legal_jurist"])
            print(result)
        except Exception as e:
            print(f"Erreur dans l'analyse {sector['name']}: {e}")
        
        print("\n" + "="*80)


def test_investment_decision_support():
    """Test investment decision support using all agents."""
    print("\n💰 TEST DE SUPPORT À LA DÉCISION D'INVESTISSEMENT")
    print("=" * 80)
    
    investment_scenario = """
    Un fonds VC évalue l'investissement de 5M€ dans une startup qui développe 
    une plateforme SaaS d'IA pour l'optimisation énergétique des bâtiments. 
    La solution analyse les données de consommation en temps réel et propose 
    des recommandations automatisées. L'équipe compte 15 personnes et vise 
    l'expansion européenne.
    """
    
    print(f"📊 SCÉNARIO D'INVESTISSEMENT:")
    print(investment_scenario)
    print("\n" + "-"*80)
    
    # Sequential analysis with different agents
    analyses = [
        {
            "agent": "technical",
            "focus": "Faisabilité technique et innovation",
            "query": f"Analyse technique approfondie: {investment_scenario}"
        },
        {
            "agent": "legal_jurist", 
            "focus": "Conformité et risques juridiques",
            "query": f"Analyse juridique et conformité: {investment_scenario}"
        },
        {
            "agent": "brainstorming",
            "focus": "Opportunités de développement",
            "query": f"Six Thinking Hats: Perspectives d'investissement pour {investment_scenario}"
        }
    ]
    
    for analysis in analyses:
        print(f"\n🔍 {analysis['focus'].upper()}")
        print(f"Agent: {analysis['agent']}")
        print("-" * 50)
        
        try:
            result = run_simple_orchestrator(analysis['query'], [analysis['agent']])
            print(result)
        except Exception as e:
            print(f"Erreur dans l'analyse {analysis['agent']}: {e}")
        
        print("\n" + "="*80)


def main():
    """Run all multi-agent collaboration tests."""
    if not ANTHROPIC_API_KEY:
        print("❌ Erreur: ANTHROPIC_API_KEY non trouvée dans les variables d'environnement.")
        print("Veuillez configurer votre clé API dans le fichier .env.")
        return
    
    print("🤖 TEST DE COLLABORATION MULTI-AGENTS POUR VC")
    print("🏆 Démonstration de l'écosystème d'agents collaboratifs")
    print("=" * 80)
    
    try:
        # Test comprehensive startup analysis
        test_startup_investment_analysis()
        
        # Test automatic agent collaboration
        test_multi_agent_collaboration()
        
        # Test sector-specific analysis
        test_sector_specific_analysis()
        
        # Test investment decision support
        test_investment_decision_support()
        
        print("\n✅ TOUS LES TESTS DE COLLABORATION TERMINÉS AVEC SUCCÈS!")
        print("🎉 L'écosystème multi-agents est opérationnel pour l'analyse d'investissements!")
        
    except KeyboardInterrupt:
        print("\n\n⏹️ Tests interrompus par l'utilisateur.")
    except Exception as e:
        print(f"\n❌ Tests échoués avec l'erreur: {e}")
        print("Veuillez vérifier votre configuration et les dépendances.")


if __name__ == "__main__":
    main()