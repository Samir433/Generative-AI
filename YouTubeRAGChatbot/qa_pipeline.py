from config import Config
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate

# Initialize LLM endpoint & chat wrapper
llm = HuggingFaceEndpoint(repo_id=Config.LLM_REPO, task=Config.LLM_TASK)
model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="""
    You are a helpful assistant.
    Answer ONLY from provided transcript context.
    If context is insufficient, say you don't know.

    {context}
    Question: {question}
    """,
    input_variables=["context", "question"]
)

def run_qa(retriever, question: str) -> str:
    docs = retriever.invoke(question)
    context = "\n\n".join(d.page_content for d in docs)
    final = prompt.invoke({"context": context, "question": question})
    return model.invoke(final).content