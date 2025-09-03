FROM python:3.10-slim
WORKDIR /app
COPY service1.py /app
RUN pip install flask
EXPOSE 8080
CMD ["python", "service1.py"]
