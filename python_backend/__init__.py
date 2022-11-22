from flask import Flask

app = Flask(__name__)

from python_backend import views
from python_backend.resources import user
from python_backend.resources import note
from python_backend.resources import category