from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import AccountSettingsForm

app = Blueprint('app', __name__)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard/account_settings.html')

@app.route('/dashboard/account-settings', methods=['POST'])
def account_settings():
    form = AccountSettingsForm()
    if form.validate_on_submit():
        # Here you would typically save the data to the database
        flash('Account settings updated successfully!', 'success')
        return redirect(url_for('app.dashboard'))
    return render_template('dashboard/account_settings.html', form=form)