# -*- coding: utf-8 -*-
# Copyright (c) 2018-2019 Linh Pham
# wwdtm is relased under the terms of the Apache License 2.0
"""This module provides functions that handle the API endpoint requests
for /scorekeepers"""

import mysql.connector
from mysql.connector.errors import DatabaseError, ProgrammingError
from flask import Flask, jsonify, abort, make_response, request

from .dicts import error_dict, fail_dict, success_dict
from wwdtm.scorekeeper import details, info

def get_scorekeepers(database_connection: mysql.connector.connect):
    """Retrieve a list of scoreekeepers and their corresponding
    information"""
    try:
        database_connection.reconnect()
        scorekeepers = info.retrieve_all(database_connection)
        if not scorekeepers:
            response = fail_dict("scorekeepers", "No scorekeepers found")
            return jsonify(response), 404

        return jsonify(success_dict("scorekeepers", scorekeepers)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve scorekeepers from the "
                              "database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "scorekeepers from the database")
        return jsonify(response), 500
    except:
        abort(500)

def get_scorekeeper_by_id(scorekeeper_id: int,
                          database_connection: mysql.connector.connect):
    """Retrieve a scorekeeper based on their ID"""
    try:
        database_connection.reconnect()
        scorekeeper_info = info.retrieve_by_id(scorekeeper_id, database_connection)
        if not scorekeeper_info:
            message = "Scorekeeper ID {} not found".format(scorekeeper_id)
            response = fail_dict("scorekeeper", message)
            return jsonify(response), 404

        return jsonify(success_dict("scorekeeper", scorekeeper_info)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve scorekeeper information "
                              "from the database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "scorekeeper information")
        return jsonify(response), 500
    except:
        abort(500)

def get_scorekeeper_details_by_id(scorekeeper_id: int,
                                  database_connection: mysql.connector.connect):
    """Retrieve a scorekeeper and their appearance data based on their
    ID"""
    try:
        database_connection.reconnect()
        scorekeeper_details = details.retrieve_by_id(scorekeeper_id,
                                                     database_connection)
        if not scorekeeper_details:
            message = "Scorekeeper ID {} not found".format(scorekeeper_id)
            response = fail_dict("scorekeeper", message)
            return jsonify(response), 404

        return jsonify(success_dict("scorekeeper", scorekeeper_details)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve scorekeeper information "
                              "from the database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "scorekeeper information")
        return jsonify(response), 500
    except:
        abort(500)

def get_scorekeeper_details(database_connection: mysql.connector.connect):
    """Retrieve a list of scorekeeper and their corresponding
    appearances"""
    try:
        database_connection.reconnect()
        scorekeeper_details = details.retrieve_all(database_connection)
        if not details:
            response = fail_dict("scorekeepers", "No scorekeepers found")
            return jsonify(response), 404

        return jsonify(success_dict("scorekeepers", scorekeeper_details)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve scorekeepers from the "
                              "database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "scorekeepers from database")
        return jsonify(response), 500
    except:
        abort(500)

def get_scorekeeper_by_slug(scorekeeper_slug: str,
                            database_connection: mysql.connector.connect):
    """Retrieve a scorekeeper based on their slug"""
    try:
        database_connection.reconnect()
        scorekeeper_info = info.retrieve_by_slug(scorekeeper_slug,
                                                 database_connection)
        if not scorekeeper_info:
            message = "Scorekeeper slug '{}' not found".format(scorekeeper_slug)
            response = fail_dict("scorekeeper", message)
            return jsonify(response), 404

        return jsonify(success_dict("scorekeeper", scorekeeper_info)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve scorekeeper information "
                              "from the database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "scorekeeper information")
        return jsonify(response), 500
    except:
        abort(500)

def get_scorekeeper_details_by_slug(scorekeeper_slug: str,
                                    database_connection: mysql.connector.connect):
    """Retrieve a scorekeeper and their appearance data based on their
    slug"""
    try:
        database_connection.reconnect()
        scorekeeper_details = details.retrieve_by_slug(scorekeeper_slug,
                                                       database_connection)
        if not scorekeeper_details:
            message = "Scorekeeper slug '{}' not found".format(scorekeeper_slug)
            response = fail_dict("scorekeeper", message)
            return jsonify(response), 404

        return jsonify(success_dict("scorekeeper", scorekeeper_details)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve scorekeeper information "
                              "from the database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "scorekeeper information")
        return jsonify(response), 500
    except:
        abort(500)
