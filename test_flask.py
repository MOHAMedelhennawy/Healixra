from models.patient import Patient
from models.base_model import db
from routes import app

with app.app_context():
    patient_email = db.session.query(Patient).filter_by(email="elhennawy@ex.com").first()
    if patient_email:
        print(patient_email)