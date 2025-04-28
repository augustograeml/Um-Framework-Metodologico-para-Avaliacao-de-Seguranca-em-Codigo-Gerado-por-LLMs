from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

class UploadForm(FlaskForm):
    file = FileField('Upload Document', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'doc', 'docx', 'txt'], 'Documents only!')
    ])
    submit = SubmitField('Upload')