#!/usr/bin/python3
"""Module for blueprint index"""

from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns status Ok"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'],
                 strict_slashes=False)
def count():
    """Retrieves the number of objects"""
    obj_type = [Amenity, State, City, Review, Place, User]
    stats = {}
    for obj in obj_type:
        stats_result = storage.count(obj)
        stats[obj] = stats_result
    return jsonify(stats)
