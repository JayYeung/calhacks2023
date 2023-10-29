from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
from utils.get_gpt_response import get_gpt_response
from utils.description_to_image import description_to_image

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request): 
    return templates.TemplateResponse("search.html", {"request": request})

@app.get("/query", response_class=HTMLResponse)
async def read_item(request: Request, query: str):
    text = get_gpt_response(query)
    
    print(text)
    
    for idx, description in enumerate(text.split('<image>')[1::2]):
        description_to_image(description, idx)
        print('description', description)

    steps = text.split('<image>')[::2]  # Text steps
    images = [f"static/{idx}.png" for idx, _ in enumerate(text.split('<image>')[1::2])]  # Image paths
    zipped_steps_images = list(zip(steps, images))
    print(zipped_steps_images)
    return templates.TemplateResponse("index.html", {"request": request, "zipped_steps_images": zipped_steps_images})