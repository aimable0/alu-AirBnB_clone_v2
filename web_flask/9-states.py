#!/usr/bin/python3
"""A script that runs a flask application"""

from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
