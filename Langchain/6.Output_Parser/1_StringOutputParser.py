from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    model="mistralai/Devstral-Small-2507",  
    task="text-generation"
)

template1 = PromptTemplate(
    template="Tell me about this {country} in 100 words?",
    input_variables=["country"]
)

template2 = PromptTemplate(
    template="Summarize the given text in only 3 lines{text}?",
    input_variables=["text"]
)

# without string output parser
# prompt1 = template1.format(country="India")
# text = llm.invoke(prompt1)

# prompt2 = template2.format(text=text)
# print(llm.invoke(prompt2))

# with string output parser

parser = StrOutputParser()

chain = template1 | llm | parser | template2 | llm | parser
print(chain.invoke({"country": "India"}))