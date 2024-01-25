#!/bin/bash
# send request to the url with curl, to display the body of size
curl -s "$1" | wc -c
