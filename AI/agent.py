
from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage, ToolMessage,SystemMessage,HumanMessage,AIMessage
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph,START,END
from typing import TypedDict
from tools import all_tools

class ChatState(TypedDict):
    messages:list[dict | BaseMessage]


chat_model = init_chat_model("qwen3:1.7b",model_provider="ollama").bind_tools(all_tools)


# Define the LLM response function
def llm_response(state:ChatState)->ChatState:
    response = chat_model.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}


# Define the router function
def router(state:ChatState)->str:
    last_message = state["messages"][-1]
    print(f"Router examining last message: {last_message}")
    # Support both dict-style messages (e.g. initial user messages) and message objectswho i

    
    if isinstance(last_message, ToolMessage):
        return "tool"
    
    elif isinstance(last_message, dict):
        if "tool_calls" in last_message and last_message["tool_calls"]:
            return "tool"

    elif isinstance(last_message, AIMessage):
        if last_message.tool_calls:
            return "tool"
    
    return "end"


tool_node = ToolNode(all_tools)

def tool_response(state:ChatState)->ChatState:
    response = tool_node.invoke(state["messages"])
    return {"messages": state["messages"] + response}


def build_graph():
    # Create the state graph graph
    
    graph = StateGraph(ChatState)
    
    
    
    # Define the nodes
    graph.add_node("llm", llm_response)
    graph.add_node("tool", tool_response)
    
    # Define the edges
    graph.add_edge(START, "llm")
    graph.add_edge("tool", "llm")

    # Define the conditional edges
    graph.add_conditional_edges(
        "llm",
        router,
        {
            "tool": "tool",
            "end": END
        }
    )
    return graph.compile()

agent = build_graph()

def run_agent(user_input:str)->str:
    global agent
    
    state =ChatState(messages=[
        SystemMessage(content="You are Jarvis, a helpful assistant. You can use tools to help answer the user's question. Always try to use tools when appropriate."),
        HumanMessage(content=user_input)
        ]
    )
    
    # Run the agent
    final_state = agent.invoke(state) # Get agent response
    final_response = final_state["messages"][-1].content
    
    return final_response



if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        response = run_agent(user_input)
        print(f"Jarvis: {response}")