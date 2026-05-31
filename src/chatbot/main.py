import streamlit as st
from src.chatbot.Frontend.stremlit.loadui import LoadUI

def load_chatbot_ui():
    load_ui=LoadUI()
    user_controls=load_ui.load_ui()
    
    
    user_message=st.chat_input("Enter your message here.....")