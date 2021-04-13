
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Top_SECRET_KEY'
    MAX_CONTENT_LENGTH= 50 * 1024 * 1024
    UPLOAD_PATH= os.path.join(os.path.realpath(__package__), "uploads")