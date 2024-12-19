from langgraph.graph import StateGraph, MessagesState

#Initialize the LangGraph Workflow
chatbot_graph = StateGraph(MessagesState)

#Define function that generates assistant response
def generate_answer(state:MessagesState):
    user_message = state['messages'][-1].content                # Get the last user message
    response = f"Answer coming soon ... Your question was: {user_message}"
    return {"messages": [{"role": "assistant", "content": response}]}

#Add the function to the graph
chatbot_graph.add_node("response", generate_answer)

# Define the flow
chatbot_graph.set_entry_point("response")
chatbot_graph.set_finish_point("response")

flow = chatbot_graph.compile()

if __name__ == "__main__":
    initial_state = {"messages": [
        {"role": "user", "content": "Who is the president of France?"}
    ]}

    final_state = flow.invoke(initial_state)

    print(final_state["messages"][-1].content)