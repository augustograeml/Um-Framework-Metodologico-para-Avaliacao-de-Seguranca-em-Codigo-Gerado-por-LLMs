from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .forms import UpdateEmailForm

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile_view():
    form = UpdateEmailForm()
    if form.validate_on_submit():
        current_user.email = form.email.data
        # Here you would typically save the updated user information to the database
        flash('Your email has been updated!', 'success')
        return redirect(url_for('profile.profile_view'))
    
    form.email.data = current_user.email
    return render_template('profile.html', form=form)