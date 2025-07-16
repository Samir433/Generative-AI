from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

template = PromptTemplate(
    template="What is the capital of {country}?",
    input_variables=["country"]
)

chain = template | model

print(chain.invoke({"country": "India"}))