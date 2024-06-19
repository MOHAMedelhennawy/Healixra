#!/usr/bin/python3
"""Specialization Class defenition"""

from models.base_model import BaseModel, Base 
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.orm import relationship


class Specialization(BaseModel, Base):
    __tablename__ = 'specializations'
    specialization_name = Column(String(128), nullable=False)
    doctors = relationship('Doctor', back_populates='specializations', cascade='all, delete')