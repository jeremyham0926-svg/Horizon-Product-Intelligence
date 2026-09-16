from horizon.domain.decision import DecisionResult

class DecisionEngine:
    def synthesize(
        self,
        company,
        opportunity,
        market,
        competitor,
        viability,
        constraints,
        strategic_fit
    ) -> DecisionResult:
        """
        Combine all engine outputs into a final executive decision.
        """

        # Weighted composite score
        composite_score = (
            (market.market_score or 0) * 0.25 +
            (competitor.competitor_score or 0) * 0.15 +
            (viability.viability_score or 0) * 0.25 +
            (constraints.constraint_score or 0) * 0.10 +
            (strategic_fit.strategic_fit_score or 0) * 0.25
        )

        # Recommendation tier
        if composite_score >= 75:
            recommendation = "GO — Strong strategic and market alignment."
        elif composite_score >= 50:
            recommendation = "CONSIDER — Mixed signals; refine scope or mitigate risks."
        else:
            recommendation = "NO-GO — Insufficient alignment or high constraints."

        # Narrative summary
        summary = f"""
        Product Opportunity: {opportunity.name}

        Composite Score: {round(composite_score, 2)}
        Recommendation: {recommendation}

        Breakdown:
        - Market Score: {market.market_score}
        - Competitor Score: {competitor.competitor_score}
        - Viability Score: {viability.viability_score}
        - Constraint Score: {constraints.constraint_score}
        - Strategic Fit Score: {strategic_fit.strategic_fit_score}

        Key Insights:
        - Market: {', '.join(market.insights) if market.insights else 'No insights'}
        - Competitors: {', '.join(competitor.threats + competitor.opportunities)}
        - Viability: {', '.join(viability.strengths + viability.weaknesses)}
        - Constraints: {', '.join(constraints.blockers + constraints.mitigations)}
        - Strategic Fit: {', '.join(strategic_fit.alignment_factors + strategic_fit.risks)}
        """

        scores = {
            "composite_score": composite_score,
            "recommendation": recommendation,
            "market": market.market_score,
            "competitor": competitor.competitor_score,
            "viability": viability.viability_score,
            "constraints": constraints.constraint_score,
            "strategic_fit": strategic_fit.strategic_fit_score
        }

        return DecisionResult(summary=summary, scores=scores)
