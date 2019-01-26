from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddListingForm(FlaskForm):
    title = StringField('Listing Title: ', validators=[DataRequired()])
    price = StringField('Price: ', validators=[DataRequired()])
    description = StringField('Description: ', validators=[DataRequired()])
    seller = StringField('Your Contact Name: ', validators=[DataRequired()])
    photo = FileField(validators =[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Create Listing')
