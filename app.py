from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Soham Desai</h1><br><h2>Aryaman</h2>"

@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)