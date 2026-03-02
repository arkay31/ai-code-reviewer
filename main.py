from fastapi import FastAPI, Request
import requests
from auth import get_installation_token
from llm import review_code
from dotenv import load_dotenv
import traceback

load_dotenv()

app = FastAPI()


@app.post("/webhook")
async def github_webhook(request: Request):
    try:
        payload = await request.json()

        print("\n==============================")
        print("🔔 WEBHOOK RECEIVED")
        print("Action:", payload.get("action"))
        print("==============================\n")

        # Trigger on new PR or updated PR
        if payload.get("action") in ["opened", "synchronize"]:

            pr_number = payload["pull_request"]["number"]
            repo_name = payload["repository"]["full_name"]
            installation_id = payload["installation"]["id"]

            print(f"📌 PR #{pr_number} in {repo_name}")
            print(f"🔐 Installation ID: {installation_id}")

            # Get GitHub installation token
            token = get_installation_token(installation_id)

            if not token:
                print("❌ Failed to get installation token")
                return {"status": "error getting token"}

            headers = {
                "Authorization": f"token {token}",
                "Accept": "application/vnd.github+json"
            }

            # Fetch PR details
            pr_url = f"https://api.github.com/repos/{repo_name}/pulls/{pr_number}"
            pr_response = requests.get(pr_url, headers=headers)

            if pr_response.status_code != 200:
                print("❌ Failed to fetch PR details")
                print(pr_response.text)
                return {"status": "error fetching PR"}

            pr_data = pr_response.json()

            # Fetch diff
            diff_url = pr_data.get("diff_url")
            diff_response = requests.get(diff_url, headers=headers)

            if diff_response.status_code != 200:
                print("❌ Failed to fetch diff")
                print(diff_response.text)
                return {"status": "error fetching diff"}

            diff_text = diff_response.text

            print("\n🚀 Sending diff to Groq...")

            # Limit diff size to avoid token overflow
            diff_text = diff_text[:8000]

            # Generate AI review
            review = review_code(diff_text)

            print("\n🤖 AI Review Generated:\n")
            print(review)

            # Post comment on PR
            comment_url = f"https://api.github.com/repos/{repo_name}/issues/{pr_number}/comments"

            comment_response = requests.post(
                comment_url,
                headers=headers,
                json={"body": f"## 🤖 AI Code Review\n\n{review}"}
            )

            if comment_response.status_code == 201:
                print("\n✅ Comment posted successfully!")
            else:
                print("\n❌ Failed to post comment")
                print(comment_response.text)

        return {"status": "received"}

    except Exception as e:
        print("\n❌ ERROR OCCURRED:")
        traceback.print_exc()
        return {"status": "internal error"}