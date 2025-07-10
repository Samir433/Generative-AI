from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    cache_folder="D:/huggingface_cache"
)


document1 = [
    "GDP of India in 2023 is 3.73 trillion USD",
    "GDP of China in 2023 is 18.33 trillion USD",
    "GDP of USA in 2023 is 25.72 trillion USD",
    "GDP of Japan in 2023 is 5.11 trillion USD",
    "GDP of Germany in 2023 is 4.38 trillion USD",
]

document2 = [
    "Lion is king of the jungle",
    "Mango is King of fruits"
]

document3 = [
    "Narendra Modi is the Prime Minister of India",
    "Donald Trump is the President of USA",
    "Devendra Fadnavis is the Chief Minister of Maharashtra"
]

document4 = [
    "Virat Kohali is From RCB "
    "Rohit Sharma is From MI",
    "MS Dhoni is From CSK",
    "Sachin Tendulkar is From MI",
    "Yuvraj Singh is From RCB",
    "Ravindra Jadeja is From CSK",
    "Hardik Pandya is From MI",
    "K L Rahul is From RCB",
    "Rishabh Pant is From DC",
]


# Combine all documents into a list of lists
all_documents = [document1, document2, document3, document4]
document_names = ["document1", "document2", "document3", "document4"]

# Concatenate each document's texts into a single string for each document
concatenated_docs = [" ".join(docs) for docs in all_documents]

# Embed each concatenated document
doc_embeddings = embedding.embed_documents(concatenated_docs)

# Get query from user or define it here
query = "Who is King of the jungle?"

# Embed the query
query_embedding = embedding.embed_query(query)

# Compute cosine similarity between query embedding and each document embedding
# Reshape for sklearn
query_embedding_np = np.array(query_embedding).reshape(1, -1)
doc_embeddings_np = np.array(doc_embeddings)

similarities = cosine_similarity(query_embedding_np, doc_embeddings_np)[0]

# Find the index of the most similar document
most_similar_idx = np.argmax(similarities)
most_similar_doc_name = document_names[most_similar_idx]
most_similar_score = similarities[most_similar_idx]

print(f"Query: {query}")
print("Similarity scores with each document:")
for name, score in zip(document_names, similarities):
    print(f"{name}: {score:.4f}")

print(f"\nThe query matches most with: {most_similar_doc_name} (score: {most_similar_score:.4f})")