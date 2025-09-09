import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

# Functions
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

# Load model with local caching
model_name = "sentence-transformers/all-MiniLM-L6-v2"
cache_dir = os.path.join(os.getcwd(), "hf_cache")

if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

embedder = SentenceTransformer(model_name, cache_folder=cache_dir)

def create_faiss_index(chunks):
    embeddings = embedder.encode(chunks)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings, dtype=np.float32))
    return index, embeddings

def search_index(query, index, chunks, k=3):
    query_vec = embedder.encode([query])
    D, I = index.search(np.array(query_vec, dtype=np.float32), k)
    return [chunks[i] for i in I[0]]

def ask_gemini(query, retrieved_chunks):
    context = "\n".join(retrieved_chunks)
    prompt = f"Answer based on context:\n{context}\n\nQuestion: {query}"
    response = genai.GenerativeModel("gemini-2.5-flash").generate_content(prompt)
    return response.text

st.title(" PDF Q&A with Gemini + FAISS")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    # Extract and process
    pdf_text = extract_text_from_pdf(uploaded_file)
    chunks = chunk_text(pdf_text)
    index, _ = create_faiss_index(chunks)
    st.success("PDF processed and indexed!")

    # Chat loop
    if "chat_active" not in st.session_state:
        st.session_state.chat_active = True

    if st.session_state.chat_active:
        query = st.text_input("Ask a question about the PDF:")
        if query:
            retrieved = search_index(query, index, chunks)
            answer = ask_gemini(query, retrieved)
            st.write("**Answer:**", answer)

        if st.button("Exit Chat"):
            st.session_state.chat_active = False
            st.warning("Chat ended. Upload a new PDF to start again.")