from flask import request
from flask_restful import Resource
from models.artist import Artist
from models.db import db
from sqlalchemy.orm import joinedload


class Artists(Resource):
    def get(self):
        artists = Artist.find_all()
        return [a.json() for a in artists]

    def post(self):
        data = request.get_json()
        artist = Artist(**data)
        artist.create()
        return artist.json(), 201


class ArtistDetail(Resource):
    def get(self, artist_id):
        artist = Artist.query.options(joinedload(
            'posts')).filter_by(id=artist_id).first()
        print(artist.posts)
        posts = [p.json() for p in artist.posts]
        return {**artist.json(), "posts": posts}

    def put(self, artist_id):
        data = request.get_json()
        artist = Artist.find_by_id(artist_id)
        for k in data.keys():
            artist[k] = data[k]
        db.session.commit()
        return artist.json()

    def delete(self, artist_id):
        artist = Artist.find_by_id(artist_id)
        if not artist:
            return {"msg": "artist not found"}, 404
        db.session.delete(artist)
        db.session.commit()
        return {"msg": "Artist Deleted", "payload": artist_id}