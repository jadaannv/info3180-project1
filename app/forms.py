from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    bedrooms = StringField('No. of Bedrooms', validators=[InputRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    propertytype = SelectField('Property Type', choices=[("House", "House"), ("Apartment", "Apartment")])
    image = FileField('Photo', validators=[FileRequired(), FileAllowed(['png', 'jpeg'], 'Images only!')])
    




