from src.agents.agent import Agent
from src.tools import current_weather_tool, weather_alerts_tool



weather_assistant_agen_config = Agent(
    name="Weather_Assistant_Agent",
    tools=[current_weather_tool, weather_alerts_tool],
    prompt="""You are a helpful weather assistant. 
        You should identify for which countries weather information is needed from the user messages {messages}. 
        Use only the country name or postal code if there is any in user message, for tool calling.
        lways call the weather tool when you detect a location query. Do not stop after reasoning; fetch and return the weather in the same response.
        Also fetch if there is any weather alerts.""",
)

