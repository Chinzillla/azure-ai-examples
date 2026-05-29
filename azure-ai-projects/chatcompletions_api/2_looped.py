from helper.ai_start import get_openai_client_and_deployment

openai_client, deployment_name = get_openai_client_and_deployment()

conversation_messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant that answers questions clearly."
    }
]

print("Assistant: Enter a prompt (or type 'quit' to exit)")

while True:
    input_text = input("\nYou: ")
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    conversation_messages.append(
        {
            "role": "user",
            "content": input_text
        }
    )

    completion = openai_client.chat.completions.create(
        model=deployment_name,
        messages=conversation_messages,
        temperature=1,
        max_tokens=1000
    )

    assistant_message = completion.choices[0].message.content
    print("\nAssistant:", assistant_message)

    conversation_messages.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )
