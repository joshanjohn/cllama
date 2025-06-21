from langchain_ollama import ChatOllama


class LLM:
    def __init__(self, model: str) -> None:
        self.model: str = model
        self.llm: ChatOllama = self.load_model()

    def load_model(self) -> ChatOllama:
        if not self.model:
            raise ValueError("Model name is required to load ChatOllama.")
        return ChatOllama(model=self.model)

    def run(self, msg: str) -> str:
        if not msg:
            return "Failed to generate LLM response"

        print(self.llm.get_name())  # if get_name() is a method
        return self.llm.invoke(msg).content
