import os

from dotenv import load_dotenv

load_dotenv()


class Pretty:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(os.getcwd())}/tmp/psychotherapist.db'  # os.environ['sql_url']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    JSON_AS_ASCII = False
