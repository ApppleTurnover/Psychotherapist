import os

from backend.config import Pretty

from airtable import Airtable

from flask import Flask, jsonify
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Load env variables #
from dotenv import load_dotenv

load_dotenv()
#


table = Airtable('app1dlRnFMmkTqj78', 'Psychotherapists', api_key=os.environ['api_key'])

app = Flask(__name__)
app.config.from_object(Pretty)

manager = Manager(app)
db = SQLAlchemy(app)
CORS(app)

@app.route('/data', methods=['GET'])
def index():
    return jsonify(table.get_all())
