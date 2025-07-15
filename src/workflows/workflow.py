"""
Author: Joshan John
contact: joshanjohn2003@gmail.com
subjected to copyright@2025
"""

from src.llm.llm import LLM

class WorkFlow:
    def __init__(self, llm: str):
        print("- Initializing workflow")
        self.llm_model: str = llm

    def invoke(self, query: str):
        llm = LLM(model=self.llm_model)
        response = llm.run(query)
        return response
