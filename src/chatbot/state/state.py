from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
State represents the current state of the chatbot, 
including the conversation history and any relevant
context. It is used to maintain the flow of the 
conversation and provide necessary information for
generating responses.
    """
    
    messages: Annotated[List, add_messages]