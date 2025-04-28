from flask import render_template, request, redirect, url_for
from .forms import CommentForm
from .models import Comment

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data)
        # Here you would typically add the comment to the database
        # db.session.add(comment)
        # db.session.commit()
        return redirect(url_for('index'))
    
    # Here you would typically query the comments from the database
    # comments = Comment.query.all()
    comments = []  # Placeholder for comments
    return render_template('index.html', form=form, comments=comments)