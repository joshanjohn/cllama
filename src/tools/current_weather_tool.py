from langchain_core.tools import tool
from src.utils import logger
from src.constants import WEATHER_API_KEY, WEATHER_BASE_URL
import requests


@tool
def current_weather_tool(query: str) -> dict:
    """function to get the current weather for a given Country or post code"""
    if not query:
        raise ValueError("No place name provided to current weather api tool.")

    url = f"{WEATHER_BASE_URL}current.json?key={WEATHER_API_KEY}&q={query}"
    logger.info(f"URL = {url}")

    logger.info(f"calling current weather api tool...")
    data = requests.get(url=url)
    logger.info(f"fetched {query} weather information!")

    if data.status_code != 200:
        logger.error(f"{data.status_code}  - {data.json().get("error").get("message")}")
        return "No data find"

    logger.debug(f"DATA = {data.json()}")
    return data.json()
