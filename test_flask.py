from models.patient import Patient
from models.base_model import db
from routes import app

with app.app_context():
    session = db.session
    id='0723efb9-ee86-449f-af3c-3a18581190a7'
    patient_email = Patient.query.filter_by(email='Jihan123@ec.com').first()
    if patient_email:
        print(patient_email)