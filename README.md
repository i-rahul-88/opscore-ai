<div align="center">

# 🤖 OpsCore AI

### Multi-Agent DevOps Intelligence Platform

[![Microsoft Foundry IQ](https://img.shields.io/badge/Microsoft-Foundry%20IQ-0078d4?style=for-the-badge&logo=microsoft&logoColor=white)](https://ai.azure.com)
[![Microsoft Fabric IQ](https://img.shields.io/badge/Microsoft-Fabric%20IQ-7c3aed?style=for-the-badge&logo=microsoft&logoColor=white)](https://fabric.microsoft.com)
[![Microsoft Work IQ](https://img.shields.io/badge/Microsoft-Work%20IQ-00b4d8?style=for-the-badge&logo=microsoft&logoColor=white)](https://microsoft.com)
[![Django](https://img.shields.io/badge/Django-5.2-092e20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Hackathon](https://img.shields.io/badge/Agents%20League-AISF%202026-f97316?style=for-the-badge)](https://github.com)

> **Resolve production incidents, debug CI/CD pipelines, scan security vulnerabilities and auto-generate runbooks — all in plain English, powered by Microsoft Foundry IQ.**

[🚀 View Demo](#-demo) • [📖 Documentation](#-installation) • [🏆 Hackathon](#-hackathon-details) • [👨‍💻 Developer](#-developer)

</div>

---

## 🎯 Problem Statement

Every engineering team faces these critical daily challenges:

| Problem | Impact |
|---------|--------|
| 🔴 Production incidents at 2AM | 2-3 hours of manual debugging |
| 🟡 CI/CD pipeline failures | Deployment delays & lost productivity |
| 🔵 Security vulnerabilities | Compliance risks & data breaches |
| 🟣 Missing documentation | Knowledge gaps & onboarding delays |

**Engineering teams waste 3-4 hours daily** on manual troubleshooting across multiple disconnected tools — Grafana, GitHub, Slack, Confluence — switching contexts constantly while under pressure.

---

## 💡 Solution

**OpsCore AI** is a 5-agent DevOps intelligence platform that gives every engineering team a **24/7 AI-powered SRE expert** accessible through a single chat interface.

```
Engineer types problem in plain English
              ↓
Router Agent (Foundry IQ) analyzes & routes
              ↓
Specialist Agent provides detailed solution
              ↓
Analytics Dashboard (Fabric IQ) tracks everything
```

---

## 🎬 Demo

🎥 **Demo Video:** [Watch on YouTube](#)

🌐 **Repository:** https://github.com/i-rahul-88/opscore-ai

---

## ✨ Features

### 🔴 Incident Analyzer Agent
- Root cause analysis in under 30 seconds
- Severity classification (Critical/High/Medium/Low)
- Step-by-step immediate fix instructions
- Long-term prevention recommendations

### 🟡 CI/CD Debugger Agent
- Pipeline failure diagnosis & analysis
- Exact fix code provided instantly
- Pipeline optimization suggestions
- Prevention strategies for future

### 🔵 Security Scanner Agent
- Vulnerability detection in code & configs
- CVE reference numbers provided
- Security score rating (out of 10)
- Fix code for each vulnerability found

### 🟣 Runbook Generator Agent
- Professional runbook auto-creation
- Detailed step-by-step procedures
- Pre-requisites & verification steps
- Rollback plans included

### 📊 Analytics Dashboard (Fabric IQ)
- Real-time metrics & KPIs
- Agent usage breakdown donut chart
- Query history & activity tracking
- Microsoft Fabric IQ powered

---

## 🏗 Architecture

```
┌─────────────────────────────────────────┐
│            Engineer (User)              │
│      Types problem in plain English     │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│         Django Web Application          │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│       Router Agent (Foundry IQ)         │
│  Analyzes query & routes automatically  │
└──────┬──────────┬──────────┬────────────┘
       │          │          │        │
       ▼          ▼          ▼        ▼
  Incident    CI/CD      Security  Runbook
  Analyzer   Debugger    Scanner  Generator
                   │
                   ▼
┌─────────────────────────────────────────┐
│     Microsoft Fabric IQ Dashboard       │
│   Analytics, Charts, Metrics & History  │
└─────────────────────────────────────────┘
```

---

## 🤖 AI Agents

| Agent | Purpose | Triggered By |
|-------|---------|-------------|
| **Router Agent** | Routes queries to right specialist | All queries |
| **Incident Analyzer** | Production RCA & fixes | down, error, crash, OOM |
| **CI/CD Debugger** | Pipeline failure resolution | build, pipeline, deploy |
| **Security Scanner** | Vulnerability detection | scan, vulnerability, CVE |
| **Runbook Generator** | Documentation creation | runbook, procedure, steps |

---

## ⚡ Microsoft IQ Integration

### 🔷 Foundry IQ
- Powers all 5 AI agents
- Multi-step problem solving & analysis
- Autonomous intelligent query routing
- Natural language understanding

### 🔷 Fabric IQ
- Real-time analytics dashboard
- Agent usage breakdown charts
- Query history & metrics tracking
- Business intelligence insights

### 🔷 Work IQ
- Microsoft 365 integration
- Microsoft Teams deployment
- Enterprise-ready architecture
- Workplace productivity automation

---

## 🛠 Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Language | Python 3.11 | Core development |
| Framework | Django 5.2 | Web application |
| AI Engine | Microsoft Foundry IQ | Agent reasoning |
| Analytics | Microsoft Fabric IQ | Dashboard |
| Database | SQLite3 | Data storage |
| Frontend | Bootstrap 5.3 | User interface |
| Charts | Chart.js | Analytics charts |
| Version Control | GitHub | Code management |

---

## 🚀 Installation

### Step 1 — Clone Repository
```bash
git clone https://github.com/i-rahul-88/opscore-ai.git
cd opscore-ai
```

### Step 2 — Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Configure Environment
Create `.env` file in root directory:
```env
SECRET_KEY=your-django-secret-key
DEBUG=True
GITHUB_TOKEN=your-github-personal-access-token
GITHUB_MODEL=gpt-4o-mini
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
```

### Step 5 — Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6 — Start Server
```bash
python manage.py runserver
```

### Step 7 — Open Browser
```
http://127.0.0.1:8000
```

---

## 💡 Real World Example

### Without OpsCore AI
```
2:00 AM — Production server crashes
2:05 AM — Engineer wakes up
2:10 AM — Opens Grafana, checks metrics
2:20 AM — Opens GitHub, checks deployments
2:35 AM — Pings senior engineer on Slack
3:30 AM — Root cause finally found
4:00 AM — Incident report written manually
Total: 2+ hours of stress
```

### With OpsCore AI
```
2:00 AM — Production server crashes
2:01 AM — Engineer opens OpsCore AI
2:01 AM — Types problem in plain English
2:02 AM — Root cause identified by AI
2:02 AM — Fix steps provided immediately
2:03 AM — Runbook auto-generated
Total: Under 3 minutes ✅
```

---

## 🏆 Hackathon Details

**Event:** Agents League @ AISF 2026

**Tracks:** Reasoning Agents + Enterprise Agents

| Microsoft IQ Layer | Usage |
|-------------------|-------|
| Foundry IQ | Powers all 5 AI agents |
| Fabric IQ | Analytics dashboard |
| Work IQ | Enterprise Teams integration |

| Criterion | Weight |
|-----------|--------|
| Accuracy & Relevance | 20% |
| Reasoning & Multi-step | 20% |
| Creativity & Originality | 15% |
| UX & Presentation | 15% |
| Reliability & Safety | 20% |
| Community Vote | 10% |

---

## 👨‍💻 Developer

<div align="center">

**Rahul Thonukunuri**

🎓 Computer Science Engineering Student
🚀 Aspiring SRE & DevOps Engineer
🌍 Telangana, India

[![GitHub](https://img.shields.io/badge/GitHub-i--rahul--88-181717?style=for-the-badge&logo=github)](https://github.com/i-rahul-88)

</div>

---

<div align="center">

**Built with ❤️ for Agents League @ AISF 2026**

⚡ Powered by Microsoft Foundry IQ | 📊 Microsoft Fabric IQ | 💼 Microsoft Work IQ

⭐ Star this repo if you found it useful!

</div>