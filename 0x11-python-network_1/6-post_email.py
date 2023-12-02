#!/usr/bin/python3
"""
 Python script that takes in a URL and an email address,
  sends a POST request to the passed URL with the email as a parameter,
  and finally displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    myUrl = sys.argv[1]
    myValue = {"email": sys.argv[2]}

    myRequest = requests.post(myUrl, data=myValue)
    print(myRequest.text)
