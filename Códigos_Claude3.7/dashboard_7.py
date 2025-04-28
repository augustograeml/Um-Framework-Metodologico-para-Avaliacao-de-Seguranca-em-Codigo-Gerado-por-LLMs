from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms.account_settings import AccountSettingsForm
from app.models.user import User

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = AccountSettingsForm()
    if form.validate_on_submit():
        # Assuming user is fetched from session or database
        user = User.query.get(current_user.id)
        user.username = form.username.data
        user.email = form.email.data
        # Save changes to the database
        db.session.commit()
        flash('Your account settings have been updated!', 'success')
        return redirect(url_for('dashboard.dashboard'))
    
    return render_template('dashboard/index.html', form=form)