from horizon.domain.company_profile import CompanyProfile
from horizon.domain.product_opportunity import ProductOpportunity

class ViabilityResult:
    def __init__(self, viability_score, strengths, weaknesses):
        self.viability_score = viability_score
        self.strengths = strengths
        self.weaknesses = weaknesses

class ViabilityEngine:
    def evaluate(
        self,
        company: CompanyProfile,
        opportunity: ProductOpportunity,
        market_result,
        competitor_result
    ) -> ViabilityResult:

        strengths = []
        weaknesses = []
        score = 0

        # Capability alignment
        for feature in opportunity.features:
            if feature in company.capabilities:
                score += 10
                strengths.append(f"Company has capability for: {feature}")
            else:
                score -= 5
                weaknesses.append(f"Missing capability for: {feature}")

        # Market synergy
        score += (market_result.market_score or 0) * 0.2

        # Competitive synergy
        score += (competitor_result.competitor_score or 0) * 0.1

        return ViabilityResult(score, strengths, weaknesses)
