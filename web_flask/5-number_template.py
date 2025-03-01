#!/usr/bin/python3
"""Script that starts a flask web application"""
from flask import Flask, render_template_string, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    """Returns C <text>"""
    return "C " + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """Returns Python <text>"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Returns <n> is a number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Returns HTML page if n is an integer"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    """running the app"""
    app.run(host="0.0.0.0", port=5000)
