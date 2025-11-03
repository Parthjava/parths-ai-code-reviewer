
# Parth’s AI Code Reviewer 🤖

An automated GitHub bot that reviews pull requests using GPT-4.

## Features
- Auto-analyzes code diffs from pull requests
- Uses GPT-4 to provide intelligent review suggestions
- Posts comments directly to the PR

## Stack
- **Backend:** Python (FastAPI)
- **LLM:** OpenAI GPT-4
- **Automation:** GitHub Actions

## Setup
1. Add `OPENAI_API_KEY` and `GITHUB_TOKEN` in GitHub Secrets.
2. Push code to GitHub.
3. The bot automatically reviews new pull requests.
