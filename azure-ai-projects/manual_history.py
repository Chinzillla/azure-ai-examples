from helper.ai_start import get_openai_client_and_deployment

openai_client, deployment_name = get_openai_client_and_deployment()

try:
    # Start with initial message
    conversation_history = [
        {
            "type": "message",
            "role": "user",
            "content": "What is machine learning?"
        }
    ]

    # First response
    response1 = openai_client.responses.create(
        model=deployment_name,
        input=conversation_history
    )

    print("Assistant:", response1.output_text)

    # Add assistant response to history
    conversation_history += response1.output

    # Add new user message
    conversation_history.append({
        "type": "message",
        "role": "user", 
        "content": "Can you give me an example?"
    })

    # Second response with full history
    response2 = openai_client.responses.create(
        model=deployment_name,
        input=conversation_history
    )

    print("Assistant:", response2.output_text)

except Exception as ex:
    print(f"Error: {ex}")