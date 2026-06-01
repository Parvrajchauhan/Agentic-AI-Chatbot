import streamlit as st
from src.chatbot.Frontend.stremlit.loadui import LoadUI
from src.chatbot.LLMs.groqllm import GroqLLM
from src.chatbot.graph.graph import Graph
from src.chatbot.Frontend.stremlit.display_result import DisplayResult
from langchain_core.messages import HumanMessage, AIMessage


def load_chatbot_ui():

    load_ui = LoadUI()
    user_controls = load_ui.load_ui()

    # Require API key
    if not user_controls.get("API_KEY"):
        st.info("Enter your Groq API key to start chatting.")
        return

    # Create LLM once
    if "llm" not in st.session_state:
        st.session_state.llm = GroqLLM(user_controls).get_llm()

    # Create graph once
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = Graph(
            st.session_state.llm
        ).setup_graph(user_controls["usecase"])

    chatbot = st.session_state.chatbot

    config = {
        "configurable": {
            "thread_id": "1"
        }
    }

    # Display full history
    state = chatbot.get_state(config)

    messages = state.values.get("messages", [])

    for msg in messages:

        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)

        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    # New input
    user_message = st.chat_input("Enter your message here.....")

    if user_message:
        try:
            DisplayResult(
                user_controls["usecase"],
                chatbot,
                user_message
            ).display()

            st.rerun()

        except Exception as e:
            st.error(f"An error occurred: {e}")