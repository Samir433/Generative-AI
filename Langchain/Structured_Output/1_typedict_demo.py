from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    city: str

person = Person(name='Samir', age=20, city='Pune')
print(person)







