from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms.account_settings import AccountSettingsForm
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/settings', methods=['GET', 'POST'])
def account_settings():
    form = AccountSettingsForm()
    if form.validate_on_submit():
        # Here you would typically update the user account settings in the database
        # For example:
        # user = User.query.get(current_user.id)
        # user.username = form.username.data
        # user.email = form.email.data
        # db.session.commit()
        
        flash('Your account settings have been updated!', 'success')
        return redirect(url_for('auth.account_settings'))
    
    return render_template('settings/account.html', form=form)