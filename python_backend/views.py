from flask_smorest import Api
from python_backend import app
from . import db
from python_backend.resources.user import blp as UserBlueprint
from python_backend.resources.category import blp as CategoryBlueprint
from python_backend.resources.note import blp as NoteBlueprint
from python_backend.resources.currency import blp as CurrencyBlueprint


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Backend labs, REST API for finance control"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "supermegasecretkey"

db.db.init_app(app)

api = Api(app)

# clears all tables (for developing mode)
# with app.app_context():
#     db.db.drop_all()

with app.app_context():
    db.db.create_all()

api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(NoteBlueprint)
api.register_blueprint(CurrencyBlueprint)



@app.route("/")
def hello():
    return "Hello world!"


