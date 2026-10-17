import requests


def get_weather(city):
    try:
        # Find the city's latitude and longitude
        location_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

        location_response = requests.get(location_url, timeout=10)
        location_data = location_response.json()

        if "results" not in location_data:
            return None

        latitude = location_data["results"][0]["latitude"]
        longitude = location_data["results"][0]["longitude"]

        # Get the current weather
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}&longitude={longitude}"
            f"&current=temperature_2m,wind_speed_10m"
        )

        weather_response = requests.get(weather_url, timeout=10)
        weather_data = weather_response.json()

        temperature = weather_data["current"]["temperature_2m"]
        wind_speed = weather_data["current"]["wind_speed_10m"]

        return temperature, wind_speed

    except requests.exceptions.RequestException:
        return None