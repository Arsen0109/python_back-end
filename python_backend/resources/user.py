from flask_smorest import Blueprint, abort
from python_backend.db import db
from python_backend.models.user_model import UserModel
from python_backend.schemas import UserSchema
from sqlalchemy.exc import IntegrityError
from python_backend import token_required
from werkzeug.security import generate_password_hash
blp = Blueprint("user", __name__, description="more comfortable operations with users")


@blp.route("/user/<int:user_id>")
@blp.response(200, UserSchema)
@token_required
def get(current_user, user_id):
    if not current_user.admin:
        abort(400, message="This operation supported only for admin user")
    user = UserModel.query.get_or_404(user_id)
    return user


@blp.route("/user/<int:user_id>", methods=["PUT"])
@blp.response(200, UserSchema)
@blp.arguments(UserSchema)
@token_required
def update(current_user, request_data, user_id):
    if not current_user.admin:
        abort(400, message="This operation supported only for admin user")
    user = UserModel.query.get_or_404(user_id)
    user.name = request_data["name"]
    user.password = generate_password_hash(request_data["password"], method='sha256')
    user.admin = request_data["admin"]
    db.session.commit()
    return user


@blp.route("/user/<int:user_id>", methods=["DELETE"])
@blp.response(200, UserSchema)
@token_required
def delete(current_user, user_id):
    if not current_user.admin:
        abort(400, message="This operation supported only for admin user")
    user = UserModel.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return user


@blp.route("/user")
@blp.response(200, UserSchema(many=True))
@token_required
def get(current_user):
    if not current_user.admin:
        abort(400, message="This operation supported only for admin user")
    return UserModel.query.all()


@blp.route("/user", methods=["POST"])
@blp.arguments(UserSchema)
@blp.response(200, UserSchema)
def post(request_data):
    user = UserModel(**request_data)
    hashed_password = generate_password_hash(request_data['password'], method='sha256')
    user.password = hashed_password
    user.admin = False
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        abort(400, message="User with this name already exists")
    return user
