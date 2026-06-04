import os
import streamlit as st
from src.chatbot.Frontend.config import Config

class LoadUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}
        
    def load_ui(self):
        st.set_page_config(page_title="🔗" + self.config.get_page_title()[0],layout="wide")
        st.title("🔗" + self.config.get_page_title()[0])
        
        with st.sidebar:
            llm_options= self.config.get_llm_options()
            usecase_options=self.config.get_usecase_options()
            
            self.user_controls["llm"]=st.selectbox("Select LLM", options=llm_options)
            
            if(self.user_controls["llm"]=="Groq"):
                model_options=self.config.get_groq_model_options()
                self.user_controls["model"]=st.selectbox("Select model", options=model_options)
                
                self.user_controls["API_KEY"]=st.text_input("API Key",type="password")
                if not self.user_controls["API_KEY"]:
                    st.warning("Please enter your API key to use ChatBot.")
                st.session_state["API_KEY"]=self.user_controls["API_KEY"]
                    
            self.user_controls["usecase"]=st.selectbox("Select Use Case", options=usecase_options)
            
            if self.user_controls["usecase"]=="Chat with WebSearch":
                self.user_controls["TAVILY_API_KEY"]=st.session_state["TAVILY_API_KEY"]=st.text_input("Tavily API Key",type="password")
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your Tavily API key to use Web Search features.")
            
        return self.user_controls