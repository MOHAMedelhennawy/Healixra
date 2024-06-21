#!/usr/bin/python3
"""Location Class definition"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Location(BaseModel, Base):
    __tablename__ = 'locations'
    location_name = Column(String(128), nullable=False)
    doctors = relationship('Doctor', backref='location', cascade='all, delete')
