from helper.ai_start import get_openai_client_and_deployment

openai_client, deployment_name = get_openai_client_and_deployment()

try:
    conversation_messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant that answers questions and provides information."
        }
    ]

    conversation_messages.append(
        {
            "role": "user",
            "content": "When was Microsoft founded?"
        }
    )

    completion1 = openai_client.chat.completions.create(
        model=deployment_name,
        messages=conversation_messages
    )

    assistant_message = completion1.choices[0].message.content
    print("Assistant:", assistant_message)

    conversation_messages.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )

    conversation_messages.append(
        {
            "role": "user",
            "content": "Who founded it?"
        }
    )

    completion2 = openai_client.chat.completions.create(
        model=deployment_name,
        messages=conversation_messages
    )

    assistant_message = completion2.choices[0].message.content
    print("Assistant:", assistant_message)

    conversation_messages.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )

    print("\nConversation history:", conversation_messages)

except Exception as ex:
    print(f"Error: {ex}")
