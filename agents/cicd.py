import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("GITHUB_ENDPOINT"),
    api_key=os.getenv("GITHUB_TOKEN"),
)

def debug_cicd(user_query):
    response = client.chat.completions.create(
        model=os.getenv("GITHUB_MODEL"),
        messages=[
            {
                "role": "system",
                "content": """You are a senior DevOps engineer
                specializing in CI/CD pipeline debugging.
                When given a pipeline failure, provide:

                1. FAILURE REASON: Why the pipeline failed
                2. EXACT FIX: The specific code or config to fix
                3. PIPELINE OPTIMIZATION: 3 ways to improve pipeline
                4. ESTIMATED FIX TIME: How long to implement fix
                5. PREVENTION: How to avoid this failure next time

                Be specific with code examples where needed.
                Format response with these exact headings."""
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
    )

    return response.choices[0].message.content