from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddListingForm(FlaskForm):
    title = StringField('Listing Title: ', validators=[DataRequired()])
    submit = SubmitField('Create Listing')
