from flask import render_template, request
from . import app

@app.route('/admin')
def admin_panel():
    param1 = request.args.get('param1', 'default_value1')
    param2 = request.args.get('param2', 'default_value2')
    return render_template('admin.html', param1=param1, param2=param2)