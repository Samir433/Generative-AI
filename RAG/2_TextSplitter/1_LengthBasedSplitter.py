from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"D:\NLP_Papers\Transformer.pdf")

doc = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
      separator=''
)

chunks = splitter.split_documents(doc)


# print(f"Total Chunks: {len(chunks)}")
print(f"First Chunk: {chunks[0].page_content[:100]}...")  # Display first 100 characters of the first chunk