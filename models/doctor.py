#!/usr/bin/python3
"""Doctor Class defenition"""

from models.base_model import BaseModel, Base 
from sqlalchemy import Column, String, DateTime, Text, ForeignKey, BLOB
from sqlalchemy.orm import relationship

class Doctors(BaseModel, Base):
    __tablename__ = 'doctors'
    specialization_id = Column(String(60), ForeignKey('specializations.id'),nullable=False)
    location_id = Column(String(128), ForeignKey('locations.id'), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    schedule = Column(Text)
    image = Column(BLOB)
    # reviews = relationship('Review', backref='doctor', cascade='all, delete')
    specialization = relationship('Specialization', back_populates='doctor')
    patients = relationship('Patient', secondary='doctor_patient', back_populates='doctors')
