#!/bin/bash
#Script catches the error message an put "You got me!"
curl -sL -X PUT -H "Origin:School" -d "user_id=98" 0.0.0.0:5000/catch_me
