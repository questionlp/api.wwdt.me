# -*- coding: utf-8 -*-
# Copyright (c) 2018-2019 Linh Pham
# wwdtm is relased under the terms of the Apache License 2.0
"""This module provides functions that wrap data or messages being
returned in a formatted dictionary"""

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