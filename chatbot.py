import chainlit as cl
from graph import flow

@cl.on_message
async def main(message: cl.Message):
    initial_state = {"messages": [
        {"role": "system", "content": "You are a friendly assistant."},
        {"role": "user", "content": message.content}
    ]}

    final_state = flow.invoke(initial_state)
    content = final_state["messages"][-1].content

    await cl.Message(content).send()
