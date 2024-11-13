#!/bin/bash

# Source environment variables from .env file
export $(cat .env | xargs) 

# Use envsubst to replace placeholders in nginx.conf.template and output nginx.conf
envsubst < nginx/nginx.conf.template > nginx/nginx.conf

echo "nginx.conf has been configured successfully!"
