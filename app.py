from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Soham Desai</h1><br><h2>Aryaman</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)