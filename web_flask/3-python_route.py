#!/usr/bin/python3

"""
Flask web application module.

This module starts a Flask web application with the following routes:
- `/` : Returns "Hello HBNB!"
- `/hbnb` : Returns "HBNB"
- `/c/<text>` : Displays "C " followed by the value of `text`,
with underscores replaced by spaces.
- `/python` (default: "is cool") : Displays "Python "
followed by the value of `text`,
with underscores replaced by spaces.

The application listens on all available network
interfaces (0.0.0.0) at port 5000.
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Handle requests to the root URL.

    Returns:
        str: A greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Handle requests to the `/hbnb` route.

    Returns:
        str: The string "HBNB".
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    """
    Handle requests to the `/c/<text>` route.

    Args:
        text (str): A string provided in the URL.

    Returns:
        str: "C " followed by the given text, with underscores
        replaced by spaces.
    """
    text_underscore_removed = text.replace("_", " ")
    return f"C {escape(text_underscore_removed)}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_Python(text):
    """
    Handle requests to the `/python` or `/python/<text>` route.

    Args:
        text (str): A string provided in the URL, defaults to "is cool".

    Returns:
        str: "Python " followed by the given text, with underscores
        replaced by spaces.
    """
    text_underscore_removed = text.replace("_", " ")
    return f"Python {escape(text_underscore_removed)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
