from fastapi import FastAPI
from utils.text_to_JSON import text_to_JSON
from utils.JSON_to_gcal import json_to_google_calendar_link

app = FastAPI()

@app.get("/api/hello")
def hello_world():
    return {"message": "Hello World"}

@app.get("/api/convert")
def convert(text: str): 
    json = text_to_JSON(text)
    link = json_to_google_calendar_link(json)
    return {"link": link}