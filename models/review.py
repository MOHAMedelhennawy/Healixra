#!/usr/bin/python3
"""Specialization Class defenition"""

from models.base_model import BaseModel 
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from models.base_model import db

class Review(BaseModel, db.Model):
    __tablename__ = 'reviews'
    patient_id = db.Column(db.String(60), db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.String(60), db.ForeignKey('doctors.id'), nullable=False)
    review_text = db.Column(db.Text)
    rating = db.Column(db.Integer)
