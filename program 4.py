from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Learn Python",
    "Think Like Developer",
    "Code Every Day"
]

@app.route("/")
def quote():
    return random.choice(quotes)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
