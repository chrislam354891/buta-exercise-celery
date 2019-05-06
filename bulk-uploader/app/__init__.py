import logging
import logging.config

from celery import Celery

from config import Config
from .image_downloader import ImageDownloader

# from celery.app.log import TaskFormatter

# logger = logging.getLogger()
# sh = logging.StreamHandler()
# sh.setFormatter(TaskFormatter('%(asctime)s - %(task_id)s - %(task_name)s - %(name)s - %(levelname)s - %(message)s'))
# logger.setLevel(logging.INFO)
# logger.addHandler(sh)


img_download = ImageDownloader()

celery = Celery(__name__)
celery.conf.update(Config.CELERY)
