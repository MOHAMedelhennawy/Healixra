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
from sqlalchemy import and_
from models.base_model import db
from __init__ import app

doctors = models.storage.all(Doctor)
print(len(doctors))

location_name = 'Sohag'
specialization_name = 'Psychiatry'
with app.app_context():
    session = db.session
    location = session.query(Location).filter_by(location_name=location_name).first()
    specialization = session.query(Specialization).filter_by(specialization_name=specialization_name).first()
    all_doc = session.query(Doctor).filter(
        and_(
            Doctor.location_id == location.id,
            Doctor.specialization_id == specialization.id
        )
    ).all()
    for doc in all_doc:
        print(doc)
    print(len(all_doc))