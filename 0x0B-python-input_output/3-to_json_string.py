#!/usr/bin/python3
"""
  Module that prints the json representation of a number
"""

import json


def to_json_string(my_obj):
    """A function that returns json rep"""
    return json.dumps(my_obj)
