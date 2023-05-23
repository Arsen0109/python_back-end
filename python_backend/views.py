from flask_smorest import Api
from werkzeug.security import generate_password_hash

from python_backend import app
from . import db
from python_backend.resources.user import blp as UserBlueprint
from python_backend.resources.category import blp as CategoryBlueprint
from python_backend.resources.note import blp as NoteBlueprint
from python_backend.resources.currency import blp as CurrencyBlueprint
from python_backend.models.user_model import UserModel

db.db.init_app(app)
api = Api(app)
# clears all tables (for developing mode)
# with app.app_context():
# #     db.db.drop_all()
# #     db.db.create_all()
#     admin_user = UserModel(name="Admin")
#     hashed_password = generate_password_hash("Admin", method='sha256')
#     admin_user.password = hashed_password
#     admin_user.admin = True
#     db.db.session.add(admin_user)
#     db.db.session.commit()

# with app.app_context():
#     db.db.create_all()


api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(NoteBlueprint)
api.register_blueprint(CurrencyBlueprint)


@app.route("/")
def hello():
    return "Hello world!"


