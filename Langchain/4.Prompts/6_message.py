from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceEndpoint(
    model="meta-llama/Meta-Llama-3-8B",
    task="text-generation"
)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="What is the capital of France?")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result))
print(messages)
