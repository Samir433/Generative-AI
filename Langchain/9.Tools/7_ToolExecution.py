from langchain_core.tools import tool
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv  

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm, verbose=True)

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

model_with_tools = model.bind_tools([multiply])

query = HumanMessage(
    content="What is 3 times 4?"
)
messages = [query]
 
result = model_with_tools.invoke(messages)

messages.append(result)

tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)

result = model_with_tools.invoke(messages)
print(result.content)