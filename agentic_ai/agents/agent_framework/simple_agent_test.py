import asyncio
import os
from dotenv import load_dotenv
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential

# Load .env file (same folder or specify full path)
load_dotenv(dotenv_path=".env")

# Retrieve values from .env
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

print("Using Azure OpenAI endpoint:", endpoint)
print("Deployment name:", deployment_name)
print("API version:", api_version)

# ✅ Correct parameter name is deployment_name (not deployment)
agent = AzureOpenAIChatClient(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    endpoint=endpoint,
    deployment_name=deployment_name,
    api_version=api_version
).create_agent(
    instructions="You are a helpful and funny assistant who tells short jokes.",
    name="Joker"
)

async def main():
    result = await agent.run("Tell me a joke about the Earth.")
    print("\nAgent response:\n", result.text)

asyncio.run(main())
