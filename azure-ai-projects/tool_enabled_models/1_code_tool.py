import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv

load_dotenv()

project_endpoint = os.environ.get("PROJECT_ENDPOINT")
deployment_name = os.environ.get("DEPLOYMENT_NAME")

project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)

client = project_client.get_openai_client()

response = client.responses.create(
    model=deployment_name,
    instructions="You are a mathematician. Use the code interpreter tool to verify the result before answering.",
    input="Use Python to calculate the square root of 16, then give the result and show the python tool and code you used.",
    tools=[
        {
            "type": "code_interpreter",
            "container": {
                "type": "auto"
            }
        }
    ]
)

print(response.output_text)
