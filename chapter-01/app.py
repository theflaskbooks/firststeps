from flask import Flask, render_template

app = Flask(__name__)

# routes
@app.route("/")
def index():
    return render_template("index.html", title="My Flask App")

