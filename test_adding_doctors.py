from models.doctor import Doctor
from models.base_model import db
from __init__ import app
with app.app_context():
    # Create all tables
    db.create_all()

    dr1 = Doctor(
        first_name="Ahmed",
        last_name="Elgammal",
        specializtion="Dermatology"
    )
    db.session.add(dr1)

    dr2 = Doctor(
        first_name="Nora",
        last_name="Hamdy",
        specializtion="Surgery"
    )
    db.session.add(dr2)

    dr3 = Doctor(
        first_name="Hazem",
        last_name="Esmail",
        specializtion="Pediatrics"
    )
    db.session.add(dr1)

    db.session.commit()

    all_drs = Doctor.query.all()

    for dr in all_drs:
        print(dr)
