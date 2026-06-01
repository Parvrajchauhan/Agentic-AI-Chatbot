import streamlit as st
from src.chatbot.Frontend.stremlit.loadui import LoadUI
from src.chatbot.LLMs.groqllm import GroqLLM
from src.chatbot.graph.graph import Graph
from src.chatbot.Frontend.stremlit.display_result import DisplayResult  

def load_chatbot_ui():
    load_ui=LoadUI()
    user_controls=load_ui.load_ui()
    
    
    user_message=st.chat_input("Enter your message here.....")
    
    if user_message:
        try:
            llm=GroqLLM(user_controls).get_llm()
            
            if not llm:
                st.error("Failed to initialize the LLM. Please check your API key and model selection.")
                return
            usecase=user_controls["usecase"]
            if not usecase:
                st.error("No use case selected.")
                return
            graph=Graph(llm)
             
            chatbot=graph.setup_graph(usecase)
            DisplayResult(usecase,chatbot,user_message).display()
            if not chatbot:
                st.error("Failed to set up the chatbot graph.")
                return
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return