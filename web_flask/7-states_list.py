#!/usr/bin/python3
"""A script that runs a flask application
and renders to browsers data from storage (file and db)
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

# @app.teardown_appcontext()
# def teardown():
# storage.close()


@app.route("/states_list", strict_slashes=False)
def display_state():
    # retrieve the list of states

    states = storage.all(State)
    # dictionary to store state id and name as key-value pair
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run()
