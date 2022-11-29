from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from python_backend.db import *
from python_backend.models import NoteModel
from python_backend.schemas import NoteSchema, NoteQuerySchema
blp = Blueprint("note", __name__, description="more comfortable operations with notes")


@blp.route("/note/<int:note_id>")
class Note(MethodView):
    @blp.response(200, NoteSchema)
    def get(self, note_id):
        note = NoteModel.query.get_or_404(note_id)
        return note

    @blp.response(200, NoteSchema)
    def delete(self, id_note):
        raise NotImplementedError("Not implemented for now")


@blp.route("/note")
class NoteList(MethodView):
    @blp.arguments(NoteQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, NoteSchema(many=True))
    def get(self, **kwargs):
        try:
            user_id = int(kwargs.get("user_id"))
            print(user_id)
            query = NoteModel.query.filter(user_id == user_id)
            try:
                category_id = int(kwargs.get("category_id"))
                query = NoteModel.query.filter(category_id == category_id)
                return query.all()
            except TypeError:
                return query.all()
        except TypeError:
            abort(400, message="Error, missing user_id")

    @blp.arguments(NoteSchema)
    @blp.response(200, NoteSchema)
    def post(self, request_data):
        try:
            request_data["currency_id"]
        except KeyError:
            request_data["currency_id"] = 1
        note = NoteModel(**request_data)
        try:
            db.session.add(note)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Error bad request")

        return note
