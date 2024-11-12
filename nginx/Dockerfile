# Use the Ubuntu base image
FROM ubuntu:20.04

# Install Nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*



# Create the directory for the custom HTML file
RUN mkdir -p /var/www/custom

EXPOSE 8080 9090
# Copy the Nginx server block configuration
COPY nginx.conf /etc/nginx/conf.d/nginx.conf

# Set the default command to run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
