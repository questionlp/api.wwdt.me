# -*- coding: utf-8 -*-
# Copyright (c) 2018-2019 Linh Pham
# wwdtm is relased under the terms of the Apache License 2.0
"""This module provides functions that handle the API endpoint requests
for /shows"""

import mysql.connector
from mysql.connector.errors import DatabaseError, ProgrammingError
from flask import Flask, jsonify, abort, make_response, request

from .dicts import error_dict, fail_dict, success_dict
from wwdtm import show

def get_shows(database_connection: mysql.connector.connect):
    """Return a list of shows and the corresponding information"""
    try:
        database_connection.reconnect()
        shows = show.retrieve_all(database_connection)
        if not shows:
            response = fail_dict("shows", "No shows found")
            return jsonify(response), 404

        return jsonify(success_dict("shows", shows)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve shows from the database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving shows "
                              "from the database")
        return jsonify(response), 500
    except:
        abort(500)

def get_show_by_id(show_id: int, database_connection: mysql.connector.connect):
    """Retrieve a show and corresponding information based on the
    show ID"""
    try:
        database_connection.reconnect()
        info = show.retrieve_by_id(show_id, database_connection)
        if not info:
            message = "Show ID {} not found".format(show_id)
            response = fail_dict("show", message)
            return jsonify(response), 404

        return jsonify(success_dict("show", info)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve show information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "show information")
        return jsonify(response), 500
    except:
        abort(500)

def get_show_details_by_id(show_id: int,
                           database_connection: mysql.connector.connect):
    """Retrieve a show and detailed information based on the show ID"""
    try:
        database_connection.reconnect()
        details = show.retrieve_details_by_id(show_id, database_connection)
        if not details:
            message = "Show ID {} not found".format(show_id)
            response = fail_dict("show", message)
            return jsonify(response), 404

        return jsonify(success_dict("show", details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve show information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "show information")
        return jsonify(response), 500
    except:
        abort(500)

def get_show_by_year(show_year: int,
                     database_connection: mysql.connector.connect):
    """Retrieve a list of shows and corresponding information for a
    requested year"""
    try:
        database_connection.reconnect()
        info = show.retrieve_by_year(show_year, database_connection)
        if not info:
            message = "Shows for year {} not found".format(show_year)
            response = fail_dict("shows", message)
            return jsonify(response), 404

        return jsonify(success_dict("shows", info)), 200
    except ValueError:
        message = "Invalid year {}".format(show_year)
        response = fail_dict("shows", message)
        return jsonify(response), 400
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve show information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "show information")
        return jsonify(response), 500
    except:
        abort(500)

def get_show_details_by_year(show_year: int,
                             database_connection: mysql.connector.connect):
    """Retrieve a list of shows and detailed information for the
    requested year"""
    try:
        database_connection.reconnect()
        details = show.retrieve_details_by_year(show_year, database_connection)
        if not details:
            message = "Shows for year {} not found".format(show_year)
            response = fail_dict("shows", message)
            return jsonify(response), 404

        return jsonify(success_dict("shows", details)), 200
    except ValueError:
        message = "Invalid year {}".format(show_year)
        response = fail_dict("shows", message)
        return jsonify(response), 400
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve show information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "show information")
        return jsonify(response), 500
    except:
        abort(500)

def get_show_by_year_month(show_year: int,
                           show_month: int,
                           database_connection: mysql.connector.connect):
    """Retrieve a list of shows and corresponding information for the
    requested year and month"""
    try:
        database_connection.reconnect()
        info = show.retrieve_by_year_month(show_year,
                                           show_month,
                                           database_connection)
        if not info:
            message = "Shows for {}-{} not found".format(show_year, show_month)
            response = fail_dict("shows", message)
            return jsonify(response), 404

        return jsonify(success_dict("shows", info)), 200
    except ValueError:
        message = "Invalid year-month {}-{}".format(show_year, show_month)
        response = fail_dict("shows", message)
        return jsonify(response), 400
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve show information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "show information")
        return jsonify(response), 500
    except:
        abort(500)

def get_show_details_by_year_month(show_year: int,
                                   show_month: int,
                                   database_connection: mysql.connector.connect):
    """Retrieve a list of shows and detailed information for the
    requested year and month"""
    try:
        database_connection.reconnect()
        details = show.retrieve_details_by_year_month(show_year,
                                                      show_month,
                                                      database_connection)
        if not details:
            message = "Shows for {}-{} not found".format(show_year, show_month)
            response = fail_dict("shows", message)
            return jsonify(response), 404

        return jsonify(success_dict("shows", details)), 200
    except ValueError:
        message = "Invalid year-month {}-{}".format(show_year, show_month)
        response = fail_dict("shows", message)
        return jsonify(response), 400
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve show information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "show information")
        return jsonify(response), 500
    except:
        abort(500)

def get_show_by_date(show_year: int,
                     show_month: int,
                     show_day: int,
                     database_connection: mysql.connector.connect):
    """Retrieve a show and corresponding information based on the
    show's year, month and day"""
    try:
        database_connection.reconnect()
        info = show.retrieve_by_date(show_year,
                                     show_month,
                                     show_day,
                                     database_connection)
        if not info:
            message = "Show date {}-{}-{} not found".format(show_year,
                                                            show_month,
                                                            show_day)
            response = fail_dict("show", message)
            return jsonify(response), 404

        return jsonify(success_dict("show", info)), 200
    except ValueError:
        message = "Invalid date {}-{}-{}".format(show_year,
                                                 show_month,
                                                 show_day)
        response = fail_dict("show", message)
        return jsonify(response), 400
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve show information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "show information")
        return jsonify(response), 500
    except:
        abort(500)

def get_show_by_date_string(show_date: str,
                            database_connection: mysql.connector.connect):
    """Retrieve a show and corresponding information based on the
    show's year, month and day in ISO format (YYYY-MM-DD)"""
    try:
        database_connection.reconnect()
        info = show.retrieve_by_date_string(show_date,
                                            database_connection)
        if not info:
            message = "Show date {} not found".format(show_date)
            response = fail_dict("show", message)
            return jsonify(response), 404

        return jsonify(success_dict("show", info)), 200
    except ValueError:
        message = "Invalid date {}".format(show_date)
        response = fail_dict("show", message)
        return jsonify(response), 400
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve show information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "show information")
        return jsonify(response), 500
    except:
        abort(500)

def get_show_details_by_date(show_year: int,
                             show_month: int,
                             show_day: int,
                             database_connection: mysql.connector.connect):
    """Retrieve a list of shows and detailed information for the
    requested year, month and day"""
    try:
        database_connection.reconnect()
        details = show.retrieve_details_by_date(show_year,
                                                show_month,
                                                show_day,
                                                database_connection)
        if not details:
            message = "Show date {}-{}-{} not found".format(show_year,
                                                            show_month,
                                                            show_day)
            response = fail_dict("show", message)
            return jsonify(response), 404

        return jsonify(success_dict("show", details)), 200
    except ValueError:
        message = "Invalid date {}-{}-{}".format(show_year,
                                                 show_month,
                                                 show_day)
        response = fail_dict("show", message)
        return jsonify(response), 400
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve show information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "show information")
        return jsonify(response), 500
    except:
        abort(500)

def get_show_details_by_date_string(show_date: str,
                                    database_connection: mysql.connector.connect):
    """Retrieve a show and detailed information based on the
    show's year, month and day in ISO format (YYYY-MM-DD)"""
    try:
        database_connection.reconnect()
        details = show.retrieve_details_by_date_string(show_date,
                                                       database_connection)
        if not details:
            message = "Show date {} not found".format(show_date)
            response = fail_dict("show", message)
            return jsonify(response), 404

        return jsonify(success_dict("show", details)), 200
    except ValueError:
        message = "Invalid date {}".format(show_date)
        response = fail_dict("show", message)
        return jsonify(response), 400
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve show information from the "
                              "database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving "
                              "show information")
        return jsonify(response), 500
    except:
        abort(500)

def get_show_details(database_connection: mysql.connector.connect):
    """Retrieve a list of all shows and corresponding detailed
    information"""
    try:
        database_connection.reconnect()
        shows = show.retrieve_all_details(database_connection)
        if not shows:
            response = fail_dict("show", "No shows found")
            return jsonify(response), 404

        return jsonify(success_dict("show", shows)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve shows from the database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving shows "
                              "from database")
        return jsonify(response), 500
    except:
        abort(500)

def get_recent_shows(database_connection: mysql.connector.connect):
    """Retrieve a list of recent shows and corresponding information"""
    try:
        database_connection.reconnect()
        info = show.retrieve_recent(database_connection)
        if not info:
            response = fail_dict("shows", "No recent shows found")
            return jsonify(response), 404

        return jsonify(success_dict("shows", info)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve shows from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving shows "
                              "from database")
        return jsonify(response), 500
    except:
        abort(500)

def get_recent_shows_details(database_connection: mysql.connector.connect):
    """Retrieve a list of recent shows and corresponding detailed
    information"""
    try:
        database_connection.reconnect()
        details = show.retrieve_recent_details(database_connection)
        if not details:
            response = fail_dict("shows", "No recent shows found")
            return jsonify(response), 404

        return jsonify(success_dict("shows", details)), 200
    except ProgrammingError:
        repsonse = error_dict("Unable to retrieve shows from database")
        return jsonify(repsonse), 500
    except DatabaseError:
        repsonse = error_dict("Database error occurred while retrieving shows "
                              "from database")
        return jsonify(response), 500
    except:
        abort(500)
