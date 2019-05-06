import os
from dotenv import load_dotenv, find_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# Load the .env enviroment file
# Don't know why find_dotenv() not working so I load the env file from app root
dotenv_path=find_dotenv() or os.path.join(os.getcwd(),'.env')
load_dotenv(dotenv_path=dotenv_path)

class Config:

    class FileStore:
        basedir = os.environ.get('FILE_STORE_BASEDIR') or '/tmp/bulkuploader'
        download_folder = 'download'

    CELERY = {
        'broker_url': os.environ.get('CELERY_BROKER_URL') or 'amqp://',
        'result_backend': os.environ.get('CELERY_RESULT_BACKEND') or 'rpc://',
        'result_expires': 3600
    }
