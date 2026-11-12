import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")
PUUID = os.getenv("FAKER_PUUID")

def get_matches():
    url = (
        f"https://asia.api.riotgames.com/lol/match/v5/"
        f"matches/by-puuid/{PUUID}/ids"
    )

    params = {
        "start": 0,
        "count": 5,
        "queue": 420
    }

    headers = {
        "X-Riot-Token": API_KEY
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()
    match_ids = response.json()
    return match_ids