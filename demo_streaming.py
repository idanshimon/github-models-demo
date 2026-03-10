"""
GitHub Models — Streaming Chat Demo
Real-time token streaming, just like Azure OpenAI does.
"""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"]
)

MODEL = "gpt-4o"

print(f"=== Streaming from GitHub Models ({MODEL}) ===\n")

stream = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a senior healthcare architect at a large hospital system."},
        {"role": "user", "content": "Design a high-level architecture for a patient scheduling API that handles PHI securely. Be concise."}
    ],
    stream=True,
    temperature=0.7,
    max_tokens=600
)

for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

print("\n\n✅ Done — same code works with Azure OpenAI, just change base_url")
