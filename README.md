# 🤖 AI Code Reviewer

AI Code Reviewer is an automated GitHub bot that reviews Pull Requests using AI.  
When a PR is opened or updated, the system fetches the code changes, analyzes them using an LLM, and posts review feedback directly on the Pull Request.

This helps developers identify potential bugs, code quality issues, and improvement suggestions automatically.

---

## 🚀 Features

- Automated AI-based Pull Request review
- GitHub App integration
- Code diff analysis
- AI-powered suggestions
- Automatic PR comment generation
- Cloud deployment (Render)

---

## 🧠 How It Works

1. A developer opens a Pull Request on GitHub.
2. GitHub triggers a webhook event.
3. The FastAPI backend receives the webhook.
4. The system fetches the PR code diff using the GitHub API.
5. The diff is sent to an AI model (Groq LLM).
6. The AI analyzes the code and generates a structured review.
7. The bot posts the review as a comment on the Pull Request.

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI

### AI Model
- Groq LLM API

### GitHub Integration
- GitHub Apps
- Webhooks
- Installation Tokens
- GitHub REST API

### Deployment
- Render (Cloud Hosting)

---

## 📁 Project Structure

```
ai-code-reviewer
│
├── main.py          # FastAPI webhook server
├── auth.py          # GitHub App authentication
├── llm.py           # AI code review logic
├── requirements.txt # Project dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/arkay31/ai-code-reviewer.git
cd ai-code-reviewer
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file and add:

```
GROQ_API_KEY=your_groq_api_key
GITHUB_APP_ID=your_github_app_id
GITHUB_PRIVATE_KEY=your_private_key
```

---

## ▶️ Running Locally

Start the FastAPI server:

```bash
uvicorn main:app --reload --port 8000
```

Expose the server using ngrok:

```bash
ngrok http 8000
```

Update your GitHub App webhook URL with the ngrok endpoint.

---

## 🌍 Production Deployment

The project is deployed on Render.

**Production URL**

```
https://ai-code-reviewer-lhbt.onrender.com
```

**Webhook Endpoint**

```
/webhook
```

---

## 🧪 Example AI Review Output

```
Potential Bugs:
- Missing input validation in the function.

Code Quality Improvements:
- Variable naming could be more descriptive.

Security Concerns:
- API keys should not be hardcoded.

Suggestions:
- Add proper error handling for API requests.
```

---

## 🔮 Future Improvements

- Inline comments on specific lines of code
- Support for multiple repositories
- Security vulnerability detection
- Code quality scoring
- GitHub Checks API integration
- Web dashboard for analytics

---

## 👨‍💻 Author

**Rakshit Kapoor**

GitHub  
https://github.com/arkay31

---

## 📜 License

MIT License
