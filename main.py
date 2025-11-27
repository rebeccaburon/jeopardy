import streamlit as st



def main():

    st.set_page_config(
    page_title=" Quiz Game",
    layout="wide",
)

st.switch_page("pages/game_rules.py")


if __name__ == "__main__":
    main()