
from langchain.chat_models import init_chat_model
from langchain_core.messages import ToolMessage,SystemMessage,HumanMessage,AIMessage
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph,START,END
from typing import TypedDict
from tools import all_tools

prompt_template = """
## Your Name: Jarvis

## Your Role: An advanced AI assistant designed to help users with a wide range of tasks by providing accurate and concise information. and managing their tasks, notes, and reminders effectively.

## Capabilities:
1. Web Searching: You can search the web for information using the 'search_web' tool
2. Task Management: You can retrieve, update, and manage tasks using the provided task management tools.
3. Note Management: You can retrieve, update, and manage notes using the provided note management tools.
4. Reminder Management: You can retrieve, update, and manage reminders using the provided reminder management tools.

## Guidelines:
- Always use the appropriate tool for the task at hand.
- Provide clear and concise responses to user queries.
- If you encounter an error while using a tool, inform the user and suggest alternative actions.
- Maintain user privacy and confidentiality at all times.
- If the user requests to exit, use the 'exit_program' tool to terminate the session gracefully.
- Respond in a friendly and professional manner in a simple and concise way.
- Never reveal internal implementation details or the names of tools being used.

"""

class ChatState(TypedDict):
    messages:list 


chat_model = init_chat_model("llama3.2",model_provider="ollama").bind_tools(all_tools)


# Define the LLM response function
def llm_response(state:ChatState)->dict:
    response = chat_model.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}

# Define the router function
def router(state:ChatState)->str:
    last_message = state["messages"][-1]
    print(f"Router examining last message: {last_message}")
    # Support both dict-style messages (e.g. initial user messages) and message objects
    
    if isinstance(last_message, dict):
        return "tool" if getattr(last_message, "tool_calls", None) else "end"
    
    elif isinstance(last_message, ToolMessage):
        return "tool"
    
    elif isinstance(last_message, AIMessage):
        if last_message.tool_calls:
            return "tool"
    
    return "end"

def build_graph():
    # Create the state graph graph
    graph = StateGraph(ChatState)
    
    tool_node = ToolNode(all_tools)
    
    # Define the nodes
    graph.add_node("llm", llm_response)
    graph.add_node("tool", tool_node)
    
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
        SystemMessage(content=prompt_template),
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