from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP("Government Permit MCP")

with open("permit_data.json") as f:
    permits = json.load(f)

@mcp.tool()
def get_permit_status(permit_id: str):

    if permit_id not in permits:
        return {
            "status": "Not Found"
        }

    return permits[permit_id]

if __name__ == "__main__":
    mcp.run()