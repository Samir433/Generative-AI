from langchain.schema.runnable import RunnableLambda

def word_count(text):
    return len(text.split())

word_count_runnable = RunnableLambda(word_count)

text = "Samir is a talented AI engineer"

print(word_count_runnable.invoke(text))





