## 🚀 Trained Artifacts (Download Links)
Due to file size limits on GitHub, the trained weights and quantized model are hosted on Google Drive:

1. **Quantized Model (.gguf):** (https://drive.google.com/file/d/1dyWVLTnyw_a9X5kMstGTW1HwUAfALV1v/view?usp=sharing)]
2. **LoRA Adapter Weights (.safetensors):** (https://drive.google.com/file/d/1Pm5_90Sd7F4eJXJ2AEios4Ojq9UFChDC/view?usp=sharing)
3. **LoRA Adapter Config (.json):** https://drive.google.com/file/d/1O2CVK_FBb-R4HK4fdUvUDhcZvIGPPnwm/view?usp=sharing

*Note: The grader should use these weights to verify the fine-tuning process.* 

# Pocket-Agent Submission

## Base Model
- **Qwen2.5-0.5B-Instruct**: Chosen to pass the **500MB Hard Gate** (~380MB quantized) and ensure **latency < 200ms** on CPU.

## Design Decisions
- **Quantization**: GGUF Q4_K_M used to meet offline/mobile constraints while maintaining tool-calling accuracy.
- **Data Strategy**: Injected multi-turn conversation history for reference resolution and multilingual examples for adversarial robustness.

## Error Analysis (Debugging Insight)
- Initially, the model would hallucinate tool calls for general chitchat. I added 'Refusal' training examples to ensure it only uses tools when a request matches the schema, avoiding negative scoring.
