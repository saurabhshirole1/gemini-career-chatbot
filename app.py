import streamlit as st
from services.gemini_service import generate_response
from services.memory_service import add_message
from prompts.system_prompt import SYSTEM_PROMPT

st.set_page_config(page_title="AI Career Advisor", page_icon="💼")

st.title("💼 AI Career Advisor Chatbot")
st.write("Your personal AI mentor for career growth and interview preparation.")

# Initialize session memory
if "memory" not in st.session_state:
    st.session_state.memory = []

# Display chat history
for msg in st.session_state.memory:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask your career-related question...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.memory = add_message(
        st.session_state.memory,
        "user",
        user_input
    )

    # Generate response with spinner
    with st.spinner("Thinking..."):
        response = generate_response(user_input, st.session_state.memory)

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.memory = add_message(
        st.session_state.memory,
        "assistant",
        response
    )