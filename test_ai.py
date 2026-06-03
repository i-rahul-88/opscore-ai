import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("GITHUB_ENDPOINT"),
    api_key=os.getenv("GITHUB_TOKEN"),
)

response = client.chat.completions.create(
    model=os.getenv("GITHUB_MODEL"),
    messages=[
        {"role": "user", "content": "Say: OpsCore AI is ready!"}
    ]
)

print(response.choices[0].message.content)