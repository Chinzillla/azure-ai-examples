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

You can combine these techniques

### Supervised fine-tuning (SFT)

Train model on labeled data set of prompt and response pairs
- model learns to produce outputs that match pattern in training data
- best when clear, well defined ways to approach a task

### Reinforcement fine-tuning (RFT)

Optimize model behavior through iterative feedback, using a grader to reward better responses
- works well for complex or dynamic tasks with many possbile solutions
- goal is to improve model reasoning quality

### Direct Preference Optimization (DPO)

align model based on human preference by providing preferred and non-preferred response pairs
- computationally lighter than traditional reinforcement
- equally effective at alignment

## Preparing training data

Fine-tuning requires a dataset of high quality examples in JSONL format

Each example has conversation with system, user, and assistant messages:

```json
//MESSAGE 1
{
  "messages": [
    {
      "role": "system",
      "content": "You are a friendly travel advisor for Margie's Travel."
    },
    {
      "role": "user",
      "content": "What's a good beach destination in Europe?"
    },
    {
      "role": "assistant",
      "content": "For a beautiful European beach experience, consider the Algarve in southern Portugal! It offers stunning golden cliffs, warm waters, and charming coastal towns. The best time to visit is from May through September."
    }
  ]
}

//MESSAGE 2
{
  "messages": [
    {
      "role": "system",
      "content": "You are a friendly travel advisor for Margie's Travel."
    },
    {
      "role": "user",
      "content": "I need a budget hotel in Tokyo."
    },
    {
      "role": "assistant",
      "content": "Here are some great budget-friendly options in Tokyo:\n\n- **Sakura Hotel Jimbocho** - Central location, from $45/night\n- **Khaosan World Asakusa** - Near Senso-ji temple, from $35/night\n- **Imano Tokyo Ginza Hostel** - Modern design, from $40/night\n\nAll three options are close to public transit, making it easy to explore the city."
    }
  ]
}
```

### When prepping training data
- include consistent system message across examples
- use high-quality examples that cover range of scenarios
- aim for at least hundreds of examples; more is better
- Ensure assistant response reflect exactly style, format, and tone you want

Note:
```
Including a system message in your training data is important. Leaving it blank tends to produce lower-accuracy models. Use the same system message when you deploy your fine-tuned model for inference.
```

## Consider the challenges

### Training costs

Upfront costs for training and ongoing hourly costs for hosting custom models

### Data quality requirements

Poor-quality or unrepresentative training data leads to overfitting, underfitting, or bias

### Maintenance

FIne-tuned models need to be retrained when data changes or when updated base models are released

### Experimentation

FInding right combo of hyperparameters (epochs, batch size, learning rate) requires testing and iteration

### Model drift

Specializing too marrowly can make model less effective at general language tasks outside the fine-tuned domain