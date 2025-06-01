# Anthoropic : https://github.com/modelcontextprotocol/python-sdk
from mcp.server.fastmcp import FastMCP

# create instance
mcp = FastMCP("Weather Service")


# Tool Implementation
@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a specified location"""
    return f"Weather in {location} : Sunny, 75F"  # fake fetch


@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource"""
    return f"Weather data for {location}: Sunny, 75F"  # Fake database


# Prompt implemenentation
@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt"""
    return f"""Yow are a weather reporter. Weather report for {location}"""


if __name__ == "__main__":
    # default transportType is stdio
    mcp.run(host="0.0.0.0")
