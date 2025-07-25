from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
# Hello World

This is a test of the markdown splitter.

## Subheading

This is a test of the markdown splitter.
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

for chunk in chunks:
    print(chunk)
    print("-"*100)





