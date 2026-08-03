from mcp import ClientSession
from contextlib import AsyncExitStack
from mcp.client.streamable_http import streamablehttp_client
import os

class MCPHTTPCLIENT:
    def __init__(self,url):
        ## TODO
        ## initialize any required class variables
        self.exit_stack = AsyncExitStack()
        self.session = None
        self._client = None
        self.mcp_server_url = url

    async def __aenter__(self):
        await self.connect()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.cleanup()

    async def connect(self):
        ## TODO
        ## connect to mcp server and initialize client session
        self._client = streamablehttp_client(self.mcp_server_url)
        self._receive, self._send, self._transport = await self.exit_stack.enter_async_context(self._client)
        
        session = ClientSession(self._receive, self._send)
        self.session = await self.exit_stack.enter_async_context(session)
        
        await self.session.initialize()
    
    async def list_tools(self):
        if not self.session:
            raise RuntimeError("MCP client is not connected.")
        response = await self.session.list_tools()
        return response.tools

    async def call_tool(self, tool_name: str, tool_args: dict):
        if not self.session:
            raise RuntimeError("MCP client is not connected.")
        return await self.session.call_tool(tool_name, tool_args)

    async def cleanup(self):
        ## TODO
        ## clean up resources
        await self.exit_stack.aclose()
        self.session = None
        self._client = None