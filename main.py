from scrapers.scrape_for_ids import scrape_and_save
from scrapers.scrape_for_data import walk

teams = {
    "inter": "https://www.sofascore.com/team/football/inter/2697",
    "juventus": "https://www.sofascore.com/team/football/juventus/2687",
    "milan": "https://www.sofascore.com/team/football/milan/2692",
    "fiorentina": "https://www.sofascore.com/team/football/fiorentina/2693",
    "atalanta": "https://www.sofascore.com/team/football/atalanta/2686",
    "lazio": "https://www.sofascore.com/team/football/lazio/2699",
    "roma": "https://www.sofascore.com/team/football/roma/2702",
    "bologna": "https://www.sofascore.com/team/football/bologna/2685",
    "napoli": "https://www.sofascore.com/team/football/napoli/2714",
    "torino": "https://www.sofascore.com/team/football/torino/2696",
    "genoa": "https://www.sofascore.com/team/football/genoa/2713",
    "monza": "https://www.sofascore.com/team/football/monza/2729",
    "lecce": "https://www.sofascore.com/team/football/lecce/2689",
    "sassuolo": "https://www.sofascore.com/team/football/sassuolo/2793",
    "udinese": "https://www.sofascore.com/team/football/udinese/2695",
    "cagliari": "https://www.sofascore.com/team/football/cagliari/2719",
    "hellas-verona": "https://www.sofascore.com/team/football/hellas-verona/2701",
    "empoli": "https://www.sofascore.com/team/football/empoli/2705",
    "salernitana": "https://www.sofascore.com/team/football/salernitana/2710",
}

for team in teams:
    id_players = scrape_and_save({team: teams[team]})
    file_name = f"{team}.json"
    walk(file_name=file_name, players_id=id_players)

