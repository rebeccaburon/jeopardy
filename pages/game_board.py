import streamlit as st
import pandas as pd
from pathlib import Path
from utils.loader import load_css

st.set_page_config(layout="wide")
load_css()

# ---- State helpers ----
def init_state():
    if "used_cells" not in st.session_state:
        # stores tuples like ("Sampled Legends", 1)
        st.session_state.used_cells = set()
    if "current_question_idx" not in st.session_state:
        st.session_state.current_question_idx = None

def load_questions():
    csv_path = Path(__file__).resolve().parent.parent / "questions.csv"
    df = pd.read_csv(csv_path)
    df["Level"] = df["Level"].astype(int)
    return df

init_state()
df = load_questions()

# ---- Title ----
categories = list(df["Category"].unique())
levels = sorted(df["Level"].unique())

# ---------- HEADER ROW (Categories) ----------
header_cols = st.columns(len(categories))
for col, cat in zip(header_cols, categories):
    with col:
        st.markdown(
            f'<div class="category-header">{cat}</div>',
            unsafe_allow_html=True,
        )

st.write("")  # small spacer

# ---------- MONEY TILES ----------
for lvl in levels:
    row_cols = st.columns(len(categories))
    for col, cat in zip(row_cols, categories):
        with col:
            # Find question for this category + level
            mask = (df["Category"] == cat) & (df["Level"] == lvl)
            if not mask.any():
                st.write("")  # no question for this cell
                continue

            idx = df[mask].index[0]
            cell_key = (cat, lvl)
            label = f"${lvl * 100}"

            if cell_key in st.session_state.used_cells:
                # Already played → show red tile, not clickable
                st.markdown(
                    f'<div class="used-money-tile">{label}</div>',
                    unsafe_allow_html=True,
                )
            else:
                # Clickable money button
                if st.button(label, key=f"{cat}-{lvl}"):
                    st.session_state.current_question_idx = int(idx)
                    st.session_state.used_cells.add(cell_key)
                    st.switch_page("pages/question_view.py")
