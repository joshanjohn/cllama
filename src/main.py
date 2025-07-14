import streamlit as st
from utils.get_models import get_ollama_names
from llm import LLM


def update_model():
    st.session_state.model = st.session_state.selected_model


col1, col2 = st.columns([3, 1])

if "model" not in st.session_state:
    default_model = get_ollama_names()[0]
    st.session_state.model = default_model

# Initialize chat history in session state if not present
if "messages" not in st.session_state:
    st.session_state.messages = []


with col1:
    st.title("Cllama")
    st.write(f"current model : {st.session_state.model}")

with col2:
    st.selectbox(
        "Select LLM model",
        get_ollama_names(),
        key="selected_model",  # Bind widget state
        on_change=update_model,  # Call function on change
    )

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("whats up")

if prompt:
    # Show user's message immediately
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Show a spinner while waiting for the AI response
    with st.spinner("AI is typing..."):
        llm = LLM(model=st.session_state.model)
        response = llm.run(prompt)

    # Show assistant's response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
