from sqlalchemy.exc import IntegrityError
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from python_backend.db import db
from python_backend.models import CurrencyModel
from python_backend.schemas import CurrencySchema

blp = Blueprint("currency", __name__, description="more comfortable operations with currencies")


@blp.route("/currency/<int:currency_id>")
class Currency(MethodView):
    @blp.response(200, CurrencySchema)
    def get(self, currency_id):
        currency = CurrencyModel.query.get_or_404(currency_id)
        return currency

    @blp.response(200, CurrencySchema)
    def delete(self, currency_id):
        currency = CurrencyModel.query.get_or_404(currency_id)
        db.session.delete(currency)
        db.session.commit()
        return currency


@blp.route("/currency")
class CurrencyList(MethodView):
    @blp.response(200, CurrencySchema(many=True))
    def get(self):
        return CurrencyModel.query.all()

    @blp.arguments(CurrencySchema)
    @blp.response(200, CurrencySchema)
    def post(self, request_data):
        currency = CurrencyModel(**request_data)
        try:
            db.session.add(currency)
            db.session.commit()
        except IntegrityError:
            abort(400, "Currency with this name already exists")
        return currency
