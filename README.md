# HRhelper-employee-faq-chatbot


HRHelper – Employee FAQ Chatbot (FastAPI)


## Overview
HRHelper is a FastAPI-powered chatbot API that answers HR-related FAQs. It integrates with Slack’s free tier and provides a web-based fallback UI. Responses are served from a JSON dataset, and unmatched questions are logged for future improvements.

Features

✅ FastAPI Backend: High-performance API with automatic docs (/docs and /redoc).
✅ Slack Integration: Connects to Slack’s Events API for real-time messaging.
✅ Web UI: Minimalist chat interface (HTML/JS) for non-Slack users.
✅ FAQ Dataset: Answers sourced from faq_dataset.json.
✅ Logging: Unanswered questions saved to unknown_questions.log.

Setup
Prerequisites
Python 3.7+
Slack workspace (for Slack integration)
FastAPI dependencies:

bash

pip install fastapi uvicorn python-multipart slack-sdk
Installation
Clone the repo:

bash
git clone https://github.com/akhilkl52/HRHelper-employee-faq-chatbot.git
cd HRHelper

Install dependencies:

bash
pip install -r requirements.txt
Configure the FAQ dataset:

Add your Q&A pairs to faq_dataset.json


Running the API
Start the FastAPI server with Uvicorn:

bash
uvicorn main:app --reload
Access interactive docs at:

http://localhost:8000/docs

http://localhost:8000/redoc

Slack Integration

Create a Slack App:
Go to Slack API → "Create New App".
Enable Event Subscriptions and add the following events:
message.im (direct messages)
message.channels (public channels)
Set Up Webhook:
Under "Event Subscriptions", input your server’s /slack/events endpoint (e.g., https://yourdomain.com/slack/events).
Verify the URL using Slack’s challenge request.

Install App:
Navigate to "Install App" → "Install to Workspace".

Configure .env:
Add your Slack tokens:

text
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_SIGNING_SECRET=your-signing-secret
API Endpoints
POST /chat
Purpose: Get answers to HR questions.

Request:

json
{"message": "How can I apply for leave?"}
Response:

json
{"answer": "You can apply for leave through the HR portal under 'Leave Management"}
POST /slack/events
Purpose: Handle Slack event payloads.

Web UI
A simple chat interface is available at http://localhost:8000/static/index.html.

Uses Fetch API to call /chat.

Displays responses in a chat bubble format.

Logging
Unmatched questions are logged to unknown_questions.log. Example:

text
2025-08-11 12:00:00 | Unknown question: "hii"


Testing
Run tests with:

bash
pytest tests/
Tests cover:

FAQ matching logic

API response validation

Slack event parsing
