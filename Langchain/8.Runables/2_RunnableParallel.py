from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.schema.runnable import RunnableParallel, RunnableSequence
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "Generate the short tweet for the following topic: {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Generate the short linkedin post for the following topic: {topic}",
    input_variables = ["topic"]
)

Tweet = RunnableSequence(prompt1, model, parser)
Linkedin = RunnableSequence(prompt2, model, parser)

parallel_chain = RunnableParallel({
    "tweet": Tweet,
    "linkedin": Linkedin
})

result = parallel_chain.invoke({"topic": "The future of AI"})

print(result)



