from ast import Return
from email.policy import default
from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    Photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    note = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):

         return self.photo_url or GENERIC_IMAGE


def connect_db(app):

    db.app  = app
    db.init_app(app)
    