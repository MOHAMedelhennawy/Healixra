#!/usr/bin/python3
"""Location Class definition"""

import models
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from models.base_model import db
from __init__ import app

class Location(BaseModel, db.Model):
    __tablename__ = 'locations'
    location_name = db.Column(db.String(128), nullable=False)
    doctors = db.relationship('Doctor', backref='location', cascade='all, delete')