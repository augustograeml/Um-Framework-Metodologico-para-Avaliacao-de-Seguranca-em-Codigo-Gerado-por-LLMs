from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms.account_settings import AccountSettingsForm
from app.models.user import User
from flask_login import current_user, login_required

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def account_settings():
    form = AccountSettingsForm(obj=current_user)
    if form.validate_on_submit():
        form.populate_obj(current_user)
        # Here you would typically save the user to the database
        # db.session.commit()  # Uncomment this line after setting up the database
        flash('Your account settings have been updated!', 'success')
        return redirect(url_for('settings.account_settings'))
    return render_template('settings/account.html', form=form)