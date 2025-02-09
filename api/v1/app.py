#!/usr/bin/python3
"""
api flask app
"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(self):
    """close database"""
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """error handler function"""
    return jsonify(error="Not found"), 404


if __name__ == '__main__':
    if getenv('HBNB_API_HOST') and getenv('HBNB_API_PORT'):
        app.run(host=getenv('HBNB_API_HOST'), port=getenv('HBNB_API_PORT'),
                threaded=True)
    else:
        app.run(host='0.0.0.0', port='5000', threaded=True)
