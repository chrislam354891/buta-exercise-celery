import logging
import logging.config

import json

from flask import Flask
from celery import Celery

from config import Config
from .image_downloader import ImageDownloader
from .filestore import FileStore

# from celery.app.log import TaskFormatter

# logger = logging.getLogger()
# sh = logging.StreamHandler()
# sh.setFormatter(TaskFormatter('%(asctime)s - %(task_id)s - %(task_name)s - %(name)s - %(levelname)s - %(message)s'))
# logger.setLevel(logging.INFO)
# logger.addHandler(sh)


img_downloader = ImageDownloader()
filestore = FileStore()

celery = Celery(__name__)


def create_app(config_name):
    app = Flask(__name__)
    # app.config.from_object(config[config_name])
    celery.conf.update(Config.CELERY)
    celery.autodiscover_tasks([
            'app.tasks',
        ],
        force=True
    )

    # app.run(port=5000, debug=True)

    return app