from flask_restful import Resource
from flask import request
from models.user import User
from middleware import create_token, gen_password, strip_token, read_token, compare_password



class Login(Resource):
  def post(self, LoginObj):
    user = User.find_by_email(LoginObj.email)    
    if user and compare_password(LoginObj.password, user.password_digest):
      payload = {
        "id": user.id,
        "email": user.email
      }
      token = create_token(payload)
      return {"user" : payload, "token": token}
    return {"msg": "Unauthorized"}, 404


  def get(self):
    
    if token


class Register(Resource):
  def post(self):
    data = request.get_json()
    params = {
        "name": data['name'],
        "email": data['email'],
        "password_digest": gen_password(data['password'])
    }
    user = User(**params)
    user.create()
    return user.json(), 201
