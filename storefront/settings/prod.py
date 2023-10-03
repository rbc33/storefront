import os
import dj_database_url
from .common import *
from dat.db_encryption import db_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = []

DATABASES = {
    'default': dj_database_url.parse(db_url)
}