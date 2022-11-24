from flask_smorest import Blueprint, abort
from flask.views import MethodView
from python_backend.db import *
from flask import request, jsonify
from python_backend.schemas import NoteSchema
blp = Blueprint("note", __name__, description="more comfortable operations with notes")
noteId = 1


@blp.route("/note/<int:note_id>")
class Note(MethodView):
    def get(self, note_id):
        try:
            return NOTES[note_id]
        except KeyError:
            abort(400, "Error note not found")

    def delete(self, note_id):
        try:
            deleted_note = NOTES[note_id]
            del NOTES[note_id]
            return deleted_note
        except KeyError:
            abort(400, "Error note not found")


@blp.route("/note")
class NoteList(MethodView):
    def get(self):
        request_data = request.get_json()
        user_notes = [*NOTES.values()]
        try:
            id_user = request_data["user_id"]
            try:
                id_category = request_data["category_id"]
                return list(filter(lambda x: (x.get("user_id") == id_user
                                              and x.get("category_id") == id_category), user_notes))
            except KeyError:
                return list(filter(lambda x: (x.get("user_id") == id_user), user_notes))
        except KeyError:
            abort(400, message="Error, missing user_id")

    @blp.arguments(NoteSchema)
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
