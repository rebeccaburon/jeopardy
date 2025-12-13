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
            <h2 class="rule-heading">1. Teams</h2>
            <ul>
                <li>For the first question, the team of the youngest person chooses category + level.</li>
                <li>After that, the winning team from the previous question chooses the next category + level.</li>
            </ul>
            <h3>Bidding for First Attempt</h3>
            <ul>
                <li>After the category and level are chosen but before the question is revealed, all teams may bid fake money for the right to answer first.</li>
                <li>Teams may bid up to $500 and the highest bid wins.</strong>.</li>
                <li>If multiple teams bid $500 → Rock–Paper–Scissors decides the winner..</li>
                <li>If the first team answers incorrectly → they take a punish sip and the question opens to all teams, and we roll a dice for who answers next.</li>
                <li>All teams must write answers down.</li>
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
            <h2 class="rule-heading">2. Money System</h2>
            <ul>
                <li>Level 1 → <strong>$100</strong></li>
                <li>Level 2 → <strong>$200</strong></li>
                <li>Level 3 → <strong>$300</strong></li>
                <li>Level 4 → <strong>$400</strong></li>
                <li>Level 5 → <strong>$500</strong></li>
            </ul>
            <h3>Categories & Questions </h3>
            <ul>
                <li>Correct answer = money earned</li>
                <li>Wrong answer = no money</li>
            </ul>
        </div>

        <div class="rule-card">
            <h2 class="rule-heading">3. Lifeline — Half the Risk</h2>
            <ul>
                <li>Each team has one lifeline.</li>
                <li>If they win a bidding round and activate it → they only pay <strong>half</strong> of their bid.</li>
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
            <h2 class="rule-heading">4. Sabotage System</h2>
            <h3 class="rule-subheading">Silence Spell — $150</h3>
            <ul>
                <li>Silence 1 player on another team for one round.</li>
                <li>If they speak → <strong>their team loses $300</strong>.</li>
            </ul>
            <h3 class="rule-subheading"> Money Freeze — $200</h3>
            <ul>
                <li>Freeze another team’s earnings for one question.</li>
                <li>Even if they’re correct → they earn <strong>$0</strong>.</li>
            </ul>
        </div>
        <div class="rule-card">
            <h2 class="rule-heading">5. Broke But Not Out</h2>
            <ul>
                <li>If a team reaches $0:</li>
            </ul>
            <ul class="nested-list">
                <li>They cannot bid.</li>
                <li>They cannot buy sabotage.</li>
                <li>They <strong>can still answer</strong> open questions.</li>
            </ul>
            <p>They are not eliminated — only struggling.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if st.button("Start Game", key="button"):
        st.switch_page("pages/game_board.py")