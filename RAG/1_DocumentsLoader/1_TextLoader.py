from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-9b-it",
    task = "text-generation"
)

model = ChatHuggingFace(
    llm = llm,
    max_tokens = 100
)
parser = StrOutputParser()

prompt = PromptTemplate(
    template = "What is the main idea of the following text: {text}",
    input_variables = ["text"]
)


loader = TextLoader("sample.txt", encoding="utf-8")
docs = loader.load()

# print(type(docs))
# print(docs[0].page_content)
# print(len(docs))

chain = prompt | model | parser
print(chain.invoke({"text": docs[0].page_content}))




