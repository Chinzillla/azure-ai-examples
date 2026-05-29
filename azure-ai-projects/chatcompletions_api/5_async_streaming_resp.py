import asyncio

from helper.ai_start import get_async_openai_client_and_deployment


async def stream_response():
    async with get_async_openai_client_and_deployment() as (openai_client, deployment_name):
        stream = await openai_client.chat.completions.create(
            model=deployment_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": "Write a haiku about 2 + 2."
                }
            ],
            stream=True
        )

        async for chunk in stream:
            if chunk.choices:
                delta = chunk.choices[0].delta.content
                if delta:
                    print(delta, end="", flush=True)


asyncio.run(stream_response())
