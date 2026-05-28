import requests
import logging
from config import BASE_URL, PARAMS

logging.basicConfig(level=logging.INFO)

def fetch_weather_data():
    try:
        logging.info("Fetching weather data...")

        response = requests.get(BASE_URL, params=PARAMS)

        response.raise_for_status()

        data = response.json()

        logging.info("Weather data fetched successfully")

        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None
    