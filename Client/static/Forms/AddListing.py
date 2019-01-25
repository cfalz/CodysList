from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddListingForm(FlaskForm):
    Title = StringField('Listing Title: ', validators=[DataRequired()])
    submit = SubmitField('Create Listing')