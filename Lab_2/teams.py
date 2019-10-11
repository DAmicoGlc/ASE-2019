from flask import Blueprint, jsonify

teams = Blueprint('teams', __name__)

_DEV = ['Derek', 'Bob']
_OPS = ['Paul', 'Matt']
_TEAMS = {1: _DEV, 2: _OPS }

@teams.route('/team', methods=['GET', 'DELETE', 'POST'])
def get_all_teams():
    response = jsonify(_TEAMS)

    return response

@teams.route('/team/<int:team_id>', methods=['GET', 'DELETE', 'POST'])
def get_team(team_id):
    response = jsonify(_TEAMS[team_id])

    return response