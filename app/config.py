class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # 'sqlite:///../movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JSON_AS_ASCII = False
#######################################################################################################################
