from django.shortcuts import render
from .router import route_query
from .incident import analyze_incident
from .cicd import debug_cicd
from .security import scan_security
from .runbook import generate_runbook
from .models import AgentQuery

def chat(request):
    response = None
    agent_used = None
    user_query = None

    if request.method == 'POST':
        user_query = request.POST.get('query')

        # Router decides which agent to use
        agent_used = route_query(user_query)

        # Call the right agent
        if agent_used == 'incident':
            response = analyze_incident(user_query)
        elif agent_used == 'cicd':
            response = debug_cicd(user_query)
        elif agent_used == 'security':
            response = scan_security(user_query)
        elif agent_used == 'runbook':
            response = generate_runbook(user_query)

        # Save to database
        AgentQuery.objects.create(
            agent_type=agent_used,
            user_query=user_query,
            ai_response=response
        )

    context = {
        'response': response,
        'agent_used': agent_used,
        'user_query': user_query,
    }

    return render(request, 'agents/chat.html', context)


def history(request):
    queries = AgentQuery.objects.all().order_by('-created_at')[:20]
    return render(request, 'agents/history.html', {'queries': queries})