import requests
import json
import os


def walk(players_id, file_name):
    # Iterare attraverso un range di ID
    base_url = "https://api.sofascore.app/api/v1/player/{}"
    data_players = []
    for player_id in players_id:
        url = base_url.format(player_id)
        try:
            response = requests.get(url)

            # Se la risposta non è 404, analizzarla
            if response.status_code != 404:
                data = response.json()

                try:
                    data_players.append(data)
                except KeyError:
                    # Gestire il caso in cui il campo non sia presente
                    continue
        except Exception as e:
            pass
    
    os.makedirs('./data/', exist_ok=True)
    with open(f"./data/{file_name}", "a", encoding="utf-8") as file:
        json.dump(data_players, file, ensure_ascii=False, indent=4)
        file.write("\n")

