import os
import json
import requests
from dotenv import load_dotenv
from get_matches import get_matches

load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")
PUUID = os.getenv("FAKER_PUUID")
match_ids = get_matches()

def get_match_details(match_id):
    url = (
        f"https://asia.api.riotgames.com/lol/match/v5/"
        f"matches/{match_id}"
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

    match_data = response.json()
    info = match_data["info"]

    for participant in info["participants"]:
        if participant["puuid"] == PUUID:

            match_data = {
                "match_id": match_id,
                "champion": participant["championName"],
                "kills": participant["kills"],
                "deaths": participant["deaths"],
                "assists": participant["assists"],
                "result": "Win" if participant["win"] else "Loss"
            }
            return match_data
    return None

def save_match(match_data):
    FILE_NAME = "faker_matches.json"

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            matches = json.load(f)
    else:
        matches = []

    existing_ids = {
        match["match_id"] for match in matches
    }

    if match_data["match_id"] not in existing_ids:
        matches.append(match_data)

        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(matches, f, ensure_ascii=False, indent=4)

        print("New match saved!")
    else:
        print("Match already exists!")