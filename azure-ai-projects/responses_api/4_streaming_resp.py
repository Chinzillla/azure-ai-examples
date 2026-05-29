from helper.ai_start import get_openai_client_and_deployment

openai_client, deployment_name = get_openai_client_and_deployment()

stream = openai_client.responses.create(
    model=deployment_name,
    input="Write a short story about 2 + 2",
    stream=True
)

for event in stream:
    # Only print the text deltas as they arrive
    if getattr(event, "type", None) == "response.output_text.delta":
        print(event.delta, end="", flush=True)
