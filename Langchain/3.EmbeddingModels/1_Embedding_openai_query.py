from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv 

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=64, chunk_size=1000)

result = embedding.embed_query("GDP of India in 2023 is 3.73 trillion USD")
print(str(result))