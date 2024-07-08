#!/usr/bin/python3
from __init__ import app
from models.base_model import db
from models.doctor import Doctor
from models.patient import Patient
from models.review import Review
from faker import Faker
from datetime import time

faker = Faker()
with app.app_context():
    # Create a new doctor
    doctor = Doctor.query.first()
    
    for i in range(20):
        patient = Patient(
            first_name=faker.first_name(), last_name=faker.last_name(), email=faker.email(),
            phone=faker.random_number(), password=faker.password()
        )
        
        doctor.patients.append(patient)
        db.session.commit()

        review  = Review(
            patient_id=patient.id,
            doctor_id=doctor.id,
            review_text=faker.text(),
            rating = faker.random_number(1, 5)
        )
        review.save()

    db.session.commit()
