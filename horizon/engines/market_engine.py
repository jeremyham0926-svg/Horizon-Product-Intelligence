from horizon.domain.market import MarketInput
from typing import Optional

class MarketResult:
    def __init__(self, market_score: Optional[float], insights: list):
        self.market_score = market_score
        self.insights = insights

class MarketEngine:
    def evaluate(self, market: MarketInput) -> MarketResult:
        insights = []

        score = 0

        # Trend-based scoring
        if market.trends:
            score += len(market.trends) * 5
            insights.append("Strong trend activity detected.")

        # Pain point scoring
        if market.pain_points:
            score += len(market.pain_points) * 7
            insights.append("Multiple customer pain points identified.")

        # Growth rate scoring
        if market.growth_rate:
            score += market.growth_rate * 2
            insights.append(f"Growth rate contributes {market.growth_rate * 2} points.")

        return MarketResult(market_score=score, insights=insights)
