#!/bin/bash
#Script sends a JSON post
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
