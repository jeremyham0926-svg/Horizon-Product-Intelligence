import streamlit as st
from horizon.ui.layout import section, score_badge

def render_analysis_view(result):
    st.title("Analysis Results")

    section("Composite Score")
    score_badge("Overall Score", result.scores["composite_score"])

    section("Recommendation")
    st.write(result.scores["recommendation"])

    section("Score Breakdown")
    col1, col2, col3 = st.columns(3)

    with col1:
        score_badge("Market", result.scores["market"])
        score_badge("Competitor", result.scores["competitor"])

    with col2:
        score_badge("Viability", result.scores["viability"])
        score_badge("Constraints", result.scores["constraints"])

    with col3:
        score_badge("Strategic Fit", result.scores["strategic_fit"])

    section("Executive Summary")
    st.markdown(result.summary)

    if st.button("View Decision Summary"):
        st.session_state["page"] = "decision"

