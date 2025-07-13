from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Samir"
    age: int 
    city: Optional[str] = None
    email: EmailStr = 'samir@gmail.com'
    cgpa: float = Field(default=9.0, ge=0, le=10, description="The CGPA of the student")

Student1 = {'age':'25', 'cgpa':9.999}

student = Student(**Student1)

student_dict = dict(student)
print(student_dict)

student_json = student.model_dump_json()
print(student_json)






