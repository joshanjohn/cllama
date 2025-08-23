# from langgraph.graph import StateGraph
from src.llm.llm import LLM
from src.states import AgentState
from src.agents import weather_assistant_agen_config, Agent

from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import StateGraph
from langgraph.prebuilt import create_react_agent
from langgraph.graph.state import CompiledStateGraph
from langchain_ollama import ChatOllama


class AgenticWorkflow:
    def __init__(
        self,
        llm: str,
    ):
        self.llm = LLM(llm).get_llm_model()

    def weather_agent(self, state: AgentState) -> AgentState:
        config: Agent = weather_assistant_agen_config

        prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages(
            [
                ("system", config.system_prompt),
                MessagesPlaceholder("messages"),
            ]
        )
        agent = create_react_agent(
            name=config.name, model=self.llm, prompt=prompt, tools=config.tools
        )

        if not state["messages"]:
            print("No message has been passed...")
            return state

        query = state["messages"][-1].content
        result = agent.invoke({"messages": state["messages"], "input": query})

        answer = result["messages"][-1].content

        # Return updated conversation
        return {"messages": state["messages"] + [AIMessage(content=answer)]}

    def get_workflow(self) -> CompiledStateGraph:
        graph = StateGraph(AgentState)
        graph.add_node("weather_agent_node", self.weather_agent)

        graph.set_entry_point("weather_agent_node")
        graph.set_finish_point("weather_agent_node")

        return graph.compile()
