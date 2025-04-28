from flask import render_template, request, redirect, url_for
from .forms import CommentForm
from .models import Comment
from . import db

@app.route('/')
def index():
    comments = Comment.query.all()
    return render_template('index.html', comments=comments)

@app.route('/comment', methods=['POST'])
def comment():
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(name=form.name.data, content=form.content.data)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('index'))
    return redirect(url_for('index'))  # Redirect if form is not valid