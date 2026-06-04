from src.chatbot.state.state import State
from langchain_core.messages import SystemMessage


SYSTEM_PROMPT = SystemMessage(content="""You are a helpful assistant with access to web search.
You MUST use the web_search tool when the user asks about:
- Current weather
- Latest news
- Stock prices
- Any real-time or recent information

Do not answer these from memory. Always call the tool first.""")

class ChatbotWithToolNode:
    def __init__(self, model):
        self.llm = model
        
    def process(self, state:State) ->dict:
        """
        This function processes the input state and generates a response using the LLM.
        It takes the conversation history from the state, generates a response, and returns it.
        """
        user_input =state["messages"][-1]  if state["messages"] else ""
        llm_response = self.llm.invoke({"role": "user", "content": user_input})
        
        tools_response =f"Tool response based on {user_input}"
        
        return {"messages": [llm_response, tools_response]}
    

    def create_chatbot(self, tools):
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            messages = [SYSTEM_PROMPT] + state["messages"]
            response = llm_with_tools.invoke(messages)

            print("\nTOOL CALLS:", response.tool_calls)
            return {"messages": [response]}

        return chatbot_node

        return chatbot_node