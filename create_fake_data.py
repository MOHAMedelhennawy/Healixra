#!/usr/bin/python3
"""
Create Fake database
Tables: Location, Doctor, Patient, Specialization.

Command:
HBNB_MYSQL_USER=Name HBNB_MYSQL_PWD=Password HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=Healixra HBNB_TYPE_STORAGE=db python3 create_fake_data.py 
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.patient import Patient
from models.doctor import Doctor
from models.location import Location
from models.specialization import Specialization
import models
from __init__ import app

doctors = models.storage.all(Doctor)
print(len(doctors))

location = 'Sohag'
specialization = 'Psychiatry'
with app.app_context():
    specialization_obj = Specialization.query.filter_by(specialization_name=specialization).first()
    location_obj = Location.query.filter_by(location_name=location).first()
    matched_doctors = Doctor.query.filter_by(location_id=location_obj.id).all()
    for doctor in matched_doctors:
        print(doctor)
print(len(matched_doctors))