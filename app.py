from flask import Flask, render_template, request
from fetcher import fetch_odds
from analysis import analyze_matches

app = Flask(__name__)

@app.route("/")
def index():
    sport = request.args.get("sport", "soccer")
    data = fetch_odds(sport)
    matches = analyze_matches(data)
    return render_template("index.html", matches=matches)

if __name__ == "__main__":
    app.run(debug=True)
