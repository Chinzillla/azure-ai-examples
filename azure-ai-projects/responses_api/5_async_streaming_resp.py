import asyncio
from helper.ai_start import get_async_openai_client_and_deployment

async def stream_response():
    async with get_async_openai_client_and_deployment() as (openai_client, deployment_name):
        stream = await openai_client.responses.create(
            model=deployment_name,
            input="Write a haiku about 2 + 2.",
            stream=True
        )

        async for event in stream:
            # Only print the text deltas as they arrive
            if getattr(event, "type", None) == "response.output_text.delta":
                print(event.delta, end="", flush=True)

asyncio.run(stream_response())
