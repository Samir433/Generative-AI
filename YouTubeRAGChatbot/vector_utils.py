from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

splitter = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=100)

def build_vector_store(transcript: str, cache_folder: str, model_name: str):
    docs = splitter.create_documents([transcript])
    embeddings = HuggingFaceEmbeddings(model_name=model_name, cache_folder=cache_folder)
    return FAISS.from_documents(docs, embeddings)


def get_retriever(vector_store, k: int = 4):
    return vector_store.as_retriever(search_type="similarity", search_kwargs={"k": k})