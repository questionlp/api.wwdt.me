# -*- coding: utf-8 -*-
# Copyright (c) 2018-2019 Linh Pham
# api.wwdt.me is relased under the terms of the Apache License 2.0
"""Flask application startup file"""

import json
import os

import mysql.connector
from mysql.connector.errors import DatabaseError, ProgrammingError
from flask import Flask, jsonify, abort, make_response, request

from resources import guests, hosts, locations, panelists, scorekeepers, shows
from resources.dicts import error_dict, fail_dict, success_dict

app = Flask(__name__)

#region Bootstrap Functions
def load_config():
    """Bootstrap the API by loading in configuration and initializing
    Flask app"""
    app_environment = os.getenv("API_ENV", "local").strip().lower()

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

#region Default Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify(fail_dict("resource", "Resource not found")), 404

#endregion

#region Guest API Endpoints
@app.route("/guests/", methods=["GET"])
def get_guests():
    """Retrieve a list of guests and their corresponding information"""
    return guests.get_guests(database_connection)

@app.route("/guests/<int:guest_id>/", methods=["GET"])
def get_guest_by_id(guest_id: int):
    """Retrieve a guest based on their ID"""
    return guests.get_guest_by_id(guest_id, database_connection)

@app.route("/guests/<int:guest_id>/details/", methods=["GET"])
def get_guest_details_by_id(guest_id: int):
    """Retrieve a guest with their appearance data based on their ID"""
    return guests.get_guest_details_by_id(guest_id, database_connection)

@app.route("/guests/details/", methods=["GET"])
def get_guest_details():
    """Retrieve all guests and their corresponding appearances"""
    return guests.get_guest_details(database_connection)

@app.route("/guests/slug/<string:guest_slug>/", methods=["GET"])
def get_guest_by_slug(guest_slug: str):
    """Retrieve a guest based on their slug"""
    return guests.get_guest_by_slug(guest_slug, database_connection)

@app.route("/guests/slug/<string:guest_slug>/details/", methods=["GET"])
def get_guest_details_by_slug(guest_slug: str):
    """Retrieve a guest with their appearances based on their slug"""
    return guests.get_guest_details_by_slug(guest_slug, database_connection)

#endregion

#region Host API Endpoint
@app.route("/hosts/", methods=["GET"])
def get_hosts():
    """Retrieve a list of hosts and their corresponding information"""
    return hosts.get_hosts(database_connection)

@app.route("/hosts/<int:host_id>/", methods=["GET"])
def get_host_by_id(host_id: int):
    """Retrieve a host based on their ID"""
    return hosts.get_host_by_id(host_id, database_connection)

@app.route("/hosts/<int:host_id>/details/", methods=["GET"])
def get_host_details_by_id(host_id: int):
    """Retrieve a host and their appearance data based on their ID"""
    return hosts.get_host_details_by_id(host_id, database_connection)

@app.route("/hosts/details/", methods=["GET"])
def get_host_details():
    """Retrieve a list of hosts and their corresponding appearances"""
    return hosts.get_host_details(database_connection)

@app.route("/hosts/slug/<string:host_slug>/", methods=["GET"])
def get_host_by_slug(host_slug: str):
    """Retrieve a host based on their slug"""
    return hosts.get_host_by_slug(host_slug, database_connection)

@app.route("/hosts/slug/<string:host_slug>/details/", methods=["GET"])
def get_host_details_by_slug(host_slug: str):
    """Retrieve a host and their appearance data based on their ID"""
    return hosts.get_host_details_by_slug(host_slug, database_connection)

#endregion

#region Location API Endpoints
@app.route("/locations/", methods=["GET"])
def get_locations():
    """Retrieve a list of locations"""
    return locations.get_locations(database_connection)

@app.route("/locations/<int:location_id>/", methods=["GET"])
def get_location_by_id(location_id: int):
    """Retrieve a location and its information based on its ID"""
    return locations.get_location_by_id(location_id, database_connection)

@app.route("/locations/<int:location_id>/recordings/", methods=["GET"])
def get_location_recordings_by_id(location_id: int):
    """Retrieve show recordings for a location based on its ID"""
    return locations.get_location_recordings_by_id(location_id,
                                                   database_connection)

@app.route("/locations/recordings/", methods=["GET"])
def get_location_recordings():
    """Retrieve show recordings for all locations"""
    return locations.get_location_recordings(database_connection)

#endregion

#region Panelist API Endpoints
@app.route("/panelists/", methods=["GET"])
def get_panelists():
    """Retrieve a list of panelists and their corresponding
    information"""
    return panelists.get_panelists(database_connection)

@app.route("/panelists/<int:panelist_id>/", methods=["GET"])
def get_panelist_by_id(panelist_id: int):
    """Retrieve a panelist based on their ID"""
    return panelists.get_panelist_by_id(panelist_id, database_connection)

@app.route("/panelists/<int:panelist_id>/details/", methods=["GET"])
def get_panelist_details_by_id(panelist_id: int):
    """Retrieve a panelist with their statistics and appearances based
    on their ID"""
    return panelists.get_panelist_details_by_id(panelist_id,
                                                database_connection)

@app.route("/panelists/<int:panelist_id>/scores/", methods=["GET"])
def get_panelist_scores_by_id(panelist_id: int):
    """Retrieve a list of scores for the requested panelist ID"""
    return panelists.get_panelist_scores_by_id(panelist_id,
                                               database_connection)

@app.route("/panelists/<int:panelist_id>/scores/ordered-pair/", methods=["GET"])
def get_panelist_scores_ordered_pair_by_id(panelist_id: int):
    """Retrieve a list of scores, as an ordered pair, for the requested
    panelist ID"""
    return panelists.get_panelist_scores_ordered_pair_by_id(panelist_id,
                                                            database_connection)

@app.route("/panelists/details/", methods=["GET"])
def get_panelists_details():
    """Retrieve a list of panelists with their corresponding statistics
    and appearances"""
    return panelists.get_panelists_details(database_connection)

@app.route("/panelists/slug/<string:panelist_slug>/", methods=["GET"])
def get_panelist_by_slug(panelist_slug: str):
    """Retrieve a panelist based on their slug"""
    return panelists.get_panelist_by_slug(panelist_slug, database_connection)

@app.route("/panelists/slug/<string:panelist_slug>/details/", methods=["GET"])
def get_panelist_details_by_slug(panelist_slug: str):
    """Retrieve a panelist with their statistics and appearances based
    on their slug"""
    return panelists.get_panelist_details_by_slug(panelist_slug,
                                                  database_connection)

@app.route("/panelists/slug/<string:panelist_slug>/scores/", methods=["GET"])
def get_panelist_scores_by_slug(panelist_slug: str):
    """Retrieve a list of scores for the requested panelist slug"""
    return panelists.get_panelist_scores_by_slug(panelist_slug,
                                                 database_connection)

@app.route("/panelists/slug/<string:panelist_slug>/scores/ordered-pair/", methods=["GET"])
def get_panelist_scores_ordered_pair_by_slug(panelist_slug: str):
    """Retrieve a list of scores, as an ordered pair, for the requested
    panelist slug"""
    return panelists.get_panelist_scores_ordered_pair_by_slug(panelist_slug,
                                                              database_connection)

#endregion

#region Scorekeeper API Endpoints
@app.route("/scorekeepers/", methods=["GET"])
def get_scorekeepers():
    """Retrieve a list of scoreekeepers and their corresponding
    information"""
    return scorekeepers.get_scorekeepers(database_connection)

@app.route("/scorekeepers/<int:scorekeeper_id>/", methods=["GET"])
def get_scorekeeper_by_id(scorekeeper_id: int):
    """Retrieve a scorekeeper based on their ID"""
    return scorekeepers.get_scorekeeper_by_id(scorekeeper_id,
                                              database_connection)

@app.route("/scorekeepers/<int:scorekeeper_id>/details/", methods=["GET"])
def get_scorekeeper_details_by_id(scorekeeper_id: int):
    """Retrieve a scorekeeper and their appearance data based on their
    ID"""
    return scorekeepers.get_scorekeeper_details_by_id(scorekeeper_id,
                                                      database_connection)

@app.route("/scorekeepers/details/", methods=["GET"])
def get_scorekeeper_details():
    """Retrieve a list of scorekeeper and their corresponding
    appearances"""
    return scorekeepers.get_scorekeeper_details(database_connection)

@app.route("/scorekeepers/slug/<string:scorekeeper_slug>/", methods=["GET"])
def get_scorekeepers_by_slug(scorekeeper_slug: str):
    """Retrieve a scorekeeper based on their slug"""
    return scorekeepers.get_scorekeepers_by_slug(scorekeeper_slug,
                                                 database_connection)

@app.route("/scorekeepers/slug/<string:scorekeeper_slug>/details/", methods=["GET"])
def get_scorekeeper_details_by_slug(scorekeeper_slug: str):
    """Retrieve a scorekeeper and their appearance data based on their
    slug"""
    return scorekeepers.get_scorekeeper_details_by_slug(scorekeeper_slug,
                                                        database_connection)

#endregion

#region Show API Endpoints
@app.route("/shows/", methods=["GET"])
def get_shows():
    """Return a list of shows and the corresponding information"""
    return shows.get_shows(database_connection)

@app.route("/shows/<int:show_id>/", methods=["GET"])
def get_show_by_id(show_id: int):
    """Retrieve a show and corresponding information based on the
    show ID"""
    return shows.get_show_by_id(show_id, database_connection)

@app.route("/shows/<int:show_id>/details/", methods=["GET"])
def get_show_details_by_id(show_id: int):
    """Retrieve a show and detailed information based on the show ID"""
    return shows.get_show_details_by_id(show_id, database_connection)

@app.route("/shows/date/<int:show_year>/", methods=["GET"])
def get_show_by_year(show_year: int):
    """Retrieve a list of shows and corresponding information for a
    requested year"""
    return shows.get_show_by_year(show_year, database_connection)

@app.route("/shows/date/<int:show_year>/details/", methods=["GET"])
def get_show_details_by_year(show_year: int):
    """Retrieve a list of shows and detailed information for the
    requested year"""
    return shows.get_show_details_by_year(show_year, database_connection)

@app.route("/shows/date/<int:show_year>/<int:show_month>/", methods=["GET"])
def get_show_by_year_month(show_year: int, show_month: int):
    """Retrieve a list of shows and corresponding information for the
    requested year and month"""
    return shows.get_show_by_year_month(show_year,
                                        show_month,
                                        database_connection)

@app.route("/shows/date/<int:show_year>/<int:show_month>/details/",
           methods=["GET"])
def get_show_details_by_year_month(show_year: int, show_month: int):
    """Retrieve a list of shows and detailed information for the
    requested year and month"""
    return shows.get_show_details_by_year_month(show_year,
                                                show_month,
                                                database_connection)

@app.route("/shows/date/<int:show_year>/<int:show_month>/<int:show_day>/",
           methods=["GET"])
def get_show_by_date(show_year: int, show_month: int, show_day: int):
    """Retrieve a list of shows and corresponding information for the
    requested year, month and day"""
    return shows.get_show_by_date(show_year,
                                  show_month,
                                  show_day,
                                  database_connection)

@app.route("/shows/date/<int:show_year>/<int:show_month>/<int:show_day>/details/",
           methods=["GET"])
def get_show_details_by_date(show_year: int, show_month: int, show_day: int):
    """Retrieve a list of shows and detailed information for the
    requested year, month and day"""
    return shows.get_show_details_by_date(show_year,
                                          show_month,
                                          show_day,
                                          database_connection)

@app.route("/shows/details/", methods=["GET"])
def get_show_details():
    """Retrieve a list of all shows and corresponding detailed
    information"""
    return shows.get_show_details(database_connection)

@app.route("/shows/recent/", methods=["GET"])
def get_recent_shows():
    """Retrieve a list of recent shows and corresponding information"""
    return shows.get_recent_shows(database_connection)

@app.route("/shows/recent/details/", methods=["GET"])
def get_recent_shows_details():
    """Retrieve a list of recent shows and corresponding detailed
    information"""
    return shows.get_recent_shows_details(database_connection)

#endregion

#region Application Initialization

app.url_map.strict_slashes = False
app.config["JSON_SORT_KEYS"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False
config_dict = load_config()
database_connection = mysql.connector.connect(**config_dict["database"])
database_connection.autocommit = True

if __name__ == '__main__':    
    app.run(debug=False, host="0.0.0.0", port="9248")

#endregion