#!/usr/bin/python3
"""sends a POST with variable q, displays [<id>] <name> or print error"""
import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) == 2:
        var = sys.argv[1]
    else:
        var = ""
    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': var})
    try:
        dir_element = req.json()
        if len(dir_element) == 0:
            print("No result")
        else:
            print("[{}] {}".format(dir_element['id'], dir_element['name']))
    except ValueError:
        print("Not a valid JSON")
