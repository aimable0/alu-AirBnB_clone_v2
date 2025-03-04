#!/usr/bin/python3
"""
Flask web application to display a list of states.

This module initializes a Flask web application that retrieves
state data from the storage and renders it on an HTML page.

Routes:
    /states_list: Displays a list of states in an HTML template.

Teardown:
    Closes the current SQLAlchemy session after each request.

Usage:
    Run this script to start the web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def return_states():
    """Fetches states from storage and renders them in an HTML page."""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_storage(self):
    """Closes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5)
