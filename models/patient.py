#!/usr/bin/python3
"""Patient Class defenition"""

from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Text, BLOB, Table
from sqlalchemy.orm import relationship
from models.doctor import Doctor
from models.base_model import db
from routes import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Patient.get(user_id)


doctor_patient = db.Table(
    'doctor_patient',
    db.metadata,
    db.Column('patient_id', db.String(60), db.ForeignKey('patients.id'), primary_key=True, nullable=False),
    db.Column('doctor_id', db.String(60), db.ForeignKey('doctors.id'), primary_key=True, nullable=False)
        )


class Patient(BaseModel, db.Model, UserMixin):
    __tablename__ = 'patients'
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.String(128))
    phone = db.Column(db.String(15))
    images = db.Column(db.BLOB)

    reviews = db.relationship('Review', backref='Patient', cascade='all, delete')
    doctors = db.relationship('Doctor', secondary='doctor_patient', back_populates='patients')
