import os
from contextlib import asynccontextmanager
from pathlib import Path

from azure.identity import DefaultAzureCredential
from azure.identity.aio import DefaultAzureCredential as AsyncDefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.aio import AIProjectClient as AsyncAIProjectClient
from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parents[1] / ".env"


def get_openai_client_and_deployment():
    load_dotenv(ENV_PATH)
    project_endpoint = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
    deployment_name = (
        os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT")
        or os.environ.get("AZURE_OPENAI_DEPLOYMENT")
    )
    project_client = AIProjectClient(
        credential=DefaultAzureCredential(),
        endpoint=project_endpoint
    )
    openai_client = project_client.get_openai_client()
    return openai_client, deployment_name


@asynccontextmanager
async def get_async_openai_client_and_deployment():
    load_dotenv(ENV_PATH)
    project_endpoint = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
    deployment_name = (
        os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT")
        or os.environ.get("AZURE_OPENAI_DEPLOYMENT")
    )

    async with AsyncDefaultAzureCredential() as credential:
        async with AsyncAIProjectClient(
            credential=credential,
            endpoint=project_endpoint
        ) as project_client:
            openai_client = project_client.get_openai_client()
            try:
                yield openai_client, deployment_name
            finally:
                await openai_client.close()
