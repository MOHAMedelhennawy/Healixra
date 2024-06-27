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


# Create location
location = Location(location_name='Tanta')
location.save()

# Create specialization
specialization = Specialization(specialization_name='Internal Medicine')
specialization.save()


# Create Doctors
doctor1 = Doctor(
    first_name='Mansour', last_name='Fekry',
    specialization_id=specialization.id, location_id=location.id
)
doctor1.save()

doctor2 = Doctor(
       first_name='Khaled', last_name='Mokhtar',
       specialization_id=specialization.id, location_id=location.id
)
doctor2.save()

doctor3 = Doctor(
       first_name='Mohamed', last_name='Abo elnaga',
       specialization_id=specialization.id, location_id=location.id
)
doctor3.save()


# Create Patients
patient1 = Patient(
    first_name='Ibrahim', last_name='elkelany', email='elkelany@ex.com', gender='male',
    phone='010165', password='test0234'
)
patient1.save()

patient2 = Patient(
    first_name='Michel', last_name='Nour', email='micfhel@ex.com', gender='male',
    phone='010325', password='2332p'
)
patient2.save()

patient3 = Patient(
    first_name='Hager', last_name='Khaled', email='Hagerd@ex.com', gender='female',
    phone='01034165', password='213-test'
)
patient3.save()

patient4 = Patient(
    first_name='Mohammed', last_name='Ahmed', email='Mohammfed@ex.com', gender='male',
    phone='010165', password='test0234'
)
patient4.save()

patient5 = Patient(
    first_name='Ahmed', last_name='Khaled', email='Ahmed@ex.com', gender='male',
    phone='010325', password='2332p'
)
patient5.save()

patient6 = Patient(
    first_name='Mona', last_name='Elsayed', email='Mona@ex.com', gender='female',
    phone='01034165', password='213-test'
)
patient6.save()



patient1.doctors.append(doctor1)
patient1.doctors.append(doctor2)
patient1.doctors.append(doctor3)

doctor2.patients.append(patient4)
doctor2.patients.append(patient6)

doctor3.patients.append(patient5)

# save all changes in DB
storage.save()
