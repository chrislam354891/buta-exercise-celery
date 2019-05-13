"""
Sample run script of Celery Worker for this project
USAGE:
(at project home folder)
$ python -m app.run_celery_worker
"""

import os
from .app import create_app
from .app import app_conf
from .extensions import celery
from .config import config

# Create the Flask app with celery, configuration will be loaded too.
flask_app = create_app()

if __name__ == '__main__':
    # if app_config.DEBUG:
    #     log_level = 'DEBUG'
    # else:
    #     log_level = 'INFO'
    # print(app_conf.get_log_level())
    # print(app_conf.DEBUG)
    with flask_app.app_context():
        # Start as worker
        argv = [
                'worker',
                '--loglevel=' + app_conf.get_log_level(),
            ]
        celery.worker_main(argv)
        # celery.start()
