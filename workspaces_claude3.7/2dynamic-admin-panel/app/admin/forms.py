from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ParameterForm(FlaskForm):
    parameter_name = StringField('Parameter Name', validators=[DataRequired()])
    parameter_value = StringField('Parameter Value', validators=[DataRequired()])
    display_option = SelectField('Display Option', choices=[('default', 'Default'), ('custom', 'Custom')], validators=[DataRequired()])
    submit = SubmitField('Submit')