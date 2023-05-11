from flask import jsonify
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from python_backend.db import db
from python_backend.models.user_model import UserModel
from python_backend.schemas import UserSchema
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
blp = Blueprint("user", __name__, description="more comfortable operations with users")


@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    @blp.response(200, UserSchema)
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return user


@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, request_data):
        user = UserModel(**request_data)
        hashed_password = generate_password_hash(request_data['password'], method='sha256')
        user.password = hashed_password
        user.admin = False
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, "User with this name already exists")
        return user
