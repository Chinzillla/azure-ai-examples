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

vector_store = client.vector_stores.create(name="service manual")
client.vector_stores.files.upload_and_poll(
    vector_store_id=vector_store.id,
    file=open("files/mohave.pdf", "rb")
)

response = client.responses.create(
    model=deployment_name,
    instructions="You are an AI assistant that provides info on dental Dry Vacuum System",
    input="What is the Electrical requirements for the site if they want a mohave?",
    tools=[
        {
            "type": "file_search",
            "vector_store_ids": [vector_store.id]
        }
    ],
    include=["file_search_call.results"]
)

print(response.output_text)