from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import LoginForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Implement authentication logic here
        flash('Login successful!', 'success')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/login.html', form=form)

@auth_bp.route('/logout')
def logout():
    # Implement logout logic here
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))