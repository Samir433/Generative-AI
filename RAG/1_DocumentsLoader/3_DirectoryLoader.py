from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path=r"D:\NLP_Papers",
    glob="*.pdf", 
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(docs[0].metadata)