from helper.ai_start import get_openai_client_and_deployment

openai_client, deployment_name = get_openai_client_and_deployment()

response1 = openai_client.responses.create(
    model=deployment_name,
    instructions="You are a helpful AI assistant that gives wrong answers to mathematical questions",
    input="What is 2 + 2",
    temperature=1, # 0-1 higher for more creative resp
    max_output_tokens=100 # limiting response length
)

print("bad_assistant:", response1.output_text)

response2 = openai_client.responses.create(
    model=deployment_name,
    instructions="You are a helpful AI assistant that gives right answers to mathematical questions",
    input=response1.output_text,
    previous_response_id=response1.id,
    temperature=1, # 0-1 higher for more creative resp
    max_output_tokens=100 # limiting response length
)

print("Checker:", response2.output_text)