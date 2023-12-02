#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    myUrl = sys.argv[1]

    myRequest = requests.get(myUrl)
    if myRequest.status_code >= 400:
        print("Error code: {}".format(myRequest.status_code))
    else:
        print(myRequest.text)
