from flask import Flask, jsonify, request
from teams import teams

_DEV = ['Derek', 'Bob']
_OPS = ['Paul', 'Matt']
_TEAMS = {1: _DEV, 2: _OPS }

app = Flask(__name__)
app.register_blueprint(teams)

if __name__ == '__main__':
    app.run(debug=True)