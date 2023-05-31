#!/usr/bin/python3
"""Module for amenity views"""

from flask import jsonify, request, abort
from models import storage
from models import Amenity

@app_views.route('/api/v1/amenities', methods=['GET'],
                 strict_slashes=False)
def get_all_amenities:
    """Retrives all amenities objects"""
    amenities = storage.all(Amenity)
    amenities_dict = [amenity.to_dict for amenity in 
                      amenities.value()]
    return jsonify(amenities_dict), 200

@app_views.route('/api/v1/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """Retrieves an amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict()), 200

@app_views.route('/api/v1/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_amenity(amenity_id):
    """Deletes an amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    return jsonify({})
@app_views.route('/api/v1/amenities', methods=['POST'],
                 strict_slashes=False)
def create_amenity():
    """Creates a new amenity object"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    amenity = Amenity(**data)
    amenity.save()
    return jsonify(amenity.to_dict()), 201

@app_views.route('/api/v1/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes)
def update_amenity(amenity_id):
    """Updates an amenity object"""
    amenity = get(Amenity, state_id)
    if not amenity:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    amenity_data = {key: value for key, value in data.items() 
                    if key not in ['id', 'created_at', 'updated_at']}
    amenity.update(amenity_data)
    return jsonify(amenity.to_dict()), 200
    return jsonify(state.to_dict()), 200
