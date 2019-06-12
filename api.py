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

#region Guest API Endpoints


#endregion

#region Host API Endpoint
@app.route("/hosts/", methods=["GET"])
def get_hosts():
    """Retrieve a list of hosts and their corresponding information"""
    try:
        hosts = host.retrieve_all(database_connection)
        if not hosts:
            response = fail_dict("host", "No hosts found")
            return jsonify(response), 404

        return jsonify(success_dict(hosts)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve hosts from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "hosts from database")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/hosts/<int:host_id>/", methods=["GET"])
def get_host_by_id(host_id: int):
    """Retrieve a host based on their ID"""
    try:
        info = host.retrieve_by_id(host_id, database_connection)
        if not info:
            message = "Host ID {} not found".format(host_id)
            response = fail_dict("host", message)
            return jsonify(response), 404

        return jsonify(success_dict(info)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve host information from "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "host information")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/hosts/<int:host_id>/details/", methods=["GET"])
def get_host_details_by_id(host_id: int):
    """Retrieve a host and their appearance data based on their ID"""
    try:
        details = host.retrieve_details_by_id(host_id,
                                              database_connection)
        if not details:
            message = "Host ID {} not found".format(host_id)
            response = fail_dict("host", message)
            return jsonify(response), 404

        return jsonify(success_dict(details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve host information from "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "host information")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/hosts/details/", methods=["GET"])
def get_host_details():
    """Retrieve a list of hosts and their corresponding appearances"""
    try:
        details = host.retrieve_all_details(database_connection)
        if not details:
            response = fail_dict("host", "No hosts found")
            return jsonify(response), 404

        return jsonify(success_dict(details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve hosts from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "host information")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/hosts/slug/<string:host_slug>/", methods=["GET"])
def get_host_by_slug(host_slug: str):
    """Retrieve a host based on their slug"""
    try:
        info = host.retrieve_by_slug(host_slug, database_connection)
        if not info:
            message = "Host slug '{}' not found".format(host_slug)
            response = fail_dict("host", message)
            return jsonify(response), 404

        return jsonify(success_dict(info)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve host information from "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "host information")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/hosts/slug/<string:host_slug>/details/", methods=["GET"])
def get_host_details_by_slug(host_slug: str):
    """Retrieve a host and their appearance data based on their ID"""
    try:
        details = host.retrieve_details_by_slug(host_slug,
                                                database_connection)
        if not details:
            message = "Host slug '{}' not found".format(host_slug)
            response = fail_dict("host", message)
            return jsonify(response), 404

        return jsonify(details), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve host information from "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "host information")
        return jsonify(response), 500
    except:
        abort(500)

#endregion

#region Location API Endpoints
@app.route("/locations/", methods=["GET"])
def get_locations():
    """Retrieve a list of locations"""
    try:
        locations = location.retrieve_all(database_connection)
        if not locations:
            response = fail_dict("location", "No locations found")
            return jsonify(response), 404

        return jsonify(success_dict(locations)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve locations from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "locations from database")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/locations/<int:location_id>/", methods=["GET"])
def get_location_by_id(location_id: int):
    """Retrieve a location and its information based on its ID"""
    try:
        info = location.retrieve_by_id(location_id, database_connection)
        if not info:
            message = "Location ID {} not found".format(location_id)
            response = fail_dict("location", message)
            return jsonify(response), 404

        return jsonify(success_dict(info)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve location information "
                              "from database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "location information")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/locations/<int:location_id>/recordings/", methods=["GET"])
def get_location_recordings_by_id(location_id: int):
    """Retrieve show recordings for a location based on its ID"""
    try:
        recordings = location.retrieve_recordings_by_id(location_id,
                                                        database_connection)
        if not recordings:
            message = "Location ID {} not found".format(location_id)
            response = fail_dict("location", message)
            return jsonify(response), 404

        return jsonify(success_dict(recordings)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve location information "
                              "from database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "location information")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/locations/recordings/", methods=["GET"])
def get_location_recordings():
    """Retrieve show recordings for all locations"""
    try:
        recordings = location.retrieve_all_recordings(database_connection)
        if not recordings:
            response = fail_dict("location", "No location recordings found")
            return jsonify(response), 404

        return jsonify(recordings), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve locations from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "locations from database")
        return jsonify(response), 500
    except:
        abort(500)

#endregion

#region Panelist API Endpoints
@app.route("/panelists/", methods=["GET"])
def get_panelists():
    """Retrieve a list of panelists and their corresponding
    information"""
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
        repsonse = error_dict("Database error occurred while retrieving "
                              "panelists from database")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/panelists/<int:panelist_id>/", methods=["GET"])
def get_panelist_by_id(panelist_id: int):
    """Retrieve a panelist based on their ID"""
    try:
        info = panelist.retrieve_by_id(panelist_id, database_connection)
        if not info:
            message = "Panelist ID {} not found".format(panelist_id)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict(info)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist information "
                              "from database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist information")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/panelists/<int:panelist_id>/details/", methods=["GET"])
def get_panelist_details_by_id(panelist_id: int):
    """Retrieve a panelist with their statistics and appearances based
    on their ID"""
    try:
        details = panelist.retrieve_details_by_id(panelist_id,
                                                  database_connection)
        if not details:
            message = "Panelist ID {} not found".format(panelist_id)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict(details)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist from database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist details")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/panelists/<int:panelist_id>/scores/", methods=["GET"])
def get_panelist_scores_by_id(panelist_id: int):
    """Retrieve a list of scores for the requested panelist ID"""
    try:
        scores = panelist.retrieve_scores_list_by_id(panelist_id,
                                                     database_connection)
        if not scores:
            message = "Panelist ID {} not found".format(panelist_id)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict(scores)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist scores from "
                              "database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist scores")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/panelists/<int:panelist_id>/scores/ordered-pair/", methods=["GET"])
def get_panelist_scores_ordered_pair_by_id(panelist_id: int):
    """Retrieve a list of scores, as an ordered pair, for the requested
    panelist ID"""
    try:
        scores = panelist.retrieve_scores_ordered_pair_by_id(panelist_id,
                                                             database_connection)
        if not scores:
            message = "Panelist ID {} not found".format(panelist_id)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict(scores)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist scores from "
                              "database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist scores")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/panelists/details/", methods=["GET"])
def get_panelists_details():
    """Retrieve a list of panelists with their corresponding statistics
    and appearances"""
    try:
        details = panelist.retrieve_all_details(database_connection)
        if not details:
            response = fail_dict("panelist", "No panelists found")
            return jsonify(response), 404

        return jsonify(success_dict(details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve panelists from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "panelists from database")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/panelists/slug/<string:panelist_slug>/", methods=["GET"])
def get_panelist_by_slug(panelist_slug: str):
    """Retrieve a panelist based on their slug"""
    try:
        info = panelist.retrieve_by_slug(panelist_slug, database_connection)
        if not info:
            message = "Panelist slug '{}' not found".format(panelist_slug)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict(info)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist information "
                              "from database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist information")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/panelists/slug/<string:panelist_slug>/details/", methods=["GET"])
def get_panelist_details_by_slug(panelist_slug: str):
    """Retrieve a panelist with their statistics and appearances based
    on their slug"""
    try:
        details = panelist.retrieve_details_by_slug(panelist_slug,
                                                    database_connection)
        if not details:
            message = "Panelist slug '{}' not found".format(panelist_slug)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict(details)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist from database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist details")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/panelists/slug/<string:panelist_slug>/scores/", methods=["GET"])
def get_panelist_scores_by_slug(panelist_slug: str):
    """Retrieve a list of scores for the requested panelist slug"""
    try:
        scores = panelist.retrieve_scores_list_by_slug(panelist_slug,
                                                       database_connection)
        if not scores:
            message = "Panelist slug '{}' not found".format(panelist_slug)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict(scores)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist scores from "
                              "database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist scores")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/panelists/slug/<string:panelist_slug>/scores/ordered-pair/", methods=["GET"])
def get_panelist_scores_ordered_pair_by_slug(panelist_slug: str):
    """Retrieve a list of scores, as an ordered pair, for the requested
    panelist slug"""
    try:
        scores = panelist.retrieve_scores_ordered_pair_by_slug(panelist_slug,
                                                               database_connection)
        if not scores:
            message = "Panelist slug '{}' not found".format(panelist_slug)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict(scores)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist scores from "
                              "database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist scores")
        return jsonify(response), 500
    except:
        abort(500)

#endregion

#region Scorekeeper API Endpoints
@app.route("/scorekeepers/", methods=["GET"])
def get_scorekeepers():
    """Retrieve a list of scoreekeepers and their corresponding
    information"""
    try:
        scorekeepers = scorekeeper.retrieve_all(database_connection)
        if not scorekeepers:
            response = fail_dict("scorekeeper", "No scorekeepers found")
            return jsonify(response), 404

        return jsonify(success_dict(scorekeepers)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve scorekeepers from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "scorekeepers from database")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/scorekeepers/<int:scorekeeper_id>/", methods=["GET"])
def get_scorekeeper_by_id(scorekeeper_id: int):
    """Retrieve a scorekeeper based on their ID"""
    try:
        info = scorekeeper.retrieve_by_id(scorekeeper_id, database_connection)
        if not info:
            message = "Scorekeeper ID {} not found".format(scorekeeper_id)
            response = fail_dict("scorekeeper", message)
            return jsonify(response), 404

        return jsonify(success_dict(info)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve scorekeeper information "
                              "from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "scorekeeper information")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/scorekeepers/<int:scorekeeper_id>/details/", methods=["GET"])
def get_scorekeeper_details_by_id(scorekeeper_id: int):
    """Retrieve a scorekeeper and their appearance data based on their
    ID"""
    try:
        details = scorekeeper.retrieve_details_by_id(scorekeeper_id,
                                                     database_connection)
        if not details:
            message = "Scorekeeper ID {} not found".format(scorekeeper_id)
            response = fail_dict("scorekeeper", message)
            return jsonify(response), 404

        return jsonify(success_dict(details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve scorekeeper information "
                              "from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "scorekeeper information")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/scorekeepers/details/", methods=["GET"])
def get_scorekeeper_details():
    """Retrieve a list of scorekeeper and their corresponding
    appearances"""
    try:
        details = scorekeeper.retrieve_all_details(database_connection)
        if not details:
            response = fail_dict("scorekeeper", "No scorekeepers found")
            return jsonify(response), 404

        return jsonify(success_dict(details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve scorekeepers from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "scorekeepers from database")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/scorekeepers/slug/<string:scorekeeper_slug>/", methods=["GET"])
def get_scorekeepers_by_slug(scorekeeper_slug: str):
    """Retrieve a scorekeeper based on their slug"""
    try:
        info = scorekeeper.retrieve_by_slug(scorekeeper_slug,
                                            database_connection)
        if not info:
            message = "Scorekeeper slug '{}' not found".format(scorekeeper_slug)
            response = fail_dict("scorekeeper", message)
            return jsonify(response), 404

        return jsonify(success_dict(info)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve scorekeeper information "
                              "from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "scorekeeper information")
        return jsonify(response), 500
    except:
        abort(500)

@app.route("/scorekeepers/slug/<string:scorekeeper_slug>/details/", methods=["GET"])
def get_scorekeeper_details_by_slug(scorekeeper_slug: str):
    """Retrieve a scorekeeper and their appearance data based on their
    slug"""
    try:
        details = scorekeeper.retrieve_details_by_slug(scorekeeper_slug,
                                                       database_connection)
        if not details:
            message = "Scorekeeper slug '{}' not found".format(scorekeeper_slug)
            response = fail_dict("scorekeeper", message)
            return jsonify(response), 404

        return jsonify(success_dict(details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve scorekeeper information "
                              "from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "scorekeeper information")
        return jsonify(response), 500
    except:
        abort(500)

#endregion

#region Show API Endpoints


#endregion

#region Application Initialization
if __name__ == '__main__':
    config_dict = load_config()
    database_connection = mysql.connector.connect(**config_dict["database"])

    # Set Flask app settings
    app.url_map.strict_slashes = False
    app.config["JSON_SORT_KEYS"] = False
    app.run(debug=False)

#endregion