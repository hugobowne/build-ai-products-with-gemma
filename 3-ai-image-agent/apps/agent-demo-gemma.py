import gradio as gr
import re
import json
import requests
import ollama
from ollama import chat, ChatResponse

# --- Helper functions ---

model = 'gemma4:latest'

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

# --- Gradio app function ---

def gradio_chat_interaction(user_prompt):
    response = ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': user_prompt}],
        tools=tools,
    )

    if response.message.tool_calls:
        for tool_call in response.message.tool_calls:
            city = tool_call.function.arguments['city']
            weather = get_weather_for_city(city)
            final_response = f"The weather in {city} is {weather}"
            return final_response, f"Tool call detected: city = {city}, weather = {weather}"

    return response.message.content, "No tool call detected."

# --- Gradio Interface ---

iface = gr.Interface(
    fn=gradio_chat_interaction,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs=[
        gr.Textbox(label="Final Model Response"),
        gr.Textbox(label="Under the Hood (Tool Calls)"),
    ],
    title="Agent Demo: Chat with Tool Usage",
    description="Type a message. If a tool call is needed, the system will call the tool and update the response.",
)

if __name__ == "__main__":
    iface.launch()
