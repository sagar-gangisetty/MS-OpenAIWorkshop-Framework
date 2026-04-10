Start the MCP Server (Terminal 1):
cd mcp
uv run python mcp_service.py

pip install uv
uv run python mcp_service.py

Start the Backend (Terminal 2):
cd agentic_ai/applications
uv run python backend.py


Start the React Frontend (Terminal 3):

cd agentic_ai/applications/react-frontend
npm start
