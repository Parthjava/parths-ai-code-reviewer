
from fastapi import FastAPI, Request
from review import review_pull_request

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    if "pull_request" in data:
        await review_pull_request(data["pull_request"])
    return {"status": "ok"}
