from helper.ai_start import get_openai_client_and_deployment

openai_client, deployment_name = get_openai_client_and_deployment()

try:
    # Start with initial message
    conversation_history = [
        {
            "type": "message",
            "role": "user",
            "content": "What is 10 * 10"
        }
    ]

    # First response
    response1 = openai_client.responses.create(
        model=deployment_name,
        input=conversation_history
    )

    print("Assistant:", response1.output_text)

    # Add assistant response to history
    # response1.output is a list of messages from ai so you want to append each message instead of the entire list of messages by using +=
    conversation_history += response1.output
    print("conversation history:", conversation_history)

    resp_id = response1.output[0].response_id

    # Add new user message
    conversation_history.append({
        "type": "message",
        "role": "user", 
        "content": "Can you tell me why"
    })

    # Second response with full history
    response2 = openai_client.responses.create(
        model=deployment_name,
        input=conversation_history
    )

    print("Assistant:", response2.output_text)

    previous_response = openai_client.responses.retrieve(resp_id)
    print(f"\n\nPrevious response: {previous_response.output_text}")

except Exception as ex:
    print(f"Error: {ex}")