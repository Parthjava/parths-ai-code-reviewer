
import os
import openai
import requests

openai.api_key = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

async def review_pull_request(pr):
    diff_url = pr["diff_url"]
    comments_url = pr["comments_url"]
    files = requests.get(diff_url).text

    prompt = f"Review this code diff and suggest improvements:\n\n{files[:6000]}"

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    review_text = response["choices"][0]["message"]["content"]

    requests.post(
        comments_url,
        headers={"Authorization": f"token {GITHUB_TOKEN}"},
        json={"body": review_text},
    )
