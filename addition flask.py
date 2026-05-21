from flask import Flask

app = Flask(__name__)

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return str(a + b)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)


