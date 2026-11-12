from get_matches import get_matches
from get_match_details import get_match_details, save_match

def main():
    match_ids = get_matches()

    for match_id in match_ids:
        match_data = get_match_details(match_id)

        if match_data:
            print(match_data)
            save_match(match_data)

if __name__ == "__main__":
    main()
