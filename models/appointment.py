# #!/usr/bin/python3
# """Specialization Class defenition"""

# from models.base_model import BaseModel, Base 
# from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey


# class Appointment(BaseModel, Base):
#     __tablename__ = 'appointments'
#     patient_id = Column(String(60), ForeignKey('patients.id'), nullable=False)
#     doctor_id = Column(String(60), ForeignKey('doctors.id'), nullable=False)
#     appointment_date  = Column(DateTime(), nullable=False)
#     status = Column(Boolean())
