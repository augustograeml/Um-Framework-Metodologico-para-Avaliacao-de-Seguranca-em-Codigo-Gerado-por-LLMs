from flask import Blueprint, render_template, request

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
@admin_bp.route('/admin/<string:custom_param>')
def admin_panel(custom_param=None):
    # Retrieve parameters from the URL
    params = request.args.to_dict()
    
    # Render the index.html template with the parameters
    return render_template('index.html', custom_param=custom_param, params=params)