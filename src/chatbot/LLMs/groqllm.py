import os
import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self, user_controls):
        self.user_controls = user_controls
        
    def get_llm(self):
        try:
            groq_api_key=self.user_controls["API_KEY"]
            model=self.user_controls["model"]
            print("API KEY:", groq_api_key)
            print("MODEL:", model)
            if groq_api_key=='' and os.environ["GROQ_API_KEY"]=='':
                st.error("Please Enter the Groq API KEY")
                
            llm=ChatGroq(api_key=groq_api_key,model=model)
            
        except Exception as e:
            st.error(f"Error creating LLM: {e}")
            raise
        return llm