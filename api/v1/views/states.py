#!/usr/bin/python3
"""Module for state views"""

from flask import jsonify, Blueprint, request, abort
from models import storage
from api.v1.views import state_views
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_States():
    """Retrieves all the state objects"""
    states = storage.all(State)
    states_dict = [state.to_dict for state in states.value()]
    return jsonify(states_dict), 200

@app_views.route('/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state(state_id):
    """Retrieves a specific state if id exist"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    states_dict = state.to_dict
    return jsonify(states_dict), 200

@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_state(state_id):
    """Deletes a state, if id exist"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    return jsonify({}), 200

@app_views.route('/states/)', methods=['POST'],
                 strict_slashes=False)
def post_state():
    """Adds a new state if name exists"""
    response = request.get_json()
    if not response:
        abort(400, 'Not a JSON')
    if not in response 'name':
        abort(400, 'Missing name')
    new_state = State(**response)
    new_state.save()
    state_dict = state.to_dict()
    return jsonify(state_dict), 200

@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def put_state(state_id):
    """Updates a state if id exists"""
    state = storage.get(State, state_id)
    if state is None:
        abort(400)
    response = request.get_json()
    if not response:
        abort(400, 'Not a JSON')
    state_data = {key: value for key, value in response.items()
                  if key not in ['id', 'created_at', 'updated_at']}
    state.update(state_data)
    return jsonify(state.to_dict()), 200


