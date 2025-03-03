#!/usr/bin/python3
"""A script that runs a flask application
and renders to browsers data from storage (file and db)
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def return_states():
    """return all states objects from storage"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_storage(exception=None):
    """Removes the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
