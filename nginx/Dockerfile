# Use the Ubuntu base image
FROM ubuntu:20.04

# Install Nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create the directory for the custom HTML file
RUN mkdir -p /var/www/custom

# Copy the custom HTML file to the appropriate directory
COPY custom.html /var/www/custom/index.html

# Copy the Nginx server block configuration
COPY custom.conf /etc/nginx/conf.d/custom.conf

# Expose the ports for the two servers
EXPOSE 8080 9090

# Set the default command to run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
