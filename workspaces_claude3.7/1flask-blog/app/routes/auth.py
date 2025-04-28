from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms.comment_form import CommentForm
from app.models.comment import Comment
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Logic for user login will be implemented here
    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    # Logic for user registration will be implemented here
    return render_template('auth/register.html')