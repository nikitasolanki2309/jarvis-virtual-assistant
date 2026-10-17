import requests
import os

def get_news():
    newsapi = os.getenv("NEWS_API_KEY")

    try:
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
        )

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            return articles[:5]

        return []

    except requests.exceptions.RequestException:
        return []