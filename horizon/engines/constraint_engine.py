from horizon.domain.constraints import Constraints
from horizon.domain.product_opportunity import ProductOpportunity

class ConstraintResult:
    def __init__(self, constraint_score, blockers, mitigations):
        self.constraint_score = constraint_score
        self.blockers = blockers
        self.mitigations = mitigations

class ConstraintEngine:
    def evaluate(self, constraints: Constraints, opportunity: ProductOpportunity) -> ConstraintResult:
        blockers = []
        mitigations = []
        score = 100  # Start with perfect score and subtract

        for reg in constraints.regulatory:
            score -= 10
            blockers.append(f"Regulatory constraint: {reg}")

        for tech in constraints.technical:
            score -= 8
            blockers.append(f"Technical constraint: {tech}")

        for op in constraints.operational:
            score -= 5
            blockers.append(f"Operational constraint: {op}")

        if score < 50:
            mitigations.append("High constraints detected — consider scope reduction.")

        return ConstraintResult(score, blockers, mitigations)
