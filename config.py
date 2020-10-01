import os
class Config:
    '''
    General configuration parent class
    '''
    API_KEY = '18506704-0831dbdfabcb3e9a4d1c92a1b'
    BASE_URL = 'https://pixabay.com/api/?key={}&image_type={}'
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''


    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}