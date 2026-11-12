from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent / "template"))


@app.get("/", response_class=HTMLResponse)
@app.get("/index.html", response_class=HTMLResponse)
def my_page(request:Request, message:str=""):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"message": message},
    )
