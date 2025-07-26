# main.py
import streamlit as st
from dotenv import load_dotenv
from config import Config
from transcript_utils import extract_video_id, fetch_transcript
from vector_utils import build_vector_store, get_retriever
from qa_pipeline import run_qa

# Load environment variables
load_dotenv()

st.set_page_config(page_title="YouTube Video Chat-QA", layout="centered")
st.title("YouTube Video Chat-QA App")

# Initialize session state
if 'ready' not in st.session_state:
    st.session_state.ready = False
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Setup section for video link
with st.expander("Setup Video", expanded=not st.session_state.ready):
    url = st.text_input("YouTube Video Link", key='input_url')
    if st.button("Submit Link"):
        vid = extract_video_id(url)
        if not vid:
            st.error("Invalid YouTube URL.")
        else:
            st.session_state.video_id = vid
            st.session_state.ready = True

# Chat interface after video is ready
def chat_interface():
    st.video(f"https://www.youtube.com/watch?v={st.session_state.video_id}")
    # Input new message
    new_q = st.chat_input("Ask a question about this video...")
    if new_q:
        st.session_state.messages.append({'role': 'user', 'content': new_q})
        transcript = fetch_transcript(st.session_state.video_id, languages=["en", "hi"])
        if not transcript:
            st.session_state.messages.append({'role': 'assistant', 'content': "Transcript not available."})
        else:
            vector_store = build_vector_store(transcript, Config.HF_CACHE, Config.EMBEDDING_MODEL)
            retriever = get_retriever(vector_store)
            answer = run_qa(retriever, new_q)
            st.session_state.messages.append({'role': 'assistant', 'content': answer})

    # Display chat history
    for msg in st.session_state.messages:
        st.chat_message(msg['role']).write(msg['content'])

    if st.button("Exit Chat"):
        for key in ['ready', 'video_id', 'messages', 'input_url']:
            if key in st.session_state:
                del st.session_state[key]

if st.session_state.ready:
    chat_interface()