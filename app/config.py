class Config:
    '''
    General configuration parent class
    '''
    pass
      MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key=963a9822dbb8bae3f86c8d6fa3792e7b'



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