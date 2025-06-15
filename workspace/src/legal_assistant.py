#!/usr/bin/env python3

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

from workspace.src.legifrance_search import search_legal_texts, analyze_legal_compliance, search_jurisprudence
from smolagents import CodeAgent
from smolagents.models import LiteLLMModel


class LegalAssistant:
    def __init__(self, api_key):
        self.agent = CodeAgent(
            tools=[search_legal_texts, analyze_legal_compliance, search_jurisprudence],
            model=LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest", api_key=api_key),
            add_base_tools=False,
        )

    def analyze_startup_legal_framework(self, startup_description: str, business_sector: str = "") -> str:
        """
        Comprehensive legal analysis of a startup for investment due diligence.
        Evaluates regulatory compliance, legal risks, and regulatory framework.
        """
        analysis_prompt = f"""
        As a legal expert specializing in startup investments and French law, provide a comprehensive legal analysis of this startup:
        
        Startup Description: {startup_description}
        Business Sector: {business_sector}
        
        Your analysis should include:
        1. Applicable regulatory framework (French and EU law)
        2. Required licenses and authorizations
        3. Data protection and privacy compliance (GDPR)
        4. Intellectual property considerations
        5. Employment law implications
        6. Tax and corporate law requirements
        7. Sector-specific regulations
        8. Legal risk assessment for investors
        9. Compliance roadmap and recommendations
        
        Use the available tools to search for relevant legal texts and jurisprudence to support your analysis.
        Provide specific legal references and citations.
        """
        
        return self.agent.run(analysis_prompt)

    def evaluate_legal_risks(self, business_model: str, target_market: str = "France") -> str:
        """
        Evaluates legal risks associated with a specific business model.
        """
        risk_prompt = f"""
        Analyze the legal risks associated with this business model:
        
        Business Model: {business_model}
        Target Market: {target_market}
        
        Determine:
        1. Primary legal risks and liabilities
        2. Regulatory compliance requirements
        3. Potential legal challenges and disputes
        4. Intellectual property risks
        5. Data protection and privacy risks
        6. Consumer protection obligations
        7. Competition law considerations
        8. Cross-border legal implications (if applicable)
        9. Risk mitigation strategies
        
        Search for relevant legal precedents and regulatory guidance.
        """
        
        return self.agent.run(risk_prompt)

    def research_sector_regulations(self, sector: str) -> str:
        """
        Researches specific regulations applicable to a business sector.
        """
        research_prompt = f"""
        Research the regulatory landscape for the following sector: {sector}
        
        Provide:
        1. Key regulatory authorities and oversight bodies
        2. Primary laws and regulations applicable to this sector
        3. Recent regulatory changes and updates
        4. Licensing and authorization requirements
        5. Compliance obligations and reporting requirements
        6. Penalties and sanctions for non-compliance
        7. Industry-specific legal considerations
        8. Emerging regulatory trends and future changes
        9. Best practices for regulatory compliance
        
        Use tools to gather current legal information from Légifrance and other sources.
        """
        
        return self.agent.run(research_prompt)

    def analyze_investment_legal_structure(self, investment_type: str, amount: str = "") -> str:
        """
        Analyzes the legal structure and requirements for different types of investments.
        """
        structure_prompt = f"""
        Analyze the legal framework for this type of investment:
        
        Investment Type: {investment_type}
        Investment Amount: {amount}
        
        Provide analysis on:
        1. Legal structure options (SAS, SARL, SA, etc.)
        2. Corporate governance requirements
        3. Shareholder rights and protections
        4. Due diligence legal requirements
        5. Investment documentation and contracts
        6. Tax implications for investors
        7. Exit strategy legal considerations
        8. Regulatory approvals and notifications
        9. Investor protection regulations
        
        Search for relevant legal texts and recent jurisprudence.
        """
        
        return self.agent.run(structure_prompt)


if __name__ == "__main__":
    # Example usage
    assistant = LegalAssistant(ANTHROPIC_API_KEY)
    
    # Test startup legal framework analysis
    startup_desc = """
    Une startup française développe une plateforme d'intelligence artificielle pour l'analyse 
    automatique de documents juridiques. La plateforme utilise des modèles de langage pour 
    extraire des informations clés des contrats et identifier les risques juridiques. 
    Elle cible les cabinets d'avocats et les départements juridiques d'entreprises.
    """
    
    print("=== ANALYSE DU CADRE JURIDIQUE STARTUP ===")
    result = assistant.analyze_startup_legal_framework(startup_desc, "LegalTech")
    print(result)
    
    print("\n=== ANALYSE DES RISQUES JURIDIQUES ===")
    business_model = "Plateforme SaaS d'analyse de documents juridiques par IA"
    risk_result = assistant.evaluate_legal_risks(business_model)
    print(risk_result)