#!/usr/bin/python3
"""A script that runs a flask application"""

from flask import Flask, render_template_string
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def return_filters():
    """A script that runs a flask application"""
    states = storage.all(State)
    return render_template_string("<h1>Welcome</h1>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
