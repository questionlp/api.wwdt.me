# -*- coding: utf-8 -*-
# Copyright (c) 2018-2019 Linh Pham
# wwdtm is relased under the terms of the Apache License 2.0
"""This module provides functions that handle the API endpoint requests
for /locations"""

import mysql.connector
from mysql.connector.errors import DatabaseError, ProgrammingError
from flask import Flask, jsonify, abort, make_response, request

from .dicts import error_dict, fail_dict, success_dict
from wwdtm import location

def get_locations(database_connection: mysql.connector.connect):
    """Retrieve a list of locations"""
    try:
        database_connection.reconnect()
        locations = location.retrieve_all(database_connection)
        if not locations:
            response = fail_dict("locations", "No locations found")
            return jsonify(response), 404

        return jsonify(success_dict("locations", locations)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve locations from the database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "locations from the database")
        return jsonify(response), 500
    except:
        abort(500)

def get_location_by_id(location_id: int,
                       database_connection: mysql.connector.connect):
    """Retrieve a location and its information based on its ID"""
    try:
        database_connection.reconnect()
        info = location.retrieve_by_id(location_id, database_connection)
        if not info:
            message = "Location ID {} not found".format(location_id)
            response = fail_dict("location", message)
            return jsonify(response), 404

        return jsonify(success_dict("location", info)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve location information from "
                              "the database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "location information")
        return jsonify(response), 500
    except:
        abort(500)

def get_location_recordings_by_id(location_id: int,
                                  database_connection: mysql.connector.connect):
    """Retrieve show recordings for a location based on its ID"""
    try:
        database_connection.reconnect()
        recordings = location.retrieve_recordings_by_id(location_id,
                                                        database_connection)
        if not recordings:
            message = "Location ID {} not found".format(location_id)
            response = fail_dict("location", message)
            return jsonify(response), 404

        return jsonify(success_dict("recordings", recordings)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve location recording "
                              "information from the database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "location recording information")
        return jsonify(response), 500
    except:
        abort(500)

def get_location_recordings(database_connection: mysql.connector.connect):
    """Retrieve show recordings for all locations"""
    try:
        database_connection.reconnect()
        recordings = location.retrieve_all_recordings(database_connection)
        if not recordings:
            response = fail_dict("recordings", "No location recordings found")
            return jsonify(response), 404

        return jsonify(success_dict("recordings", recordings)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve location recording "
                              "information from the database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "location recording information")
        return jsonify(response), 500
    except:
        abort(500)
