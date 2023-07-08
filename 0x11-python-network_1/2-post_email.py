#!/usr/bin/python3
"""takes in URL, email, sends a POST request with the email as a parameter"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        page = resp.read().decode('utf-8')
        print(page)
