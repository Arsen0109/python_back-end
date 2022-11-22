from flask_smorest import Blueprint, abort
from flask.views import MethodView
from python_backend.db import *
from flask import request, jsonify

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
        user_notes = [*NOTES.values()]
        request_data = request.get_json()
        try:
            id_user = request_data["user_id"]
            try:
                id_category = request_data["category_id"]
                return list(filter(lambda x: (x.get("user_id") == id_user and x.get("category_id") == id_category), user_notes))
            except KeyError:
                return list(filter(lambda x: (x.get("user_id") == id_user), user_notes))
        except KeyError:
            abort(400, message="Error, missing user_id")

    def post(self):
        request_data = request.get_json()
        note = {}
        global noteId
        try:
            if not ("user_id" in request_data or "category_id" in request_data or "price" in request_data):
                abort(400, message="Error, bad request")
            noteId += 1
            note["id"] = noteId
            note["user_id"] = request_data["user_id"]
            note["category_id"] = request_data["category_id"]
            note["date_of_creating"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            note["price"] = request.get_json()["price"]
        except KeyError:
            abort(400, message="Error, bad request")

        NOTES[noteId] = note
        return note
