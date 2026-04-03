import logging
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather_server")

@mcp.resource("echo://{message}")
def echo_resource(message: str) -> str:
    """Echo a message as a resource"""
    return f"Resource echo: {message}"


@mcp.tool()
def weather_tool(city: str) -> str:
    """Get weather"""
    logging.info("Server called with weather function %s", city)
    if city.lower() in {"austin", "sydney"}:
        return "sunny"
    else:
        return "cloudy"


@mcp.prompt()
def weather_prompt() -> str:
    """Weather system prompt"""
    system_prompt = '''
    You have the following functions available
     def get_weather(city: str)
       """Given a city returns the weather for that city""
    
     If you call this function return the json [{"city": city}] and nothing else
     otherwise respond normally
    '''
    return system_prompt

# @mcp.prompt()
# def weather_prompt(weather) -> str:
#     """Weather system prompt"""
#     system_prompt = '''
#     '''

#     return system_prompt

@mcp.prompt()
def weather_response_prompt(city, weather) -> str:
    """Weather response prompt"""
    weather_prompt = f"The weather in {city} is {weather}, tell me the weather nicely"
    return weather_prompt 

if __name__ == "__main__":
    mcp.run()
