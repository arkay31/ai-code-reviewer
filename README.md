AI Code Reviewer Bot
Overview

AI Code Reviewer is an automated GitHub bot that reviews Pull Requests using AI.
When a PR is opened or updated, the system fetches the code diff, analyzes it using an LLM, and posts review feedback directly on the PR.

This helps developers identify potential bugs, code quality issues, and improvements automatically.

Features

Automated AI-based Pull Request review

GitHub App integration

Code diff analysis

AI-powered suggestions

Automatic PR comment generation

Cloud deployment (Render)

Architecture

Workflow:

Developer opens a Pull Request on GitHub

GitHub triggers a webhook

FastAPI backend receives the webhook

The system fetches the PR diff

The diff is sent to an AI model (Groq)

AI generates a structured code review

The bot posts the review as a PR comment

Tech Stack

Backend

Python

FastAPI

AI Model

Groq LLM API

GitHub Integration

GitHub Apps

Webhooks

Installation Tokens

REST API

Deployment

Render (Cloud Hosting)

Project Structure
ai-code-reviewer
│
├── main.py          # FastAPI webhook server
├── auth.py          # GitHub App authentication
├── llm.py           # AI code review logic
├── requirements.txt # Dependencies
└── README.md
Setup Instructions
1 Clone the Repository
git clone https://github.com/arkay31/ai-code-reviewer.git
cd ai-code-reviewer
2 Create Virtual Environment
python -m venv venv
source venv/bin/activate
3 Install Dependencies
pip install -r requirements.txt
4 Add Environment Variables

Create a .env file.

GROQ_API_KEY=your_groq_api_key
GITHUB_APP_ID=your_github_app_id
GITHUB_PRIVATE_KEY=your_private_key
Running Locally

Start the FastAPI server:

uvicorn main:app --reload --port 8000

Expose the server to GitHub using ngrok:

ngrok http 8000

Update the GitHub webhook URL with the ngrok endpoint.

Production Deployment

The project is deployed on Render.

Production API:

https://ai-code-reviewer-lhbt.onrender.com

Webhook endpoint:

/webhook
Example AI Review Output
Potential Bugs:
- No input validation for user input.

Code Quality:
- Function naming could be more descriptive.

Security Concerns:
- API keys should not be hardcoded.

Suggestions:
- Add error handling for API calls.
Future Improvements

Inline code comments on specific lines

Support for multiple repositories

Security vulnerability detection

Code scoring system

GitHub Checks integration

Author

Rakshit Kapoor

GitHub:
https://github.com/arkay31

License

MIT License
