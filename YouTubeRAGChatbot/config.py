import os

class Config:
    HF_CACHE = os.getenv("HF_CACHE", "./hf_cache")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    LLM_REPO = os.getenv("LLM_REPO", "google/gemma-2-2b-it")
    LLM_TASK = os.getenv("LLM_TASK", "text-generation")