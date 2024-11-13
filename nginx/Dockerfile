# Use the Ubuntu base image
FROM ubuntu:20.04

# Install Nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Copy the Nginx server block configuration
COPY nginx.conf /etc/nginx/conf.d/nginx.conf

# Set the default command to run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
