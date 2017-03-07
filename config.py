import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'piouslove'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'myblog.db')#sqlite数据库地址
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

