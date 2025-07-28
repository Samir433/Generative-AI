from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

class MathToolkit:
    """Toolkit for mathematical operations."""
    def get_tools(self):
        """Return the tools in this toolkit."""
        return [multiply, add]  
    
tools = MathToolkit().get_tools()
for tool in tools:
    print(f"Tool Name: {tool.name}, Description: {tool.description}")