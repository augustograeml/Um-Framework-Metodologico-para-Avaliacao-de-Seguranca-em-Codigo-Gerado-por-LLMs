from flask import Blueprint

# Initialize the routes blueprint
routes = Blueprint('routes', __name__)

from .auth import *
from .blog import *
from .comments import *