#!/bin/bash
#Script sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | head -n 3 | tail -n 1 | awk '{print $2}'
