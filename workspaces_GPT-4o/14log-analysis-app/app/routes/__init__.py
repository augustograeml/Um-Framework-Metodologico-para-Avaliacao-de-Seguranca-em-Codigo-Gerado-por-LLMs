from flask import Blueprint

routes = Blueprint('routes', __name__)

from . import log_analysis_routes  # Assuming you will create a log_analysis_routes.py for handling log analysis specific routes.