#!/bin/bash
# Get the response body for a given URL for 200 status code responses.
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request using curl and display the body for 200 status code
curl -s -o /dev/null -w "%{http_code}" "$1" | {
    read -r status_code
    if [ "$status_code" -eq 200 ]; then
        curl -s "$1"
    else
        echo "Error: HTTP $status_code"
    fi
}