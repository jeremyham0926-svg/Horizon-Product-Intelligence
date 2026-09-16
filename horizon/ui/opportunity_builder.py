import streamlit as st
from horizon.domain.company_profile import CompanyProfile
from horizon.domain.product_opportunity import ProductOpportunity
from horizon.domain.competitor import Competitor, CompetitorInput
from horizon.domain.constraints import Constraints
from horizon.orchestrator.product_cycle import run_product_analysis

def render_opportunity_builder():
    st.title("Opportunity Builder")

    st.header("Company Profile")
    company_name = st.text_input("Company Name")
    industry = st.text_input("Industry")
    segments = st.text_input("Segments (comma-separated)").split(",")

    st.header("Product Opportunity")
    opp_name = st.text_input("Opportunity Name")
    value_prop = st.text_area("Value Proposition")
    features = st.text_input("Features (comma-separated)").split(",")

    st.header("Competitors")
    competitor_names = st.text_input("Competitor Names (comma-separated)").split(",")

    competitors = []
    for name in competitor_names:
        if name.strip():
            competitors.append(
                Competitor(
                    name=name.strip(),
                    strengths=["brand", "distribution"],
                    weaknesses=["slow innovation"]
                )
            )

    st.header("Constraints")
    regulatory = st.text_input("Regulatory Constraints").split(",")
    technical = st.text_input("Technical Constraints").split(",")
    operational = st.text_input("Operational Constraints").split(",")

    if st.button("Run Analysis"):
        company = CompanyProfile(
            name=company_name,
            industry=industry,
            segments=segments,
            capabilities=["AI", "Cloud", "Analytics"],
            strategic_goals=["growth", "innovation"]
        )

        opportunity = ProductOpportunity(
            name=opp_name,
            value_proposition=value_prop,
            features=features
        )

        competitor_input = CompetitorInput(competitors=competitors)

        constraints = Constraints(
            regulatory=regulatory,
            technical=technical,
            operational=operational
        )

        result = run_product_analysis(
            company=company,
            opportunity=opportunity,
            constraints=constraints,
            competitors=competitor_input
        )

        st.session_state["analysis_result"] = result
        st.session_state["page"] = "analysis"
