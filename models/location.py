#!/usr/bin/python3
"""Location Class definition"""

from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from routes import db

class Location(BaseModel, db.Model):
    __tablename__ = 'locations'
    location_name = db.Column(db.String(128), nullable=False)
    doctors = db.relationship('Doctor', backref='location', cascade='all, delete')
