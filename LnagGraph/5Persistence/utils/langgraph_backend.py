from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages

from typing import TypedDict, Literal, Annotated
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, BaseMessage
from dotenv import load_dotenv
import os

load_dotenv()

gemini = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5
)
class SimpleState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages()]

def response_generator(state: SimpleState) -> SimpleState:
    messages = state['messages']
    response = gemini.invoke(messages)
    return {"messages": response.content}

#define the graph
graph = StateGraph(SimpleState)
graph.add_node("response_generator", response_generator)

#add adges
graph.add_edge(START, "response_generator")
graph.add_edge("response_generator", END)

#configure the checkpoint saver
saver = InMemorySaver()

#compile the graph with checkpointer
chatbot = graph.compile(checkpointer=saver)