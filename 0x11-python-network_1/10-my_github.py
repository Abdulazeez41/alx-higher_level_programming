#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    myAuth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    myRequest = requests.get("https://api.github.com/user", auth=myAuth)
    print(myRequest.json().get("id"))
