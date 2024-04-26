#!/bin/bash
# script that takes in a URL, sends a request to that URL, 
# and displays the size of the body of the response

link="$1"
response=$(curl -sI "$url")
content_length=$(echo "$response" | awk '/content_length/ {print $2}' | tr -d '\r')
