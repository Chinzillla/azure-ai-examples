from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv
import os

load_dotenv()

project_endpoint = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
deployment_name = os.environ.get("AZURE_OPENAI_DEPLOYMENT")

project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)

openai_client = project_client.get_openai_client()
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