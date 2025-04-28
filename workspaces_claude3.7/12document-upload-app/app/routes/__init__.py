from flask import Blueprint

# Initialize the routes blueprint
routes_bp = Blueprint('routes', __name__)

from . import auth, upload  # Import routes from auth and upload modules