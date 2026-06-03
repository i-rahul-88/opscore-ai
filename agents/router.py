import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("GITHUB_ENDPOINT"),
    api_key=os.getenv("GITHUB_TOKEN"),
)

def route_query(user_query):
    response = client.chat.completions.create(
        model=os.getenv("GITHUB_MODEL"),
        messages=[
            {
                "role": "system",
                "content": """You are a DevOps query router.
                Analyze the user query and respond with ONLY one word:
                - incident → if about system failures, errors, downtime
                - cicd → if about build failures, pipelines, deployments
                - security → if about vulnerabilities, security issues
                - runbook → if about procedures, documentation, steps
                Just respond with one word only."""
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
    )
    
    agent = response.choices[0].message.content.strip().lower()
    
    valid_agents = ['incident', 'cicd', 'security', 'runbook']
    if agent not in valid_agents:
        agent = 'incident'
    
    return agent