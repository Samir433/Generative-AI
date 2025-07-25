from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")  

person = Person("John", 30)
person.say_hello()  
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=250,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

# print(chunks)

print(len(chunks))

for chunk in chunks:
    print(chunk)
    print("-"*100)