# Pocket-Agent Submission

## Base Model
- **Qwen2.5-0.5B-Instruct**: Chosen to pass the **500MB Hard Gate** (~380MB quantized) and ensure **latency < 200ms** on CPU.

## Design Decisions
- **Quantization**: GGUF Q4_K_M used to meet offline/mobile constraints while maintaining tool-calling accuracy.
- **Data Strategy**: Injected multi-turn conversation history for reference resolution and multilingual examples for adversarial robustness.

## Error Analysis (Debugging Insight)
- Initially, the model would hallucinate tool calls for general chitchat. I added 'Refusal' training examples to ensure it only uses tools when a request matches the schema, avoiding negative scoring.
