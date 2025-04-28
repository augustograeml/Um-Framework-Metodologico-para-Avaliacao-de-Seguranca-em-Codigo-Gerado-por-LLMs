from flask import Blueprint

routes = Blueprint('routes', __name__)

from .auth import *
from .dashboard import *
from .settings import *