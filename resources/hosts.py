# -*- coding: utf-8 -*-
# Copyright (c) 2018-2019 Linh Pham
# wwdtm is relased under the terms of the Apache License 2.0
"""This module provides functions that handle the API endpoint requests
for /hosts"""

import mysql.connector
from mysql.connector.errors import DatabaseError, ProgrammingError
from flask import Flask, jsonify, abort, make_response, request

from .dicts import error_dict, fail_dict, success_dict
from wwdtm.host import details, info

def get_hosts(database_connection: mysql.connector.connect):
    """Retrieve a list of hosts and their corresponding information"""
    try:
        database_connection.reconnect()
        hosts = info.retrieve_all(database_connection)
        if not hosts:
            response = fail_dict("hosts", "No hosts found")
            return jsonify(response), 404

        return jsonify(success_dict("hosts", hosts)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve hosts from the database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "hosts from the database")
        return jsonify(response), 500
    except:
        abort(500)

def get_host_by_id(host_id: int, database_connection: mysql.connector.connect):
    """Retrieve a host based on their ID"""
    try:
        database_connection.reconnect()
        host_info = info.retrieve_by_id(host_id, database_connection)
        if not host_info:
            message = "Host ID {} not found".format(host_id)
            response = fail_dict("host", message)
            return jsonify(response), 404

        return jsonify(success_dict("host", host_info)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve host information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "host information")
        return jsonify(response), 500
    except:
        abort(500)

def get_host_details_by_id(host_id: int,
                           database_connection: mysql.connector.connect):
    """Retrieve a host and their appearance data based on their ID"""
    try:
        database_connection.reconnect()
        host_details = details.retrieve_by_id(host_id,
                                              database_connection)
        if not host_details:
            message = "Host ID {} not found".format(host_id)
            response = fail_dict("host", message)
            return jsonify(response), 404

        return jsonify(success_dict("host", host_details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve host information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "host information")
        return jsonify(response), 500
    except:
        abort(500)

def get_host_details(database_connection: mysql.connector.connect):
    """Retrieve a list of hosts and their corresponding appearances"""
    try:
        database_connection.reconnect()
        host_details = details.retrieve_all(database_connection)
        if not host_details:
            response = fail_dict("hosts", "No hosts found")
            return jsonify(response), 404

        return jsonify(success_dict("hosts", host_details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve hosts from the database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "host information")
        return jsonify(response), 500
    except:
        abort(500)

def get_host_by_slug(host_slug: str,
                     database_connection: mysql.connector.connect):
    """Retrieve a host based on their slug"""
    try:
        database_connection.reconnect()
        host_info = info.retrieve_by_slug(host_slug, database_connection)
        if not host_info:
            message = "Host slug '{}' not found".format(host_slug)
            response = fail_dict("host", message)
            return jsonify(response), 404

        return jsonify(success_dict("host", host_info)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve host information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "host information")
        return jsonify(response), 500
    except:
        abort(500)

def get_host_details_by_slug(host_slug: str,
                             database_connection: mysql.connector.connect):
    """Retrieve a host and their appearance data based on their ID"""
    try:
        database_connection.reconnect()
        host_details = details.retrieve_by_slug(host_slug,
                                                database_connection)
        if not host_details:
            message = "Host slug '{}' not found".format(host_slug)
            response = fail_dict("host", message)
            return jsonify(response), 404

        return jsonify(success_dict("host", host_details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve host information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "host information")
        return jsonify(response), 500
    except:
        abort(500)
