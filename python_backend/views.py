from python_backend import app
from flask import jsonify, request
import datetime
from . import db
from flask_smorest import abort

user_id = 1
category_id = 1
note_id = 1

CATEGORIES = db.CATEGORIES
USERS = db.USERS
NOTES = db.NOTES


def validation(key, value, arr):
    for i in arr:
        if i[key] == value:
            return True
    return False


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/user", methods=["POST"])
def create_user():
    request_data = {}

    try:
        global user_id
        user_id += 1
        request_data["id"] = user_id
        request_data["name"] = request.get_json()["name"]
    except:
        return "Error bad request"


    db.USERS.append(request_data)
    return request_data


@app.route("/category", methods=["POST"])
def create_category():
    request_data = {}
    try:
        global category_id
        category_id += 1
        request_data["id"] = category_id
        request_data["title"] = request.get_json()["title"]
    except:
        return "Error bad request"
    db.CATEGORIES.append(request_data)
    return request_data


@app.route("/note", methods=["POST"])
def create_note():
    request_data = request.get_json()

    try:
        if not (validation("id", request.get_json()["user_id"], USERS) or validation("id", request.get_json()["category_id"], CATEGORIES)):
            return "Error, user or category is not found"
        global note_id
        note_id += 1
        request_data["id"] = note_id
        request_data["date_of_creating"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        request_data["price"] = request.get_json()["price"]
    except:
        return "Error bad request"

    db.NOTES.append(request_data)
    return request_data


@app.route("/users")
def get_user():
    return jsonify({"users": USERS})


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


@app.route("/notes")
def get_notes():
    return jsonify({"notes": NOTES})


@app.route("/user-notes", methods=["POST"])
def get_user_notes():
    request_data = request.get_json()
    try:
        id_user = request_data["user_id"]
        user_notes = []
        for note in NOTES:
            if note["user_id"] == id_user:
                user_notes.append(note)
        return jsonify(user_notes)
    except:
        return "Error bad request"


@app.route("/user_notes_by_category", methods=["POST"])
def get_user_notes_by_category():
    request_data = request.get_json()
    try:
        id_user = request_data["user_id"]
        id_category = request_data["category_id"]
        user_notes = []
        for note in NOTES:
            if note["user_id"] == id_user and note["category_id"] == id_category:
                user_notes.append(note)
        return jsonify(user_notes)
    except:
        return "Error bad request"




