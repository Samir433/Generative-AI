from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

response_schemas = [
    ResponseSchema(name="Capital", description="Captial of the country"),
    ResponseSchema(name="Fincial Capital", description="Financial Capital of the country"),
    ResponseSchema(name="Population", description="Population of the country"),
]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

template = PromptTemplate(
    template="You are a helpful assistant that can answer questions about the countries and their capitals. /n {format_instructions} /n {country}",
    input_variables=["country"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()}
)

# prompt = template.format(country="India")

# result = model.invoke(prompt)

# print(result.content)

chain = template | model | output_parser
print(chain.invoke({"country": "India"}))