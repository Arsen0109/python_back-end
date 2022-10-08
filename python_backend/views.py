from python_backend import app
from flask import jsonify, request
import datetime


user_id = 1
category_id = 1
note_id = 1


CATEGORIES = [
    {
        "id": category_id,
        "name": "Payment for apartments"
    }
]

USERS = [
    {
        "id": user_id,
        "name": "Vasyl",
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
        request_data["name"] = "User" + str(user_id)

    USERS.append(request_data)
    print(USERS)
    return request_data


@app.route("/users")
def get_user():
    return jsonify({"users": USERS})


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})
