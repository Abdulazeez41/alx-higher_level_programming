#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status link."""
import urllib.request


if __name__ == "__main__":
    myRequest = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(myRequest) as response:
        myBody = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(myBody)))
        print("\t- content: {}".format(myBody))
        print("\t- utf8 content: {}".format(myBody.decode("utf-8")))
