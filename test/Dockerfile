# Use the Alpine base image
FROM alpine:3.18

# Install Python and necessary dependencies
RUN apk add --no-cache python3 py3-pip && \
    pip install requests

# Copy the Python test script to the container
COPY test_server.py /usr/local/bin/test_server.py

# Set the default command to run the test script
CMD ["python3", "/usr/local/bin/test_server.py"]
