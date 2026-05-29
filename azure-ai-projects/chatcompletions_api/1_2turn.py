from helper.ai_start import get_openai_client_and_deployment

openai_client, deployment_name = get_openai_client_and_deployment()

bad_completion = openai_client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant that gives wrong answers to mathematical questions."
        },
        {
            "role": "user",
            "content": "What is 2 + 2?"
        }
    ],
    temperature=1,
    max_tokens=100
)

bad_answer = bad_completion.choices[0].message.content
print("bad_assistant:", bad_answer)

checker_completion = openai_client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant that checks mathematical answers."
        },
        {
            "role": "user",
            "content": f"Check this answer to 'What is 2 + 2?': {bad_answer}"
        }
    ],
    temperature=1,
    max_tokens=100
)

checker_answer = checker_completion.choices[0].message.content
print("Checker:", checker_answer)
