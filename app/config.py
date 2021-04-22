import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

class Config:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR,"database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = "asdasdasdsad"
    SECURITY_PASSWORD_HASH = "sha512_crypt"