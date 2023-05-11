from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from functools import wraps
from .models import UserModel
from werkzeug.security import check_password_hash
from . import settings

app = Flask(__name__)
settings.setup(app)


@app.route("/login")
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = UserModel.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, key=app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = UserModel.query.filter_by(id=data['id']).first()
            # print(f"{current_user.id} {current_user.name}")
        except Exception:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


from python_backend import views
from python_backend.resources import user
from python_backend.resources import note
from python_backend.resources import category
from python_backend.resources import currency