import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("GITHUB_ENDPOINT"),
    api_key=os.getenv("GITHUB_TOKEN"),
)

def analyze_incident(user_query):
    response = client.chat.completions.create(
        model=os.getenv("GITHUB_MODEL"),
        messages=[
            {
                "role": "system",
                "content": """You are a senior SRE engineer 
                specializing in incident analysis.
                When given an incident description, provide:
                
                1. ROOT CAUSE: What caused this issue
                2. SEVERITY: Critical/High/Medium/Low
                3. IMMEDIATE FIX: Step by step fix right now
                4. LONG TERM FIX: Prevent this from happening again
                5. ESTIMATED RESOLUTION TIME: How long to fix
                
                Be specific, clear and actionable.
                Format your response with these exact headings."""
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
    )
    
    return response.choices[0].message.content