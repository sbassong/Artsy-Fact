from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models import artist, post, user
from resources import artist, post, auth

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/flask_artsy"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)


api.add_resource(auth.Login, '/users/login')
api.add_resource(auth.Register, '/users/register')

api.add_resource(artist.Artists, '/artists')
api.add_resource(artist.ArtistDetail, '/artists/<int:artist_id>')

api.add_resource(post.Posts, '/posts')
api.add_resource(post.PostDetail,'/posts/<int:post_id>')
if __name__ == '__main__':
    app.run(debug=True)
