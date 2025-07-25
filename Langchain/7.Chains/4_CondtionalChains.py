from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

# model = ChatOpenAI(model="gpt-3.5-turbo")

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

parser = StrOutputParser()

model = ChatHuggingFace(llm=llm)

class Feedback(BaseModel):
    Sentiment: Literal["Negative", "Positive"] = Field(description="The sentiment of the feedback. Must be either 'Negative' or 'Positive'.")

pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template=(
        "Classify the sentiment of the following feedback as either 'Positive' or 'Negative'.\n"
        "Respond ONLY with a valid JSON object as per the following format:\n"
        "{format_instructions}\n"
        "Feedback: {text}"
    ),
    input_variables=["text"],
    partial_variables={"format_instructions": pydantic_parser.get_format_instructions()}
)

classifier_chain = prompt1 | model | pydantic_parser

prompt2 = PromptTemplate(
    template="Write an appropriate response for the positive feedback: {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Write an appropriate response for the negative feedback: {feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
   (lambda x: x.Sentiment == "Positive", prompt2 | model | parser),
   (lambda x: x.Sentiment == "Negative", prompt3 | model | parser),
   RunnableLambda(lambda x: "No response needed" if getattr(x, "Sentiment", None) == "Neutral" else None)
)

chain = classifier_chain | branch_chain

result = chain.invoke({"text": "I am very frustrated with the service"})
print(result)