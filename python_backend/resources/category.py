from sqlalchemy.exc import IntegrityError
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from python_backend.db import db

from python_backend.models import CategoryModel
from python_backend.schemas import CategorySchema

blp = Blueprint("category", __name__, description="more comfortable operations with categories")


@blp.route("/category/<int:category_id>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)
        return category

    @blp.response(200, CategorySchema)
    def delete(self, category_id):
        raise NotImplementedError("Not implemented for now")


@blp.route("/category")
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, request_data):
        category = CategoryModel(**request_data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(400, "Category with this name already exists")
        return category
