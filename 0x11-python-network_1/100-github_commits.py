#!/usr/bin/python3
"""10 commits from the newest of the repository rails by given user"""
import requests
import sys

if __name__ == "__main__":

    user = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/" + user + "/" + repo + "/commits"
    req = requests.get(url)
    d = req.json()
    c = 0
    for i in d:
        print("{}: {}".format(i['sha'], i['commit']['author']['name']))
        c += 1
        if c == 10:
            break
