#!/usr/bin/python3
"""A script that starts a flask web application:
    Routes:
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
            /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
"""
from flask import Flask, url_for
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    text_underscore_removed = text.replace("_", " ")
    return f"C {escape(text_underscore_removed)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
