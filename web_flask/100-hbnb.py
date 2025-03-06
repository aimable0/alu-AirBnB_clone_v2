#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask, render_template, url_for
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def return_hbnb():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("100-hbnb.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exception=None):
    """Closes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run()
