from flask import Blueprint, render_template, request
from .parameter_handler import handle_parameters

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET'])
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/admin/parameters', methods=['GET'])
def parameters_view():
    params = request.args.to_dict()
    processed_params = handle_parameters(params)
    return render_template('admin/parameter_view.html', params=processed_params)