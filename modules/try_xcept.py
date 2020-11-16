"""
errror handling
"""
import re

def validate(username):
    try:
        if( bool(re.match("^[a-zA-Z]", username))):
            print(username)
    except:
        print("invalid input")

