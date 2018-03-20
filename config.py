class Config(object):
    DEBUG = False
    TESTING = False
    HOST = 'localhost'
    PORT = 8000


class DevelopmentConfig(Config):
    DEBUG = True
    FT_SERVER_MODEL_PATH = "./models/lid.176.bin"


class TestConfig(Config):
    DEBUG = True
    FT_SERVER_MODEL_PATH = "./models/lid.176.ftz"


class DockerConfig(Config):
    HOST = '0.0.0.0'
    FT_SERVER_MODEL_PATH = "/models/lid.176.bin"
