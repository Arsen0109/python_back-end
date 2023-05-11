from sqlalchemy.exc import IntegrityError
from flask_smorest import Blueprint, abort
from python_backend.db import db

from python_backend.models import CategoryModel
from python_backend.schemas import CategorySchema, CategoryResponseSchema
from python_backend import token_required

blp = Blueprint("category", __name__, description="more comfortable operations with categories")


@blp.route("/category/<int:category_id>")
@token_required
@blp.response(200, CategoryResponseSchema)
def get(current_user, category_id):
    category = CategoryModel.query.filter_by(id=category_id, user_id=current_user.id).first()
    return category


@blp.route("/category/<int:category_id>", methods=["PUT"])
@token_required
@blp.arguments(CategorySchema)
@blp.response(200, CategoryResponseSchema)
def update(current_user, request_data, category_id):
    category = CategoryModel.query.get_or_404(category_id)
    try:
        category.title = request_data["title"]
        db.session.commit()
        return category
    except Exception:
        abort(400, "You need to input title")


@blp.route("/category/<int:category_id>", methods=["DELETE"])
@blp.response(200, CategorySchema)
@token_required
def delete(current_user, category_id):
    category = CategoryModel.query.filter_by(id=category_id, user_id=current_user.id).first()
    db.session.delete(category)
    db.session.commit()
    return category


@blp.route("/category")
@blp.response(200, CategoryResponseSchema(many=True))
@token_required
def get(current_user):
    print(current_user.id, current_user.name)
    return CategoryModel.query.filter_by(user_id=current_user.id).all()


@blp.route("/category", methods=["POST"])
@blp.arguments(CategorySchema)
@blp.response(200, CategoryResponseSchema)
@token_required
def post(current_user, request_data):
    category = CategoryModel(**request_data)
    category.user_id = current_user.id
    try:
        db.session.add(category)
        db.session.commit()
    except IntegrityError:
        abort(400, "Category with this name already exists")
    return category
