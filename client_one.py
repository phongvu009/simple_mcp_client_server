from smolagents import ToolCollection
from smolagents.mcp_client import MCPClient
from mcp.client.stdio import StdioServerParameters


# connect to local server via Stdio
server_parameters = StdioServerParameters(command="uv", args=["run", "server.py"])

with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tools:
    print("\n".join(f"{tool.name}: {tool.description}" for tool in tools.tools))


# Connect Other MCP server
with MCPClient(
    {"url": "https://abidlabs-mcp-tools.hf.space/gradio_api/mcp/sse"}
) as tools:
    # list tools
    print("\n".join(f"{t.name} - descripton: {t.description}" for t in tools))
