from flask_smorest import Api
from python_backend import app
from . import db
from python_backend.resources.user import blp as UserBlueprint
from python_backend.resources.category import blp as CategoryBlueprint
from python_backend.resources.note import blp as NoteBlueprint

CATEGORIES = db.CATEGORIES
USERS = db.USERS
NOTES = db.NOTES


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Backend labs, REST API for finance control"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"

api = Api(app)

api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(NoteBlueprint)



@app.route("/")
def hello():
    return "Hello world!"


