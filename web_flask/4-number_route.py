#!/usr/bin/python3
"""
A script that starts a Flask web application with multiple routes.

Routes:
    - `/` : Displays "Hello HBNB!"
    - `/hbnb` : Displays "HBNB"
    - `/c/<text>` : Displays "C <text>", replacing underscores with spaces
    - `/python/<text>` : Displays "Python <text>", replacing underscores with spaces
      - If no text is provided, defaults to "is cool"
    - `/number/<n>` : Displays "<n> is a number" only if <n> is an integer
"""

from flask import Flask, abort  # Import Flask framework and abort function
from markupsafe import escape  # Import escape function for input sanitization

# Initialize Flask web application
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    Handles requests to the root URL ('/').

    Returns:
        str: "Hello HBNB!"
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Handles requests to '/hbnb'.

    Returns:
        str: "HBNB"
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """
    Handles requests to '/c/<text>'.

    Parameters:
        text (str): Dynamic text input from the URL.

    Returns:
        str: "C <text>" with underscores replaced by spaces.

    Example:
        - '/c/Flask_is_fun' → "C Flask is fun"
    """
    text_underscore_removed = text.replace('_', ' ')  # Replace underscores with spaces
    return f"C {escape(text_underscore_removed)}"  # Escape to prevent XSS attacks

@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_Python(text):
    """
    Handles requests to '/python' and '/python/<text>'.

    Parameters:
        text (str, optional): Dynamic text input from the URL. Defaults to "is cool".

    Returns:
        str: "Python <text>" with underscores replaced by spaces.

    Example:
        - '/python/rocks' → "Python rocks"
        - '/python' → "Python is cool"
    """
    text_underscore_removed = text.replace('_', ' ')  # Replace underscores with spaces
    return f"Python {escape(text_underscore_removed)}"  # Escape to prevent XSS attacks

@app.route('/number/<n>', strict_slashes=False)
def display_num(n):
    """
    Handles requests to '/number/<n>'.

    Parameters:
        n (str): Dynamic numeric input from the URL.

    Returns:
        str: "<n> is a number" if <n> is a valid integer.

    Raises:
        404 Not Found: If <n> is not a valid integer.

    Example:
        - '/number/42' → "42 is a number"
        - '/number/hello' → 404 error
    """
    if n.isdigit():  # Check if input is a numeric string
        return f"{n} is a number"
    else:
        abort(404)  # Return 404 Not Found if input is not a number

if __name__ == "__main__":
    """
    Runs the Flask application.

    - host='0.0.0.0': Makes the app accessible from any IP address.
    - port=5000: Runs the app on port 5000.
    """
    app.run(host='0.0.0.0', port=5000)