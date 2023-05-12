from sqlalchemy.exc import IntegrityError
from flask_smorest import Blueprint, abort
from python_backend.db import db
from python_backend.models import CurrencyModel
from python_backend.schemas import CurrencySchema
from python_backend import token_required

blp = Blueprint("currency", __name__, description="more comfortable operations with currencies")


@blp.route("/currency/<int:currency_id>")
@blp.response(200, CurrencySchema)
def get(currency_id):
    currency = CurrencyModel.query.get_or_404(currency_id)
    return currency


@blp.route("/currency/<int:currency_id>", methods=["PUT"])
@blp.response(200, CurrencySchema)
@blp.arguments(CurrencySchema)
@token_required
def update(current_user, request_data, currency_id):
    if not current_user.admin:
        abort(400, message="This operation supported only for admin user")
    currency = CurrencyModel.query.get_or_404(currency_id)
    currency.title = request_data["title"]
    db.session.commit()
    return currency


@blp.route("/currency/<int:currency_id>", methods=["DELETE"])
@blp.response(200, CurrencySchema)
@token_required
def delete(current_user, currency_id):
    if not current_user.admin:
        abort(400, message="This operation supported only for admin user")
    currency = CurrencyModel.query.get_or_404(currency_id)
    db.session.delete(currency)
    db.session.commit()
    return currency


@blp.route("/currency")
@blp.response(200, CurrencySchema(many=True))
def get():
    return CurrencyModel.query.all()


@blp.route("/currency", methods=["POST"])
@blp.arguments(CurrencySchema)
@blp.response(200, CurrencySchema)
@token_required
def post(current_user, request_data):
    if not current_user.admin:
        abort(400, message="This operation supported only for admin user")
    currency = CurrencyModel(**request_data)
    try:
        db.session.add(currency)
        db.session.commit()
    except IntegrityError:
        abort(400, message="Currency with this name already exists")
    return currency
