#!/usr/bin/python3
"""
Test the relationship between Doctor and Specialization

Command to execute:
 HBNB_MYSQL_USER=Name HBNB_MYSQL_PWD=Password HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=Healixra HBNB_TYPE_STORAGE=db python3 test_specialization.py
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.patient import Patient
from models.doctor import Doctor
from models.specialization import Specialization

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

# Create specialization odj
specialization_ = Specialization(specialization_name='Internal Medicine2')
specialization_.save()


# Create doctor ojb
doctor1 = Doctor(first_name='Mnsour', last_name='Fekry', specialization=specialization_)
doctor1.save()

# List doctor
doctor = session.query(Doctor).first()
print("============ doctor ============")
print(doctor)

print("============ specialization ============")
print(doctor.specialization)

print("============ specialization id ============")
print(doctor.specialization_id)

print("============ specialization name ============")
print(doctor.specialization.specialization_name)

print("============ specialization doctors ============")
for doctor in specialization_.doctors:
    print(doctor)
