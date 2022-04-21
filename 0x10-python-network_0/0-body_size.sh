#!/bin/bash
# This script sends a request to an URL and displays of th body of the response
curl -sI "$1" | grep Content-Length | awk '{print $2}'
