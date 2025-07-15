"""
Author: Joshan John
contact: joshanjohn2003@gmail.com
subjected to copyright@2025
"""

import streamlit as st
from utils.get_models import get_ollama_names
from src.workflows.workflow import WorkFlow


def update_model():
    st.session_state.model = st.session_state.selected_model


def init_workflow(llm_model: str):
    return WorkFlow(llm=llm_model)


def main():
    col1, col2 = st.columns([3, 1])

    # Initialize model and dropdown selection
    if "model" not in st.session_state:
        default_model = get_ollama_names()[0]
        st.session_state.model = default_model

    if "selected_model" not in st.session_state:
        st.session_state.selected_model = st.session_state.model

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # UI - Left: Title + Model info
    with col1:
        st.title("Cllama")
        st.write(f"Current model: `{st.session_state.model}`")

    # UI - Right: Model selector
    with col2:
        st.selectbox(
            "Select LLM model",
            get_ollama_names(),
            key="selected_model",
            on_change=update_model,
        )

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    prompt = st.chat_input("Ask me...")

    if prompt:
        # Show user input
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Process AI response
        with st.spinner("AI is typing..."):
            workflow = init_workflow(st.session_state.model)
            response = workflow.invoke(prompt)

        # Show assistant response
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Author credit footer at bottom-right
    st.markdown(
        """
        <style>
        .footer-credit {
            position: fixed;
            bottom: 8px;
            right: 16px;
            font-size: 12px;
            color: gray;
            z-index: 9999;
        }
        .footer-credit a {
            color: yellow;
            text-decoration: none;
            font-size: 14px;
        }
        </style>
        <div class="footer-credit">
            Author <a href="https://github.com/joshanjohn" target="_blank">Joshan John</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
