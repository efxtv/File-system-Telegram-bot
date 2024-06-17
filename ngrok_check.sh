#!/bin/bash

# Check if ngrok is running using pgrep
# if pgrep -x "ngrok" > /dev/null; then
#    echo "ngrok is running."
#else
#    echo "ngrok is not running."
#/usr/bin/python3 ~/tools/ngrok-tools/run.py
#fi


while true; do
    # Check if ngrok is running using pgrep
    if pgrep -x "ngrok" > /dev/null; then
        echo "ngrok is running."
    else
        echo "ngrok is not running."
        /usr/bin/python3 ~/home/path/to/file/run.py
    fi

    # Sleep for 20 seconds before checking again
    sleep 20
done

