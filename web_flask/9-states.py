#!/usr/bin/python3
"""A script that runs a flask application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def return_states():
    """Fetches states from storage and renders them in an HTML page."""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def return_states_id(id):
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    else:
        return render_template("9-states.html")


@app.teardown_appcontext
def close_storage(self):
    """Closes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run()
    # app.run(host="0.0.0.1", port=5000)
