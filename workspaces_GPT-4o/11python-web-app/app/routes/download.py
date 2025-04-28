from flask import Blueprint, send_from_directory, request, abort
import os

download_bp = Blueprint('download', __name__)

@download_bp.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    reports_dir = os.path.join(os.path.dirname(__file__), '../static/reports')
    try:
        return send_from_directory(reports_dir, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)