from datetime import datetime
from models.db import db


class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(255), nullable=False, unique=True)
    bio = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=str(
        datetime.utcnow()), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.now())

    posts = db.relationship("Post", cascade='all', backref=db.backref('posts', lazy=True))


    def __init__(self, name, picture, bio):
        self.name = name
        self.picture = picture
        self.bio = bio

    def json(self):
        return {"id": self.id, "name": self.name, "picture": self.picture, "bio": self.bio, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return Artist.query.all()

    @classmethod
    def find_by_id(cls, artist_id):
        artist = Artist.query.filter_by(id=artist_id).first()
        return artist