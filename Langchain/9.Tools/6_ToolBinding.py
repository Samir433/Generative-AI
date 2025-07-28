from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from pydantic import BaseModel, Field
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",
    task="text-generation"
)

chat = ChatHuggingFace(llm=llm, verbose=True)

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

chat_with_tools = chat.bind_tools([multiply])

result = chat_with_tools.invoke("What is 3 times 4?")

print(result)  # Output: 12