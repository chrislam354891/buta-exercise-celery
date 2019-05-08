import os
from celery import task
from celery.utils.log import get_task_logger
from app import img_downloader
from app.utils import get_task_data_basepath
from config import Config

logger = get_task_logger(__name__)

@task(bind=True)
def download_images(self, user_id, img_list):
    save_to_path = os.path.join(
        get_task_data_basepath(
            user_id,
            self.request.id
        ), Config.FileStore.download_folder)
    try:
        saved_file = img_downloader.download_image(save_to_path, img_list)
        result = ("Image saved at: %s" % saved_file)
    except Exception as e:
        err_msg = ("Fail to download image, err: %s" % str(e))
        logger.error(err_msg)
        result = err_msg
    return result

@task(bind=True)
def get_task_ids(self, user_id):
    return filestore.get_user_task_list(user_id)