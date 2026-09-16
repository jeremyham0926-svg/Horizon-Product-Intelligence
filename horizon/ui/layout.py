import streamlit as st

def section(title: str):
    st.markdown(f"### {title}")

def score_badge(label: str, value: float):
    color = "green" if value >= 75 else "orange" if value >= 50 else "red"
    st.markdown(
        f"""
        <div style="
            padding: 10px;
            border-radius: 8px;
            background-color: {color};
            color: white;
            font-weight: bold;
            margin-bottom: 10px;
        ">
            {label}: {round(value, 2)}
        </div>
        """,
        unsafe_allow_html=True
    )

def recommendation_box(text: str):
    st.markdown(
        f"""
        <div style="
            padding: 15px;
            border-radius: 10px;
            background-color: #f0f2f6;
            border-left: 6px solid #4CAF50;
            font-size: 18px;
            margin-top: 20px;
        ">
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )
