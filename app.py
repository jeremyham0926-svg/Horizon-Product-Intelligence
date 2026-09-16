import streamlit as st
from horizon.ui.home import render_home
from horizon.ui.opportunity_builder import render_opportunity_builder
from horizon.ui.analysis_view import render_analysis_view
from horizon.ui.decision_view import render_decision_view

def main():
    st.set_page_config(page_title="Horizon Product Intelligence", layout="wide")

    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    if st.session_state["page"] == "home":
        render_home()
    elif st.session_state["page"] == "builder":
        render_opportunity_builder()
    elif st.session_state["page"] == "analysis":
        render_analysis_view(st.session_state["analysis_result"])
    elif st.session_state["page"] == "decision":
        render_decision_view(st.session_state["analysis_result"])

if __name__ == "__main__":
    main()
