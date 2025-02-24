from flask import Flask

"""A script that starts a flask app that displays 'Hello HBNB' """
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
