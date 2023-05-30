#!/usr/bin/python3
"""Module for Cities View"""

from flask import Flask, jsonify, request
from models import storage
from models import State, City

@app_views.route('/api/v1/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_all_cities(state_id):
    """Retrieves all the cities, affiliated
       with a state
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = [city.to_dict for city in state.cities()]
    return jsonify(cities), 200

@app_views.route('/api/v1/cities/<city_id>', methods=
                 ['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieves a City object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict()), 200

@app_views.route('/api/v1/cities/<city_id>', methods=
                 ['DELETE'], strict_slashes=False)
def del_city(city_id):
    """Deletes a City object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    return jsonify({}), 200

@app_views.route('/api/v1/states/<state_id>/cities', methods=
                 ['POST'], strict_slashes=False)
def post_city(state_id):
    """Creates a new state object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    new_city = City(**data)
    new_city.save()
    return jsonify(new_city.to_dict()), 200

@app_views.route('/api/v1/cities/<city_id>', methods=
                 ['PUT'], strict_slashes=False)
def update_city(city_id):
    """Updates a city details"""
    city = storage.get(City, city_id)
    if City is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")
    city_data = {key: value for key, value in data.items()
                 if key not in ['id', 'created_at', 'updated_at']}
    city.update(city_data)
    return jsonify(city.to_dict), 200
