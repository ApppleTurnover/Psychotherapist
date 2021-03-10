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

app = Flask(__name__)
app.config.from_object(Pretty)

manager = Manager(app)
db = SQLAlchemy(app)
CORS(app)


@app.route('/data', methods=['GET'])
def index():
    return jsonify(db_to_list_of_dict())


def db_to_list_of_dict():  # crutch
    from backend.models import Psychotherapist
    from datetime import datetime
    list_of_dict = []
    for psychotherapist in Psychotherapist.query.all():
        list_of_dict.append({
            "createdTime": psychotherapist.createdTime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "fields": {
                "Имя": psychotherapist.field.name,
                "Методы": [str(method.name) for method in psychotherapist.field.methods],
                "Фотография": [{
                    "filename": psychotherapist.field.photo.filename,
                    "id": psychotherapist.field.photo.id,
                    "size": psychotherapist.field.photo.size,
                    "thumbnails": {
                        "full": {
                            "height": psychotherapist.field.photo.thumbnails[2].height,
                            "url": psychotherapist.field.photo.thumbnails[2].url,
                            "width": psychotherapist.field.photo.thumbnails[2].width,
                        },
                        "large": {
                            "height": psychotherapist.field.photo.thumbnails[1].height,
                            "url": psychotherapist.field.photo.thumbnails[1].url,
                            "width": psychotherapist.field.photo.thumbnails[1].width,
                        },
                        "small": {
                            "height": psychotherapist.field.photo.thumbnails[0].height,
                            "url": psychotherapist.field.photo.thumbnails[0].url,
                            "width": psychotherapist.field.photo.thumbnails[0].width,
                        },
                    },
                    "type": psychotherapist.field.photo.type,
                    "url": psychotherapist.field.photo.url
                }]
            },
            'id': psychotherapist.id
        })

    return list_of_dict
