import os
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")

try:
    # Initialize the embedding model
    embedding = OpenAIEmbeddings(
        model="text-embedding-3-small",
        dimensions=64,  # Adjust as needed
    )
    # Load the document
    documents = [
        "GDP of India in 2023 is 3.73 trillion USD",
        "GDP of China in 2023 is 18.33 trillion USD",
        "GDP of USA in 2023 is 25.72 trillion USD",
        "GDP of Japan in 2023 is 5.11 trillion USD",
        "GDP of Germany in 2023 is 4.38 trillion USD",
    ]
    # Embed the documents   
    result = embedding.embed_documents(documents)
    print(result)
except Exception as e:
    print(f"An error occurred: {e}") 