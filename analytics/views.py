from django.shortcuts import render
from agents.models import AgentQuery

def dashboard(request):
    total = AgentQuery.objects.count()
    
    incident = AgentQuery.objects.filter(
        agent_type='incident').count()
    cicd = AgentQuery.objects.filter(
        agent_type='cicd').count()
    security = AgentQuery.objects.filter(
        agent_type='security').count()
    runbook = AgentQuery.objects.filter(
        agent_type='runbook').count()
    
    recent = AgentQuery.objects.order_by(
        '-created_at')[:10]
    
    context = {
        'total': total,
        'incident': incident,
        'cicd': cicd,
        'security': security,
        'runbook': runbook,
        'recent': recent,
    }
    
    return render(request, 
        'analytics/dashboard.html', context)