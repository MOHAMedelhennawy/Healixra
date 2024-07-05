from models.doctor import Doctor
from models.base_model import db
from __init__ import app
# Create a new doctor
with app.app_context():
    new_doctor = Doctor.query.first()

    docotr = Doctor.query.first()
    print(type(docotr.schedule))
