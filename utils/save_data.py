from pymongo import MongoClient
from dotenv import load_dotenv
import os

def get_database():
    load_dotenv()
    username = os.getenv("MONGO_DB_USERNAME")
    password = os.getenv("MONGO_DB_PASSWORD")
    database_name = 'query-to-json'
    collection_name = 'calendar'
    
    client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.6daltzl.mongodb.net/?retryWrites=true&w=majority")

    try: # make sure we are connected
        client.list_database_names()
    except Exception as e:
        return None

    db = client[database_name]
    collection = db[collection_name]

    return collection

def save_data(query, event_data):
    if not event_data: # event_data cannot be completely empty
        return 

    collection = get_database()

    if collection is None: # something went wrong, abort
        return

    data = {
        'query': query,
        'start_date': event_data.get('start_date', None),
        'end_date': event_data.get('end_date', None),
        'start_time': event_data.get('start_time', None),
        'end_time': event_data.get('end_time', None),
        'event_name': event_data.get('event_name', None),
        'location': event_data.get('location', None)
    }
    
    collection.insert_one(data)

