"""Gemma MCP Client."""

import asyncio
import requests
from typing import Optional
from contextlib import AsyncExitStack
import logging

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import ollama


logging.basicConfig(
    level=logging.DEBUG,
)

CITY_COORDS = {
    "london": (51.5074, -0.1278),
    "sydney": (-33.8688, 151.2093),
    "austin": (30.2672, -97.7431),
}

def get_weather_for_city(city: str) -> str:
    """Fetch real current temperature for a city by name."""
    lat, lon = CITY_COORDS.get(city.lower(), (51.5074, -0.1278))
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    )
    temp = response.json()['current']['temperature_2m']
    return f"{temp}°C"

tools = [
    {
        'type': 'function',
        'function': {
            'name': 'get_weather_for_city',
            'description': 'Given a city name, returns the current temperature',
            'parameters': {
                'type': 'object',
                'properties': {
                    'city': {
                        'type': 'string',
                        'description': 'The name of the city',
                    },
                },
                'required': ['city'],
            },
        },
    }
]


class MCPClient:
    def __init__(self):
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

        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    async def process_user_prompt(self, user_prompt: str) -> str:
        """Process a user prompt using native Ollama tool calling."""
        response = ollama.chat(
            model='gemma4:latest',
            messages=[{'role': 'user', 'content': user_prompt}],
            tools=tools,
        )

        if response.message.tool_calls:
            for tool_call in response.message.tool_calls:
                city = tool_call.function.arguments['city']
                logging.info("Tool call for city: %s", city)
                weather = get_weather_for_city(city)
                return f"The weather in {city} is {weather}"

        return response.message.content

    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'q' to exit.")

        while True:
            try:
                user_prompt = input("\nuser_prompt: ").strip()
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
        server = "weather_server.py"
        await client.connect_to_server(server)
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
