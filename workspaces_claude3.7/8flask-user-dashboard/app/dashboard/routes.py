from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .forms import UpdateEmailForm

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard/index.html')

@dashboard_bp.route('/dashboard/update_email', methods=['GET', 'POST'])
@login_required
def update_email():
    form = UpdateEmailForm()
    if form.validate_on_submit():
        current_user.email = form.email.data
        # Here you would typically save the user to the database
        flash('Your email has been updated!', 'success')
        return redirect(url_for('dashboard.dashboard'))
    return render_template('dashboard/update_email.html', form=form)