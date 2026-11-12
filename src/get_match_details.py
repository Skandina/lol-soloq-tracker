import os
import json
import requests
from dotenv import load_dotenv
from get_matches import get_matches

load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")
PUUID = "zIfXhAnk2-EuapxEbFe5U2yzGKiUcofnpGZzLfO5gZh1IfI6nWFVPdZVgyBKQAY-1PFpk79qekmdxA"
match_ids = get_matches()

for match_id in match_ids:
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

            print(match_data)

        # 결과를 json파일에 저장 
            FILE_NAME = "faker_matches.json"

            # 기존 데이터 불러오기
            if os.path.exists(FILE_NAME):
                with open(FILE_NAME, "r", encoding="utf-8") as f:
                    matches = json.load(f)
            else:
                matches = []

            # 기존 Match ID 확인
            existing_ids = {match["match_id"] for match in matches}

            if match_data["match_id"] not in existing_ids:
                matches.append(match_data)

                with open(FILE_NAME, "w", encoding="utf-8") as f:
                    json.dump(matches, f, ensure_ascii=False, indent=4)

                print("New match saved!")
            else:
                print("Match already exists!")