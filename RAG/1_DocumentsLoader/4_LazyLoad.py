from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path=r"D:\NLP_Papers",
    glob="*.pdf", 
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for doc in docs:
    print(doc.page_content)
    print("-"*200)






