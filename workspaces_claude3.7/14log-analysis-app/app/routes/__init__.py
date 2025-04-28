from flask import Blueprint

routes = Blueprint('routes', __name__)

from .web_routes import *