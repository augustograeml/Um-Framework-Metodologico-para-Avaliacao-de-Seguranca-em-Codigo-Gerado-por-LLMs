from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.comment import Comment
from app.forms.comment_form import CommentForm
from app import db

comments_bp = Blueprint('comments', __name__)

@comments_bp.route('/post/<int:post_id>/comments', methods=['GET', 'POST'])
def post_comments(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(content=form.content.data, post_id=post_id)
        db.session.add(new_comment)
        db.session.commit()
        flash('Your comment has been posted!', 'success')
        return redirect(url_for('blog.post', post_id=post_id))
    
    comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template('blog/post.html', form=form, comments=comments)