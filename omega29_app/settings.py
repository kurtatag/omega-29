import os

basedir = os.path.dirname(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'db.sqlite')

SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
