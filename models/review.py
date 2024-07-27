#!/usr/bin/python3
"""Specialization Class defenition"""

from models.base_model import BaseModel 
from models.base_model import db
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, RadioField
from wtforms.validators import InputRequired

class Review(BaseModel, db.Model):
    __tablename__ = 'reviews'
    patient_id = db.Column(db.String(60), db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.String(60), db.ForeignKey('doctors.id'), nullable=False)
    review_text = db.Column(db.Text)
    rating = db.Column(db.Integer)


class Add_review(FlaskForm):
    text = TextAreaField(
        'review'
    )
    rating = RadioField('Rating', choices=[
        ('5', '5 stars'),
        ('4', '4 stars'),
        ('3', '3 stars'),
        ('2', '2 stars'),
        ('1', '1 star')
    ], validators=[InputRequired(message="Rating is required.")])
    submit = SubmitField('submit')