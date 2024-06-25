from models.patient import Patient
from routes import db, app
with app.app_context():
    # Create all tables
    db.create_all()

    # Create Patients
    patient1 = Patient(
        first_name='adgas', last_name='elkelany', email='asdfds@ex.com', gender='male',
        phone='010165', password='test0234'
    )
    db.session.add(patient1)

    patient2 = Patient(
        first_name='Msgsdichel', last_name='Noufgasgr', email='sgasd@ex.com', gender='male',
        phone='010325', password='2332p'
    )
    db.session.add(patient2)

    patient3 = Patient(
        first_name='adfaf', last_name='dafasdf', email='ewqrqwe@ex.com', gender='female',
        phone='01034165', password='213-test'
    )
    db.session.add(patient3)

    db.session.commit()

    all_patient = Patient.query.all()

    for patient in all_patient:
        print(patient)
