# -*- coding: utf-8 -*-
# Copyright (c) 2018-2019 Linh Pham
# wwdtm is relased under the terms of the Apache License 2.0
"""This module provides functions that handle the API endpoint requests
for /panelists"""

import mysql.connector
from mysql.connector.errors import DatabaseError, ProgrammingError
from flask import Flask, jsonify, abort, make_response, request

from .dicts import error_dict, fail_dict, success_dict
from wwdtm.panelist import details, info

def get_panelists(database_connection: mysql.connector.connect):
    """Retrieve a list of panelists and their corresponding
    information"""
    try:
        database_connection.reconnect()
        panelists = info.retrieve_all(database_connection)
        if not panelists:
            response = fail_dict("panelists", "No panelists found")
            return jsonify(response), 404

        return jsonify(success_dict("panelists", panelists)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve panelists from the database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "panelists from database")
        return jsonify(response), 500
    except:
        abort(500)

def get_panelist_by_id(panelist_id: int,
                       database_connection: mysql.connector.connect):
    """Retrieve a panelist based on their ID"""
    try:
        database_connection.reconnect()
        panelist_info = info.retrieve_by_id(panelist_id, database_connection)
        if not panelist_info:
            message = "Panelist ID {} not found".format(panelist_id)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict("panelist", panelist_info)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist information from "
                              "the database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist information")
        return jsonify(response), 500
    except:
        abort(500)

def get_panelist_details_by_id(panelist_id: int,
                               database_connection: mysql.connector.connect):
    """Retrieve a panelist with their statistics and appearances based
    on their ID"""
    try:
        database_connection.reconnect()
        panelist_details = details.retrieve_by_id(panelist_id,
                                                  database_connection)
        if not panelist_details:
            message = "Panelist ID {} not found".format(panelist_id)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict("panelist", panelist_details)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist information from "
                              "the database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist details")
        return jsonify(response), 500
    except:
        abort(500)

def get_panelist_scores_by_id(panelist_id: int,
                              database_connection: mysql.connector.connect):
    """Retrieve a list of scores for the requested panelist ID"""
    try:
        database_connection.reconnect()
        scores = info.retrieve_scores_list_by_id(panelist_id,
                                                 database_connection)
        if not scores:
            message = "Panelist ID {} not found".format(panelist_id)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict("scores", scores)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist scores from the "
                              "database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist scores")
        return jsonify(response), 500
    except:
        abort(500)

def get_panelist_scores_ordered_pair_by_id(panelist_id: int,
                                           database_connection: mysql.connector.connect):
    """Retrieve a list of scores, as an ordered pair, for the requested
    panelist ID"""
    try:
        database_connection.reconnect()
        scores = info.retrieve_scores_ordered_pair_by_id(panelist_id,
                                                         database_connection)
        if not scores:
            message = "Panelist ID {} not found".format(panelist_id)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict("scores", scores)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist scores from the "
                              "database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist scores")
        return jsonify(response), 500
    except:
        abort(500)

def get_panelists_details(database_connection: mysql.connector.connect):
    """Retrieve a list of panelists with their corresponding statistics
    and appearances"""
    try:
        database_connection.reconnect()
        panelist_details = details.retrieve_all(database_connection)
        if not panelist_details:
            response = fail_dict("panelists", "No panelists found")
            return jsonify(response), 404

        return jsonify(success_dict("panelists", panelist_details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve panelists from the database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "panelists from database")
        return jsonify(response), 500
    except:
        abort(500)

def get_panelist_by_slug(panelist_slug: str,
                         database_connection: mysql.connector.connect):
    """Retrieve a panelist based on their slug"""
    try:
        database_connection.reconnect()
        panelist_info = info.retrieve_by_slug(panelist_slug,
                                              database_connection)
        if not panelist_info:
            message = "Panelist slug '{}' not found".format(panelist_slug)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict("panelist", panelist_info)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist information from "
                              "the database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist information")
        return jsonify(response), 500
    except:
        abort(500)

def get_panelist_details_by_slug(panelist_slug: str,
                                 database_connection: mysql.connector.connect):
    """Retrieve a panelist with their statistics and appearances based
    on their slug"""
    try:
        database_connection.reconnect()
        panelist_details = details.retrieve_by_slug(panelist_slug,
                                                    database_connection)
        if not panelist_details:
            message = "Panelist slug '{}' not found".format(panelist_slug)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict("panelist", panelist_details)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist information from "
                              "the database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist details")
        return jsonify(response), 500
    except:
        abort(500)

def get_panelist_scores_by_slug(panelist_slug: str,
                                database_connection: mysql.connector.connect):
    """Retrieve a list of scores for the requested panelist slug"""
    try:
        database_connection.reconnect()
        scores = info.retrieve_scores_list_by_slug(panelist_slug,
                                                   database_connection)
        if not scores:
            message = "Panelist slug '{}' not found".format(panelist_slug)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict("scores", scores)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist scores from the "
                              "database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist scores")
        return jsonify(response), 500
    except:
        abort(500)

def get_panelist_scores_ordered_pair_by_slug(panelist_slug: str,
                                             database_connection: mysql.connector.connect):
    """Retrieve a list of scores, as an ordered pair, for the requested
    panelist slug"""
    try:
        database_connection.reconnect()
        scores = info.retrieve_scores_ordered_pair_by_slug(panelist_slug,
                                                           database_connection)
        if not scores:
            message = "Panelist slug '{}' not found".format(panelist_slug)
            response = fail_dict("panelist", message)
            return jsonify(response), 404

        return jsonify(success_dict("scores", scores)), 200
    except ProgrammingError:
        response = error_dict("Unable to retrieve panelist scores from the "
                              "database")
        return jsonify(response), 500
    except DatabaseError:
        response = error_dict("Database error occurred while retrieving "
                              "panelist scores")
        return jsonify(response), 500
    except:
        abort(500)
