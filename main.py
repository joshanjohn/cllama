import streamlit as st
from streamlit_option_menu import option_menu

# ---- CONFIG ----
st.set_page_config(page_title="Card Navigation App", layout="wide")

# ---- SIDEBAR MENU ----
with st.sidebar:
    selected = option_menu(
        "Navigation",
        ["Home", "Page 1", "Page 2", "Page 3", "Page 4"],
        icons=["house", "1-circle", "2-circle", "3-circle", "4-circle"],
        menu_icon="list",
        default_index=0,
    )

# ---- MAIN CONTENT ----
if selected == "Home":
    st.markdown("<h2 style='text-align:center;'>Choose a Page</h2>", unsafe_allow_html=True)

    cols = st.columns(4, gap="large")

    # Four cards in center
    with cols[0]:
        if st.button("Page 1", use_container_width=True):
            st.session_state['selected'] = "Page 1"
    with cols[1]:
        if st.button("Page 2", use_container_width=True):
            st.session_state['selected'] = "Page 2"
    with cols[2]:
        if st.button("Page 3", use_container_width=True):
            st.session_state['selected'] = "Page 3"
    with cols[3]:
        if st.button("Page 4", use_container_width=True):
            st.session_state['selected'] = "Page 4"

elif selected == "Page 1":
    st.title("📘 Page 1")
    st.write("Welcome to Page 1 content")

elif selected == "Page 2":
    st.title("📙 Page 2")
    st.write("Welcome to Page 2 content")

elif selected == "Page 3":
    st.title("📗 Page 3")
    st.write("Welcome to Page 3 content")

elif selected == "Page 4":
    st.title("📕 Page 4")
    st.write("Welcome to Page 4 content")
