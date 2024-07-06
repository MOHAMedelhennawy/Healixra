from __init__ import app
from models.base_model import db
from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment
from faker import Faker
from datetime import timedelta

faker = Faker()

with app.app_context():
    # Create a new doctor
    doctor = Doctor.query.first()
    patient = Patient.query.first()

    print(doctor.schedule)
    for day, time in doctor.schedule.items():
        print(day , ': ', time)
    
    appointment = Appointment(patient_id=patient.id, doctor_id= doctor.id, appointment_date=faker.date_time(), appointment_time=faker.time())
    appointment.save()
    doctor.patients.append(patient)
    print(doctor.patients)
    db.session.commit()


    print(doctor.schedule)
    for day, time in doctor.schedule.items():
        print(day , ': ', time)

    appointments = patient.get_appointments()
    for appointment in appointments:
        print(appointment.appointment_date + timedelta(days=1))
