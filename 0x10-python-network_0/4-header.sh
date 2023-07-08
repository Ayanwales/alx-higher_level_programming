#!/bin/bash
#Script with a GET request and a header variable
curl -s "$1" -X GET -H "X-School-User-Id: 98"
