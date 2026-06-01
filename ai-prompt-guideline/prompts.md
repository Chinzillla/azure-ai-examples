# Prompts

When you interact with a language model, the quality of your question directly influences the quality of the response. A well-constructed prompt helps the model understand what you need and generate a more useful answer.

## Goal

To optimize a model's performance through prompt engineering (low effort)

## Prompts components:
- System message: Instructions that define the model's behavior, role, and constraints.
- User message: The question or input from the user.
- Assistant message: Previous model responses, used in multi-turn conversations.
- Examples: Sample input/output pairs that demonstrate the expected response format.

### Notes:
When your prompt includes multiple sections — such as instructions, source text, and examples — use delimiters like ---, Markdown headings, or XML tags to separate them. Clear boundaries help the model distinguish instructions from content and reduce the chance of misinterpretation.

Models are susceptible to recency bias, meaning text near the end of a prompt can have more influence than text at the beginning

If the model isn't following your instructions consistently, try repeating the key instruction at the end of the prompt.

## Effective System Prompt

```md
You are a friendly travel advisor for Margie's Travel.

Answer only questions related to travel, hotels, and trip planning.
Use a warm, conversational tone.

If you don't have enough information to answer, ask a clarifying question.

Format hotel recommendations as a bulleted list with the hotel name, location, and price range.
```

A system message influences the model but doesn't guarantee compliance. You should test and iterate on your system messages, and layer them with other mitigations like content filtering and evaluation.

### Check List
- Start with the assistant's role (state role and expected outcome)
- Define boundaries (list topics, actions, and content types assistant should avoid)
- Specify the output format (specific format)
- Add a "when unsure" policy (handle ambiguous, out of scope or model lack info)

### Persona Pattern

Give the agent a well defined persona:

```md
You're a seasoned marketing professional writing for technical customers.
```

### Format Pattern

Providing a structured format will help get a specific output:

```md
Format the result to show:
- Hotel name
- Location
- Star rating
- Price range per night

and provide it to me in JSON format:

{
    "hotel_name": "hotel name",
    "location": "location",
    "star rating": "star_rating"
    "price_range_per_night": "Price range per night"
}
```

## User Prompt

### Chain-of-thought pattern

Asking a model to explain its reasoning step by step to reduce chance of inaccurate results and make it easier to verify model logic.

Instead of asking:

```md
Which hotel is best for a family of four?
```

Better prompt with chain of thought:

```md
Which hotel is best for a family of four? Take a step-by-step approach: 
consider room size, amenities for children, location, and price.
```

Note!
```md
Chain-of-thought prompting is a technique for non-reasoning models. Reasoning models like o-series models handle step-by-step logic internally.
```

### Few-shot learning pattern

Providing one or more examples of desired input and output helps model identify the pattern you want

zero shot learning - no example provided
one shot learning - one example provided
few shot learning - two or more examples provided


Example
```md
Classify the following customer messages:

Message: "I need to change my flight to Rome"
Category: Booking change

Message: "What's the weather like in Bali in March?"
Category: Travel information

Message: "Can I get a refund for my cancelled tour?"
Category:
```

## Adjusting model parameters

### Temperature

Higher value
- More creative and varied responses

Lower value
- more focused and deterministic responses

### Top P

Top_p of 0.9 means the model considers only the top 90% of probable token

#### Higher value
- adds more possible tokens to predict from (randomness)
- higher temperature (0.7) when generating creative suggestions

#### Lower value
- reduces the possible tokens to predict from
- you might use a low temperature (0.2) when answering factual questions

#### Note: 
The general recommendation is to adjust either temperature or top_p, not both at the same time.

## When to prompt engineer

### Starting point for model optimization
- guide model tone, format, behavior
- provide specific instructions for a task
- quickly iterate on results without infrastructure changes
- keep costs low, as no additional training or data storage is required

### limits of prompt engineering
- model doesnt have info it needs
- consistently fails to mainain a specific behavior despite detailed instructions