import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("GITHUB_ENDPOINT"),
    api_key=os.getenv("GITHUB_TOKEN"),
)

def scan_security(user_query):
    response = client.chat.completions.create(
        model=os.getenv("GITHUB_MODEL"),
        messages=[
            {
                "role": "system",
                "content": """You are a senior security engineer
                specializing in DevSecOps.
                When given code or config to scan, provide:

                1. VULNERABILITIES FOUND: List each vulnerability
                2. SEVERITY LEVEL: Critical/High/Medium/Low
                3. CVE REFERENCE: If applicable
                4. FIX CODE: Exact fix for each vulnerability
                5. SECURITY SCORE: Rate security out of 10
                6. BEST PRACTICES: 3 security improvements

                Be specific with code examples.
                Format response with these exact headings."""
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
    )

    return response.choices[0].message.content