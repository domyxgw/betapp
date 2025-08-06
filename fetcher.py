import requests
API_KEY = "TWÓJ_API_KEY"
BOOKMAKERS = ["betclic", "sts", "superbet", "fuksiarz"]

def fetch_odds(sport="soccer"):
    url = f"https://api.the-odds-api.com/v4/sports/{sport}/odds"
    params = {
        "apiKey": API_KEY,
        "regions": "eu",
        "markets": ["h2h"],
        "bookmakers": ",".join(BOOKMAKERS)
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()
