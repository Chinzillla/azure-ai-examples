import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}",
    api_key=os.environ["AZURE_OPENAI_API_KEY"]
)

response = client.responses.create(
    model=os.environ["DEPLOYMENT_NAME"],
    input=[{"role": "system", "content": "You're a helpful assistant."},
           {"role": "user", "content": "Tell me what 4 + 4 is"}],
    max_output_tokens=300,
    temperature=0.7
)

print(response.output_text)