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
    
    steps = text.split(':')
    title = steps[0].split('\n')[0]

    instructions = []
    descriptions = []

    for idx, step in enumerate(steps[1:]):
        pair = step.split("Step")[0].split('<image>')
        instructions.append(f'Step {idx+1}: {pair[0].strip()}')
        descriptions.append(pair[1].strip())
        description_to_image(descriptions[-1], idx)

    images = [f"static/{idx}.png" for idx, _ in enumerate(descriptions)]
    
    zipped_steps_images = list(zip(instructions, images))
    
    print(title)
    print(descriptions)
    print()
    
    return templates.TemplateResponse("index.html", {"request": request, "title": title, "zipped_steps_images": zipped_steps_images})
