import streamlit as st

def sidebar(get_ollama_names, update_model): 
    with st.sidebar:
        with st.expander("⚙️ Model Settings", expanded=True):
            st.selectbox(
                "Select LLM model",
                get_ollama_names(),
                key="selected_model",
                on_change=update_model,
            )
            st.divider()