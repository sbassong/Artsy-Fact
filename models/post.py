from datetime import datetime
from models.db import db


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer(255), foreign_key=False)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=str(
        datetime.utcnow()), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.now())

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    post = db.relationship("post", backref=db.backref('post', lazy=True))


    def __init__(self, artist_id, content):
        self.artist_id = artist_id
        self.content = content
        

    def json(self):
        return {"id": self.id, "artist_id": self.artist_id, "content": self.content, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return Post.query.all()

    @classmethod
    def find_by_id(cls, post_id):
        post = Post.query.filter_by(id=post_id).first()
        return post