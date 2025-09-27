from mcp.server.fastmcp import FastMCP
from src.joke import get_chuck_norris_joke
from typing import Dict, Any
import sys

class MCPServer:
    def __init__(self):
        self.mcp = FastMCP("My first MCP server")
        self._register_tools()

    def _register_tools(self):
        """Register all MCP tools"""

        @self.mcp.tool()
        async def get_chuck_norris_joke_mcp() -> Dict[str, Any]:
            try:
                return get_chuck_norris_joke()
            except Exception as e:
                print(e)
                return {}

    def run(self):
        """Start MCP server"""
        try:
            print("Running the MCP server...", file=sys.stderr)
            self.mcp.run(transport="stdio")
        except Exception as e:
            print(e)
            sys.exit(1)
