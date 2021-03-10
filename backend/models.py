from .app import db

field_method = db.Table('field_method',
                        db.Column('psychotherapist_id', db.ForeignKey('field.psychotherapist_id'), primary_key=True),
                        db.Column('method_id', db.ForeignKey('method.id'), primary_key=True))


class Psychotherapist(db.Model):
    __tablename__ = 'psychotherapist'

    id = db.Column(db.String(80), primary_key=True)
    createdTime = db.Column(db.DateTime)
    field = db.relationship('Field', backref='psychotherapist', lazy=True, uselist=False)



class Field(db.Model):
    __tablename__ = 'field'

    name = db.Column(db.String(140))
    methods = db.relationship('Method', secondary=field_method, lazy='subquery',
                              backref=db.backref('field', lazy=True))
    photo = db.relationship('Photo', backref='field', lazy=True, uselist=False)
    psychotherapist_id = db.Column(db.String(80), db.ForeignKey('psychotherapist.id'), nullable=False, primary_key=True)


class Photo(db.Model):
    __tablename__ = 'photo'

    id = db.Column(db.String(80), primary_key=True)
    filename = db.Column(db.String(140))
    size = db.Column(db.Integer)
    thumbnails = db.relationship('Thumbnail', backref='photo', lazy=True)
    psychotherapist_id = db.Column(db.String(80), db.ForeignKey('field.psychotherapist_id'), nullable=False)
    type = db.Column(db.String(80))
    url = db.Column(db.String(280))


class Thumbnail(db.Model):
    __tablename__ = 'thumbnail'

    name = db.Column(db.String(140))
    height = db.Column(db.Integer)
    width = db.Column(db.Integer)
    url = db.Column(db.String(280), primary_key=True)
    photo_id = db.Column(db.String(80), db.ForeignKey('photo.id'), nullable=False)


class Method(db.Model):
    __tablename__ = 'method'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))

