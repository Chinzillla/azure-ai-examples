from helper.ai_start import get_openai_client_and_deployment

openai_client, deployment_name = get_openai_client_and_deployment()

print("Bob: Enter a fucking prompt mate ( or tyoe 'quit' if your scared)")
while True:
    input_text = input('\nYou: ')
    if input_text.lower() == "quit":
        print("Bob: Fuck off mate!")
        break

    response = openai_client.responses.create(
        model=deployment_name,
        instructions="Your name is bob and you are an angry austrailian that likes to say bad words in the sentences.",
        input=input_text,
        temperature=1, # 0-1 higher for more creative resp
        max_output_tokens=1000 # limiting response length
    )
    assistant_text = response.output_text
    print("\nBob:", assistant_text)
    last_response_id = response.id