"""
The Repoint Story — ONE env var change
This file shows the ONLY difference between Phase 1 and Phase 2.
"""
import os
from openai import OpenAI

# Read from environment — app code NEVER changes
PROVIDER = os.environ.get("AI_PROVIDER", "github")  # "github" or "azure"

if PROVIDER == "github":
    # Phase 1: GitHub Models (no Azure needed)
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.environ["GITHUB_TOKEN"]
    )
    model = "gpt-4o"
elif PROVIDER == "azure":
    # Phase 2: Azure OpenAI (when environment is ready)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/deployments/{os.environ.get('AZURE_DEPLOYMENT', 'gpt-4o')}",
        api_key=os.environ["AZURE_OPENAI_KEY"],
        default_headers={"api-key": os.environ["AZURE_OPENAI_KEY"]},
        api_version="2024-06-01"
    )
    model = os.environ.get("AZURE_DEPLOYMENT", "gpt-4o")

# === EVERYTHING BELOW IS IDENTICAL REGARDLESS OF PROVIDER ===

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a healthcare compliance expert."},
        {"role": "user", "content": "List the top 5 HIPAA technical safeguards for a REST API."}
    ],
    temperature=0.7,
    max_tokens=400
)

print(f"Provider: {PROVIDER.upper()}")
print(f"Model: {model}")
print(f"\n{response.choices[0].message.content}")
