#!/usr/bin/python3
"""A Script that starts a flask application"""
from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def return_cities():
    """Fetches states and cities from storage and renders them."""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_storage(self):
    """Closes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.1", port=5000)
