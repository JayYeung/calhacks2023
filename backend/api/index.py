from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from backend.utils.get_gpt_response import get_gpt_response
from backend.utils.description_to_image import description_to_image

app = FastAPI()
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

ALLOWED_ORIGINS = ["http://localhost:3000"]
TEMPLATES = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request): 
    return TEMPLATES.TemplateResponse("search.html", {"request": request})

@app.get("/query")
async def query_instructions(query: str):
    print(query)
    try:
        text_response = get_gpt_response(query)
        title, *steps = text_response.split(':')
        title = title.split('\n')[0]

        parsed_data = parse_steps(steps)
        return {
            "title": title,
            "steps": parsed_data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error processing query")

def parse_steps(steps: list) -> list:
    parsed_data = []
    for idx, step in enumerate(steps, start=1):
        segments = step.split('<image>', 1)  
        
        if len(segments) != 2:
            continue

        instruction, description = segments
        if not instruction.startswith("Step"):
            instruction = f'Step {idx}:{instruction}'
        else:
            instruction = f'Step {idx}: {instruction.split(":", 1)[1]}'
        
        print(f'instructions {instruction}')
        print(f'description {description}')
        parsed_data.append({
            "instruction": instruction.strip(),
            "image_path": description_to_image(description.split("<image>")[0].strip())
        })
    return parsed_data

