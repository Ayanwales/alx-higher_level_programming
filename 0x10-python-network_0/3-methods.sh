#!/bin/bash
#Script display all the HTTP methods the server will accept
curl -s -X OPTIONS "$1" -i | head -n 4 | tail -n 1 | awk -F': ' '{print $2}'
