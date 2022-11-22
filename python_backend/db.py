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
        "date_of_creating": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    }
]
