from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# Initialize the OpenAI chat model
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.7)


# Example usage of the chat model
result = llm.invoke("Hello, how are you?")
print(result)