# Use the Ubuntu base image
FROM ubuntu:20.04

# Install Nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the Nginx configuration template and startup script
COPY nginx.conf /etc/nginx/conf.d/nginx.conf

# run Nginx in the foreground to keep the container running
CMD ["nginx", "-g", "daemon off;"]