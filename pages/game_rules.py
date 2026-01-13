import streamlit as st
from pathlib import Path
from utils.loader import load_css

# Use wide layout (if not already set in app.py)
st.set_page_config(layout="wide")

# ---- Load SS ----

load_css()

# ---- Title ----
st.markdown('<div class="rule-page-title">📜 GAME RULES</div>', unsafe_allow_html=True)

# ---- 3 columns ----
col1, col2, col3 = st.columns(3, gap="large")

# ---------- COLUMN 1 ----------
with col1:
    st.markdown(
        """
        <div class="rule-card">
            <h2 class="rule-heading">Teams</h2>
            <ul>
                <li>For the first question, the team of the youngest person chooses category + level.</li>
                <li>After that, the winning team from the previous question chooses the next category + level.</li>
                <li>To answer a questoin, each team gets 1 minut pr question.</li>
                <li>The game has a <strong>unknown timer</strong>. When time is up, the game ends immediately, and each team needs to count their money.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- COLUMN 2 ----------
with col2:
    st.markdown(
        """
        <div class="rule-card">
            <h2 class="rule-heading">Money System</h2>
            <ul>
            <p>Each team starts with <strong>$1000</strong></p>
                <li>Level 1 → <strong>$100</strong></li>
                <li>Level 2 → <strong>$200</strong></li>
                <li>Level 3 → <strong>$300</strong></li>
                <li>Level 4 → <strong>$400</strong></li>
                <li>Level 5 → <strong>$500</strong></li>
            </ul>
            <h3>Categories & Questions </h3>
            <ul>
                <li>Correct answer = <strong>Money</strong> earned</li>
                <li>Wrong answer = No <strong>money</strong> , and the next (clockwise) team is allowed to asnwer</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- COLUMN 3 ----------
with col3:
    st.markdown(
        """
        <div class="rule-card">
            <h2 class="rule-heading">Sabotage System</h2>
            <p>A team may sabotage only on their turn, and before choosing a question.</p>
            <p>You may: <strong>Buy ONE</strong> sabotage, or skip it.</p>
            <h3 class="rule-subheading">Silence Spell — $500</h3>
            <ul>
                <li>Silence a team for one round.</li>
                <li>If they speak → <strong>Their team loses $200</strong>.</li>
            </ul>
            <h3 class="rule-subheading">Money Freezze — $600</h3>
             <ul>
                <li>Freeze another team’s money for their next question.</li>
                <li>This mean that they can not spend or earn any money</strong>.</li>
            </ul>
             </ul>
            <h3 class="rule-subheading">Time Pressure — $300</h3>
             <ul>
                <li>The targeted team has <strong>half the normal time, meaning 30 sec</strong> to answer their next question</li>
                <li>If time runs out → the next (clockwise) team is allowed to asnwer.</li>
            </ul>
            
        </div>
        """,
        unsafe_allow_html=True,
    )

if st.button("Start Game", key="button"):
        st.switch_page("pages/game_board.py")