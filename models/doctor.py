#!/usr/bin/python3
"""Doctor Class defenition"""

from models.base_model import BaseModel 
from sqlalchemy import Column, String, DateTime, Text, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from models.base_model import db


class Doctor(BaseModel, db.Model):
    __tablename__ = 'doctors'
    specialization_id = db.Column(db.String(60), db.ForeignKey('specializations.id'),nullable=False)
    location_id = db.Column(db.String(128), db.ForeignKey('locations.id'), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    schedule = db.Column(db.Text)
    image = db.Column(db.BLOB)
    reviews = db.relationship('Review', backref='doctor', cascade='all, delete')
    specialization = db.relationship('Specialization', back_populates='doctors')
    patients = db.relationship('Patient', secondary='doctor_patient', back_populates='doctors')