from fastapi import FastAPI, Request
import requests
import os
from auth import get_installation_token
from llm import generate_review

app = FastAPI()

# --------------------------------------
# Home route (so browser doesn't show 404)
# --------------------------------------
@app.get("/")
def home():
    return {
        "project": "AI Code Reviewer",
        "status": "Live",
        "message": "This service automatically reviews GitHub Pull Requests using AI."
    }


# --------------------------------------
# Webhook route for GitHub
# --------------------------------------
@app.post("/webhook")
async def webhook(request: Request):

    payload = await request.json()

    # Check event type
    action = payload.get("action")
    pull_request = payload.get("pull_request")

    if pull_request is None:
        return {"message": "No PR data"}

    if action not in ["opened", "synchronize", "reopened"]:
        return {"message": "Event ignored"}

    repo = payload["repository"]["full_name"]
    pr_number = pull_request["number"]
    installation_id = payload["installation"]["id"]

    print(f"PR #{pr_number} in {repo}")
    print(f"Installation ID: {installation_id}")

    # --------------------------------------
    # Get GitHub installation token
    # --------------------------------------
    token = get_installation_token(installation_id)

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    # --------------------------------------
    # Fetch PR diff
    # --------------------------------------
    diff_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    response = requests.get(diff_url, headers=headers)

    diff_data = response.json()
    diff = diff_data.get("body", "")

    print("🚀 Sending diff to AI...")

    # --------------------------------------
    # Send diff to AI model
    # --------------------------------------
    review = generate_review(diff)

    print("🤖 AI Review Generated")

    # --------------------------------------
    # Post comment to PR
    # --------------------------------------
    comment_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    comment_body = {
        "body": review
    }

    requests.post(comment_url, headers=headers, json=comment_body)

    print("✅ Comment posted successfully!")

    return {"message": "Review completed"}