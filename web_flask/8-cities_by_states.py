from flask import Flask
from models import storage
from models.city import City
from models.state import State


app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def return_cities():
    ...

@app.teardown_appcontext
def teardown(self):
    ...

if __name__ == "__main__":
    # host changed for the sake of test
    app.run(host="0.0.0.1", port=5000)