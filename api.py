# -*- coding: utf-8 -*-
# Copyright (c) 2018-2019 Linh Pham
# api.wwdt.me is relased under the terms of the Apache License 2.0
"""Flash application startup file"""

import json
import os

import mysql.connector
from mysql.connector.errors import DatabaseError, ProgrammingError
from flask import Flask, jsonify, abort, make_response, request

from wwdtm import guest, host, location, panelist, scorekeeper, show

app = Flask(__name__)
database_connection = None

#region Bootstrap Functions
def load_config():
    """Bootstrap the API by loading in configuration and initializing
    Flask app"""
    app_environment = os.getenv("FLASK_ENV", "local").strip().lower()

    try:
        with open('config.json', 'r') as config_file:
            config_dict = json.load(config_file)
    except FileNotFoundError as err:
        raise FileNotFoundError("Unable to locate config.json") from err
    except IOError as err:
        raise IOError("Unable to read config.json") from err

    if app_environment.startswith("develop"):
        if "development" in config_dict:
            return config_dict["development"]
        else:
            raise EnvironmentError("Missing 'development' section in config file")
    elif app_environment.startswith("prod"):
        if "production" in config_dict:
            return config_dict["production"]
        else:
            raise EnvironmentError("Missing 'production' section in config file")
    else:
        if "local" in config_dict:
            return config_dict["local"]
        else:
            raise EnvironmentError("Missing 'local' section in config file")

#endregion

#region Response Dictionary Functions
def success_dict(data: object):
    """Return a success dictionary containing response data"""
    return {"status": "success",
            "data": data}

def fail_dict(key_name: str, value: str):
    """Return a fail dictionary containing the failed request and
    message"""
    return {"status": "fail",
            "data": {key_name: value}}

def error_dict(error_message: str):
    """Return an error dictionary containing the error message"""
    return {"status": "error",
            "error": error_message}

#endregion

#region API: Panelists
@app.route('/panelists', methods=["GET"])
def get_panelists():
    """Return JSON payload based on result of panelist.retrieve_all()"""
    try:
        panelists = panelist.retrieve_all(database_connection)
        if not panelists:
            response = fail_dict("panelist", "No panelists found")
            return jsonify(response), 404

        return jsonify(success_dict(panelists)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve panelists from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Unable to retrieve panelists from database")
        return jsonify(response), 500
    except:
        abort(500)

@app.route('/panelists/<int:panelist_id>', methods=["GET"])
def get_panelist_by_id(panelist_id: int):
    """Return JSON payload based on result of panelist.retrieve_by_id()"""
    try:
        panelist_info = panelist.retrieve_by_id(panelist_id,
                                                database_connection)
        if not panelist_info:
            message = "Panelist ID {} not found".format(panelist_id)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict(panelist_info)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist from database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Unexpected error when retrieving data")
        return jsonify(response), 500
    except:
        abort(500)

@app.route('/panelists/<int:panelist_id>/details', methods=["GET"])
def get_panelist_details_by_id(panelist_id: int):
    """Return JSON payload based on result of
    panelist.retrieve_details_by_id()"""
    try:
        panelist_info = panelist.retrieve_details_by_id(panelist_id,
                                                        database_connection)
        if not panelist_info:
            message = "Panelist ID {} not found".format(panelist_id)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict(panelist_info)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist from database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Unexpected error when retrieving data")
        return jsonify(response), 500
    except:
        abort(500)

#endregion

# Only run if executed as a script and not imported
if __name__ == '__main__':
    config_dict = load_config()
    database_connection = mysql.connector.connect(**config_dict["database"])

    app.run(debug=False)
