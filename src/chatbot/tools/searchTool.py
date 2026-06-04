from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
import streamlit as st

def get_tool():
    """Return the list of tools to be used by the agent."""
    tavily_api_key = st.session_state.get("TAVILY_API_KEY")
    tools= [TavilySearchResults(max_results=3,tavily_api_key=tavily_api_key)]
    
    return tools



def create_tool_nodes(tools):
    return ToolNode(tools)