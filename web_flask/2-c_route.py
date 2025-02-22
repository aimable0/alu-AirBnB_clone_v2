#!/usr/bin/python3
"""
Flask web application module.

This module starts a simple Flask web application with multiple routes:
- `/` -> Returns "Hello HBNB!"
- `/hbnb` -> Returns "HBNB"
- `/c/<text>` -> Returns "C " followed by the value of `text`, replacing underscores with spaces.

The application listens on all available network interfaces (0.0.0.0) at port 5000.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    Route handler for the root URL.

    Returns:
        str: "Hello HBNB!"
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for `/hbnb`.

    Returns:
        str: "HBNB"
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    Route handler for `/c/<text>`.

    Args:
        text (str): The dynamic text passed in the URL.

    Returns:
        str: "C " followed by `text`, with underscores replaced by spaces.
    """
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
