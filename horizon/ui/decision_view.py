import streamlit as st
from horizon.ui.layout import section, recommendation_box

def render_decision_view(result):
    st.title("Decision Summary")

    section("Final Recommendation")
    recommendation_box(result.scores["recommendation"])

    section("Composite Score")
    st.metric("Overall Score", round(result.scores["composite_score"], 2))

    section("Full Executive Summary")
    st.markdown(result.summary)

    if st.button("Back to Home"):
        st.session_state["page"] = "home"

