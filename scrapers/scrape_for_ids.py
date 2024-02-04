import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "your-user-agent-string",
    "Accept": "application/json",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
}


def scrape_and_save(data_dict):
    for nome_file, url_web in data_dict.items():
        try:
            response = requests.get(url_web, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                links = soup.find_all("a", href=True)

                ids_set = set()
                for link in links:
                    href = link["href"]
                    if "/player/" in href:
                        parts = href.split("/")
                        if len(parts) == 4:
                            player_id = parts[-1]
                            ids_set.add(player_id)

                ids_list = list(ids_set)

                if ids_set:
                    # with open(f"{nome_file}.txt", "w") as file:
                    #     for player_id in ids_set:
                    #         file.write(f"{player_id}\n")
                    print(
                        f"{nome_file.capitalize()} players' data have been retrieved."
                    )

                else:
                    print(f"Nessun dato trovato su {url_web}")
            else:
                print(
                    f"Errore {response.status_code} durante il recupero dei dati da {url_web}"
                )
        except Exception as e:
            print(f"Errore durante il recupero dei dati da {url_web}: {str(e)}")
    return ids_list
