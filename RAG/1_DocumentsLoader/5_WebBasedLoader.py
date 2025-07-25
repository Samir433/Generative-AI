from langchain_community.document_loaders import WebBaseLoader

url = "https://wordpress.com/discover"

loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)

