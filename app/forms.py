from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length

class CreateForm(FlaskForm):
    url = StringField('URL: ', validators=[DataRequired()])
    colour = StringField('Colour: ', validators=[DataRequired()])
    row = SelectField('Row: ', choices=['1','2','3'], validators=[DataRequired()])
    submit = SubmitField('Create Website')

class UpdateForm(FlaskForm):
    url = StringField('URL: ', validators=[DataRequired()])
    colour = StringField('Colour: ', validators=[DataRequired()])
    row = SelectField('Row: ', choices=['1','2','3'], validators=[DataRequired()])
    submit = SubmitField('Update Website')
    submit2 = SubmitField('Delete Website')
