# app/slack_handler.py
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import json
from pathlib import Path
import httpx
import os

router = APIRouter()

# Load FAQ data from JSON
faq_path = Path(__file__).parent / "faq_data.json"
with open(faq_path, "r", encoding="utf-8") as f:
    faq_data = json.load(f)

# Slack bot token from environment
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")


def find_faq_answer(user_message: str) -> str:
    """Search FAQ for an answer based on exact or partial match."""
    user_message_lower = user_message.lower()
    for faq in faq_data:
        if faq["question"].lower() in user_message_lower:
            return faq["answer"]
    return None


async def send_message_to_slack(channel: str, text: str):
    """Send a message to a Slack channel."""
    url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}
    payload = {"channel": channel, "text": text}

    async with httpx.AsyncClient() as client:
        await client.post(url, headers=headers, json=payload)


@router.post("/slack/events")
async def slack_events(request: Request):
    body = await request.json()

    # URL verification challenge
    if body.get("type") == "url_verification":
        return JSONResponse(content={"challenge": body.get("challenge")})

    # Handle event callbacks
    if "event" in body:
        event = body["event"]

        # Ignore bot messages
        if event.get("subtype") == "bot_message":
            return JSONResponse(content={"status": "ignored"})

        # Handle user messages
        if event.get("type") == "message" and "text" in event:
            user_message = event["text"]
            channel = event["channel"]

            answer = find_faq_answer(user_message)
            if answer:
                await send_message_to_slack(channel, answer)
            else:
                await send_message_to_slack(
                    channel,
                    "Sorry, I couldn't find an answer to that in the FAQ."
                )

    return JSONResponse(content={"status": "ok"})
