import json
import os
from pathlib import Path

from fastmcp import FastMCP


mcp = FastMCP(
    name="Government Permit MCP",
    instructions=(
        "Use this server to retrieve mock government development "
        "application and permit information."
    )
)

data_file = Path(__file__).with_name("permit_data.json")

with data_file.open("r", encoding="utf-8") as file:
    permits = json.load(file)


@mcp.tool()
def get_permit_status(permit_id: str) -> dict:
    """
    Retrieve the current status and details of a government permit.

    Args:
        permit_id: Permit identifier, for example DA-2026-4567.
    """

    normalized_id = permit_id.strip().upper()

    if normalized_id not in permits:
        return {
            "found": False,
            "permitId": normalized_id,
            "message": "No permit was found for the supplied permit ID."
        }

    return {
        "found": True,
        **permits[normalized_id]
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))

    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port
    )
