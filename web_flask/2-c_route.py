#!/usr/bin/python3
"""This script starts a Flask web application and read text"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    content = text.replace("_", " ")
    return f"C {content}"


if __name__ == "__main__":
    app.run()
