"""
Development environment settings.
"""
from .base import *  # NOQA

DEBUG = True

# Hardcoded secret key for faster development purpose.
# Production key is stored in environment variable and it differs from this one.
SECRET_KEY = "q!%*q6__xj96xzhdm8i7()3cd1z2@_j0%_!-(r94w2i!2uj++%"

ALLOWED_HOSTS = ("*", )

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
