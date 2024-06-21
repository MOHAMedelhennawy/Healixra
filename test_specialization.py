#!/usr/bin/python3
"""
Test the relationship between Doctor and Specialization
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
specialization_ = Specialization(specialization_name='Internal Medicine')
id = specialization_.id
specialization_.save()

# Create doctor obj's
doctor1 = Doctor(first_name='Mnsour', last_name='Fekry', specialization=specialization_)
doctor1.save()

doctor2 = Doctor(first_name='Mohammed', last_name='Emara', specialization=specialization_)
doctor2.save()

doctor3 = Doctor(first_name='Mohammed', last_name='aboelsafa', specialization_id=id)
doctor3.save()

for doctor in session.query(Doctor).all():
    print(doctor)
    print

# print('=' * 50)


# # Test to remove Specialization and all Doctors related to his Specialization
# specialization = session.query(Specialization).first()
# session.delete(specialization)
# session.commit()


# for doctor in session.query(Doctor).all():
#     print(doctor)
    print