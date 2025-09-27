# MCP Server

## Tools that my MCP server provides
- Get a chuck norris joke

## Install requirement libraries
```bash
pip3 install -r requirements.txt
```

## Add to Claude developer configuration file named `claude_desktop_config.json`

```json
{
  "mcpServers": {
    "joke": {
      "command": "/Users/thangphan/code/personal/mcp-server/.venv/bin/python3",
      "args": [
        "/Users/thangphan/code/personal/mcp-server/main.py"
      ]
    }
  }
}
```

