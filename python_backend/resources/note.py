from flask_smorest import Blueprint, abort
from flask.views import MethodView
from python_backend.db import *
from flask import request, jsonify
from python_backend.schemas import NoteSchema, NoteQuerySchema
blp = Blueprint("note", __name__, description="more comfortable operations with notes")
noteId = 1


@blp.route("/note/<int:note_id>")
class Note(MethodView):
    @blp.response(200, NoteSchema)
    def get(self, note_id):
        try:
            return NOTES[note_id]
        except KeyError:
            abort(400, "Error note not found")

    @blp.response(200, NoteSchema)
    def delete(self, note_id):
        try:
            deleted_note = NOTES[note_id]
            del NOTES[note_id]
            return deleted_note
        except KeyError:
            abort(400, "Error note not found")


@blp.route("/note")
class NoteList(MethodView):
    @blp.arguments(NoteQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, NoteSchema(many=True))
    def get(self, **kwargs):
        user_notes = [*NOTES.values()]
        try:
            id_user = int(kwargs.get("user_id"))
            print(id_user)
            try:
                id_category = int(kwargs.get("category_id"))
                print(id_category)
                print(user_notes)
                return list(filter(lambda x: (x.get("user_id") == id_user
                                              and x.get("category_id") == id_category), user_notes))
            except TypeError:
                return list(filter(lambda x: (x.get("user_id") == id_user), user_notes))
        except TypeError:
            abort(400, message="Error, missing user_id")

    @blp.arguments(NoteSchema)
    @blp.response(200, NoteSchema)
    def post(self, request_data):
        note = {}
        global noteId
        noteId += 1
        note["id"] = noteId
        note["user_id"] = request_data["user_id"]
        note["category_id"] = request_data["category_id"]
        note["date_of_creating"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        note["price"] = request.get_json()["price"]
        NOTES[noteId] = note
        return note
