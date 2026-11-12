import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")

GAME_NAME = "hide on bush"
TAG_LINE = "KR1"

url = (
    "https://asia.api.riotgames.com/riot/account/v1/"
    f"accounts/by-riot-id/{GAME_NAME}/{TAG_LINE}"
)

headers = {
    "X-Riot-Token": API_KEY
}

response = requests.get(
    url,
    headers=headers,
    timeout=15
)

response.raise_for_status()

account = response.json()

print("Game Name:", account["gameName"])
print("Tag Line:", account["tagLine"])
print("PUUID:", account["puuid"])