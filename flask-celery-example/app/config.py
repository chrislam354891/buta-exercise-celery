"""Application Configuration."""
import os
from dotenv import load_dotenv, find_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# Load the .env enviroment file
# Don't know why find_dotenv() not working so I load the env file from app root
dotenv_path=find_dotenv() or os.path.join(os.getcwd(),'.env')
load_dotenv(dotenv_path=dotenv_path)

class Config(object):
    """Parent configuration class."""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET = os.environ.get('SECRET')

    TITLE = "Flask API with Celery"
    VERSION = "0.1.0"
    DESCRIPTION = "An API Example with Celery."

    # CELERY_BROKER_URL = 'amqp://badbuta:rabbit@192.168.11.23:5672//'
    # CELERY_RESULT_BACKEND = 'redis://:rabbitredis@192.168.11.23:6379/1'
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL') or 'amqp://'
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') or 'rpc://'
    BROKER_URL = CELERY_BROKER_URL

    @staticmethod
    def get_env_as_bool(env_name, default_value):
        ret_val = default_value
        if os.environ.get(env_name) is not None:
            try:
                ret_val = os.environ.get(env_name).lower() in ("yes", "true", "t", "1")
            except:
                pass
        return ret_val

    @classmethod
    def get_log_level(cls):
        if cls.DEBUG:
            return 'DEBUG'
        else:
            return 'INFO'


class DevelopmentConfig(Config):
    """Configurations for Development."""

    DEBUG = Config.get_env_as_bool('DEBUG', True)

class TestingConfig(Config):
    """Configurations for Testing."""

    TESTING = True
    DEBUG = Config.get_env_as_bool('DEBUG', True)

    CELERY_ALWAYS_EAGER = True


class StagingConfig(Config):
    """Configurations for Staging."""

    DEBUG = Config.get_env_as_bool('DEBUG', True)


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False

    # ** Control by Env
    # CELERY_BROKER_URL = 'redis://redis:6379/0'
    # CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    # BROKER_URL = CELERY_BROKER_URL


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}