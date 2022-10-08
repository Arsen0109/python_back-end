from python_backend import app
from flask import jsonify, request
import datetime

user_id = 1
category_id = 1
note_id = 1

CATEGORIES = [
    {
        "id": category_id,
        "title": "Payment for apartments"
    }
]

USERS = [
    {
        "id": user_id,
        "name": "Vasyl"
    }
]

NOTES = [
    {
        "id": note_id,
        "user_id": user_id,
        "category_id": category_id,
        "price": 1000,
        "date_of_creating": datetime.date.today()
    }
]


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
    global user_id
    user_id += 1
    request_data["id"] = user_id
    try:
        request_data["name"] = request.get_json()["name"]
    except:
        return "Error bad request"

    USERS.append(request_data)
    return request_data


@app.route("/category", methods=["POST"])
def create_category():
    request_data = {}
    global category_id
    category_id += 1
    request_data["id"] = category_id
    try:
        request_data["title"] = request.get_json()["title"]
    except:
        return "Error bad request"
    CATEGORIES.append(request_data)
    return request_data


@app.route("/note", methods=["POST"])
def create_note():
    request_data = request.get_json()
    global note_id
    note_id += 1
    try:
        if not (validation("id", request.get_json()["user_id"], USERS) and validation("id", request.get_json()["category_id"], CATEGORIES)):
            return "Error, user or category is not found"
        request_data["id"] = note_id
        request_data["date_of_creating"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        request_data["price"] = request.get_json()["price"]
    except:
        return "Error bad request"

    NOTES.append(request_data)
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
