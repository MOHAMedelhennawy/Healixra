#!/usr/bin/python3
"""Specialization Class defenition"""

from models.base_model import BaseModel 
from sqlalchemy import Column, String, Date, Boolean, ForeignKey, Time
from models.base_model import db

class Appointment(BaseModel, db.Model):
    __tablename__ = 'appointments'
    patient_id = db.Column(db.String(60), db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.String(60), db.ForeignKey('doctors.id'), nullable=False)
    appointment_date  = db.Column(db.Date(), nullable=False)
    appointment_time  = db.Column(db.Time(), nullable=False)
    status = db.Column(db.Boolean())

    patient = db.relationship('Patient', back_populates='appointments')
    doctor = db.relationship('Doctor', back_populates='appointments')

