import models
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, SearchField
from wtforms.validators import DataRequired
from models.specialization import Specialization
from models.location import Location
from models.base_model import db
from __init__ import app

class Search(FlaskForm):

    locations = models.storage.all(Location).values()
    specializations = models.storage.all(Specialization).values()

    specializations_name = ['All specializations']
    for specialization in specializations:
        specializations_name.append(specialization.specialization_name)

    specialization = SelectField(
        'Specialization',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Specialization'},
        choices=specializations_name
    )

    locations_name = ['All locations']
    for location in locations:
        locations_name.append(location.location_name)

    location = SelectField(
        'Location',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Location '},
        choices=locations_name
    )

    name = SearchField(
        'Doctor Name',
        render_kw={'placeholder': 'Doctor Name '},
    )
    
    # submit = SubmitField('Search')
    submit = SubmitField('Search', render_kw={'class': 'search-button'})