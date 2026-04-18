import os
import glob
import gradio as gr

# 1. PEHLE FILE DHOONDO AUR SAHI JAGAH RAKHO
# Pure Colab mein koi bhi .gguf file dhoondo
found_models = glob.glob("**/*.gguf", recursive=True)

if not found_models:
    print("❌ ERROR: Koi .gguf file nahi mili! Pehle training khatam hone dein.")
else:
    # Sabse pehli mili hui model file ko root mein 'model.gguf' ke naam se copy karo
    actual_model_path = found_models[0]
    os.rename(actual_model_path, "model.gguf")
    print(f"✅ Fixed! Model moved from {actual_model_path} to ./model.gguf")

# 2. INFERENCE.PY KO UPDATE KARO TA_KE WO 'model.gguf' USE KARE
with open("inference.py", "w") as f:
    f.write('''
from llama_cpp import Llama
import os

# Universal path after fix
MODEL_PATH = "./model.gguf"

llm = Llama(model_path=MODEL_PATH, n_ctx=1024, verbose=False)

def run(prompt: str, history: list[dict]) -> str:
    chat = "<|im_start|>system\\nYou are a tool-calling assistant.<|im_end|>\\n"
    for turn in history:
        role = turn.get('role', 'user')
        content = turn.get('content', '')
        chat += f"<|im_start|>{role}\\n{content}<|im_end|>\\n"
    chat += f"<|im_start|>user\\n{prompt}<|im_end|>\\n<|im_start|>assistant\\n"
    output = llm(chat, max_tokens=128, stop=["<|im_end|>"], temperature=0)
    return output["choices"][0]["text"].strip()
''')


from inference import run

def predict(message, history):
    formatted_history = []
    for h in history:
        formatted_history.append({"role": "user", "content": h[0]})
        formatted_history.append({"role": "assistant", "content": h[1]})
    return run(message, formatted_history)

demo = gr.ChatInterface(fn=predict, title="Pocket-Agent Demo (Fixed)")
print("🚀 Launching UI... Use the public link below.")
demo.launch(share=True)
