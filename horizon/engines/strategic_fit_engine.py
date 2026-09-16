from horizon.domain.company_profile import CompanyProfile
from horizon.domain.product_opportunity import ProductOpportunity

class StrategicFitResult:
    def __init__(self, strategic_fit_score, alignment_factors, risks):
        self.strategic_fit_score = strategic_fit_score
        self.alignment_factors = alignment_factors
        self.risks = risks

class StrategicFitEngine:
    def evaluate(
        self,
        company: CompanyProfile,
        opportunity: ProductOpportunity,
        viability_result,
        constraint_result
    ) -> StrategicFitResult:

        score = 0
        alignment_factors = []
        risks = []

        # Strategic goal alignment
        for goal in company.strategic_goals:
            if goal.lower() in opportunity.value_proposition.lower():
                score += 15
                alignment_factors.append(f"Aligned with strategic goal: {goal}")

        # Penalize constraints
        score -= (100 - constraint_result.constraint_score) * 0.3

        # Reward viability
        score += viability_result.viability_score * 0.4

        if score < 0:
            risks.append("Low strategic alignment detected.")

        return StrategicFitResult(score, alignment_factors, risks)
