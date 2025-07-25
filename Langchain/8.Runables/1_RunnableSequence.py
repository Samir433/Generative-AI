from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="Write nice joke about {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Explain the meaning of the joke-{joke}",
    input_variables=["joke"]
)

parser = StrOutputParser()

chain = RunnableSequence(template1, model, parser, template2, model, parser)
    
print(chain.invoke({"topic": "cats"}))







