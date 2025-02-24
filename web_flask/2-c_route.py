#!/usr/bin/"""Script that starts a Flask web application."""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Handling / route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Handling /hnbn route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    """Handling /c/<text> route"""
    text_underscore_removed = text.replace("_", " ")
    return f"C {escape(text_underscore_removed)}"


if __name__ == "__main__":
    """running the app"""
    app.run(host="0.0.0.0", port=5000)
