from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import main
from app import db
from app.models import User

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        new_email = request.form.get('email')
        if new_email and new_email != current_user.email:
            current_user.email = new_email
            db.session.commit()
            flash('Your email has been updated!', 'success')
            return redirect(url_for('main.profile'))
    return render_template('profile.html', email=current_user.email)