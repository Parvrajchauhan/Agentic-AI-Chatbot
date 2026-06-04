import streamlit as st
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    ToolMessage,
    BaseMessage,
)
from langchain_core.runnables import RunnableConfig


class DisplayResult:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def _render_message(self, msg: BaseMessage):

        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)

        elif isinstance(msg, AIMessage):
            if msg.content:
                with st.chat_message("assistant"):
                    st.write(msg.content)

        elif isinstance(msg, ToolMessage):
            with st.chat_message("assistant"):
                st.caption(f"🔧 Tool: {msg.name}")
                st.write(msg.content)

    def _run_and_collect(self, config: RunnableConfig):

        initial_state = {
            "messages": [
                HumanMessage(content=self.user_message)
            ]
        }

        for event in self.graph.stream(
            initial_state,
            config=config
        ):
            print("EVENT:", event)

        state = self.graph.get_state(config)

        print("\nCURRENT STATE:")
        print(state.values)

        return state.values.get("messages", [])

    def display(self):

        config: RunnableConfig = {
            "configurable": {
                "thread_id": "1"
            }
        }

        messages = self._run_and_collect(config)

        for msg in messages:
            self._render_message(msg)