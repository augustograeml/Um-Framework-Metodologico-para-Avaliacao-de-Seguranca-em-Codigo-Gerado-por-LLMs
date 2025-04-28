from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.user import User
from app.forms.profile import ProfileForm
from app.database import get_db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile/<int:user_id>', methods=['GET'])
def view_profile(user_id):
    db = get_db()
    user = db.query(User).filter_by(id=user_id).first()
    if user is None:
        flash('User not found.', 'error')
        return redirect(url_for('index'))
    return render_template('profile/view.html', user=user)

@profile_bp.route('/profile/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_profile(user_id):
    db = get_db()
    user = db.query(User).filter_by(id=user_id).first()
    if user is None:
        flash('User not found.', 'error')
        return redirect(url_for('index'))

    form = ProfileForm(obj=user)
    if form.validate_on_submit():
        user.name = form.name.data
        user.bio = form.bio.data
        db.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile.view_profile', user_id=user.id))

    return render_template('profile/edit.html', form=form, user=user)