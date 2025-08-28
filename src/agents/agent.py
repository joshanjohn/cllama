from langchain_core.tools.base import BaseTool
from typing import List


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
