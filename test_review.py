#!/usr/bin/pyhon3
"""
Test Review

Command:
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.patient import Patient
from models.review import Review
from models.doctor import Doctor
from models.location import Location
from models.specialization import Specialization
from models import storage

HBNB_MYSQL_USER = 'Name'
HBNB_MYSQL_PWD = 'Password'
HBNB_MYSQL_HOST = 'localhost'
HBNB_MYSQL_DB = 'Healixra'
# Database connection setup (adjust connection string as needed)
engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()


# List doctor to test
doctor = session.query(Doctor).first()


# Make fake reviews
for patient in doctor.patients:
    review_text = input()
    review = Review(doctor_id=doctor.id, patient_id=patient.id, review_text=review_text)
    review.save()
storage.save()


doctor_name = doctor.first_name + ' ' + doctor.last_name
i = 1


# Try to print all reviews related to doctor
print(f"All {doctor_name} Reviews")
for review in doctor.reviews:
    patient = session.query(Patient).filter_by(id=review.patient_id).first()
    patient_name = patient.first_name + ' ' + patient.last_name
    print(f'{i}\t{patient_name}: {review.review_text}')
    i += 1