from django.shortcuts import render
from agents.models import AgentQuery, Incident

def home(request):
    total_queries = AgentQuery.objects.count()
    recent_queries = AgentQuery.objects.order_by(
        '-created_at')[:5]
    
    context = {
        'total_queries': total_queries,
        'recent_queries': recent_queries,
    }
    return render(request, 'core/home.html', context)