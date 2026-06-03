from django.db import models

class AgentQuery(models.Model):
    AGENT_CHOICES = [
        ('incident', 'Incident Analyzer'),
        ('cicd', 'CI/CD Debugger'),
        ('security', 'Security Scanner'),
        ('runbook', 'Runbook Generator'),
    ]

    agent_type = models.CharField(
        max_length=50, 
        choices=AGENT_CHOICES
    )
    user_query = models.TextField()
    ai_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.agent_type} - {self.created_at}"

class Incident(models.Model):
    SEVERITY_CHOICES = [
        ('critical', 'Critical'),
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES
    )
    root_cause = models.TextField(blank=True)
    resolution = models.TextField(blank=True)
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title