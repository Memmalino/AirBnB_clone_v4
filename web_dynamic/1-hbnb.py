#!/usr/bin/python3
""" This script sets up a Flask web application with a specific
    route (/1-hbnb) and renders the 1-hbnb.html template """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from uuid import uuid4
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ This closes the current SQLAlchemy Session """
    storage.close()


@app.route('/1-hbnb', strict_slashes=False)
def hbnb():
    """ This retieves data from database and displays them """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    s_ct = []

    for state in states:
        s_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    all_places = storage.all(Place).values()
    all_places = sorted(all_places, key=lambda k: k.name)

    return render_template('1-hbnb.html',
                           states=s_ct,
                           amenities=amenities,
                           places=all_places,
                           cache_id=uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
