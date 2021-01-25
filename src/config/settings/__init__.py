from configparser import RawConfigParser
from os.path import dirname, join

from loguru import logger

ENV_DEVELOPMENT = 'development'
ENV_PRODUCTION = 'production'

config = RawConfigParser()
path = join(dirname(__file__), 'settings.ini')
config.read(path)

ENV = config.get('settings', 'ENVIRONMENT') or 'development'

ENVIRONMENTS = (ENV_DEVELOPMENT, ENV_PRODUCTION)

if ENV not in ENVIRONMENTS:
    logger.warning('Invalid environment setting.')
    ENV = ENV_DEVELOPMENT

if ENV == ENV_DEVELOPMENT:
    from .development import *
elif ENV == ENV_PRODUCTION:
    from .production import *
