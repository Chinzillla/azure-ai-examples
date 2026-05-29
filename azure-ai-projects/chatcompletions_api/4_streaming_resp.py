from helper.ai_start import get_openai_client_and_deployment

openai_client, deployment_name = get_openai_client_and_deployment()

stream = openai_client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        },
        {
            "role": "user",
            "content": "Write a short story about 2 + 2."
        }
    ],
    stream=True
)

for chunk in stream:
    if chunk.choices:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
