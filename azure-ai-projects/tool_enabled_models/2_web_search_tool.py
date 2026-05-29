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
    instructions="You are a stock assistant that helps get stock prices and provides sources that are used to get the price",
    input="What was the latest stock price of GOOGLE",
    tools=[
        {
            "type": "web_search"
        }
    ]
)

print(response.output_text)