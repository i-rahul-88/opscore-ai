import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("GITHUB_ENDPOINT"),
    api_key=os.getenv("GITHUB_TOKEN"),
)

def generate_runbook(user_query):
    response = client.chat.completions.create(
        model=os.getenv("GITHUB_MODEL"),
        messages=[
            {
                "role": "system",
                "content": """You are a senior SRE engineer
                specializing in creating professional runbooks.
                When given a procedure request, provide:

                1. RUNBOOK TITLE: Clear title
                2. PURPOSE: What this runbook achieves
                3. PRE-REQUISITES: What is needed before starting
                4. STEP BY STEP PROCEDURE: Detailed numbered steps
                5. VERIFICATION STEPS: How to confirm success
                6. ROLLBACK PLAN: Steps if something goes wrong
                7. ESTIMATED TIME: Total time needed
                8. OWNER: Who is responsible

                Be thorough and professional.
                Format response with these exact headings."""
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
    )

    return response.choices[0].message.content