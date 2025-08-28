import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY: str = os.getenv("WEATHER_API_KEY", "")
WEATHER_BASE_URL: str = os.getenv("WEATHER_BASE_URL")

OPENAI_KEY: str = os.getenv("OPENAI_KEY", "")
