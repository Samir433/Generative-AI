from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    model="meta-llama/Meta-Llama-3-8B",
    task="text-generation"
)

result = llm.invoke("What is the capital of India")

print(result)