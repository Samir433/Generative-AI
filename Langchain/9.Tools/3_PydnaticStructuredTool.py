from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class Multiplyinput(BaseModel):
    """Input for the multiply tool."""
    a: int = Field(..., description="First number to multiply")
    b: int = Field(..., description="Second number to multiply")

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="multiply",
    description="Multiplies two numbers",
    args_schema=Multiplyinput,
)


result = multiply_tool.invoke({"a": 3, "b": 4})
print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args_schema.model_json_schema())