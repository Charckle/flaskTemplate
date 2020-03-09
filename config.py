class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    SQLALCHEMY_DATABASE_URI = "sqlite:///users.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    IMAGE_UPLOADS = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False    