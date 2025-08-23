"""
Author: Joshan John
contact: joshanjohn2003@gmail.com
subjected to copyright@2025
"""

from src.llm.llm import LLM
from src.utils import logger


class WorkFlow:
    def __init__(self, llm: str):

        self.llm_model: str = llm

    def invoke(self, query: str):
        try:
            llm = LLM(model=self.llm_model)
            logger.info("llm initialized..")
        except Exception as e:
            logger.info(str(e))
        response = llm(query)
        return response
