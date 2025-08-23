"""
Author: Joshan John
contact: joshanjohn2003@gmail.com
subjected to copyright@2025
"""

from langchain_ollama import ChatOllama
from src.utils import logger


class LLM:
    def __init__(self, model: str) -> None:
        self.model: str = model

    def get_llm_model(self) -> ChatOllama:
        if not self.model:
            raise ValueError("Model name is required to load ChatOllama.")
        return ChatOllama(model=self.model)

    def __call__(self, msg: str) -> str:
        if not msg:
            _error = "Failed to generate LLM response"
            logger.error(_error)
            return _error

        llm = self.get_llm_model()
        logger.debug(f"Model {llm.get_name()} loaded ... ")
        return llm.invoke(msg).content
