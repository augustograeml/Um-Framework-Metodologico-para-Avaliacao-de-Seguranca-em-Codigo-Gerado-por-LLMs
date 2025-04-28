from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    bio = TextAreaField('Bio', validators=[Length(max=500)])
    submit = SubmitField('Update Profile')