from backend.app import manager, db
from cli import parse, save_to_db, remove_from_db


@manager.command
def create_db():
    psychotherapists = parse()
    db.create_all()
    for psychotherapist in psychotherapists:
        save_to_db(psychotherapist)
    print('Success')


@manager.command
def update_db():  # crutch
    from backend.models import Psychotherapist
    psychotherapists = parse()
    # del
    psychotherapists_in_database = Psychotherapist.query.all()
    pi = [i['id'] for i in psychotherapists]
    for p in psychotherapists_in_database:
        if p.id not in pi:
            remove_from_db(p)

    # save
    for psychotherapist in psychotherapists:
        if not Psychotherapist.query.filter_by(id=psychotherapist['id']).first():
            save_to_db(psychotherapist)

    print('Success')


if __name__ == '__main__':
    manager.run()
