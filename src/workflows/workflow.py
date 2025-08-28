from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from src.tools import current_weather_tool, weather_alerts_tool
from src.llm import LLM
from src.states import AgentState


class Workflow:

    def __init__(self, model: str):
        self.tools = [weather_alerts_tool, current_weather_tool]
        self.llm = LLM(model=model).get_llm_model()
        self.llm = self.llm.bind_tools(tools=self.tools)
        # Create a ToolNode runnable
        self.tool_node = ToolNode(self.tools)

    def tool_calling_llm(self, state: AgentState):
        result = self.llm.invoke(state["messages"])
        # self._print_messages(state)
        return {
            "messages": [result],
            "weather_data": state.get("weather_data", {}),
        }

    def tool_handler(self, state: AgentState):
        """Runs tools via ToolNode and stores outputs into weather_data"""
        result = self.tool_node.invoke(state)

        tool_msgs = result.get("messages", [])
        weather_data = state.get("weather_data", {})

        for msg in tool_msgs:
            if hasattr(msg, "content"):
                tool_name = getattr(msg, "name", "unknown_tool")
                weather_data[tool_name] = msg.content

        return {
            "messages": tool_msgs,
            "weather_data": weather_data,
        }

    def get_workflow(self):
        graph = StateGraph(AgentState)

        graph.add_node("tool_calling_llm", self.tool_calling_llm)
        graph.add_node("tools", self.tool_handler)

        graph.set_entry_point("tool_calling_llm")
        graph.add_conditional_edges("tool_calling_llm", tools_condition)
        graph.add_edge("tools", "tool_calling_llm")
        graph.set_finish_point("tools")

        return graph.compile()

    def _print_messages(self, state):
        print(state)
        for msg in state["messages"]:
            print(msg.pretty_repr())
