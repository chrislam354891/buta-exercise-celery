import os
from celery import task
from celery.utils.log import get_task_logger
from app import img_download
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
        saved_file = img_download.download_image(save_to_path, img_list)
        result = ("Image saved at: %s" % saved_file)
    except Exception as e:
        err_msg = ("Fail to download image, err: %s" % str(e))
        logger.error(err_msg)
        result = err_msg
    return result

@task(bind=True)
def get_task_ids(self, user_id):
    file_basedir = Config.FileStore.basedir
    user_data_path = os.path.join(file_basedir, user_id)
    if not os.path.exists(user_data_path):
        return []
    else:
        d = user_data_path
        return [o for o in os.listdir(d) 
                    if os.path.isdir(os.path.join(d,o))]
