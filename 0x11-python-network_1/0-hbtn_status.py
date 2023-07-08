#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status """

import urllib.request

if __name__ == "__main__":

    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as resp:
        html = resp.read()
        print("Body response:")
        print("	- type: {}".format(type(html)))
        print("	- content: {}".format(html))
        print("	- utf8 content: {}".format(html.decode('utf-8')))
