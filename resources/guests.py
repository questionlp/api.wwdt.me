# -*- coding: utf-8 -*-
# Copyright (c) 2018-2019 Linh Pham
# wwdtm is relased under the terms of the Apache License 2.0
"""This module provides functions that handle the API endpoint requests
for /guest"""

import mysql.connector
from mysql.connector.errors import DatabaseError, ProgrammingError
from flask import Flask, jsonify, abort, make_response, request

from .dicts import error_dict, fail_dict, success_dict
from wwdtm import guest

def get_guests(database_connection: mysql.connector.connect):
    """Retrieve a list of guests and their corresponding information"""
    try:
        database_connection.reconnect()
        guests = guest.retrieve_all(database_connection)
        if not guests:
            response = fail_dict("guest", "No guests found")
            return jsonify(response), 404

        return jsonify(success_dict(guests)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve guests from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "guests from database")
        return jsonify(response), 500
    except:
        abort(500)

def get_guest_by_id(guest_id: int,
                    database_connection: mysql.connector.connect):
    """Retrieve a guest based on their ID"""
    try:
        database_connection.reconnect()
        info = guest.retrieve_by_id(guest_id, database_connection)
        if not info:
            message = "Guest ID {} not found".format(guest_id)
            response = fail_dict("host", message)
            return jsonify(response), 404

        return jsonify(success_dict(info)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve guest information from "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "guest information")
        return jsonify(response), 500
    except:
        abort(500)

def get_guest_details_by_id(guest_id: int,
                            database_connection: mysql.connector.connect):
    """Retrieve a guest with their appearance data based on their ID"""
    try:
        database_connection.reconnect()
        details = guest.retrieve_details_by_id(guest_id, database_connection)
        if not details:
            message = "Guest ID {} not found".format(guest_id)
            response = fail_dict("guest", message)
            return jsonify(response), 404

        return jsonify(success_dict(details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve guest information from "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "guest information")
        return jsonify(response), 500
    except:
        abort(500)

def get_guest_details(database_connection: mysql.connector.connect):
    """Retrieve all guests and their corresponding appearances"""
    try:
        database_connection.reconnect()
        details = guest.retrieve_all_details(database_connection)
        if not details:
            response = fail_dict("guest", "No guests found")
            return jsonify(response), 404

        return jsonify(success_dict(details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve guests from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "guests information")
        return jsonify(response), 500
    except:
        abort(500)

def get_guest_by_slug(guest_slug: str,
                      database_connection: mysql.connector.connect):
    """Retrieve a guest based on their slug"""
    try:
        database_connection.reconnect()
        info = guest.retrieve_by_slug(guest_slug, database_connection)
        if not info:
            message = "Guest slug '{}' not found".format(guest_slug)
            response = fail_dict("host", message)
            return jsonify(response), 404

        return jsonify(success_dict(info)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve guest information from "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "guest information")
        return jsonify(response), 500
    except:
        abort(500)

def get_guest_details_by_slug(guest_slug: str,
                              database_connection: mysql.connector.connect):
    """Retrieve a guest with their appearances based on their slug"""
    try:
        database_connection.reconnect()
        details = guest.retrieve_details_by_slug(guest_slug,
                                                 database_connection)
        if not details:
            message = "Guest slug '{}' not found".format(guest_slug)
            response = fail_dict("host", message)
            return jsonify(response), 404

        return jsonify(success_dict(details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve guest information from "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "guest information")
        return jsonify(response), 500
    except:
        abort(500)
