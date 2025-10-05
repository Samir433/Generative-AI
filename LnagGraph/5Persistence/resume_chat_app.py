import streamlit as st
from langchain_core.messages import HumanMessage
from utils.langgraph_backend import chatbot 
from uuid import uuid4

# ************************** utility functions **************************
def generate_thread_id():
    return str(uuid4())

def save_thread_history(thread_id, history):
    st.session_state['thread_message_histories'][thread_id] = history

def reset_chat():
    save_thread_history(st.session_state['thread_id'], st.session_state['message_history'])
    st.session_state['thread_id'] = generate_thread_id()
    if st.session_state['thread_id'] not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(st.session_state['thread_id'])
    st.session_state['message_history'] = []
    
# ********************** Session Setup **********************************
if "message_history" not in st.session_state:
    st.session_state['message_history'] = []

if "thread_id" not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state['chat_threads'] = [st.session_state['thread_id']]

if 'thread_message_histories' not in st.session_state:
    st.session_state['thread_message_histories'] = {}

# ****************************ADD SIDE BAR CHATBOT****************************
st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("Chat History")

for thread in reversed(st.session_state['chat_threads']):
    messages = st.session_state['thread_message_histories'].get(thread, [])
    
    title = "New Chat"
    
    if messages:
        first_user_message = next((msg['content'] for msg in messages if msg['role'] == 'user'), None)
        if first_user_message:
            title = first_user_message[:35] + '...' if len(first_user_message) > 35 else first_user_message

    if st.sidebar.button(title, key=thread):
        st.session_state['thread_id'] = thread
        st.session_state['message_history'] = messages

# **************************** Main Chat Interface ****************************
for msg in st.session_state['message_history']:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# Handle user input
user_input = st.chat_input("Your message here...")
if user_input:
    st.session_state['message_history'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    CONFIG = {"configurable": {'thread_id': st.session_state['thread_id']}}
    
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadat in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode = "messages"
            )
        )
    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})
    
    # FIX 3: Save the history of the current thread after every message
    save_thread_history(st.session_state['thread_id'], st.session_state['message_history'])