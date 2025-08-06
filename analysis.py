def implied_prob(odds):
    return 1.0 / odds

def analyze_matches(odds_json):
    results = []
    for match in odds_json:
        home, away = match["home_team"], match["away_team"]
        all_odds = []
        for b in match.get("bookmakers", []):
            for market in b.get("markets", []):
                if market["key"] == "h2h":
                    for outcome in market.get("outcomes", []):
                        all_odds.append((b["key"], outcome["name"], outcome["price"]))
        if not all_odds:
            continue
        fair = sum(o[2] for o in all_odds) / len(all_odds)
        for book, name, price in all_odds:
            edge = implied_prob(price) - implied_prob(fair)
            results.append({
                "home": home,
                "away": away,
                "bookmaker": book,
                "selection": name,
                "odds": price,
                "edge": edge
            })
    return sorted(results, key=lambda x: x["edge"], reverse=True)
