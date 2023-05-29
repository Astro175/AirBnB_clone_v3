#!/usr/bin/python3
"""Module for blueprint index"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns status Ok"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'],
                 strict_slashes=False)
def count():
    """Retrieves the number of objects"""
    obj_type = [Amenities, State, City, Review, Place, User]
    stats = {}
    for obj in obj_type:
        stats_result = count(obj)
        stats[obj] = stats_result
