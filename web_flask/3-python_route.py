#!/usr/bin/python3
"""
Flask web application module.

This module starts a simple Flask web application with multiple routes:
- `/` -> Returns "Hello HBNB!"
- `/hbnb` -> Returns "HBNB"
- `/c/<text>` -> Returns "C " followed by the value of `text`, replacing underscores with spaces.
- `/python` (default: "is cool") -> Returns "Python " followed by the value of `text`, replacing underscores with spaces.

The application listens on all available network interfaces (0.0.0.0) at port 5000.
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Route handler for the root URL.

    Returns:
        str: "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Route handler for `/hbnb`.

    Returns:
        str: "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    """
    Route handler for `/c/<text>`.

    Args:
        text (str): The dynamic text passed in the URL.

    Returns:
        str: "C " followed by `text`, with underscores replaced by spaces.
    """
    text_underscore_removed = text.replace("_", " ")
    return f"C {escape(text_underscore_removed)}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_Python(text):
    """
    Route handler for `/python/<text>` with a default value.

    Args:
        text (str): The dynamic text passed in the URL (default: "is cool").

    Returns:
        str: "Python " followed by `text`, with underscores replaced by spaces.
    """
    text_underscore_removed = text.replace("_", " ")
    return f"Python {escape(text_underscore_removed)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
