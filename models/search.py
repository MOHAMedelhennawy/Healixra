from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class Search(FlaskForm):
    specialization = StringField(
        'Specialization',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Specialization'}
    )
    location = StringField(
        'Location',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Location '}
    )
    submit = SubmitField('Search')