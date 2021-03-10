from backend.models import *
from backend.app import db
import datetime


def parse():
    """"Parse date from airtable"""
    from airtable import Airtable
    from dotenv import load_dotenv
    import os

    load_dotenv()
    psychotherapists = Airtable(os.environ['base_id'], 'Psychotherapists', api_key=os.environ['api_key'])
    return psychotherapists.get_all()


def save_to_db(p):  # maybe crutch
    """"Save psychotherapist in DateBase"""
    created_time = datetime.datetime.strptime(p['createdTime'], "%Y-%m-%dT%H:%M:%S.%fZ")
    psych = Psychotherapist(id=p['id'], createdTime=created_time)
    pf = p['fields']
    pp = pf['Фотография'][0]
    pt = pp['thumbnails']
    pt_sizes = [i for i in pt]
    methods = []
    methods_for_save = []
    for method_name in pf['Методы']:
        method_in_db = Method.query.filter_by(name=method_name).first()
        if method_in_db:
            methods.append(method_in_db)
        else:
            method = Method(name=method_name)
            methods.append(method)
            methods_for_save.append(method)
    psych_field = Field(name=pf['Имя'], methods=methods, psychotherapist_id=p['id'])
    psych_photo = Photo(id=pp['id'], filename=pp['filename'], size=pp['size'],
                        type=pp['type'], url=pp['url'], psychotherapist_id=p['id'])
    psycho_thumbnails = [
        Thumbnail(name=i, height=pt[i]['height'], width=pt[i]['width'],
                  url=pt[i]['url'], photo_id=pp['id']) for i in pt_sizes
    ]
    db.session.add_all([psych, psych_photo, psych_field] + methods_for_save + psycho_thumbnails)
    db.session.commit()


def remove_from_db(p):  # maybe crutch
    pp_id = Photo.query.filter_by(psychotherapist_id=p.id).first().id
    field = Field.query.filter_by(psychotherapist_id=p.id).first()
    field.methods = []

    Thumbnail.query.filter_by(photo_id=pp_id).delete()
    Photo.query.filter_by(psychotherapist_id=p.id).delete()
    Field.query.filter_by(psychotherapist_id=p.id).delete()
    Psychotherapist.query.filter_by(id=p.id).delete()
    db.session.commit()
