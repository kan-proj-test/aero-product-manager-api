# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-secret-key'
    DATABASE_URL = os.environ.get('DATABASE_URL') or \
        'postgresql://username:password@localhost:5432/database'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}