from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    text = '''
Step 1: Learn the History and Culture
Study the rich history and vibrant culture of Paris, including famous landmarks, art, and cuisine.
<image> Image of a person reading a book or studying about Parisian history and culture. <image>

Step 2: Know the Top Attractions
Familiarize yourself with popular tourist destinations, such as the Eiffel Tower, Louvre Museum, and Notre-Dame Cathedral.
<image> Image of a person holding a map with marked locations of top attractions in Paris. <image>
    '''
    steps = text.split('<image>')
    return templates.TemplateResponse("index.html", {"request": request, "steps": steps})
