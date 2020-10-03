import os
import cloudinary

class Config:
    '''
    General configuration parent class
    '''
    IMAGE_API_BASE_URL = 'https://pixabay.com/api/?key={}&q={}&image_type=photo&pretty=true'
    IMAGE_API_KEY = os.environ.get('IMAGE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:tom@localhost/photographyweb'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    cloudinary.config(
        cloud_name='dmtsu8tdt',
        api_key='272426152557254',
        api_secret='rn7Ra2FpE83xZa8mKWCQx-I0b48')

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False
class TestConfig(Config):
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'Test': TestConfig
}