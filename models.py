from conf import db, app
from sqlalchemy import Computed

class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prob = db.Column(db.Float)
    num = db.Column(db.Integer)
    url = db.Column(db.Text)
    icon = db.Column(db.Text)
    #pages = db.relationship('page', backref='Site', lazy='dynamic')


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prob = db.Column(db.Float)
    uri = db.Column(db.Text)
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'),
                        nullable=False)
    title=db.Column(db.Text)
