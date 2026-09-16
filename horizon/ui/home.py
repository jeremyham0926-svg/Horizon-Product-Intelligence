import streamlit as st
from horizon.ui.opportunity_builder import render_opportunity_builder

def render_home():
    st.title("Horizon Product Intelligence")
    st.write("Welcome to the Horizon MVP.")

    st.subheader("Start a New Product Opportunity Analysis")

    if st.button("Build Opportunity"):
        st.session_state["page"] = "builder"
