#!/usr/bin/python3
"""
This file to create fake docotrs data
Before you start this file:
    - first run this command to install faker: 'pip3 install Faker'
command:
    - USER=Name PWD=Password HOST=localhost DB=Healixra TYPE_STORAGE=db python3 create_fake_doctors.py
"""
import models
from models.location import Location
from models.specialization import Specialization
from models.doctor import Doctor
from faker import Faker
from __init__ import app
import datetime

# Initialize Faker
faker = Faker()

# Get all locations
locations = models.storage.all(Location).values()
locations_name = [location.id for location in locations]

# Get all specializations
specializations = models.storage.all(Specialization).values()
specializations_name = [specialization.id for specialization in specializations]
images = ['doctor1.jpg', 'doctor2.jpg', 'doctor3.jpg', 'doctor4.jpg', 'doctor5.jpg']

def generate_fake_schedule():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    schedule = {day: [] for day in days_of_week}
    for day in days_of_week:
        for _ in range(faker.random.randint(0, 5)):
            start_time = faker.time(pattern="%H:%M", end_datetime=None)
            end_time = faker.time(pattern="%H:%M", end_datetime=None)
            if start_time < end_time:
                schedule[day].append({
                    "start": start_time,
                    "end": end_time
                })
    return schedule

# Create fake doctors data
for i in range(500):
    doctor = Doctor(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        location_id=faker.random.choice(locations_name),
        specialization_id=faker.random.choice(specializations_name),
        image=faker.random.choice(images),
        schedule=generate_fake_schedule()
    )
    try:
        doctor.save()
    except Exception as e:
        print(f"Error saving doctor {doctor.first_name} {doctor.last_name}: {e}")

models.storage.save()
print('Fake doctors created successfully!')
