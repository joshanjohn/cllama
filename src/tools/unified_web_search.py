from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults


duckduckgo_tool = DuckDuckGoSearchResults()


@tool
def unified_web_search(query: str) -> str:
    """Search funtion to get information from internet, able to search all publicly avaiable informations."""
    results = []

    try:
        ddg_results = duckduckgo_tool.run(query)
        return ddg_results
    except Exception as e:
        results.append(f"[DuckDuckGo Error] {e}")

