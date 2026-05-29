import os
import json

from typing import List

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv

load_dotenv()

def two_sum(nums: List[int], target: int) -> dict:
    if len(nums) <= 1:
        return {"found": False, "indices": [-1, -1], "values": []}
    
    val_idx = {}

    for idx, val in enumerate(nums):
        complement = target - val
        if complement in val_idx:
            first_idx = val_idx[complement]
            return {"found": True, "indices": [first_idx, idx], "values": [nums[first_idx], val]}
        val_idx[val] = idx

    return {"found": False, "indices": [-1, -1], "values": []}

def main():
    endpoint = os.environ.get("PROJECT_ENDPOINT")
    deployment_name = os.environ.get("DEPLOYMENT_NAME")

    project_client = AIProjectClient(
        credential=DefaultAzureCredential(),
        endpoint=endpoint
    )

    function_tools = [
        {
            "type": "function",
            "name": "two_sum",
            "description": "Find two distinct entries from a list that add up to a target.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nums": {
                        "type": "array",
                        "items": {"type": "integer"},
                        "description": "The list of integers to search."
                    },
                    "target": {
                        "type": "integer",
                        "description": "The target sum."
                    }
                },
                "required": ["nums", "target"],
                "additionalProperties": False
            },
            "strict": True
        }
    ]

    client = project_client.get_openai_client()

    user_input = "I have a list of numbers [1,2,5,1,3,5,2,1], I want to find two unique numbers that add up 10"
    messages = [{"role": "user", "content": user_input}]

    response = client.responses.create(
        model=deployment_name,
        instructions="Use the two_sum tool whenever the user provides a list of numbers and a target sum. Do not solve it directly.",
        input=messages,
        tools=function_tools,
        tool_choice="required"
    )

    function_calls = [item for item in response.output if item.type == "function_call"]

    for tool_call in function_calls:
        arguments = json.loads(tool_call.arguments)
        tool_result = two_sum(arguments["nums"], arguments["target"])

        messages.append({
            "type": "function_call",
            "name": tool_call.name,
            "call_id": tool_call.call_id,
            "arguments": tool_call.arguments
        })

        messages.append({
            "type": "function_call_output",
            "call_id": tool_call.call_id,
            "output": json.dumps(tool_result)
        })

    final_response = client.responses.create(
        model=deployment_name,
        instructions="Use the tool output to answer the user clearly and briefly.",
        input=messages,
        tools=function_tools
    )

    print(final_response.output_text)

if __name__ == '__main__':
    main()
