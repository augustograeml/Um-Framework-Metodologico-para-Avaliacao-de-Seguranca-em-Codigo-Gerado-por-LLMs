from flask import Blueprint, render_template, request, redirect, url_for
from app.models.comment import Comment
from app.forms.comment_form import CommentForm

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/blog', methods=['GET'])
def index():
    # Here you would typically fetch posts from the database
    posts = []  # Placeholder for blog posts
    return render_template('blog/index.html', posts=posts)

@blog_bp.route('/blog/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    # Here you would typically fetch the post and its comments from the database
    post = {}  # Placeholder for a single blog post
    comments = []  # Placeholder for comments related to the post
    form = CommentForm()

    if form.validate_on_submit():
        new_comment = Comment(content=form.content.data, post_id=post_id)
        # Here you would typically save the new comment to the database
        return redirect(url_for('blog.post', post_id=post_id))

    return render_template('blog/post.html', post=post, comments=comments, form=form)