import openai
import datetime
import json
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def text_to_JSON(query):
    primer = '''
    You are Calendar Bot. You are helping a user to create an event on Google Calendar.

    If the query does not contain an end time, assume that the event is 1 hour long. If the query does not contain a location, assume that the event location is TBD. If the query does not contain a date, assume that the event is today. 
        
    You will be given a query containing text about an event. You need to extract the relevant information from the text and return a JSON object containing the following fields:
    - start_date
    - end_date
    - start_time
    - end_time
    - event_name
    - location
    - description

    EXAMPLE INPUT: 
    Let's meet at 9am tomorrow at Starbucks for a quick meeting. 
    DATETIME: today is 2023-09-27, Tuesday

    EXAMPLE JSON OUTPUT:
    {
        "start_date": "20230927",
        "end_date": "20230927",
        "start_time": "090000",
        "end_time": "100000",
        "event_name": "Meeting",
        "location": "Starbucks",
        "description": "Let's meet at 9am tomorrow at Starbucks for a quick meeting."
    }
    '''
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    day_of_week = datetime.datetime.now().strftime("%A")
    augmented_query = f"QUERY: {query}\nDATETIME: today is {current_date}, {day_of_week}\nJSON OUTPUT:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": primer},
            {"role": "user", "content": augmented_query}
        ],
        temperature=1.0
    )

    response_text = response['choices'][0]['message']['content'].strip()
    parsed_response = json.loads(response_text)
    parsed_response["description"] = query
    return parsed_response
