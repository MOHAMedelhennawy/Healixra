#!/usr/bin/python3
"""Specialization Class defenition"""

from models.base_model import BaseModel 
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.orm import relationship
from models.base_model import db
from __init__ import app

class Specialization(BaseModel, db.Model):
    __tablename__ = 'specializations'
    specialization_name = db.Column(String(128), nullable=False, unique=True)
    doctors = db.relationship('Doctor', back_populates='specialization', cascade='all, delete')

    def get_names():
        with app.app_context():
            session = db.session
            specializations = session.query(Specialization.specialization_name).all()
            specializations_name = []
            for specialization in specializations:
                specializations_name.append(specialization.specialization_name)
        return specializations_name