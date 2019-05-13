FROM matthieugouel/python-gunicorn-nginx:latest
MAINTAINER BadBUTA <badbuta@gmail.com>

# This file is based on 
# https://github.com/matthieugouel/python-flask-celery-example/blob/master/Dockerfile

# For the base image, see this project:
# https://github.com/matthieugouel/docker-python-gunicorn-nginx

RUN useradd -u 1000 pyuser

# Set the environment package
ENV APP_ENVIRONMENT production

# Copy the package requirements
COPY requirements.txt /tmp/

# Install the package requirements
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

# Copy the application.  Please refer to matthieugouel/python-gunicorn-nginx project
COPY ./app /app/app/
COPY ./run.py /app

