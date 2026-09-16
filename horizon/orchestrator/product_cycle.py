from horizon.domain.company_profile import CompanyProfile
from horizon.domain.product_opportunity import ProductOpportunity
from horizon.domain.constraints import Constraints

from horizon.engines.market_engine import MarketEngine
from horizon.engines.competitor_engine import CompetitorEngine
from horizon.engines.viability_engine import ViabilityEngine
from horizon.engines.constraint_engine import ConstraintEngine
from horizon.engines.strategic_fit_engine import StrategicFitEngine
from horizon.engines.decision_engine import DecisionEngine

def run_product_analysis(
    company: CompanyProfile,
    opportunity: ProductOpportunity,
    constraints: Constraints,
    competitors
):
    market_result = MarketEngine().evaluate(market=opportunity)
    competitor_result = CompetitorEngine().evaluate(company, opportunity, competitors)
    viability_result = ViabilityEngine().evaluate(company, opportunity, market_result, competitor_result)
    constraint_result = ConstraintEngine().evaluate(constraints, opportunity)
    strategic_fit_result = StrategicFitEngine().evaluate(company, opportunity, viability_result, constraint_result)

    decision = DecisionEngine().synthesize(
        company,
        opportunity,
        market_result,
        competitor_result,
        viability_result,
        constraint_result,
        strategic_fit_result
    )

    return decision
