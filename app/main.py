from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .utils import find_best_match, log_unknown_question
from .slack_handler import router as slack_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.include_router(slack_router)

@app.post("/chat")
async def chat(user_message: str = Form(...)):
    answer = find_best_match(user_message)
    if not answer:
        log_unknown_question(user_message)
        answer = "Sorry, I don't have an answer for that."
    return JSONResponse({"answer": answer})

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
