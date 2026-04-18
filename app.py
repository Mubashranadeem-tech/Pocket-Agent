
import gradio as gr
from inference import run

def chat(message, history):
    # Grader format: list of turns
    formatted_history = []
    for h in history:
        formatted_history.append({"role": "user", "content": h[0]})
        formatted_history.append({"role": "assistant", "content": h[1]})
    return run(message, formatted_history)

gr.ChatInterface(fn=chat, title="Pocket-Agent Demo").launch()
