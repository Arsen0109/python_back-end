from flask_smorest import Blueprint, abort
from python_backend import token_required
from sqlalchemy.exc import IntegrityError
from python_backend.db import *
from python_backend.models import NoteModel
from python_backend.schemas import NoteSchema, NoteResponseSchema
blp = Blueprint("note", __name__, description="more comfortable operations with notes")


@blp.route("/note/<int:note_id>")
@blp.response(200, NoteResponseSchema)
@token_required
def get(current_user, note_id):
    note = NoteModel.query.filter_by(user_id=current_user.id, id=note_id).first()
    if not note:
        abort(400, message="No note found")
    return note


@blp.route("/note/<int:note_id>", methods=["PUT"])
@blp.arguments(NoteSchema)
@blp.response(200, NoteResponseSchema)
@token_required
def update(current_user, request_data, note_id):
    note = NoteModel.query.filter_by(user_id=current_user.id, id=note_id).first()
    if not note:
        abort(400, message="No note found")
    try:
        note.category_id = request_data["category_id"]
        note.price = request_data["price"]
        db.session.commit()
    except Exception:
        abort(400, message="Error fields category_id and price are required for put operation")
    return note


@blp.route("/note/<int:note_id>", methods=["DELETE"])
@blp.response(200, NoteResponseSchema)
@token_required
def delete(current_user, note_id):
    note = NoteModel.query.filter_by(user_id=current_user.id, id=note_id).first()
    if not note:
        abort(400, message="No note found")
    db.session.delete(note)
    db.session.commit()
    return note


@blp.route("/note")
@blp.response(200, NoteResponseSchema(many=True))
@token_required
def get(current_user, **kwargs):
    try:
        query = NoteModel.query.filter(user_id == current_user.id)
        try:
            category_id = int(kwargs.get("category_id"))
            query = NoteModel.query.filter_by(user_id=current_user.id, category_id=category_id)
            return query.all()
        except TypeError:
            return query.all()
    except TypeError:
        abort(400, message="Error, missing user_id")


@blp.route("/note", methods=["POST"])
@blp.arguments(NoteSchema)
@blp.response(200, NoteResponseSchema)
@token_required
def post(current_user, request_data):
    try:
        request_data["currency_id"]
    except KeyError:
        request_data["currency_id"] = 1
    note = NoteModel(**request_data)
    note.user_id = current_user.id
    try:
        db.session.add(note)
        db.session.commit()
    except IntegrityError:
        abort(400, message="Error bad request")

    return note
