from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda, RunnableSequence, RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",  
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()


prompt = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables = ["topic"] 
)

joke_gen = RunnableSequence(prompt, model, parser)

def word_count(text):
    return len(text.split())

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(lambda x : len(x.split()))
})

final_chain = RunnableSequence(joke_gen, parallel_chain)

result = final_chain.invoke({"topic": "AI"})
print(result)






