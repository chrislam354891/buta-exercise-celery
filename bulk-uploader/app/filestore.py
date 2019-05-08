import logging
import os
import pathlib

from config import Config

class FileStore(object):

    def __init__(self, logger=None, basedir=None, **kwargs):
        self.logger = logger or logging.getLogger(__name__)
        self.basedir = basedir or Config.FileStore.basedir

        if not os.path.exists(self.basedir):
            self.logger.warning('Basedir does not exist, create it: %s' % self.basedir)
            pathlib.Path(self.basedir).mkdir(parents=True, exist_ok=True)
        
    def get_user_task_list(self, user_id):
        user_data_path = os.path.join(self.basedir, user_id)
        if not os.path.exists(user_data_path):
            return []
        else:
            d = user_data_path
            # TODO Add filter to get task related directory
            return [o for o in os.listdir(d) 
                        if os.path.isdir(os.path.join(d,o))]

