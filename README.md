# Calendar Bot Backend

## Overview

This project serves as the backend for the Calendar Bot, a service that helps users create events on Google Calendar. The backend is built using FastAPI and is hosted on Vercel.

## Installation

### Prerequisites

-   Python 3.9+
-   FastAPI
-   Uvicorn
-   OpenAI Python package

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/JayYeung/calendar-bot-backend.git
    ```

2. Navigate into the project directory:

    ```bash
    cd calendar-bot-backend
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file to store your OpenAI API key:
    ```bash
    echo "API_KEY=your_openai_api_key_here" > .env
    ```

### Running Locally

1. Start the server:

    ```bash
    npm run fastapi-dev
    ```

2. The server will start at `http://127.0.0.1:8000/`. You can test the API endpoints using Postman or any API testing tool.

### Deploying to Vercel

Endpoint will always begin with `https://calendar-bot-backend.vercel.app/`, then followed by the API endpoint.

## API Endpoints

1. `GET /api/hello`
   returns a simple JSON response to test if the server is running

2. `GET /api/convert`
   returns a JSON response with the converted event details
