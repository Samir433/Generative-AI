from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StrOutputParser
from dotenv import load_dotenv

model = ChatOpenAI(model="gpt-3.5-turbo")

parser = StrOutputParser()

template1 = PromptTemplate(
    template="Give me detailed information about {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Give me a short summary of {text}",
    input_variables=["text"]
)

chain = template1 | model | parser | template2 | model | parser

print(chain.invoke({"topic": "India"}))