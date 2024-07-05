#!/usr/bin/python3
from models.doctor import Doctor
from models.patient import Patient
from models.base_model import db
from __init__ import app

with app.app_context():
    doctor = Doctor.query.first()
    print(doctor)

    patient = Patient.query.first()
    print(patient)

    