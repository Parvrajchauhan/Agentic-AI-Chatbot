import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnableConfig


class DisplayResult:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display(self):
        if self.usecase == "Basic Chatbot":
            config: RunnableConfig = {
                "configurable": {"thread_id": "1"}
            }

            with st.chat_message("user"):
                st.write(self.user_message)

            for event in self.graph.stream(
                {"messages": ("user", self.user_message)},
                config
            ):
                for value in event.values():

                    msg = value.get("messages")

                    if isinstance(msg, AIMessage):
                        with st.chat_message("assistant"):
                            st.write(msg.content)
            state = self.graph.get_state(config)

            print("CURRENT STATE:")
            print(state.values)