from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Define the path to the HTML templates
template_path = Path(__file__).parent / "templates"

# Serve static files (CSS, JavaScript, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open(template_path / "index.html") as file:
        content = file.read()
    return HTMLResponse(content=content)


@app.get("/api/data")
async def get_data():
    return {"message": "Hello, World!"}
