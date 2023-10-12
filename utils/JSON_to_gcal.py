import urllib.parse

def json_to_google_calendar_link(event_data):
    base_url = "https://www.google.com/calendar/render?action=TEMPLATE"
    
    start_date = event_data.get('start_date', '')
    end_date = event_data.get('end_date', '')
    start_time = event_data.get('start_time', '')
    end_time = event_data.get('end_time', '')
    event_name = event_data.get('event_name', '')
    location = event_data.get('location', '')
    description = event_data.get('description', '')

    start_datetime = f"{start_date}T{start_time}"
    end_datetime = f"{end_date}T{end_time}"

    query_params = {
        'text': event_name,
        'dates': f"{start_datetime}/{end_datetime}",
        'location': location,
        'details': description
    }

    url_params = urllib.parse.urlencode(query_params)
    google_calendar_url = f"{base_url}&{url_params}"
    
    return google_calendar_url


