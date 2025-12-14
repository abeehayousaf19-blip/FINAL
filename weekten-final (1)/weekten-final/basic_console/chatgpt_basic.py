import os
from openai import OpenAI

# Load API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! What is AI?"}
    ]
)

print(response.choices[0].message.content)