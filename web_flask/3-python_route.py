#!/usr/bin/python3
"""Script that starts a flask web application"""
from flask import Flask


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
    """Handling /c/<text> links"""
    return "C " + text.replace("_", " ")


# handling defaults:
# passing defaults in the url
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """Handling /python/<text> links"""
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    """running the app"""
    app.run(host="0.0.0.0", port=5000)
