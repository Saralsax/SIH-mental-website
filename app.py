from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess

app = FastAPI()

# Mount static files if you have CSS/JS inside "static" folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates (same as Flask render_template)
templates = Jinja2Templates(directory="templates")

def query_ollama(prompt: str) -> str:
    """Send prompt to Ollama and return response."""
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.2", prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error connecting to Ollama: {e}"

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    if not user_message:
        return JSONResponse(content={"reply": "Please say something."})
    
    bot_reply = query_ollama(user_message)
    return JSONResponse(content={"reply": bot_reply})

# Run with: uvicorn app:app --reload
