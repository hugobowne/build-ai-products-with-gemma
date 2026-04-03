"""Gemini MCP Client,"""

import asyncio
from typing import Optional
from contextlib import AsyncExitStack
import logging

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.server.fastmcp import FastMCP

from google import genai
from google.genai import types

import os


mcp = FastMCP("Weather app")

logging.basicConfig(
    level=logging.DEBUG, # Log everything from DEBUG level upwards
)

client = genai.Client(api_key="AIzaSyCu2fu5q18u4V8kzKF4imOqVclydXMOvbw")
model = "gemini-2.0-flash"


class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()

    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server"""
        server_params = StdioServerParameters(
            command="python",
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    async def process_user_prompt(self, user_prompt: str) -> str:
        """Process a user_prompt using Gemma and available tools"""

        # Store all exchanges using proper gemini contents
        contents = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

        all_tools = await self.session.list_tools()

        available_tools = types.Tool(function_declarations=[
                {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.inputSchema,
                }
                for tool in all_tools.tools
            ])

        # Send request with function declarations
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # Or your preferred model supporting function calling
            contents=contents,
            config=types.GenerateContentConfig(
                temperature=0.7,
                tools=[available_tools],
            ),  # Example other config
        )

        contents.append(response.candidates[0].content)

        if response.candidates[0].content.parts[0].function_call:
            tool_response_parts: List[types.Part] = []

            function_call = response.candidates[0].content.parts[0].function_call
            logging.info("Tool call with %s" % function_call)

            tool_name = function_call.name
            args = function_call.args or {}  # Ensure args is a dict

            try:
                # Call the session's tool executor
                tool_result =  await self.session.call_tool(tool_name, args)
                logging.info(f"MCP tool '{tool_name}' executed successfully.")
                if tool_result.isError:
                    tool_response = {"error": tool_result.content[0].text}
                else:
                    tool_response = {"result": tool_result.content[0].text}
            except Exception as e:
                tool_response = {"error":  f"Tool execution failed: {type(e).__name__}: {e}"}

            # Prepare FunctionResponse Part
            tool_response_parts.append(
                types.Part.from_function_response(
                    name=tool_name, response=tool_response
                )
            )
            contents.append(types.Content(role="user", parts=tool_response_parts))

            logging.info(f"Added {len(tool_response_parts)} tool response parts to history.")
            response = await client.aio.models.generate_content(
                model=model,
                contents=contents,  # Send updated history
                config=types.GenerateContentConfig(
                    temperature=1.0,
                    tools=[available_tools],
                ),  # Keep sending same config
            )

            logging.info("Final response is: %s", response.candidates[0].content)
            contents.append(response.candidates[0].content)

        # No tool call
        else:
            logging.info("No tool call")
            contents.append(response.candidates[0].content)
        return contents[-1].parts[0].text

    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")

        while True:
            try:
                user_prompt = input("\nuser_prompt: ").strip()
                # user_prompt = "What is the weather in london?"
                # user_prompt = "How are you?"
                logging.info("User prompt is: %s", user_prompt)

                if user_prompt.lower() == 'q':
                    break

                response = await self.process_user_prompt(user_prompt)
                print("\n" + response)

            except Exception as e:
                print(f"\nError: {str(e)}")

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()


async def main():
    client = MCPClient()
    try:
        # Hardcode the client for now
        server = "weather_server.py"
        await client.connect_to_server(server)
        # await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
