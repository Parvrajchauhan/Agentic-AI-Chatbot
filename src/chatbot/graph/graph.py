from langgraph.graph import StateGraph,START, END
from src.chatbot.state.state import State
from src.chatbot.Nodes.basic_chatbot_node import BasicChatbotNode
from langgraph.checkpoint.memory import InMemorySaver

class Graph:
    def __init__(self,model):
        self.llm = model
        self.graph =StateGraph(State)
        
    def basic_chatbot_graph(self):
        """
        This function defines a basic chatbot graph
        using the StateGraph class."""
        print("GRAPH CREATED")

        chatbot_node = BasicChatbotNode(self.llm).process
        self.graph.add_node("chatbot", chatbot_node)
        self.graph.add_edge(START, "chatbot")
        self.graph.add_edge("chatbot", END)
        
        checkpointer = InMemorySaver()
        return self.graph.compile(checkpointer=checkpointer)
    
    def setup_graph(self,usecase):
        """
        This function sets up the chatbot graph and returns it.
        """
        if usecase == "Basic Chatbot":
            return self.basic_chatbot_graph()
        else:
            return self.basic_chatbot_graph()
    