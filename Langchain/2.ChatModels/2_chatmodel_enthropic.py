from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model_name="claude-2", timeout=60, stop=None)

result = model.invoke("Hello, how are you?")
print(result.content)