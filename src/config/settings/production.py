from .base import *

DEBUG = False

ALLOWED_HOSTS = ("YOUR", "ALLOWED", "HOSTS")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "0000",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
