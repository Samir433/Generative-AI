from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample_pdf.pdf")

docs = loader.load()
for doc in docs:
    print(doc.page_content)
    print("-"*200)
    print(doc.metadata)
    print("-"*200)







