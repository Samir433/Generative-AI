from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

# Define the input schema for the multiply tool
class MultiplyInput(BaseModel):
    """Input for the multiply tool."""
    a: int = Field(..., description="First number to multiply")
    b: int = Field(..., description="Second number to multiply")

# Define the tool class for multiplying two numbers
class MultiplyTool(BaseTool):
    """Tool to multiply two numbers."""

    name: str = "multiply"
    description: str = "Multiplies two numbers"
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        """Multiply two numbers."""
        return a * b

multiply_tool = MultiplyTool()

# Example usage of the multiply tool
result = multiply_tool.invoke({"a": 3, "b": 4})
print(result)  # Output: 12
print(multiply_tool.name)  # Output: multiply
    
