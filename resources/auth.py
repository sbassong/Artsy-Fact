from flask_restful import Resource
from flask import request
from models.user import User
from middleware import create_token, strip_token, read_token, compare_password, gen_password



class Login(Resource):
  def post(self):
    data = request.get_json()
    user = User.find_one(data["email"]) 
    if user and compare_password(data["password"], user.password_digest):
      payload = {
        "id": user.id,
        "email": user.email
      }
      token = create_token(payload)
      return {"user" : payload, "token": token}
    return {"msg": "Unauthorized"}, 404


  def get(self):
    token = strip_token(request)
    payload = read_token(token)
    if payload:
      return payload, 200
    return {"msg": "unauthorized"}, 404
# # figure this out! ask Instructors if need be

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
