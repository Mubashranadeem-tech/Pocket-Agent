
from llama_cpp import Llama
import os

# Unsloth naming convention for exported GGUF
MODEL_PATH = "./model-unsloth.Q4_K_M.gguf"

# Load model locally (Zero Network calls)
llm = Llama(model_path=MODEL_PATH, n_ctx=1024, verbose=False)

def run(prompt: str, history: list[dict]) -> str:
    # Build ChatML Prompt
    chat = "<|im_start|>system\nYou are a tool-calling assistant.<|im_end|>\n"
    for turn in history:
        role = turn.get('role', 'user')
        content = turn.get('content', '')
        chat += f"<|im_start|>{role}\n{content}<|im_end|>\n"
    
    chat += f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"

    # CPU Inference
    output = llm(chat, max_tokens=128, stop=["<|im_end|>"], temperature=0)
    return output["choices"][0]["text"].strip()
