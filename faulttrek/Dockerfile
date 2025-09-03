# Use slim Python 3.10 base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir \
    pyyaml \
    psutil \
    requests \
    flask \
    prometheus_client

# Expose ports for HTTP API and Prometheus metrics
EXPOSE 8080 8000

# Start the Flask HTTP API by default (so container keeps running)
ENTRYPOINT ["python", "faulttrek.py", "--http"]
