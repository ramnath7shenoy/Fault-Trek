# Use slim Python 3.10 base image
FROM python:3.10-slim

WORKDIR /app

# Copy faulttrek package and requirements.txt from root
COPY faulttrek /app/faulttrek
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 8080 8000

# Run the FaultTrek module
ENTRYPOINT ["python", "-m", "faulttrek.faulttrek", "--http"]
