import os
import logging
from config import Config

def get_task_data_basepath(user_id, task_id):
    file_basedir = Config.FileStore.basedir
    return os.path.join(
            file_basedir,
            user_id,
            task_id)
