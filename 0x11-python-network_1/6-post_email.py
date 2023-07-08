#!/usr/bin/python3
"""takes URL, email and sends a POST request with email as a parameter"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    req = requests.post(url, data={'email': email})
    print(req.text)
