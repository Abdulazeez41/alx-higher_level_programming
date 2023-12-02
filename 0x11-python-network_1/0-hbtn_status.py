#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status link."""
import urllib.request


if __name__ == "__main__":
    myRequest = urllib.myRequest.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        myBody = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(myBody)))
        print("\t- content: {}".format(myBody))
        print("\t- utf8 content: {}".format(myBody.decode("utf-8")))
