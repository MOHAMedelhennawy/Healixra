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

    for day in doctor.schedule.keys(): 
        print(day)
        print(doctor.get_valid_appointments(day))
