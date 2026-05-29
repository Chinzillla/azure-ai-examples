from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv
import os

def get_openai_client_and_deployment():
    load_dotenv()
    project_endpoint = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
    deployment_name = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
    project_client = AIProjectClient(
        credential=DefaultAzureCredential(),
        endpoint=project_endpoint
    )
    openai_client = project_client.get_openai_client()
    return openai_client, deployment_name