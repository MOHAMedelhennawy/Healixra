from __init__ import app
from models.base_model import db
from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment
from faker import Faker
from datetime import time

with app.app_context():
    # Create a new doctor
    doctor = Doctor.query.first()

    times = doctor.get_valid_appointments('2004-05-24')
    print(times)

    # {"Friday": [{"end": "12:00", "start": "09:00"}, {"end": "17:00", "start": "13:00"}], 
    # "Monday": [{"end": "12:00", "start": "09:00"}, {"end": "17:00", "start": "13:00"}], 
    # "Wednesday": [{"end": "12:00", "start": "09:00"}, {"end": "17:00", "start": "13:00"}]}