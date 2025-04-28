from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')