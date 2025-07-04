from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI chat model
model = ChatOpenAI(model="gpt-4", temperature=0.7, max_completion_tokens=400)

# Example usage of the chat model
result = model.invoke("Hello, how are you?")
print(result.content)