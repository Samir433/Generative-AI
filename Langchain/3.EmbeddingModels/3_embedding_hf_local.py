from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    cache_folder="D:/huggingface_cache"
)

result = embedding.embed_query("GDP of India in 2023 is 3.73 trillion USD")
# print(result)

documents = [
    "GDP of India in 2023 is 3.73 trillion USD",
    "GDP of China in 2023 is 18.33 trillion USD",
    "GDP of USA in 2023 is 25.72 trillion USD",
    "GDP of Japan in 2023 is 5.11 trillion USD",
    "GDP of Germany in 2023 is 4.38 trillion USD",
]

embeddings = embedding.embed_documents(documents)
print(embeddings)