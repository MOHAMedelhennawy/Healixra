#!/usr/bin/python3
"""Patient Class defenition"""

from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Text, BLOB, Table
from sqlalchemy.orm import relationship
from models.doctor import Doctor
from models.base_model import db
from flask_login import UserMixin
from flask_login import LoginManager
from __init__ import app, login_manager

# login_manager = LoginManager(app)
# login_manager.init_app(app)

# this decorator for open session for the user
@login_manager.user_loader
def load_user(id):
    session = db.session
    return session.get(Patient, id)



doctor_patient = Table(
    'doctor_patient',
    db.metadata,
    Column('patient_id', db.String(60), ForeignKey('patients.id'), primary_key=True, nullable=False),
    Column('doctor_id', db.String(60), ForeignKey('doctors.id'), primary_key=True, nullable=False),
)

class Patient(BaseModel, db.Model, UserMixin):
    __tablename__ = 'patients'
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.String(128))
    phone = db.Column(db.String(15))
    image = db.Column(db.String(40), nullable=False, default='user.jpg')

    reviews = db.relationship('Review', backref='Patient', cascade='all, delete')
    doctors = db.relationship('Doctor', secondary='doctor_patient', back_populates='patients')
