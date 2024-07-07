#!/usr/bin/python3
import models
from faker import Faker
from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment
from models.base_model import db
from datetime import time
from __init__ import app

fake = Faker()
with app.app_context():
    doctor = Doctor.query.first()
    schedule = {
        'Monday': [
            {'start': '09:00', 'end': '12:00'},
            {'start': '13:00', 'end': '17:00'}
        ],
        'Wednesday': [
            {'start': '10:00', 'end': '14:00'}
        ],
        'Friday': [
            {'start': '09:00', 'end': '12:00'}
        ]
        }

    doctor.set_schedule(schedule)
    db.session.add(doctor)
    db.session.commit()

    print(doctor)
    patient = Patient(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password="123",
    )
    db.session.add(patient)
    db.session.commit()

    appointment = Appointment(
        patient_id = patient.id,
        doctor_id = doctor.id,
        appointment_date = fake.future_date(),
        appointment_time = time(hour=11, minute=15)
    )
    db.session.add(appointment)
    db.session.commit()
    patient = Patient.query.first()
    print(patient)
