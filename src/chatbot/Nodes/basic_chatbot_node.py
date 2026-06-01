from src.chatbot.state.state import State

class BasicChatbotNode:
    def __init__(self, model):
        self.llm = model
        
    def process(self, state:State) ->dict:
        """
        This function processes the input state and generates a response using the LLM.
        It takes the conversation history from the state, generates a response, and returns it.
        """
        conversation_history = state["messages"]
        
        # Generate a response using the LLM
        response = self.llm.invoke(conversation_history)
        
        return {"messages": response}