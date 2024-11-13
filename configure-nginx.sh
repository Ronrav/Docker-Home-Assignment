#!/bin/bash

# Source environment variables from .env file
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo ".env file not found!"
    exit 1
fi

# Use envsubst to replace placeholders in nginx.conf.template and output to nginx.conf
envsubst '${SERVER_PORT_HTML} ${SHARED_DIR} ${CUSTOM_HTML_FILE} ${SERVER_PORT_ERROR} ${HTTP_ERROR_CODE}' < nginx/nginx.conf.template > nginx/nginx.conf

echo "nginx.conf has been configured successfully!"
