from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
import requests
from dotenv import load_dotenv
import os

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_STACK_API_KEY")

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm, verbose=True)

search_tool = DuckDuckGoSearchResults()

@tool
def fetch_weather(city: str) -> str:
    """Fetch the current weather for a given city."""
    url = f"https://api.weatherstack.com/current?access_key={WEATHER_API_KEY}&query={city}"
    response = requests.get(url)

    return response.json()

# Step 2: Pull the ReAct prompt from LangChain Hub
prompt = hub.pull("hwchase17/react")  # pulls the standard ReAct agent prompt

# Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=model,
    tools=[search_tool, fetch_weather],
    prompt=prompt
)

# Step 4: Wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, fetch_weather],
    verbose=True
)

# Step 5: Invoke
response = agent_executor.invoke({"input": "Find the capital of Madhya Pradesh, then find it's current weather condition"})
print(response)

print(response['output'])

# Step 6: Test the weather fetching tool