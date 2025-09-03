FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pyyaml psutil requests

CMD ["python", "faulttrek.py", "profiles/latency.yaml"]
