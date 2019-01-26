from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddListingForm(FlaskForm):
    title = StringField('Listing Title: ', validators=[DataRequired()])
    price = StringField('Price: ', validators=[DataRequired()])
    description = StringField('Description: ', validators=[DataRequired()])
    seller = StringField('Your Contact Name: ', validators=[DataRequired()])
    submit = SubmitField('Create Listing')
