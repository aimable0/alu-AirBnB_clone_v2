#!/usr/bin/python3
"""Script that starts a flask web application:
    Routes:
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
            /c/<text>: display “C ” followed by the value of the text variable
            (replace underscore _ symbols with a space )
"""
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
    """Handling /c/<text> route"""
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    """running the app"""
    app.run(host="0.0.0.0", port=5000)
