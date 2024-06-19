#!/usr/bin/python3
"""Patient Class defenition"""

from models.base_model import BaseModel, Base 
from sqlalchemy import Column, String, ForeignKey, Text, BLOB, Table
from sqlalchemy.orm import relationship
doctor_patient = Table(
    'doctor_patient', Base.metadata,
    Column('patient_id', String(60), ForeignKey('patients.id'), primary_key=True, nullable=False),
    Column('doctor_id', String(60), ForeignKey('doctors.id'), primary_key=True, nullable=False)
            )

class Patient(BaseModel, Base):
    __tablename__ = 'patients'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    gender = Column(String(128), nullable=False)
    phone = Column(String(15), nullable=False)
    description = Column(Text(500))
    images = Column(BLOB)

    # doctors = relationship('Doctor', secondary='doctor_patient', back_populates='patients')