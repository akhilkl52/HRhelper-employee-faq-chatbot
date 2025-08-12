import json
import difflib
from datetime import datetime

FAQ_PATH = "app/faq_data.json"
LOG_FILE = "unknown_questions.log"

def load_faq():
    with open(FAQ_PATH, "r") as f:
        return json.load(f)

def find_best_match(user_input):
    faqs = load_faq()
    questions = [faq["question"] for faq in faqs]
    match = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.6)
    if match:
        return next((faq["answer"] for faq in faqs if faq["question"] == match[0]), None)
    return None

def log_unknown_question(question):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {question}\n")
