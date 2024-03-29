#!/usr/bin/python3
"""save strings"""

if __name__ == "__main__":
    import sys
    import json
    save_to_json_file = \
        __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    with open(filename, 'a+') as f:  # Create add_item.json, if necessary
        if f.tell() == 0:
            json.dump([], f)
    file_data = load_from_json_file("add_item.json")
    if len(sys.argv) > 1:
        file_data.extend(sys.argv[1:])
    save_to_json_file(file_data, filename)
