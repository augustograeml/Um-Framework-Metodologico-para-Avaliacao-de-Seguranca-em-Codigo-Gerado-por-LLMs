from flask import Blueprint, request, send_from_directory, abort
import os
from app.config import Config
from app.services.file_service import FileService

download_bp = Blueprint('download', __name__)
file_service = FileService()

@download_bp.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    if file_service.is_valid_file(filename):
        return send_from_directory(Config.REPORTS_DIR, filename, as_attachment=True)
    else:
        abort(404)