# import logging
import os
import pathlib
import urllib.request
import shutil

from celery.utils.log import get_task_logger
from config import Config

class ImageDownloader(object):

    def __init__(self, logger=None, **kwargs):
        # self.logger = logger or logging.getLogger(__name__)
        self.logger = logger or get_task_logger(__name__)
        
        # self.config =  kwargs.pop('config', Config.IMG_DOWNLOADER) or {}

        # self.logger.info('Init ImageDownloader')

    def download_image(self, save_to_dir, img_url):
        if not os.path.exists(save_to_dir):
            pathlib.Path(save_to_dir).mkdir(parents=True, exist_ok=True)

        tmp_img_file = os.path.join(save_to_dir, 'img.tmp')
        
        with urllib.request.urlopen(img_url) as response, open(tmp_img_file, 'wb') as out_file:
            data = response.read() # a `bytes` object
            out_file.write(data)
        
        return tmp_img_file


        
