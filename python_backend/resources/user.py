from flask_smorest import Blueprint, abort
from flask.views import MethodView
from python_backend.db import db
from python_backend.models.user_model import UserModel
from python_backend.schemas import UserSchema
from sqlalchemy.exc import IntegrityError
blp = Blueprint("user", __name__, description="more comfortable operations with users")


@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    @blp.response(200, UserSchema)
    def delete(self, category_id):
        raise NotImplementedError("Not implemented for now")


@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, request_data):
        user = UserModel(**request_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, "User with this name already exists")
        return user
