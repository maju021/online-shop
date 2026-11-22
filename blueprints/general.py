from flask import Blueprint

app = Blueprint("app", __name__)

@app.route("/")
def home():
    return "Welcome to MAJU!"

@app.route("/about")
def about():
    return "About MAJU"
