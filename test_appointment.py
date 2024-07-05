from __init__ import app
from models.base_model import db
from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment


with app.app_context():
    # Create a new doctor
    doctor = Doctor.query.first()
    patient = Patient(
        first_name='Msgsdichel',
        last_name='Noufgasgr',
        email='sgasfd@ex.com',
        gender='male',
        phone='010325',
        password='2332p'
    )
    appointment = Appointment(doctor.id, patient.id)
    doctor.patients.append(patient)

    # Set a full weekly schedule
    # weekly_schedule = {
    #     'Monday': [{'start': '09:00', 'end': '12:00'}, {'start': '13:00', 'end': '17:00'}],
    #     'Wednesday': [{'start': '09:00', 'end': '12:00'}, {'start': '13:00', 'end': '17:00'}],
    #     'Friday': [{'start': '09:00', 'end': '12:00'}, {'start': '13:00', 'end': '17:00'}],
    # }
    # doctor.set_schedule(weekly_schedule)

    # # Add a new availability slot
    # doctor.add_availability('Tuesday', '10:00', '12:00')

    # # Remove an availability slot
    # doctor.remove_availability('Wednesday', '09:00', '12:00')

    # # Save the doctor to the database
    # db.session.add(doctor)
    # db.session.commit()

    # # Retrieve and print the schedule
    # print(doctor.get_schedule())