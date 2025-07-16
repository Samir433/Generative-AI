from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Country(BaseModel):
    capital: str = Field(description="Capital of the country")
    population: int = Field(description="Population of the country")
    nuclear_power: bool = Field(description="Whether the country has nuclear power")

parser = PydanticOutputParser(pydantic_object=Country)

template = PromptTemplate(
    template="You are a helpful assistant that can answer questions about the countries and their capitals. /n {format_instructions} /n {country}",
    input_variables=["country"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# prompt = template.invoke({"country": "USA"})

# result = model.invoke(prompt)

# print(result.content)

chain = template | model | parser
print(chain.invoke({"country": "USA"}))