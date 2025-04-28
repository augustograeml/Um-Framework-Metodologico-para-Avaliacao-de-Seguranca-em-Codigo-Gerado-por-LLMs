from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import SettingsForm

app = Blueprint('app', __name__)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    form = SettingsForm()
    if form.validate_on_submit():
        # Process the form data
        # For example, save the data to a database or update user settings
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('app.settings'))
    return render_template('settings.html', form=form)