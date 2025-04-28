from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CommentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post Comment')