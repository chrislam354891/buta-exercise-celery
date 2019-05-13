# Gunicorn entrypoint file For the base image, see this project:
# https://github.com/matthieugouel/docker-python-gunicorn-nginx

from app.app import create_app

app = create_app()
