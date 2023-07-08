#!/usr/bin/python3
"""displays body of URL response and print error for status code >= 400"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code < 400:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
