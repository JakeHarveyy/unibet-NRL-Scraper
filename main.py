import requests

UNITBET_NRL_MATCHUP_URL = "https://www.unibet.com.au/sportsbook-feeds/views/filter/rugby_league/nrl/all/matches?includeParticipants=true&useCombined=true&ncid=1739342881"

def get_headers():
    headers = {
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "priority": "u=1, i",
        "referer": "https://www.unibet.com.au/betting/sports/filter/rugby_league/nrl/all/matches",
        "requestor": "type=sys; src=unknown;",
        "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }
    return headers


def fetch_matchups(headers):
    response = requests.get(UNITBET_NRL_MATCHUP_URL, headers=headers)
    data = response.json()
    return data["layout"]["sections"][1]["widgets"][0]["matches"]["events"]

def filter_matchups(matchups):
    return {
        matchup["id"]: {
            "Home Team" : matchup["event"]["homeName"],
            "Away Team" : matchup["event"]["awayName"],
            "Start Time": matchup["event"]["start"],
            "Home Team Odds" : matchup["mainBetOffer"]["outcomes"][0]["oddsDecimal"],
            "Away Team Odds" : matchup["mainBetOffer"]["outcomes"][1]["oddsDecimal"],
        }
        for matchup in matchups
    }

def main():
    headers = get_headers()
    matchups = fetch_matchups(headers)
    filtered_matchups = filter_matchups(matchups)

    for matchup_id, data in filtered_matchups.items():
        print(f"Start Time: {data["Start Time"]}")
        print(f"{data["Home Team"]} Odds : ${data["Home Team Odds"]}")
        print(f"{data["Away Team"]} Odds : ${data["Away Team Odds"]}")
        print("-"*40)

if __name__ == "__main__":
    main()

