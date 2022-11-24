from flask_smorest import Blueprint, abort
from flask import request, jsonify
from flask.views import MethodView
from python_backend.db import USERS
from python_backend.schemas import UserSchema

blp = Blueprint("user", __name__, description="more comfortable operations with users")

userId = 1


@blp.route("/user/<int:user_id>")
class User(MethodView):
    def get(self, user_id):
        try:
            return USERS[user_id]
        except KeyError:
            abort(400, message="Error user not found")

    def delete(self, user_id):
        try:
            deleted_user = USERS[user_id]
            del USERS[user_id]
            return deleted_user
        except KeyError:
            abort(400, message="Error user not found")


@blp.route("/user")
class UserList(MethodView):
    def get(self):
        return USERS

    @blp.arguments(UserSchema)
    def post(self):
        request_data = {}
        global userId
        userId += 1
        request_data["id"] = userId
        request_data["name"] = request.get_json()["name"]
        USERS[userId] = request_data
        return jsonify(request_data)
