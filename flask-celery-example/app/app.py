import os
from flask import Flask
from flask_restplus import Api

from .apis import api

# from extensions import celery, db
from .extensions import celery

from .config import config
# from .config import config, Config

app_env = os.getenv("APP_ENVIRONMENT") or 'default'
app_conf = config[app_env]

class ReverseProxied(object):
    '''
    See: https://github.com/noirbizarre/flask-restplus/issues/223
    '''
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
            if path_info.startswith(script_name):
                environ['PATH_INFO'] = path_info[len(script_name):]

        scheme = environ.get('HTTP_X_SCHEME', '')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)

def create_app():
    app = Flask(__name__)
    app.config.from_object(app_conf)
    app.wsgi_app = ReverseProxied(app.wsgi_app)

    api.init_app(app)

    #configure/initialize all your extensions
    # db.init_app(app)
    celery.init_app(app)

    return app