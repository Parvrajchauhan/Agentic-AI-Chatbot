from langgraph.graph import StateGraph,START, END
from src.chatbot.state.state import State
from src.chatbot.Nodes.basic_chatbot_node import BasicChatbotNode
from src.chatbot.Nodes.chatbot_with_tool_node import ChatbotWithToolNode
from langgraph.checkpoint.memory import InMemorySaver

from src.chatbot.tools.searchTool import get_tool, create_tool_nodes
from langgraph.prebuilt import tools_condition


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
    
    
    def chat_with_websearch_graph(self):
        """
        This function defines a chatbot graph with web search capabilities.
        """
        tools= get_tool()
        tool_nodes=create_tool_nodes(tools)
        llm=self.llm
         
        chatbot_node=ChatbotWithToolNode(llm).create_chatbot(tools)
        
        self.graph.add_node("chatbot", chatbot_node)
        self.graph.add_node("tools", tool_nodes)
        
        self.graph.add_edge(START, "chatbot")
        self.graph.add_conditional_edges("chatbot", tools_condition)
        self.graph.add_edge("tools", "chatbot")
        print("GRAPH CREATED")

        checkpointer = InMemorySaver()
        return self.graph.compile(checkpointer=checkpointer)
    
    def setup_graph(self,usecase):
        """
        This function sets up the chatbot graph and returns it.
        """
        if usecase == "Basic Chatbot":
            return self.basic_chatbot_graph()
        elif usecase == "Chat with WebSearch":
            return self.chat_with_websearch_graph()
        
        return None