import streamlit as st
import pandas as pd
from pathlib import Path
from utils.loader import load_css

st.set_page_config(layout="wide")
load_css()

def load_questions():
    csv_path = Path(__file__).resolve().parent.parent / "questions.csv"
    df = pd.read_csv(csv_path)
    df["Level"] = df["Level"].astype(int)
    return df

df = load_questions()

idx = st.session_state.get("current_question_idx")

if idx is None:
    st.warning("No question selected. Go back to the board.")
    if st.button("⬅ Back to board"):
        st.switch_page("pages/game_board.py")
else:
    row = df.loc[idx]

    st.markdown(
        f"### {row['Category']} — Level {row['Level']} (${row['Level'] * 100})"
    )
    st.markdown("---")
    st.markdown(f"## {row['Question']}")

    if "show_answer" not in st.session_state:
        st.session_state.show_answer = False

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Show answer"):
            st.session_state.show_answer = True
    with col2:
        if st.button("⬅ Back to board"):
            st.session_state.show_answer = False
            st.switch_page("pages/game_board.py")

    if st.session_state.show_answer:
        st.markdown("---")
        st.markdown("### Answer")
        st.success(row["Answer"])