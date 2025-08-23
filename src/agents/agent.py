from langchain_core.tools.base import BaseTool
from langgraph.prebuilt import create_react_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from typing import List, Any


class Agent:
    def __init__(
        self,
        prompt: str,
        name: str = None,
        tools: list[BaseTool] = [],
    ):
        self.system_prompt: str = prompt
        self.tools: List[BaseTool] = tools
        self.name: str = name

        