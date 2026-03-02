import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def review_code(diff_text: str) -> str:
    """
    Sends git diff to Groq LLM and returns structured code review.
    """

    if not diff_text:
        return "No diff content found to review."

    # Limit size to prevent token overflow
    diff_text = diff_text[:8000]

    prompt = f"""
You are a senior software engineer reviewing a pull request.

Analyze the following git diff and provide:

1. Potential bugs
2. Code quality improvements
3. Security concerns (if any)
4. Suggestions for improvement

Be concise, professional, and structured.

Git Diff:
{diff_text}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Updated supported model
            messages=[
                {
                    "role": "system",
                    "content": "You are a strict and detail-oriented senior code reviewer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ AI Review failed due to error: {str(e)}"