#!/usr/bin/python3
""""load_from_json_file"""

import json


def load_from_json_file(filename):
    """creates Object"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
