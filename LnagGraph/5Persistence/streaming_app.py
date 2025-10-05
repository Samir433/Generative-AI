import streamlit as st
from langchain_core.messages import BaseMessage, HumanMessage
from utils.langgraph_backend import chatbot

CONFIG = {
    "configurable": {'thread_id': '1'}
}
# st.title("Chat with AI")
if "message_history" not in st.session_state:
    st.session_state['message_history'] = []

for msg in st.session_state['message_history']:
    with st.chat_message(msg['role']):
        st.text(msg['content'])

user_input = st.chat_input("Your message here...")
if user_input:
    st.session_state['message_history'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # add ai functionality here
    # response = chatbot.invoke({"messages": [HumanMessage(content=user_input)]}, config=CONFIG)
    # st.session_state['message_history'].append({"role": "assistant", "content": response['messages'][-1].content})
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadat in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode = "messages"
            )
        )
    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})