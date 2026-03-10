"""
GitHub Models Demo — Zero Azure, Zero Infrastructure
Start building AI apps NOW, repoint to Azure later.
"""
import os
from openai import OpenAI

# === PHASE 1: GitHub Models (today) ===
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"]  # Your GitHub PAT
)

# Pick any model — GPT-5 mini is free on paid Copilot plans
MODEL = "gpt-4o"  # or "gpt-5-mini", "gpt-4.1", etc.

# Simple chat
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful healthcare assistant."},
        {"role": "user", "content": "What are the key compliance requirements for handling PHI in a cloud application?"}
    ],
    temperature=0.7,
    max_tokens=500
)

print("=== GitHub Models Response ===")
print(f"Model: {MODEL}")
print(f"Response:\n{response.choices[0].message.content}")
print(f"\nTokens used: {response.usage.total_tokens}")

# === PHASE 2: When Azure is ready, change ONE line ===
# client = OpenAI(
#     base_url="https://your-elevance-aoai.openai.azure.com/openai/deployments/gpt-4o",
#     api_key=os.environ["AZURE_OPENAI_KEY"],
#     default_headers={"api-key": os.environ["AZURE_OPENAI_KEY"]},
#     api_version="2024-06-01"
# )
# Everything else stays EXACTLY the same.
