# Fine tuning models

Fine-tuning is the process of taking a pretrained language model and further training it on a smaller, task-specific dataset. This adjusts the model's internal weights so that it produces responses that are consistent with the patterns in your training data.

- prompt - guide model behavior
- RAG - ground model responses

However model still sometimes does not produce responses with consistent style, tone, or format.

when you notice that model ignores or inconsistently follows instructions after the implementing the following then it may be time to fine-tune a model:
- after detailed system message and few-shot examples
- after RAG

## What is fine tuning?

Fine tuning builds on foundation of training models with additional examples that reflect your specific requirement (specializing a generalist)

LoRA (Low-Rank Adaptation) - technique that approximates weight changes with lower-rank representation

Instead of retraining all model parameters, LoRA updates a small subset of important parameters.
- This is done because a full training will take way too long, this will be significantly faster
- cost effective because you are ultimately using less resources with a smaller subset
- model quality is not degrading, because a small subset is used there will be smaller impact on model quality.

## When to fine-tune?

When prompt engineering does not acheive consistency needed

### Common usecases:
- Consistent style and tone
- Specific output formats (producing structure outputs)
- Reducing prompt length (reduce token consumption and latency)
- Distillation (transfer capabilities of llm to smaller model - collecting outputs from high performing mode and use them to fine-tune a smaller model to achieve similar quality at lower cost and latency)
- Enhancing tool usage: fine tuning with tool calling examples can improve accuracy of tool selection and parameter generation.

Notes:
```
Fine-tuning is an advanced capability. Always start by evaluating the baseline performance of a standard model against your requirements before considering fine-tuning. Without a baseline, it's hard to detect whether fine-tuning improved or degraded the model's performance.
```

## Types of fine tuning

### Supervised fine-tuning (SFT)

### Reinforcement fine-tuning (RFT)

### Direct Preference Optimization (DPO)

## Preparing training data
