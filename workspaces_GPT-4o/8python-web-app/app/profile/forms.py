from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class UpdateEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update Email')