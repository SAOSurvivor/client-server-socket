# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

COPY server.py .
COPY log_message.proto .

RUN apt-get update && \
    apt-get install -y protobuf-compiler && \
    protoc --python_out=. log_message.proto

RUN pip install protobuf

EXPOSE 15000

CMD ["python", "server.py"]