import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TEMPLATE_URL = os.environ.get("TEMPLATE_URL")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
