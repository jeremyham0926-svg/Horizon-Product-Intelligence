from horizon.domain.company_profile import CompanyProfile
from horizon.domain.product_opportunity import ProductOpportunity
from horizon.domain.competitor import CompetitorInput
from typing import Optional

class CompetitorResult:
    def __init__(self, competitor_score: Optional[float], threats: list, opportunities: list):
        self.competitor_score = competitor_score
        self.threats = threats
        self.opportunities = opportunities

class CompetitorEngine:
    def evaluate(
        self,
        company: CompanyProfile,
        opportunity: ProductOpportunity,
        competitors: CompetitorInput
    ) -> CompetitorResult:

        threats = []
        opportunities = []
        score = 0

        for comp in competitors.competitors:
            if comp.strengths:
                score -= len(comp.strengths) * 5
                threats.append(f"{comp.name} has strong capabilities.")

            if comp.weaknesses:
                score += len(comp.weaknesses) * 4
                opportunities.append(f"{comp.name} has notable weaknesses.")

        return CompetitorResult(score, threats, opportunities)
