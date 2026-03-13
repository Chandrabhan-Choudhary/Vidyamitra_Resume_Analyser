import requests
import os
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def search_images(query):

    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": query,
        "per_page": 5
    }

    response = requests.get(url, headers=headers, params=params)

    data = response.json()

    images = []

    for photo in data.get("photos", []):

        images.append({
            "image_url": photo["src"]["medium"],
            "photographer": photo["photographer"]
        })

    return images