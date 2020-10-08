# Pull official base image
FROM python:3.8.1-slim-buster

# Set work directory
WORKDIR /usr/src/viiru-home-api

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y netcat

# Install application dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/viiru-home-api/requirements.txt
RUN pip install -r requirements.txt

# Copy the project
COPY . /usr/src/viiru-home-api/

# Run entrypoint
ENTRYPOINT [ "/usr/src/viiru-home-api/entrypoint.sh" ]