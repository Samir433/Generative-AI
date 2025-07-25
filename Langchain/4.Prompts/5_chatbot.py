from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceEndpoint(
    model="meta-llama/Meta-Llama-3-8B",
    task="text-generation"
)

chat_history = []
chat_history.append(SystemMessage(content='You are a helpful assistant'))

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    print(result)
    chat_history.append(AIMessage(content=result))
print(chat_history)