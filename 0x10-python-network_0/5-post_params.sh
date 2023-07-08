#!/bin/bash
#Script sends a POST request
curl -s --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"
