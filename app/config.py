import os
from typing import List, Type
from sqlalchemy.engine import url

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    # SECRET_KEY = os.getenv(
    #     "DEV_SECRET_KEY", "You can't see California without Marlon Widgeto's eyes"
    # )
    SECRET_KEY = 'DEV_SECRET_KEY'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = conn_url = url.URL(
        drivername='postgres',
        username='admin',
        password='1234',
        host='172.17.0.2',
        port=5432,
        database='flaskmigrate',
        query=None
    ).__to_string__(hide_password=False)


class TestingConfig(BaseConfig):
    CONFIG_NAME = "test"
    SECRET_KEY = os.getenv("TEST_SECRET_KEY", "Thanos did nothing wrong")
    SECRET_KEY = 'TEST_SECRET_KEY'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/app-test.db".format(basedir)


class ProductionConfig(BaseConfig):
    CONFIG_NAME = "prod"
    SECRET_KEY = os.getenv("PROD_SECRET_KEY", "I'm Ron Burgundy?")
    SECRET_KEY = 'PROD_SECRET_KEY'
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/app-prod.db".format(basedir)


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
