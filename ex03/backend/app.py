from flask import Flask, jsonify
import requests

app = Flask(__name__)

PROXIES = {
    "http": "socks5h://tor:9050",
    "https": "socks5h://tor:9050"
}

@app.route("/users")
def users():
    r = requests.get(
        "https://randomuser.me/api/?results=5",
        proxies=PROXIES,
        timeout=30
    )
    data = r.json()["results"]

    users = [
        {
            "name": f'{u["name"]["first"]} {u["name"]["last"]}',
            "photo": u["picture"]["medium"]
        }
        for u in data
    ]

    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
