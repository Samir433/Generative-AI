from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceEndpoint(
    model="meta-llama/Meta-Llama-3-8B",
    task="text-generation"
)

chat_history = []

while True:
    user_input = input("You: ")
    # chat_history.append({"role": "USER", "content": user_input})
    if user_input.lower() == "exit":
        break
    result = model.invoke(user_input)
    print(result)
    # chat_history.append({"role": "AI", "content": result})