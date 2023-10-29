from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    text = """How to Be a Tour Guide in Paris

Step 1: Learn the History and Culture
Study the rich history and vibrant culture of Paris, including famous landmarks, art, and cuisine.
<image> Image of a person reading a book or studying about Parisian history and culture. <image>

Step 2: Know the Top Attractions
Familiarize yourself with popular tourist destinations, such as the Eiffel Tower, Louvre Museum, and Notre-Dame Cathedral.
<image> Image of a person holding a map with marked locations of top attractions in Paris. <image>

Step 3: Master the Language
Learn basic French phrases to communicate with both locals and tourists. Practice pronunciation and common expressions.
<image> Image of a person using language learning resources or talking to a language tutor. <image>

Step 4: Develop a Route
Plan an efficient and engaging tour route that covers major landmarks and offers interesting insights and facts.
<image> Image of a person using a map and plotting a tour route with important stops in Paris. <image>

Step 5: Provide Interesting Facts and Stories
Research captivating historical anecdotes and interesting facts about the attractions to share with your tour group.
<image> Image of a person reading a book or browsing the internet for intriguing facts about Paris. <image>

Step 6: Enhance Communication Skills
Practice clear and engaging communication techniques, such as storytelling, effective body language, and group interaction.
<image> Image of a person practicing public speaking or conducting a mock tour for friends. <image>

Step 7: Learn to Handle Different Situations
Gain knowledge on managing diverse groups, handling unexpected challenges, and providing excellent customer service.
<image> Image of a person role-playing common situations like lost tourists or changes in itinerary. <image>

Step 8: Stay Updated with Current Events
Stay informed on local events, exhibitions, and festivals happening in Paris to offer the latest recommendations to your group.
<image> Image of a person reading newspapers or browsing websites to stay updated on current events in Paris. <image>

Step 9: Obtain Necessary Licenses
Check the legal requirements and obtain any necessary licenses or permits to operate as a tour guide in Paris.
<image> Image of a person filling out paperwork or applying for licenses to become a certified tour guide in Paris. <image>

Step 10: Offer Excellent Customer Service
Provide a friendly, informative, and memorable experience for your tour group. Offer assistance and address their needs.
<image> Image of a person interacting with a tour group, answering questions and providing assistance. <image>
"""

    steps = text.split('<image>')[::2]  # Text steps
    images = [f"static/{idx}.png" for idx, _ in enumerate(text.split('<image>')[1::2])]  # Image paths
    zipped_steps_images = list(zip(steps, images))
    print(zipped_steps_images)
    return templates.TemplateResponse("index.html", {"request": request, "zipped_steps_images": zipped_steps_images})